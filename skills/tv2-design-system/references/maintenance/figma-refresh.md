# Refreshing Figma measurements

Ordinary skill use reads the bundled records. A maintainer with access to the original file can refresh them through the Figma connector and supply the saved JSON to everyone else.

1. Generate the script for one registered record, using the actual capture date:

   ```sh
   python3 scripts/maintain_sources.py capture-script --record button --captured-on 2026-10-21 > /tmp/tv2-button-capture.js
   ```

2. Execute that file's code through the Figma connector's `use_figma` tool against file `cjU0zuiL2r8YXsGmnNxxy2`. Follow the connector's current usage instructions. The code reads one page, switches page context once, and returns data. It creates no canvas nodes. Independent pages can be captured with separate connector calls. Save each returned object as `<record>.json` in an import directory.

3. Compare the saved records:

   ```sh
   python3 scripts/maintain_sources.py check --figma-dir /tmp/tv2-figma-import
   ```

4. Stage the changed records for [candidate review](staged-review.md):

   ```sh
   python3 scripts/maintain_sources.py stage --figma-dir /tmp/tv2-figma-import --output /tmp/tv2-figma-review
   ```

Record names, page IDs, capture depths, and layout frame IDs live in the [source registry](sources.json). Available names are `button`, `icon-button`, `input`, `section-notice`, `snackbar`, `modal-platform`, and `layout-free`. Register a new component there before importing its local record, and add its atomic component reference. Bundle validation checks the registered set instead of a fixed record count. The [record format](../implementation/figma-records.md) describes the returned data.

A directory can contain a subset of those records. Missing files leave the corresponding bundled records unchanged; they do not signal deletion. Unknown filenames, wrong file/page identity, missing measurements, and unresolved variable aliases fail validation. Changing only `capturedOn` does not count as a design change.

The scripts do not poll Figma or store credentials. Access denial, a missing registered node, and connector call limits stop the capture. Keep the existing local snapshot and retry when access is available; a repository-only check must continue to report Figma as unchecked. If the connector's response limit is exceeded, reduce the registered capture depth or narrow the capture before importing. Record the resulting coverage limits in that component's reference.

The component capture records native defaults and variant metrics, not preview screenshots or every variant descendant. Replace affected local screenshots separately when their appearance changes. Asset URLs returned by other Figma tools are temporary; download approved artwork into the bundle before using it.
