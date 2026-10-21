# Mapping color tokens to CSS

The [web asset generator](web-assets.md) writes the full bundled color palette and both semantic themes into `tv2-tokens.css`.
Use its `--tv2-*` properties when using the generated baseline.

| JSON definition | Generated CSS |
| --- | --- |
| Primitive `blue.500` | `--tv2-blue-500: #3264ff` |
| Semantic `content.primary` | `--tv2-content-primary`, resolved for the active theme |

Names replace dots with hyphens and add the `tv2-` prefix.
Apply `data-tv2-theme="light"` or `data-tv2-theme="dark"` to the theme root.
Keep custom properties in a selector that applies to the consuming element.

Resolve primitive aliases through [color.json](../tokens/color.json). Preserve literal hexadecimal values and alpha channels as supplied.
For example, light `content.primary` resolves to `#000523`; dark `content.primary` resolves to `#ffffff`.
Use the same source token when producing native platform colors or fixed email styles.
