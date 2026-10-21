"""Check that a relocated skill works with no network or account configuration."""

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from build_web_assets import SKILL_ROOT, expected_assets


class BundlePortabilityTests(unittest.TestCase):
    def test_relocated_skill_exports_and_validates_without_network(self):
        with tempfile.TemporaryDirectory(prefix="tv2-offline-") as temporary:
            root = Path(temporary)
            relocated = root / "relocated" / "tv2-design-system"
            shutil.copytree(SKILL_ROOT, relocated, ignore=shutil.ignore_patterns("__pycache__"))
            output = root / "portable-assets"
            bootstrap = """
import runpy, socket, sys
from pathlib import Path
def unavailable(*args, **kwargs):
    raise AssertionError('Network access is unavailable in the offline test')
socket.socket.connect = unavailable
socket.socket.connect_ex = unavailable
socket.create_connection = unavailable
root = Path(sys.argv[1])
output = Path(sys.argv[2])
sys.path.insert(0, str(root / 'scripts'))
from build_web_assets import export
export(output)
sys.argv = [str(root / 'scripts/validate_bundle.py')]
runpy.run_path(sys.argv[0], run_name='__main__')
"""
            result = subprocess.run(
                [sys.executable, "-I", "-B", "-c", bootstrap, str(relocated), str(output)],
                cwd=root,
                env={"PATH": os.defpath},
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("Bundle verified:", result.stdout)
            actual = {p.relative_to(output).as_posix(): p.read_bytes()
                      for p in output.rglob("*") if p.is_file()}
            self.assertEqual(actual, expected_assets(SKILL_ROOT))


if __name__ == "__main__":
    unittest.main()
