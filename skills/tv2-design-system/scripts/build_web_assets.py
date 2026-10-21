#!/usr/bin/env python3
"""Export the bundled TV 2 tokens and web assets with Python's standard library."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
MODES = ("sm", "md", "lg", "tv")
COLOR_LITERAL = re.compile(r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F](?:[0-9a-fA-F]{2}){0,2})?\Z")
TOKEN_NAME = re.compile(r"[A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)*\Z")


class TokenError(ValueError):
    """The bundled source cannot be exported without losing information."""


def css_name(name: str) -> str:
    if not isinstance(name, str) or not TOKEN_NAME.fullmatch(name):
        raise TokenError(f"Invalid token name: {name!r}")
    return name.replace(".", "-")


def number(value: object, context: str) -> str:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TokenError(f"{context}: expected a number, received {value!r}")
    if not math.isfinite(value):
        raise TokenError(f"{context}: expected a finite number")
    return format(value, ".12g")


def indexed(rows: list[dict], context: str) -> dict[str, dict]:
    result = {}
    normalized = set()
    for row in rows:
        name = row["name"]
        token = css_name(name)
        if name in result or token in normalized:
            raise TokenError(f"{context}: duplicate token {name!r}")
        result[name] = row
        normalized.add(token)
    return result


def resolve_alias(value: str, primitives: dict[str, str], trail: tuple[str, ...] = ()) -> str:
    if not isinstance(value, str):
        raise TokenError(f"Color must be a hex literal or alias: {value!r}")
    if COLOR_LITERAL.fullmatch(value):
        return value
    if value in trail:
        raise TokenError(f"Circular color alias: {' -> '.join((*trail, value))}")
    if value not in primitives:
        raise TokenError(f"Unresolved color alias: {value!r}")
    return resolve_alias(primitives[value], primitives, (*trail, value))


def rule(selector: str, values: dict[str, str]) -> str:
    declarations = "\n".join(f"  {name}: {value};" for name, value in sorted(values.items()))
    return f"{selector} {{\n{declarations}\n}}"


def load_tokens(skill_root: Path) -> dict[str, dict]:
    result = {}
    for name in ("color", "color_election", "size", "breakpoint", "typography", "play"):
        path = skill_root / "references" / "tokens" / f"{name}.json"
        try:
            result[name] = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise TokenError(f"{path.name}: {error}") from error
    return result


def render_css(tokens: dict[str, dict]) -> str:
    """Resolve source aliases and render stable CSS without ambient machine state."""
    try:
        return _render_css(tokens)
    except (KeyError, TypeError) as error:
        raise TokenError(f"Missing or invalid token field: {error}") from error


def _render_css(tokens: dict[str, dict]) -> str:
    colors = tokens["color"]["colors"]
    primitive_rows = indexed(colors["primitives"], "color primitives")
    primitives = {name: row["value"] for name, row in primitive_rows.items()}
    static = {f"--tv2-{css_name(name)}": resolve_alias(value, primitives)
              for name, value in primitives.items()}
    themes = {}
    for mode in ("light", "dark"):
        themes[mode] = {
            f"--tv2-{css_name(name)}": resolve_alias(row[mode], primitives)
            for name, row in indexed(colors["semantics"], "color semantics").items()
        }

    for group in tokens["color_election"]["colors"]["election"]:
        for scope, rows in sorted(group.items()):
            if scope == "default":
                static["--tv2-election-default"] = resolve_alias(rows["value"], primitives)
            else:
                for name, row in indexed(rows, f"election {scope}").items():
                    static[f"--tv2-election-{css_name(scope)}-{css_name(name)}"] = resolve_alias(
                        row["value"], primitives
                    )

    breakpoints = tokens["breakpoint"]["breakpoints"]
    for name, row in sorted(breakpoints.items()):
        static[f"--tv2-breakpoint-{css_name(name)}"] = number(row["web"], name) + "px"
    if breakpoints["sm"]["web"] != 0:
        raise TokenError("The web sm breakpoint must start at 0")
    if not 0 < breakpoints["md"]["web"] < breakpoints["lg"]["web"]:
        raise TokenError("The web md and lg breakpoints must be increasing")

    sizes = tokens["size"]["sizes"]
    size_primitives = indexed(sizes["primitives"], "size primitives")
    for name, row in size_primitives.items():
        static[f"--tv2-{css_name(name)}"] = number(row["value"], name) + "px"
    responsive = {mode: {} for mode in MODES}
    for name, row in indexed(sizes["semantics"], "size semantics").items():
        for mode in MODES:
            responsive[mode][f"--tv2-{css_name(name)}"] = number(row[mode], name) + "px"

    play_rows = indexed(tokens["play"]["sizes"]["semantics"], "Play sizes")
    appletv = {}
    for name, row in play_rows.items():
        for mode in (*MODES, "appletv"):
            alias = row[mode]
            if alias not in size_primitives:
                raise TokenError(f"Play {name}/{mode}: unresolved size alias {alias!r}")
            value = number(size_primitives[alias]["value"], name) + "px"
            target = appletv if mode == "appletv" else responsive[mode]
            target[f"--tv2-play-{css_name(name)}"] = value

    typography = tokens["typography"]
    fonts = indexed(typography["fontType"], "font mappings")
    blocks = ["/* Generated from the bundled TV 2 token JSON. */"]
    for name, font in sorted(fonts.items()):
        filename = font["font"]
        if Path(filename).name != filename or Path(filename).suffix != ".ttf":
            raise TokenError(f"Font {name}: expected a bundled TTF filename")
        weight = int(font["weight"])
        style = font["style"]
        if not 1 <= weight <= 1000 or style not in ("normal", "italic"):
            raise TokenError(f"Font {name}: invalid weight or style")
        blocks.append(rule("@font-face", {
            "font-family": '"TV2"',
            "font-style": style,
            "font-weight": str(weight),
            "font-display": "swap",
            "src": f'url("fonts/tv2/{filename}") format("truetype")',
        }))

    style_rows = indexed(typography["styles"], "typography styles")
    for name, row in style_rows.items():
        key = f"--tv2-{css_name(name)}"
        font_type = row["fontType"]
        if font_type not in fonts:
            raise TokenError(f"Style {name}: unknown font mapping {font_type!r}")
        font = fonts[font_type]
        static[f"{key}-font-weight"] = str(int(font["weight"]))
        static[f"{key}-font-style"] = font["style"]
        for mode in MODES:
            font_size = row["fontSize"]
            if "value" in font_size:
                size = font_size["tvvalue" if mode == "tv" else "value"]
            else:
                size = font_size[mode]
            responsive[mode][f"{key}-font-size"] = number(size, name) + "px"
            line_height = row["lineHeight"]
            if "relative" in line_height:
                line = number(line_height["relative"], name)
            else:
                line = number(line_height["tvabsolute" if mode == "tv" else "absolute"], name) + "px"
            responsive[mode][f"{key}-line-height"] = line

    blocks.extend((rule(":root", {**static, **responsive["sm"]}),
                   rule(':root, [data-tv2-theme="light"]', themes["light"]),
                   rule('[data-tv2-theme="dark"]', themes["dark"])))
    for mode in ("md", "lg"):
        breakpoint = number(breakpoints[mode]["web"], mode)
        block = rule(":root", responsive[mode])
        blocks.append(f"@media (min-width: {breakpoint}px) {{\n" +
                      "\n".join("  " + line for line in block.splitlines()) + "\n}")
    blocks.append(rule('[data-tv2-platform="tv"], [data-tv2-platform="appletv"]', responsive["tv"]))
    blocks.append(rule('[data-tv2-platform="appletv"]', appletv))
    for name in sorted(style_rows):
        key = f"--tv2-{css_name(name)}"
        blocks.append(rule(f".tv2-type-{css_name(name)}", {
            "font-family": '"TV2", Arial, sans-serif',
            "font-size": f"var({key}-font-size)",
            "font-weight": f"var({key}-font-weight)",
            "font-style": f"var({key}-font-style)",
            "line-height": f"var({key}-line-height)",
        }))
    return "\n\n".join(blocks) + "\n"


def expected_assets(skill_root: Path = SKILL_ROOT) -> dict[str, bytes]:
    tokens = load_tokens(skill_root)
    assets = {"tv2-tokens.css": render_css(tokens).encode("utf-8")}
    for source, destination in (("assets/fonts/tv2", "fonts/tv2"),
                                ("assets/icons/basic", "icons/basic"),
                                ("assets/web", ".")):
        directory = skill_root / source
        if not directory.exists():
            if source == "assets/web":
                continue
            raise TokenError(f"Missing bundled asset directory: {source}")
        for path in sorted(directory.rglob("*")):
            if path.is_file():
                relative = (Path(destination) / path.relative_to(directory)).as_posix()
                if relative in assets:
                    raise TokenError(f"Asset output collision: {relative}")
                assets[relative] = path.read_bytes()
    for font in tokens["typography"]["fontType"]:
        if f"fonts/tv2/{font['font']}" not in assets:
            raise TokenError(f"Missing bundled font: {font['font']}")
    return dict(sorted(assets.items()))


def export(output: Path, *, check: bool = False, skill_root: Path = SKILL_ROOT) -> list[str]:
    output = output.resolve()
    for source in ("assets/web", "assets/fonts/tv2", "assets/icons/basic"):
        directory = (skill_root / source).resolve()
        if output == directory or directory in output.parents:
            raise TokenError(f"Output must be outside the bundled source directory {source}")
    assets = expected_assets(skill_root)
    mismatches = []
    for relative, content in assets.items():
        path = output / relative
        if check:
            if not path.is_file() or path.read_bytes() != content:
                mismatches.append(relative)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
    return mismatches


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, epilog=
        "Examples: --output public/assets/tv2; --output public/assets/tv2 --check. "
        "Uses Python 3.10+ standard library, offline. Exit codes: 0 success, 1 mismatch/source error, 2 invalid arguments.")
    parser.add_argument("--output", type=Path, required=True, help="Destination for the portable web assets")
    parser.add_argument("--check", action="store_true", help="Check existing output bytes without writing files")
    args = parser.parse_args(argv)
    try:
        mismatches = export(args.output, check=args.check)
    except (TokenError, OSError, ValueError) as error:
        parser.exit(1, f"Export failed: {error}\n")
    if mismatches:
        print("Assets differ: " + ", ".join(mismatches), file=sys.stderr)
        return 1
    print(json.dumps({"status": "verified" if args.check else "exported", "output": str(args.output.resolve())}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
