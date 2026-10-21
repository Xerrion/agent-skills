# Surface hierarchy

Use complete [type styles](../foundations/typography.md) and semantic [colors](../foundations/color-semantic.md) to express hierarchy.
The exact values below are from the bundled tokens; component-specific assignments are recorded in [component references](../COMPONENTS.md).

| Role | Recorded visual treatment |
| --- | --- |
| Primary content on the base surface | `content.primary` on `surface.primary`: midnight text on white in light mode, white text on midnight in dark mode |
| Supporting content | `content.secondary`: `neutral.600` in light mode and `neutral.400` in dark mode |
| Adjacent surface levels | `surface.secondary` is `neutral.50` / `neutral.900`; `surface.tertiary` is `neutral.100` / `neutral.800` for light / dark mode |
| Raised surfaces | `surface.elevation.modal` is white / `neutral.900`; `surface.elevation.float` is `neutral.50` / `neutral.700` |
| Backdrop and shadow colors | `surface.effect.scrim` is `#00000080` in both themes. `surface.effect.shadow` uses `opacity.midnight.600` / `opacity.midnight.800`; it specifies color, without shadow offset or blur |
