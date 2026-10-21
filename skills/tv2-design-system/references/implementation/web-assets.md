# Exporting web assets

Run the bundled generator with Python 3. Replace `/path/to/tv2-design-system` with this skill's location and select the application's actual static asset directory.

```sh
python3 /path/to/tv2-design-system/scripts/build_web_assets.py --output public/assets/tv2
```

The generator uses only the bundled sources and Python's standard library. It produces `tv2-tokens.css`, copies the available web baseline files, mapped TV2 fonts, and basic icons, and preserves the asset bytes. See the [web baseline](web-baseline.md) for its public classes.

For a stylesheet served at `/assets/tv2/tv2-tokens.css`, its font URLs resolve relative to that stylesheet.
The skill's local filesystem paths are not deployed web URLs.

| Skill resource | Application resource | Browser URL |
| --- | --- | --- |
| Generated token stylesheet | `public/assets/tv2/tv2-tokens.css` | `/assets/tv2/tv2-tokens.css` |
| `assets/web/tv2-components.css` | `public/assets/tv2/tv2-components.css` | `/assets/tv2/tv2-components.css` |
| `assets/fonts/tv2/TV2-Regular.ttf` | `public/assets/tv2/fonts/tv2/TV2-Regular.ttf` | `/assets/tv2/fonts/tv2/TV2-Regular.ttf` |
| `assets/icons/basic/info_circle.svg` | `public/assets/tv2/icons/basic/info_circle.svg` | `/assets/tv2/icons/basic/info_circle.svg` |

Copy any other selected artwork into the same asset tree before linking to it. For example, copy [tv2_color.svg](../../assets/logos/dark/tv2_color.svg) to `public/assets/tv2/logos/dark/tv2_color.svg` for the [panel example](web-example.md).
The `public/` directory is an example. Adjust it and all browser URLs for the consuming application's static directory and base path.

Preserve artwork aspect ratios, geometry, fills, and strokes. For decorative icons use an empty accessible name; give controls their own meaningful label.

To verify that the exported files still match this bundle, run the generator against the same directory with `--check`.

Successful commands print JSON with `status` and `output`; diagnostics go to stderr. Exit codes are 0 for success, 1 for a source error or export mismatch, and 2 for invalid arguments. `--help` includes examples. Exports can be repeated and preserve unrelated destination files; `--check` writes nothing. Reserve `tv2-tokens.css` for generated output.
