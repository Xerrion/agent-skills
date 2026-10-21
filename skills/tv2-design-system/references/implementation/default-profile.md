# Web default profile

Use `web-default-v1` when the user has not specified web presentation choices and no existing application convention supplies them. Load the exported `tv2-profile.css` after `tv2-components.css`. This is a local implementation profile. Its page shell is not an upstream rule for every TV 2 product.

| Choice | Fixed default |
| --- | --- |
| Platform | Web. Never infer television from viewport width. |
| Initial theme | Explicit `data-tv2-theme="light"` on `html`. Use `dark` only when selected by the user or application. No automatic system-theme switch. |
| Root styling | `.tv2-page`, semantic `surface.primary` and `content.primary`, complete `body.medium`, bundled TV2 font. |
| Page container | `.tv2-container`, centered, maximum outer width 1000 px, border-box sizing, horizontal gutter `size.24.step`. |
| Vertical content spacing | `.tv2-stack` uses `size.24`; `.tv2-actions` wraps with `size.8` gap. |
| Component defaults | Use each component's bundled default specimen. Button Medium/Default/Primary, Icon Button Icon only/Medium/Primary, Input Default, Section Notice Info, Snackbar neutral. |
| Motion | None in the baseline. No automatic entry animation or toast dismissal timer. |
| Product spacing | Generic profile. Apply [Free](../layout/free.md) or [Play](../layout/play.md) only when that product is selected. |

Keep the profile name and any overrides with the application's implementation notes. Reuse the same asset export and specimen markup for the same inputs.
Content, requested framework, accessible names, and destinations belong to the consuming application.
The deterministic exporter produces identical bytes from identical bundled sources. It does not promise that separate free-form page designs will be pixel-identical.

See [web baseline](web-baseline.md) for the files and markup.
