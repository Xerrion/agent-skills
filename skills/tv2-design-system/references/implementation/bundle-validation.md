# Bundle validation

Run from the skill folder with Python 3:

```sh
python3 scripts/validate_bundle.py
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/build_web_assets.py --output /tmp/tv2-web
python3 scripts/build_web_assets.py --output /tmp/tv2-web --check
```

The bundle validator checks local Markdown links and anchors, source checksums, Figma record references, and exported CSS/HTML resource paths and variables. It runs without a Figma account or source checkout. The export tests compare bytes across independent output directories and check token conversion against the bundled JSON. A portability test copies the entire skill to a new location, clears account configuration from the subprocess environment, blocks socket connections, then validates and exports that copy. Its exported files must match the original bundle byte-for-byte.

The [integrity record](../governance/source-integrity.json) pins the captured source data and implementation assets. An intentional source refresh must update that record after reviewing the changed sources; do not overwrite checksums merely to hide a failed check.

These checks validate the local package and deterministic export. They do not establish browser rendering, keyboard behavior, accessibility compliance, or pixel-identical free-form designs. Use [application verification](verification.md) for the consuming application.

The validator also checks this bundle's plain single-line metadata, the containing directory's name, and the evaluation fixture paths. This is not a general YAML validator. Use `--json` for machine-readable counts, `--skill-root <directory>` for another copy, or `--help` for usage. Exit codes are 0 for success, 1 for failed checks, and 2 for invalid arguments. Diagnostics go to stderr.
