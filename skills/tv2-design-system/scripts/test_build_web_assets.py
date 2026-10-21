#!/usr/bin/env python3
"""Verify the portable TV 2 web export without third-party dependencies."""

from __future__ import annotations

import copy
import json
import re
import tempfile
import unittest
from pathlib import Path

import build_web_assets as builder


def declarations(body: str) -> dict[str, str]:
    return dict(re.findall(r"^\s*(--[\w-]+): ([^;]+);$", body, re.MULTILINE))


def block(css: str, selector: str) -> dict[str, str]:
    match = re.search(r"^" + re.escape(selector) + r" \{\n(.*?)\n\}", css, re.MULTILINE | re.DOTALL)
    if not match:
        raise AssertionError(f"Missing CSS selector {selector}")
    return declarations(match.group(1))


class WebExportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.tokens = builder.load_tokens(builder.SKILL_ROOT)
        cls.css = builder.render_css(cls.tokens)

    def test_aliases_resolve_and_invalid_aliases_fail(self) -> None:
        self.assertEqual(builder.resolve_alias("a", {"a": "b", "b": "#12345678"}), "#12345678")
        with self.assertRaisesRegex(builder.TokenError, "Unresolved color alias"):
            builder.resolve_alias("missing", {})
        with self.assertRaisesRegex(builder.TokenError, "Circular color alias"):
            builder.resolve_alias("a", {"a": "b", "b": "a"})
        invalid = copy.deepcopy(self.tokens)
        invalid["play"]["sizes"]["semantics"][0]["sm"] = "size.missing"
        with self.assertRaisesRegex(builder.TokenError, "unresolved size alias"):
            builder.render_css(invalid)

    def test_all_theme_colors_are_concrete_and_match_source(self) -> None:
        colors = self.tokens["color"]["colors"]
        primitives = {row["name"]: row["value"] for row in colors["primitives"]}
        for mode, selector in (("light", ':root, [data-tv2-theme="light"]'),
                               ("dark", '[data-tv2-theme="dark"]')):
            actual = block(self.css, selector)
            self.assertEqual(len(actual), len(colors["semantics"]))
            for row in colors["semantics"]:
                value = row[mode]
                expected = primitives[value] if value in primitives else value
                self.assertEqual(actual["--tv2-" + row["name"].replace(".", "-")], expected)
                self.assertTrue(expected.startswith("#"))
        self.assertEqual(block(self.css, '[data-tv2-theme="dark"]')["--tv2-surface-primary"], "#000523")
        self.assertEqual(block(self.css, ':root, [data-tv2-theme="light"]')["--tv2-content-system-error"], "#9e0f1b")

    def test_election_and_size_primitives_are_exported(self) -> None:
        root = block(self.css, ":root")
        self.assertEqual(root["--tv2-election-default"], "#8d95a5")
        self.assertEqual(root["--tv2-election-us-democrats"], "#3264ff")
        self.assertEqual(root["--tv2-election-fv-nordatlantiskemandater"], "#4a5870")
        self.assertEqual(root["--tv2-size-144"], "144px")
        self.assertEqual(root["--tv2-size-0-step"], "0px")
        self.assertEqual(root["--tv2-play-page-margin"], "16px")

    def test_all_type_styles_have_complete_font_mapping(self) -> None:
        root = block(self.css, ":root")
        typography = self.tokens["typography"]
        fonts = {row["name"]: row for row in typography["fontType"]}
        self.assertEqual(self.css.count("@font-face {"), len(fonts))
        self.assertEqual(self.css.count(".tv2-type-"), len(typography["styles"]))
        for row in typography["styles"]:
            name = row["name"].replace(".", "-")
            font = fonts[row["fontType"]]
            self.assertEqual(root[f"--tv2-{name}-font-weight"], font["weight"])
            self.assertEqual(root[f"--tv2-{name}-font-style"], font["style"])
            class_body = re.search(r"\.tv2-type-" + re.escape(name) + r" \{([^}]+)\}", self.css).group(1)
            for property_name in ("font-size", "font-weight", "font-style", "line-height"):
                self.assertIn(f"{property_name}: var(--tv2-{name}-{property_name});", class_body)
            self.assertIn('font-family: "TV2", Arial, sans-serif;', class_body)
        self.assertEqual(root["--tv2-body-small-italic-font-style"], "italic")
        self.assertEqual(root["--tv2-body-small-italic-font-weight"], "400")
        self.assertEqual(root["--tv2-utility-small-medium-line-height"], "18px")
        self.assertEqual(root["--tv2-heading-large-line-height"], "1.1")
        invalid = copy.deepcopy(self.tokens)
        del invalid["typography"]["styles"][0]["fontSize"]["md"]
        with self.assertRaisesRegex(builder.TokenError, "Missing or invalid token field"):
            builder.render_css(invalid)

    def test_responsive_breakpoints_and_explicit_tv_mode(self) -> None:
        media = re.findall(r"@media \(min-width: (\d+)px\) \{\n  :root \{\n(.*?)\n  \}\n\}", self.css, re.DOTALL)
        self.assertEqual([int(width) for width, _ in media], [680, 1024])
        def values_at(width: int, platform: str = "web") -> dict[str, str]:
            values = block(self.css, ":root")
            for boundary, body in media:
                if width >= int(boundary):
                    values.update(declarations(body))
            if platform in ("tv", "appletv"):
                values.update(block(self.css, '[data-tv2-platform="tv"], [data-tv2-platform="appletv"]'))
            if platform == "appletv":
                values.update(block(self.css, '[data-tv2-platform="appletv"]'))
            return values
        for width, heading, margin in ((679, "36px", "16px"), (680, "48px", "24px"),
                                       (1023, "48px", "24px"), (1024, "60px", "64px"),
                                       (3840, "60px", "64px")):
            with self.subTest(width=width):
                values = values_at(width)
                self.assertEqual(values["--tv2-heading-3xlarge-font-size"], heading)
                self.assertEqual(values["--tv2-play-page-margin"], margin)
        for width in (360, 680, 1024, 3840):
            values = values_at(width, "tv")
            self.assertEqual(values["--tv2-heading-3xlarge-font-size"], "76px")
            self.assertEqual(values["--tv2-utility-small-medium-line-height"], "36px")
            self.assertEqual(values["--tv2-play-page-margin"], "144px")
            self.assertEqual(values_at(width, "appletv")["--tv2-play-page-margin"], "80px")

    def test_exports_are_portable_and_byte_identical(self) -> None:
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            left, right = Path(first), Path(second)
            builder.export(left)
            builder.export(right)
            def files(directory: Path) -> dict[str, bytes]:
                return {path.relative_to(directory).as_posix(): path.read_bytes()
                        for path in directory.rglob("*") if path.is_file()}
            self.assertEqual(files(left), files(right))
            self.assertNotIn(str(builder.SKILL_ROOT), (left / "tv2-tokens.css").read_text())
            source = builder.SKILL_ROOT / "assets/icons/basic"
            for icon in source.glob("*.svg"):
                self.assertEqual((left / "icons/basic" / icon.name).read_bytes(), icon.read_bytes())
            self.assertEqual(builder.export(left, check=True), [])
            (left / "icons/basic/info_circle.svg").write_text("damaged", encoding="utf-8")
            self.assertEqual(builder.export(left, check=True), ["icons/basic/info_circle.svg"])

    def test_source_directory_cannot_be_used_as_output(self) -> None:
        for relative in ("assets/web", "assets/web/nested", "assets/fonts/tv2", "assets/icons/basic"):
            with self.assertRaisesRegex(builder.TokenError, "outside the bundled source"):
                builder.export(builder.SKILL_ROOT / relative)


    def test_cli_export_and_check_return_structured_success(self) -> None:
        import contextlib
        import io
        with tempfile.TemporaryDirectory() as temporary:
            for arguments, status in (([], "exported"), (["--check"], "verified")):
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    result = builder.main(["--output", temporary, *arguments])
                self.assertEqual(result, 0)
                payload = json.loads(output.getvalue())
                self.assertEqual(payload["status"], status)
                self.assertEqual(payload["output"], str(Path(temporary).resolve()))


if __name__ == "__main__":
    unittest.main()
