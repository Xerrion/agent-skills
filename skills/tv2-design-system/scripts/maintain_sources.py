#!/usr/bin/env python3
"""Compare upstream design sources and prepare a separate, reviewable skill copy."""

from __future__ import annotations

import argparse
import copy
import difflib
import hashlib
import json
import re
import shutil
import subprocess
from datetime import date
from pathlib import Path

from build_web_assets import SKILL_ROOT
from validate_bundle import check_figma, check_integrity, check_markdown, check_skill_header, check_web, walk

REGISTRY = "references/maintenance/sources.json"
INTEGRITY = "references/governance/source-integrity.json"
IGNORED = shutil.ignore_patterns("__pycache__", ".DS_Store", "*.pyc")


def fail(message: str):
    raise ValueError(message)


def json_bytes(value) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def sha(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def git(repo: Path, *arguments: str) -> bytes:
    result = subprocess.run(["git", "-C", str(repo), *arguments], capture_output=True, check=False)
    if result.returncode:
        fail("Git source lookup failed: " + result.stderr.decode(errors="replace").strip())
    return result.stdout


def source_destination(path: str) -> str | None:
    if path in {"foundation/color.json", "foundation/color_election.json", "foundation/typography.json",
                "foundation/size.json", "foundation/breakpoint.json", "products/play.json"}:
        return "references/tokens/" + Path(path).name
    match = re.fullmatch(r"components/([^/]+)/\1(_log\.md|\.png)", path)
    if match:
        slug, suffix = match.groups()
        return ("references/components/" if suffix == "_log.md" else "assets/components/") + slug + suffix
    if path.startswith("assets/"):
        suffix = Path(path).suffix.lower()
        if suffix in {".svg", ".ttf", ".otf", ".woff", ".woff2", ".ico"}:
            return path
        if suffix == ".png" and path.startswith("assets/favicons/"):
            return path
    return None


def observed_source(path: str) -> bool:
    return bool(re.fullmatch(r"(?:foundation|products)/[^/]+\.(?:json|md)", path)
                or re.fullmatch(r"components/[^/]+/[^/]+\.json", path)
                or path == "components/README.md")


def repository_tree(repo: Path, ref: str) -> tuple[str, dict]:
    revision = git(repo, "rev-parse", "--verify", ref + "^{commit}").decode().strip()
    files = {}
    for row in git(repo, "ls-tree", "-rz", "--full-tree", revision, "--", "assets", "foundation", "products", "components").split(b"\0"):
        if not row:
            continue
        header, raw_path = row.split(b"\t", 1)
        mode, kind, object_id = header.decode().split()
        path = raw_path.decode("utf-8")
        destination = source_destination(path)
        if not destination and not observed_source(path):
            continue
        if kind != "blob" or mode not in {"100644", "100755"}:
            fail(f"Unsupported source object: {path}")
        files[path] = {"objectId": object_id}
        if destination:
            files[path]["destination"] = destination
    return revision, files


def affected_references(root: Path, source: str, destination: str | None) -> list[str]:
    result = set()
    slug = None
    if source.startswith("components/"):
        slug = source.split("/")[1]
    elif source.startswith("figma/") and source != "figma/layout-free.json":
        slug = Path(source).stem
    if slug:
        result.add(f"references/components/{slug}.md")
        css = root / f"assets/web/components/{slug}.css"
        if css.exists():
            result.add(css.relative_to(root).as_posix())
        if not (root / f"references/components/{slug}.md").exists():
            result.add("references/COMPONENTS.md")
    topics = {
        "color": ["foundations/color-primitives", "foundations/color-semantic"],
        "color_election": ["foundations/election-colors"],
        "typography": ["foundations/typography", "artwork/fonts"],
        "size": ["foundations/spacing", "implementation/default-profile"],
        "breakpoint": ["foundations/breakpoints"],
        "play": ["layout/play"],
        "layout-free": ["layout/free"],
    }
    if source.startswith(("foundation/", "products/", "figma/layout-free")):
        result.update("references/" + topic + ".md" for topic in topics.get(Path(source).stem, []))
    if destination:
        for path in (root / "references").rglob("*.md"):
            # Resolve links so renaming or removing a source points to its actual consumers.
            for match in re.finditer(r"\[[^\]]*\]\(([^\s)]+)\)", path.read_text(encoding="utf-8")):
                target = match.group(1).split("#")[0]
                if target and not ":" in target and (path.parent / target).resolve() == (root / destination).resolve():
                    result.add(path.relative_to(root).as_posix())
        if destination.startswith("assets/") and not slug:
            family = Path(destination).parent
            for path in (root / "references/artwork").glob("*.md"):
                if ("../../" + family.as_posix() + "/") in path.read_text(encoding="utf-8"):
                    result.add(path.relative_to(root).as_posix())
    return sorted(result)


def validate_import(data: dict, record: dict, file_key: str) -> None:
    if not isinstance(data, dict):
        fail("Figma import must be a JSON record object")
    source = data.get("source", {})
    if source.get("fileKey") != file_key or source.get("pageId") != record["pageId"]:
        fail("Figma import source does not match the registered file and page")
    date.fromisoformat(source["capturedOn"])
    if data.get("schemaVersion") != 1:
        fail("Unsupported Figma capture schema")
    expected_kind = "free-layout-measurements" if record["kind"] == "layout" else "native-component-measurements"
    if source.get("kind") != expected_kind:
        fail("Figma import has the wrong record kind")
    variables = data.get("variables", {})
    if not isinstance(variables, dict) or not all(isinstance(v, dict) for v in variables.values()):
        fail("Figma variables must be a map of captured variable objects")
    if any(v.get("unavailable") for v in variables.values()):
        fail("Figma import contains unavailable variable data")
    for node in walk(data):
        if node.get("type") == "VARIABLE_ALIAS" and node["id"] not in variables:
            fail("Figma import has an unresolved variable alias: " + node["id"])
    if not (data.get("sets") or data.get("standalone") or data.get("layouts")):
        fail("Figma import contains no measured components or layouts")
    for group in data.get("sets", []):
        if group["defaultVariantId"] not in [v["id"] for v in group["variants"]]:
            fail("Figma import is missing a default variant")
        if "metricColumns" in group:
            columns = group["metricColumns"]
            if not all(len(v["values"]) == len(columns) for v in group["variants"]):
                fail("Figma import has inconsistent metric columns")
            default = next(v for v in group["variants"] if v["id"] == group["defaultVariantId"])
            tree = group.get("defaultTree", {})
            if tree.get("id") != default["id"]:
                fail("Figma import has the wrong default tree")
            if any(tree.get(key) != value for key, value in zip(columns, default["values"])):
                fail("Figma import default tree and variant metrics disagree")


def comparable_figma(data: dict) -> dict:
    result = copy.deepcopy(data)
    result.get("source", {}).pop("capturedOn", None)
    return result


def compare(root: Path, repo: Path | None = None, ref: str = "HEAD", figma_dir: Path | None = None):
    root = root.resolve()
    registry = json.loads((root / REGISTRY).read_text())
    updated = copy.deepcopy(registry)
    changes = []
    payloads = {}
    if repo:
        revision, current = repository_tree(repo, ref)
        previous = registry["repository"]["files"]
        updated["repository"].update(revision=revision, files=current)
        for source in sorted(previous.keys() | current.keys()):
            before, after = previous.get(source), current.get(source)
            if before == after:
                continue
            destination = (after or before).get("destination")
            change = {"source": source, "kind": "added" if not before else "removed" if not after else "changed",
                      "destination": destination, "before": before, "after": after,
                      "review": affected_references(root, source, destination)}
            changes.append(change)
            if destination:
                payloads[destination] = git(repo, "show", f"{revision}:{source}") if after else None
            elif after:
                content = git(repo, "show", f"{revision}:{source}")
                if source.endswith(".json"):
                    change["upstreamDetails"] = json.loads(content)
                else:
                    change["upstreamText"] = content.decode("utf-8")
    if figma_dir:
        records = registry["figma"]["records"]
        imports = sorted(figma_dir.glob("*.json"))
        if not imports:
            fail("The Figma import directory contains no JSON records")
        for path in imports:
            slug = path.stem
            if slug not in records:
                fail("Unknown Figma record: " + path.name)
            data = json.loads(path.read_text())
            validate_import(data, records[slug], registry["figma"]["fileKey"])
            destination = f"references/figma/{slug}.json"
            previous = json.loads((root / destination).read_text())
            if comparable_figma(data) == comparable_figma(previous):
                continue
            changes.append({"source": "figma/" + path.name, "kind": "changed", "destination": destination,
                            "review": affected_references(root, "figma/" + path.name, destination)})
            payloads[destination] = json_bytes(data)
    report = {"schemaVersion": 1, "repositoryRevision": updated["repository"]["revision"],
              "changes": changes, "review": sorted({p for c in changes for p in c["review"]}),
              "figmaChecked": sorted(p.stem for p in figma_dir.glob("*.json")) if figma_dir else [],
              "figmaStatus": "imported-records-compared" if figma_dir else "not-checked"}
    return report, updated, payloads


def refresh_integrity(root: Path, revision: str) -> None:
    path = root / INTEGRITY
    data = json.loads(path.read_text())
    paths = {p for folder in ("references/tokens", "references/figma", "assets")
             for p in (root / folder).rglob("*") if p.is_file() and p.name != ".DS_Store"}
    paths.update((root / "references/components").glob("*_log.md"))
    data["repositoryRevision"] = revision
    data["sha256"] = {p.relative_to(root).as_posix(): sha(p.read_bytes()) for p in sorted(paths)}
    dates = [json.loads(p.read_text())["source"]["capturedOn"] for p in (root / "references/figma").glob("*.json")]
    # Individual source records retain their own capture dates.
    data["figmaCapturedOn"] = max(dates)
    path.write_bytes(json_bytes(data))


def stage(root: Path, output: Path, report: dict, registry: dict, payloads: dict) -> dict:
    root = root.resolve()
    output = output.resolve()
    if output.exists() or output == root or root in output.parents:
        fail("Stage output must be a new directory outside the skill")
    output.mkdir(parents=True)
    candidate = output / check_skill_header(root)["name"]
    shutil.copytree(root, candidate, ignore=IGNORED)
    diffs = []
    for relative, content in sorted(payloads.items()):
        target = candidate / relative
        previous = target.read_bytes() if target.exists() else b""
        if content is None:
            target.unlink()
            incoming = b""
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
            incoming = content
        try:
            diffs.extend(difflib.unified_diff(previous.decode().splitlines(True), incoming.decode().splitlines(True),
                                            fromfile="bundled/" + relative, tofile="candidate/" + relative))
        except UnicodeDecodeError:
            diffs.append(f"Binary change: {relative}; {sha(previous)} -> {sha(incoming)}\n")
    for change in report["changes"]:
        if change.get("destination"):
            continue
        if "upstreamDetails" in change or "upstreamText" in change:
            path = output / "upstream" / change["source"]
            path.parent.mkdir(parents=True, exist_ok=True)
            content = (json_bytes(change["upstreamDetails"]) if "upstreamDetails" in change
                       else change["upstreamText"].encode("utf-8"))
            path.write_bytes(content)
    (candidate / REGISTRY).write_bytes(json_bytes(registry))
    refresh_integrity(candidate, registry["repository"]["revision"])
    failures = []
    for name, check in (("links", check_markdown), ("integrity", check_integrity), ("figma", check_figma), ("web", check_web)):
        try:
            check(candidate)
        except (ValueError, OSError, KeyError) as error:
            failures.append({"check": name, "error": str(error)})
    report = {**report, "validationFailures": failures,
              "status": "needs-reference-review" if report["changes"] else "unchanged"}
    (output / "report.json").write_bytes(json_bytes(report))
    (output / "source.diff").write_text("".join(diffs), encoding="utf-8")
    (output / "review.txt").write_text(
        "Candidate sources are staged. The installed skill is unchanged.\n"
        f"Review source.diff and update the affected references and specimens in {candidate.name}/.\n"
        "Passing structural checks does not establish that written measurements still match.\n"
        + "\n".join(report["review"]) + "\n", encoding="utf-8")
    return report


def capture_script(root: Path, slug: str, captured_on: str) -> str:
    date.fromisoformat(captured_on)
    registry = json.loads((root / REGISTRY).read_text())
    record = registry["figma"]["records"].get(slug)
    if not record:
        fail("Unknown Figma record: " + slug)
    template = root / "scripts/figma" / ("capture-layout.js" if record["kind"] == "layout" else "capture-component.js")
    return (template.read_text().replace("PAGE_ID", json.dumps(record["pageId"]))
            .replace("CAPTURED_ON", json.dumps(captured_on))
            .replace("CAPTURE_DEPTH", str(record["depth"]))
            .replace("LAYOUT_IDS", json.dumps(record.get("nodeIds", []))))


def report_summary(report: dict, limit: int = 10) -> dict:
    """Keep large upstream prose and change lists out of default tool output."""
    changes = report["changes"]
    result = {"status": report.get("status", "changed" if changes else "unchanged"),
              "repositoryRevision": report["repositoryRevision"],
              "changeCount": len(changes), "reviewCount": len(report["review"]),
              "changes": [{key: row.get(key) for key in ("source", "kind", "destination")}
                          for row in changes[:limit]],
              "review": report["review"][:limit],
              "figmaChecked": report["figmaChecked"], "figmaStatus": report["figmaStatus"],
              "truncated": len(changes) > limit or len(report["review"]) > limit}
    if "validationFailures" in report:
        result["validationFailures"] = report["validationFailures"]
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, epilog=
        "Examples: check --repo /path/to/designsystem; stage --figma-dir /tmp/import --output /tmp/review. "
        "Exit codes: check 0 unchanged, 1 changes, 2 invalid input. Stage 0 means candidate created, not approved.")
    parser.add_argument("--skill-root", type=Path, default=SKILL_ROOT, help="Skill folder; defaults to this script's bundle")
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("check", "stage"):
        sub = commands.add_parser(name, help="Compare committed sources" if name == "check" else "Create a separate review candidate")
        sub.add_argument("--repo", type=Path, help="Local design-system Git checkout; uncommitted edits are excluded")
        sub.add_argument("--ref", default="HEAD", help="Committed source revision or branch (default: HEAD)")
        sub.add_argument("--figma-dir", type=Path, help="Directory of registered local Figma JSON exports")
        sub.add_argument("--details", action="store_true", help="Print full JSON, including upstream prose; default is a bounded summary")
        if name == "stage":
            sub.add_argument("--output", type=Path, required=True, help="New directory outside the skill and source checkout")
        else:
            sub.add_argument("--report", type=Path, help="Save the complete JSON report to this file")
    capture = commands.add_parser("capture-script", help="Print read-only Figma connector code; redirect stdout to a .js file")
    capture.add_argument("--record", required=True, help="Registered record name, for example button or layout-free")
    capture.add_argument("--captured-on", required=True, help="Actual capture date, YYYY-MM-DD")
    commands.add_parser("seal", help="Update checksums in a reviewed staged candidate")
    args = parser.parse_args()
    root = args.skill_root.resolve()
    try:
        if args.command == "capture-script":
            print(capture_script(root, args.record, args.captured_on))
            return 0
        if args.command == "seal":
            if not (root.parent / "report.json").is_file() or root.name != check_skill_header(root)["name"]:
                fail("Seal is supported only inside a staged candidate's skill directory")
            registry = json.loads((root / REGISTRY).read_text())
            refresh_integrity(root, registry["repository"]["revision"])
            print("Candidate checksums updated. Run bundle validation before adopting it.")
            return 0
        if not args.repo and not args.figma_dir:
            fail("Select --repo, --figma-dir, or both")
        if args.figma_dir and not args.figma_dir.is_dir():
            fail("Figma import directory does not exist")
        check_integrity(root)
        report, registry, payloads = compare(root, args.repo, args.ref, args.figma_dir)
        if args.command == "stage":
            if args.repo and args.repo.resolve() in args.output.resolve().parents:
                fail("Stage output must be outside the source repository")
            report = stage(root, args.output, report, registry, payloads)
        report_path = args.output.resolve() / "report.json" if args.command == "stage" else args.report
        if args.command == "check" and report_path:
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_bytes(json_bytes(report))
        output = report if args.details else report_summary(report)
        if report_path:
            output = {**output, "reportFile": str(report_path.resolve())}
        print(json.dumps(output, indent=2, ensure_ascii=False))
        return 1 if args.command == "check" and report["changes"] else 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, f"Maintenance failed: {error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
