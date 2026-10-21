# Semantic colors

Exact definitions: [color.json](../tokens/color.json).

Use semantic tokens for text, surfaces, input strokes, focus, and system feedback.
Choose the light or dark value for the active theme, then resolve any primitive reference.
Preserve explicit hexadecimal values and alpha channels.
Do not infer a missing state color from a neighboring palette step.

The 38 semantic tokens define a light and dark value for each UI role.
Hexadecimal entries are literal values; the other entries name primitive tokens.

| Token | Light reference | Light value | Dark reference | Dark value |
| ----- | --------------- | ----------- | -------------- | ---------- |
| `content.disabled` | `neutral.300` | `#b5bac5` | `neutral.600` | `#4a5870` |
| `content.inverted` | `white` | `#ffffff` | `midnight` | `#000523` |
| `content.link.default` | `blue.600` | `#244dea` | `blue.400` | `#64a3fb` |
| `content.link.default.hover` | `blue.700` | `#1339c8` | `blue.300` | `#8cc8f5` |
| `content.link.visited` | `violet.600` | `#6140dc` | `violet.300` | `#a596fa` |
| `content.link.visited.hover` | `violet.800` | `#45209a` | `violet.200` | `#c9b9fe` |
| `content.primary` | `midnight` | `#000523` | `white` | `#ffffff` |
| `content.secondary` | `neutral.600` | `#4a5870` | `neutral.400` | `#8d95a5` |
| `content.system.error` | `red.700` | `#9e0f1b` | `red.300` | `#eb8c82` |
| `content.system.info` | `blue.700` | `#1339c8` | `blue.400` | `#64a3fb` |
| `content.system.success` | `green.700` | `#11712c` | `grassgreen.300` | `#C3F087` |
| `content.system.warning` | `yellow.800` | `#755c00` | `yellow.600` | `#ebbb0e` |
| `stroke.focus.outline` | `blue.500` | `#3264ff` | `blue.400` | `#64a3fb` |
| `stroke.focus.outline.tv` | `opacity.white.600` | `#f6f7f851` | `opacity.white.800` | `#f6f7f8a3` |
| `stroke.input.default` | `neutral.500` | `#626e84` | `neutral.400` | `#8d95a5` |
| `stroke.input.disabled` | `neutral.300` | `#b5bac5` | `neutral.600` | `#4a5870` |
| `stroke.input.selected` | `midnight` | `#000523` | `white` | `#ffffff` |
| `stroke.system.error` | `red.700` | `#9e0f1b` | `red.300` | `#eb8c82` |
| `surface.ads` | `#DADDE3` | `#DADDE3` | `#36455F` | `#36455F` |
| `surface.effect.scrim` | `#00000080` | `#00000080` | `#00000080` | `#00000080` |
| `surface.effect.shadow` | `opacity.midnight.600` | `#07153351` | `opacity.midnight.800` | `#071533a3` |
| `surface.elevation.float` | `neutral.50` | `#f6f7f8` | `neutral.700` | `#24324d` |
| `surface.elevation.modal` | `white` | `#ffffff` | `neutral.900` | `#071533` |
| `surface.extra.bright` | `white` | `#ffffff` | `neutral.800` | `#172541` |
| `surface.extra.dim` | `neutral.100` | `#eff0f2` | `midnight` | `#000523` |
| `surface.inverted` | `midnight` | `#000523` | `white` | `#ffffff` |
| `surface.primary` | `white` | `#ffffff` | `midnight` | `#000523` |
| `surface.secondary` | `neutral.50` | `#f6f7f8` | `neutral.900` | `#071533` |
| `surface.state.hover` | `opacity.midnight.200` | `#07153314` | `opacity.white.400` | `#f6f7f828` |
| `surface.state.hover.inverted` | `opacity.white.400` | `#f6f7f828` | `opacity.midnight.200` | `#07153314` |
| `surface.system.error` | `red.50` | `#fff5f0` | `red.800` | `#640014` |
| `surface.system.info` | `blue.50` | `#ebfaff` | `blue.900` | `#0f0d52` |
| `surface.system.success` | `green.50` | `#e6f6eb` | `green.800` | `#0b491d` |
| `surface.system.warning` | `yellow.50` | `#fffae7` | `yellow.800` | `#755c00` |
| `surface.tertiary` | `neutral.100` | `#eff0f2` | `neutral.800` | `#172541` |
| `surface.transparency.strong` | `opacity.midnight.600` | `#07153351` | `opacity.white.600` | `#f6f7f851` |
| `surface.transparency.weak` | `opacity.midnight.200` | `#07153314` | `opacity.white.400` | `#f6f7f828` |
| `surface.transparency.weakest` | `opacity.midnight.100` | `#0715330a` | `opacity.white.300` | `#f6f7f81e` |
