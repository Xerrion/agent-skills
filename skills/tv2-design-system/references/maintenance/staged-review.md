# Reviewing a staged update

The staging command produces a candidate copy. Exit code 0 means that the staging operation completed, not that the source changes are ready to publish.

1. Read `report.json`, `source.diff`, and `review.txt` in the staging directory. `validationFailures` contains structural problems such as references to deleted artwork or unresolved web tokens. The installed skill and source repository remain unchanged.
2. Update the listed atomic references inside `tv2-design-system/`. Numeric tables and written Figma measurements are authored references and need review when their inputs change. Check any affected web component CSS and specimen against the new source. Preserve documented application choices and identify changed source limitations.
3. Run `python3 scripts/validate_bundle.py` and `python3 -m unittest discover -s scripts -p 'test_*.py'` from the candidate's `tv2-design-system/` directory. Compare the relevant specimens in both themes in the consuming application's browser.
4. If you intentionally changed pinned assets during review, run `python3 scripts/maintain_sources.py seal` from the candidate's `tv2-design-system/` directory, then rerun validation. This command is restricted to staged candidates. Never regenerate checksums to hide unexplained edits. Individual Figma records retain their capture dates; the integrity record's aggregate date is the latest included capture.
5. Adopt the reviewed files through the skill repository's normal diff and commit workflow. Keep a backup when the skill is outside version control. The maintenance script deliberately stops at the candidate and does not replace or delete the installed folder.

Source changes are copied deterministically. Written interpretation, new component APIs, and visual behavior still require review. The affected-file list is a starting point; a shared token can affect more rendered screens than static links reveal.
