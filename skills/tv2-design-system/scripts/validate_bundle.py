#!/usr/bin/env python3
"""Check the TV 2 skill's local references, pinned files, and portable web export."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build_web_assets import SKILL_ROOT, expected_assets


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def check_skill_header(root: Path) -> dict[str, str]:
    """Check this bundle's plain single-line metadata, not arbitrary YAML syntax."""
    root = root.resolve()
    content = (root / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", content, re.DOTALL)
    require(match is not None, "SKILL.md: missing YAML frontmatter boundaries")
    fields = {}
    for key in ("name", "description", "compatibility"):
        values = re.findall(r"^" + key + r": *([^\r\n]*)$", match.group(1), re.MULTILINE)
        require(len(values) <= 1, f"SKILL.md: duplicate {key}")
        if values:
            value = values[0].strip()
            require(value and value[0] not in "|>\"'[{", f"SKILL.md: keep {key} as a plain single-line scalar for the bundled checker; validate richer YAML with an external validator")
            fields[key] = value
    name = fields.get("name", "")
    require(len(name) <= 64 and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) is not None,
            "SKILL.md: name must be 1-64 lowercase letters/digits with single internal hyphens")
    require(name == root.name, "SKILL.md: name must match its containing directory")
    require(1 <= len(fields.get("description", "")) <= 1024, "SKILL.md: description must contain 1-1024 characters")
    if "compatibility" in fields:
        require(len(fields["compatibility"]) <= 500, "SKILL.md: compatibility must contain 1-500 characters")
    return fields


def check_eval_fixtures(root: Path) -> tuple[int, int]:
    cases = json.loads((root / "evals/evals.json").read_text())
    require(cases.get("skill_name") == "tv2-design-system", "Eval cases name the wrong skill")
    ids = set()
    for case in cases["evals"]:
        require(case["id"] not in ids and case["prompt"] and case["expected_output"], "Eval case has duplicate ID or missing purpose")
        ids.add(case["id"])
        for relative in case.get("files", []):
            path = (root / relative).resolve()
            require(path.is_relative_to(root.resolve()) and path.is_file(), f"Missing eval fixture: {relative}")
    queries = []
    for name in ("trigger-training.json", "trigger-validation.json"):
        rows = json.loads((root / "evals" / name).read_text())
        require({row["should_trigger"] for row in rows} == {True, False}, f"{name}: include positive and negative prompts")
        require(all(isinstance(row["should_trigger"], bool) and row["query"] for row in rows), f"{name}: invalid trigger query")
        queries.extend(row["query"] for row in rows)
    require(len(set(queries)) == len(queries), "Trigger train/validation split contains duplicate prompts")
    return len(ids), len(queries)


def local_target(base: Path, value: str) -> tuple[Path, str] | None:
    parts = urlsplit(value)
    if parts.scheme or parts.netloc:
        return None
    return (base / unquote(parts.path)).resolve(), unquote(parts.fragment)


def heading_ids(path: Path) -> set[str]:
    ids = set()
    counts: dict[str, int] = {}
    fenced = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            fenced = not fenced
        if fenced or not re.match(r"^#{1,6} ", line):
            continue
        title = re.sub(r"^#{1,6} ", "", line).strip().lower()
        slug = re.sub(r"[^\w\- ]", "", title).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        ids.add(slug if count == 0 else f"{slug}-{count}")
    return ids


def check_markdown(root: Path) -> int:
    root = root.resolve()
    count = 0
    for path in [root / "SKILL.md", *sorted((root / "references").rglob("*.md"))]:
        content = path.read_text(encoding="utf-8")
        for match in re.finditer(r"\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))\)", content):
            value = match.group(1) or match.group(2)
            # An empty path targets this same Markdown file.
            parts = urlsplit(value)
            target = local_target(path.parent, value)
            if target is None:
                continue
            destination, anchor = target
            if not parts.path:
                destination = path
            require(destination.is_relative_to(root), f"{path.name}: link leaves bundle: {value}")
            require(destination.exists(), f"{path.name}: missing local link: {value}")
            if anchor and destination.suffix == ".md":
                require(anchor in heading_ids(destination), f"{path.name}: missing anchor: {value}")
            count += 1
    return count


