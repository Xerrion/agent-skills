# Spacing tokens

Exact definitions: [size.json](../tokens/size.json).

The spacing scale uses a 4 px base unit and also includes 1 px and 2 px primitives.
Use named size tokens for spacing, padding, gaps, and dimensions.
Do not replace a token with a raw value in component code.

Padding controls space inside a component; a gap separates its children; a margin separates it from surrounding content.
The recorded component rules assign specific size tokens to some of these roles. A size token's existence alone does not assign it to a component.
For example, the bundled List source record assigns `size.12` to side padding and records a 12 px gap without identifying its layout level. The Accordion record assigns `size.12` to the text/icon gap. Use the individual component's current pinned measurements for exact geometry.

The 21 primitives are:

`size.1`, `size.2`, `size.4`, `size.8`, `size.12`, `size.16`, `size.20`, `size.24`, `size.28`, `size.32`, `size.36`, `size.40`, `size.44`, `size.48`, `size.56`, `size.64`, `size.80`, `size.96`, `size.112`, `size.128`, and `size.144`.

## Responsive dimensions

`*.step` and `*.jump` tokens adapt across `sm`, `md`, `lg`, and `tv`.
Select the token, then use its value for the target breakpoint.
Values below are pixels.

| Token           |  sm |  md |  lg |  tv |
| --------------- | --: | --: | --: | --: |
| `size.0.step`   |   0 |   8 |   8 |  16 |
| `size.12.step`  |  12 |  20 |  20 |  24 |
| `size.16.step`  |  16 |  24 |  24 |  32 |
| `size.20.step`  |  20 |  28 |  28 |  40 |
| `size.24.step`  |  24 |  32 |  32 |  48 |
| `size.28.step`  |  28 |  36 |  36 |  56 |
| `size.32.step`  |  32 |  40 |  40 |  64 |
| `size.40.step`  |  40 |  48 |  48 |  80 |
| `size.48.step`  |  48 |  56 |  56 |  96 |
| `size.4.jump`   |   4 |   8 |   8 |   8 |
| `size.8.jump`   |   8 |  16 |  16 |  16 |
| `size.16.jump`  |  16 |  32 |  32 |  32 |
| `size.32.jump`  |  32 |  64 |  64 |  64 |
| `size.64.jump`  |  64 | 128 | 128 | 128 |
| `size.128.jump` | 128 | 256 | 256 | 256 |

Select the [target platform and breakpoint](breakpoints.md) before resolving a responsive value.
