# Mapping dimension tokens to CSS

The [web asset generator](web-assets.md) writes named dimensions into `tv2-tokens.css`.
Use its properties when using the generated baseline.

| JSON definition | Generated CSS |
| --- | --- |
| Primitive `size.16` | `--tv2-size-16: 16px` |
| Responsive `size.24.step` | `--tv2-size-24-step`, selected for `sm`, `md`, `lg`, or explicit `tv` layout |

Add `px` to dimension values. Preserve the named token in component CSS, for example `padding: var(--tv2-size-16)`.
Resolve [Play layout aliases](../layout/play.md) through the primitive [size tokens](../tokens/size.json).
The [breakpoint reference](../foundations/breakpoints.md) defines platform contexts and wider desktop behavior.