def check_integrity(root: Path) -> int:
    root = root.resolve()
    manifest = json.loads((root / "references/governance/source-integrity.json").read_text())
    for relative, expected in manifest["sha256"].items():
        path = (root / relative).resolve()
        require(path.is_relative_to(root), f"Integrity path leaves bundle: {relative}")
        require(path.is_file(), f"Missing pinned source: {relative}")
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        require(actual == expected, f"Pinned source changed: {relative}")
    return len(manifest["sha256"])


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def check_figma(root: Path) -> int:
    paths = sorted((root / "references/figma").glob("*.json"))
    registry = json.loads((root / "references/maintenance/sources.json").read_text())["figma"]
    expected = set(registry["records"])
    require({p.stem for p in paths} == expected, "Figma records must match the source registry")
    for path in paths:
        data = json.loads(path.read_text())
        require(data["source"]["fileKey"] == registry["fileKey"], f"{path.name}: wrong Figma source")
        require(data["source"]["pageId"] == registry["records"][path.stem]["pageId"], f"{path.name}: wrong Figma page")
        variables = data["variables"]
        for node in walk(data):
            if node.get("type") == "VARIABLE_ALIAS":
                require(node["id"] in variables, f"{path.name}: missing variable alias {node['id']}")
        require(not any(v.get("unavailable") for v in variables.values()), f"{path.name}: unavailable variable")
        for group in data.get("sets", []):
            ids = [variant["id"] for variant in group["variants"]]
            require(group["defaultVariantId"] in ids, f"{path.name}: missing default variant")
            if "metricColumns" in group:
                require(all(len(v["values"]) == len(group["metricColumns"]) for v in group["variants"]), f"{path.name}: metric column mismatch")
    return len(paths)


class Resources(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls: list[str] = []
        self.ids: set[str] = set()
        self.id_refs: list[str] = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get("id"):
            require(attrs["id"] not in self.ids, f"Duplicate HTML id: {attrs['id']}")
            self.ids.add(attrs["id"])
        for name in ("src", "href"):
            if attrs.get(name):
                self.urls.append(attrs[name])
        for name in ("for", "aria-labelledby", "aria-describedby", "data-tv2-return-focus"):
            self.id_refs.extend((attrs.get(name) or "").split())


def check_web(root: Path) -> int:
    assets = expected_assets(root)
    with tempfile.TemporaryDirectory(prefix="tv2-bundle-check-") as temporary:
        output = Path(temporary)
        for relative, content in assets.items():
            path = output / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        css = "\n".join(path.read_text() for path in output.rglob("*.css"))
        defined = set(re.findall(r"(--[\w-]+)\s*:", css))
        referenced = set(re.findall(r"var\(\s*(--[\w-]+)", css))
        require(not referenced - defined, f"Undefined CSS variables: {sorted(referenced - defined)}")
        resource_count = 0
        for path in output.rglob("*.css"):
            for value in re.findall(r"url\([\"']?([^\"')]+)[\"']?\)", path.read_text()):
                target = local_target(path.parent, value)
                require(target is not None, f"{path.name}: nonlocal CSS resource: {value}")
                require(target[0].is_file(), f"{path.name}: missing CSS resource: {value}")
                resource_count += 1
        specimens = sorted((output / "specimens").glob("*.html"))
        require(len(specimens) == 5, "Expected five standalone component specimens")
        for path in specimens:
            parser = Resources()
            content = path.read_text()
            parser.feed(content)
            require('data-tv2-theme="light"' in content and 'data-tv2-theme="dark"' in content, f"{path.name}: missing theme")
            for reference in parser.id_refs:
                require(reference in parser.ids, f"{path.name}: missing accessible ID target: {reference}")
            for value in parser.urls:
                parts = urlsplit(value)
                target = local_target(path.parent, value)
                require(target is not None, f"{path.name}: nonlocal HTML resource: {value}")
                if not parts.path:
                    require(target[1] in parser.ids, f"{path.name}: missing HTML anchor: {value}")
                else:
                    require(target[0].is_file(), f"{path.name}: missing HTML resource: {value}")
                resource_count += 1
    return resource_count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, epilog=
        "Examples: python3 scripts/validate_bundle.py; python3 scripts/validate_bundle.py --json. "
        "Exit codes: 0 passed, 1 validation failure, 2 invalid arguments.")
    parser.add_argument("--skill-root", type=Path, default=SKILL_ROOT, help="Skill folder to validate")
    parser.add_argument("--json", action="store_true", help="Print machine-readable check counts")
    args = parser.parse_args()
    root = args.skill_root.resolve()
    try:
        check_skill_header(root)
        evals, queries = check_eval_fixtures(root)
        links = check_markdown(root)
        sources = check_integrity(root)
        records = check_figma(root)
        resources = check_web(root)
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"Bundle check failed: {error}\n")
    if args.json:
        print(json.dumps({"status": "verified", "localLinks": links, "pinnedFiles": sources,
                          "figmaRecords": records, "webResources": resources,
                          "evalCases": evals, "triggerQueries": queries}))
    else:
        print(f"Bundle verified: {links} local links, {sources} pinned files, {records} Figma records, {resources} web resources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
