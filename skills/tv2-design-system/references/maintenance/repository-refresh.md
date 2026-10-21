# Refreshing repository sources

Use `scripts/maintain_sources.py` when a newer `tv2/designsystem` commit is available locally. The script reads Git objects at the selected commit. It does not pull, change branches, or read uncommitted source edits.

```sh
python3 scripts/maintain_sources.py check --repo /path/to/designsystem
python3 scripts/maintain_sources.py stage --repo /path/to/designsystem --output /tmp/tv2-repo-review
```

Use `--ref <commit-or-branch>` to compare a specific revision. `HEAD` is the default. Update the source checkout through its normal Git workflow before checking a newer remote revision.

The [source registry](sources.json) pins the source commit and Git object IDs. Copy rules cover the six current token files, original artwork and font formats, favicon PNGs, component previews, and component design logs. Foundation/product documentation and component metadata are watched for changes even when they have no direct copied destination. Generated icon PNG duplicates and repository tooling remain excluded.

`check` prints a bounded JSON summary with added, changed, and removed inputs and affected atomic references. Use `--report /tmp/tv2-source-report.json` to save all details, or `--details` to explicitly print the full report. Exit codes are 0 for unchanged selected sources, 1 for detected changes, and 2 for an invalid source or command. `figmaStatus: not-checked` is explicit when no Figma import was provided. A successful repository check says nothing about live Figma freshness.

`stage` writes a new directory containing `tv2-design-system/`, `report.json`, `source.diff`, and `review.txt`. The candidate folder retains the skill name required by the Agent Skills format. Changed documentation or component metadata without a copied destination is saved under `upstream/` for review. The installed skill stays unchanged. Refer to [candidate review](staged-review.md) before adopting the copy.

New component metadata and new asset files appear in the report. Add their individual component reference or artwork catalog entry during review. A new foundation or product token format needs an explicit mapping and exporter support; watching its file does not make that new schema supported automatically.
