# TV2 font files

Exact face mapping: [typography.json](../tokens/typography.json).

The bundled TrueType files map to these font types.
Declare the matching weight and style when loading each face.

| Font type | Weight | Style | File |
| --------- | -----: | ----- | ---- |
| `regular` | 400 | `normal` | [TV2-Regular.ttf](../../assets/fonts/tv2/TV2-Regular.ttf) |
| `regularItalic` | 400 | `italic` | [TV2-RegularItalic.ttf](../../assets/fonts/tv2/TV2-RegularItalic.ttf) |
| `light` | 300 | `normal` | [TV2-Light.ttf](../../assets/fonts/tv2/TV2-Light.ttf) |
| `lightItalic` | 300 | `italic` | [TV2-LightItalic.ttf](../../assets/fonts/tv2/TV2-LightItalic.ttf) |
| `medium` | 500 | `normal` | [TV2-Medium.ttf](../../assets/fonts/tv2/TV2-Medium.ttf) |
| `mediumItalic` | 500 | `italic` | [TV2-MediumItalic.ttf](../../assets/fonts/tv2/TV2-MediumItalic.ttf) |
| `bold` | 700 | `normal` | [TV2-Bold.ttf](../../assets/fonts/tv2/TV2-Bold.ttf) |
| `boldItalic` | 700 | `italic` | [TV2-BoldItalic.ttf](../../assets/fonts/tv2/TV2-BoldItalic.ttf) |
| `black` | 900 | `normal` | [TV2-Black.ttf](../../assets/fonts/tv2/TV2-Black.ttf) |
| `blackItalic` | 900 | `italic` | [TV2-BlackItalic.ttf](../../assets/fonts/tv2/TV2-BlackItalic.ttf) |

The directory also contains [TV2.woff](../../assets/fonts/tv2/TV2.woff) and [TV2.woff2](../../assets/fonts/tv2/TV2.woff2).
The typography JSON does not map those files to a weight or style.
Use the mapped TrueType files when an exact face is required, or inspect the webfont metadata before assigning it.
