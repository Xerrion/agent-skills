# Web baseline index

Generate the portable directory using [web asset export](web-assets.md). Load `tv2-tokens.css` before `tv2-components.css`. The latter imports the individual component and icon stylesheets. Load `tv2-profile.css` separately when using the default page profile. `tv2-components.js` optionally handles explicitly marked dismissal controls.

| Baseline resource | Local reference or specimen |
| --- | --- |
| Page defaults | [web-default-v1](default-profile.md) |
| Button | [Reference](../components/button.md), [specimen](../../assets/web/specimens/button.html) |
| Icon Button | [Reference](../components/icon-button.md), [specimen](../../assets/web/specimens/icon-button.html) |
| Input | [Reference](../components/input.md), [specimen](../../assets/web/specimens/input.html) |
| Section Notice | [Reference](../components/section-notice.md), [specimen](../../assets/web/specimens/section-notice.html) |
| Snackbar | [Reference](../components/snackbar.md), [specimen](../../assets/web/specimens/snackbar.html) |
| Theme-aware icon masks | [Rendering icons](icon-rendering.md) |
| Verification | [Bundle checks](bundle-validation.md), [application checks](verification.md) |

The source specimens become runnable when exported alongside their generated token stylesheet, fonts, and icons. Open the exported specimens for a self-contained local example.
