"""Exercise source drift and staged updates against disposable Git repositories."""

import copy
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from build_web_assets import SKILL_ROOT
from maintain_sources import (REGISTRY, capture_script, compare, json_bytes,
                              repository_tree, stage, validate_import)
from validate_bundle import check_integrity


class SourceMaintenanceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="tv2-source-tests-")
        self.addCleanup(self.temporary.cleanup)
        self.folder = Path(self.temporary.name)
        self.root = self.folder / "installed" / "tv2-design-system"
        shutil.copytree(SKILL_ROOT, self.root, ignore=shutil.ignore_patterns("__pycache__"))
        self.repo = self.folder / "upstream"
        self.repo.mkdir()
        self.git("init", "-b", "source-fixture")
        self.git("config", "user.name", "Source fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.write("foundation/color.json", (self.root / "references/tokens/color.json").read_bytes())
        self.write("foundation/color.md", b"# Color source\n")
        self.write("assets/icons/basic/info_circle.svg", (self.root / "assets/icons/basic/info_circle.svg").read_bytes())
        self.commit()
        self.registry = json.loads((self.root / REGISTRY).read_text())
        revision, files = repository_tree(self.repo, "HEAD")
        self.registry["repository"].update(revision=revision, files=files)
        (self.root / REGISTRY).write_bytes(json_bytes(self.registry))

    def git(self, *arguments):
        return subprocess.run(["git", "-C", str(self.repo), *arguments], check=True,
                              capture_output=True).stdout

    def write(self, relative, content):
        path = self.repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)

    def commit(self):
        self.git("add", ".")
        self.git("commit", "-m", "chore: update source fixture")

    def test_unchanged_commit_and_uncommitted_edits_are_distinct(self):
        report, _, _ = compare(self.root, self.repo)
        self.assertFalse(report["changes"])
        self.assertEqual(report["figmaStatus"], "not-checked")
        self.write("foundation/color.md", b"Uncommitted source edit\n")
        self.assertFalse(compare(self.root, self.repo)[0]["changes"])

    def test_changed_tokens_and_added_assets_stage_without_changing_installed_skill(self):
        previous = (self.root / "references/tokens/color.json").read_bytes()
        colors = json.loads(previous)
        colors["colors"]["primitives"][0]["value"] = "#123456"
        self.write("foundation/color.json", json_bytes(colors))
        self.write("assets/icons/basic/new.svg", b'<svg xmlns="http://www.w3.org/2000/svg"/>')
        self.commit()
        report, registry, payloads = compare(self.root, self.repo)
        self.assertEqual(len(report["changes"]), 2)
        self.assertIn("references/foundations/color-semantic.md", report["review"])
        self.assertIn("references/artwork/icons-basic.md", report["review"])
        output = self.folder / "review"
        stage(self.root, output, report, registry, payloads)
        self.assertEqual((self.root / "references/tokens/color.json").read_bytes(), previous)
        self.assertEqual(json.loads((output / "tv2-design-system/references/tokens/color.json").read_text()), colors)
        self.assertTrue((output / "tv2-design-system/assets/icons/basic/new.svg").is_file())
        self.assertIn("#123456", (output / "source.diff").read_text())
        self.assertEqual(json.loads((output / "report.json").read_text())["status"], "needs-reference-review")
        check_integrity(output / "tv2-design-system")

    def test_watch_only_prose_changes_require_reference_review(self):
        self.write("foundation/color.md", b"# Changed semantic guidance\n")
        self.commit()
        report, _, payloads = compare(self.root, self.repo)
        self.assertEqual(report["changes"][0]["source"], "foundation/color.md")
        self.assertIn("references/foundations/color-semantic.md", report["review"])
        self.assertEqual(payloads, {})

    def test_cli_bounds_stdout_and_preserves_full_report(self):
        marker = "Long upstream guidance. " * 10000
        self.write("foundation/color.md", marker.encode())
        self.commit()
        destination = self.folder / "full-report.json"
        result = subprocess.run([sys.executable, "-B", str(self.root / "scripts/maintain_sources.py"),
                                 "--skill-root", str(self.root), "check", "--repo", str(self.repo),
                                 "--report", str(destination)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1, result.stderr)
        summary = json.loads(result.stdout)
        self.assertEqual(summary["changeCount"], 1)
        self.assertLess(len(result.stdout), 5000)
        self.assertEqual(json.loads(destination.read_text())["changes"][0]["upstreamText"], marker)

    def test_removed_artwork_is_reported_and_broken_links_are_visible(self):
        (self.repo / "assets/icons/basic/info_circle.svg").unlink()
        self.commit()
        report, registry, payloads = compare(self.root, self.repo)
        self.assertEqual(report["changes"][0]["kind"], "removed")
        output = self.folder / "removal-review"
        stage(self.root, output, report, registry, payloads)
        staged = json.loads((output / "report.json").read_text())
        self.assertTrue(any(f["check"] == "links" for f in staged["validationFailures"]))
        self.assertTrue((self.root / "assets/icons/basic/info_circle.svg").is_file())

    def import_record(self):
        self.imports = self.folder / "figma-import"
        self.imports.mkdir()
        self.record = json.loads((self.root / "references/figma/button.json").read_text())
        return self.imports / "button.json"

    def test_figma_timestamp_only_changes_do_not_create_drift(self):
        path = self.import_record()
        self.record["source"]["capturedOn"] = "2026-10-22"
        path.write_bytes(json_bytes(self.record))
        report, _, payloads = compare(self.root, figma_dir=self.imports)
        self.assertEqual(report["figmaChecked"], ["button"])
        self.assertFalse(report["changes"])
        self.assertFalse(payloads)

    def test_figma_geometry_changes_point_to_reference_and_component_css(self):
        path = self.import_record()
        self.record["sets"][0]["defaultTree"]["height"] = 48
        group = self.record["sets"][0]
        default = next(v for v in group["variants"] if v["id"] == group["defaultVariantId"])
        default["values"][group["metricColumns"].index("height")] = 48
        path.write_bytes(json_bytes(self.record))
        report, _, payloads = compare(self.root, figma_dir=self.imports)
        self.assertIn("references/components/button.md", report["review"])
        self.assertIn("assets/web/components/button.css", report["review"])
        self.assertIn("references/figma/button.json", payloads)

    def test_bad_figma_identity_and_missing_aliases_are_rejected(self):
        path = self.import_record()
        config = self.registry["figma"]["records"]["button"]
        wrong = copy.deepcopy(self.record)
        wrong["source"]["pageId"] = "0:0"
        with self.assertRaisesRegex(ValueError, "registered"):
            validate_import(wrong, config, self.registry["figma"]["fileKey"])
        self.record["variables"] = {}
        path.write_bytes(json_bytes(self.record))
        with self.assertRaisesRegex(ValueError, "unresolved"):
            compare(self.root, figma_dir=self.imports)

    def test_new_components_are_listed_without_inventing_a_reference(self):
        self.write("components/new-control/new-control.json", b'{"name":"New Control"}')
        self.commit()
        report, _, _ = compare(self.root, self.repo)
        self.assertIn("references/components/new-control.md", report["review"])
        self.assertIn("references/COMPONENTS.md", report["review"])
        self.assertFalse((self.root / "references/components/new-control.md").exists())

    def test_existing_and_nested_stage_directories_are_rejected(self):
        report, registry, payloads = compare(self.root, self.repo)
        with self.assertRaisesRegex(ValueError, "new directory"):
            stage(self.root, self.root / "nested", report, registry, payloads)
        with self.assertRaisesRegex(ValueError, "new directory"):
            stage(self.root, self.folder, report, registry, payloads)

    def test_capture_templates_are_complete_and_javascript_parses(self):
        for slug in self.registry["figma"]["records"]:
            code = capture_script(self.root, slug, "2026-10-21")
            self.assertNotIn("PAGE_ID", code)
            self.assertNotIn("CAPTURE_DEPTH", code)
            self.assertNotIn("CAPTURED_ON", code)
            self.assertNotIn("LAYOUT_IDS", code)
            self.assertEqual(code.count("setCurrentPageAsync"), 1)
            if shutil.which("node"):
                parser = "const fs=require('fs'); const A=Object.getPrototypeOf(async function(){}).constructor; new A('figma',fs.readFileSync(0,'utf8'));"
                result = subprocess.run(["node", "-e", parser], input=code, text=True, capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_seal_refuses_the_installed_skill(self):
        result = subprocess.run([sys.executable, "-B", str(self.root / "scripts/maintain_sources.py"),
                                 "--skill-root", str(self.root), "seal"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("staged candidate", result.stderr)


if __name__ == "__main__":
    unittest.main()
