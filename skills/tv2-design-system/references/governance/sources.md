# Source authority

The skill bundles its design sources for offline use. The original repository and Figma file are needed when refreshing those sources.

## Authority by subject

| Subject | Authority | Conflict handling |
| --- | --- | --- |
| Foundation colors, type styles, spacing, and breakpoints | Bundled JSON under [tokens/](../tokens/) | Preserve the JSON values and alias relationships when prose or examples differ. |
| Exact component geometry and supported variants | Pinned native Figma measurements linked by the individual [component reference](../COMPONENTS.md) | Use the native component or variant. Scaled preview instances are unsuitable for exact dimensions. |
| Artwork and font data | Actual files under [assets/](../../assets/) | Preserve original geometry, aspect ratio, fills, strokes, and mapped face data. |
| Component history and visible composition | Source changelog and bundled component preview | A changelog describes its dated change. A preview supports visible arrangement; it does not establish an unmeasured radius or gap. |
| Framework integration and unspecified page choices | The relevant implementation reference and the consuming application | Keep application choices identifiable. They do not become upstream design rules. |

Apply the pinned current component measurements when they replace an older preview inference. Historical changelogs keep their original scope. If an exact value is absent, retain the known composition and record the missing application choice.

## Repository snapshot

Repository: [tv2/designsystem](https://github.com/tv2/designsystem).
Checked on 2026-10-20 at revision `8cca8015c0a4959f2c83be096616bf7da7c94416`.

| Original repository content | Bundled source |
| --- | --- |
| `foundation/color.json` | [color.json](../tokens/color.json) |
| `foundation/color_election.json` | [color_election.json](../tokens/color_election.json) |
| `foundation/typography.json` | [typography.json](../tokens/typography.json) |
| `foundation/size.json` | [size.json](../tokens/size.json) |
| `foundation/breakpoint.json` | [breakpoint.json](../tokens/breakpoint.json) |
| `products/play.json` | [play.json](../tokens/play.json) |
| `foundation/*.md` and `products/play.md` | Corresponding atomic foundation and Play layout references |
| `components/*/*_log.md` and `components/*/*.png` | Source records under [components/](../components/) and previews under [assets/components/](../../assets/components/), linked by the component references |
| Original files under `assets/` | Same relative paths under [assets/](../../assets/), excluding generated PNG duplicates and operating-system files |

The six token files, source component records, and bundled artwork retain their source bytes.

## Figma snapshot

Source file: `DS | Shared`, file key `cjU0zuiL2r8YXsGmnNxxy2`.
The pinned measurements were captured on 2026-10-21. Individual component references identify their node IDs and local measurement records.
Native records cover Button, Icon Button, Input, Section Notice, Snackbar, Modal (Platform), and the Free product layout. The remaining components retain local preview images and design records, with unmeasured details identified as such. Every component has a local written reference and image.
Use those bundled records during implementation. Live Figma access is optional unless the user requests a refresh.

The capture was completed for the records above before the Figma connector reported the account's View-seat call limit. Input label and editable-text descendants and a complete Modal maximum-height contract were not captured. Their component references identify the gaps and any fixed local web conventions. No account upgrade or online access is needed to consume the saved evidence.

## Coverage

Repository tooling, nested skills, SDKs, generated documentation, maintenance scripts, and synchronization configuration are excluded.
All required design references, token definitions, and assets live inside the skill folder.

The source content does not define a universal component implementation API or every interaction state.
Component previews describe local arrangements without prescribing a complete page shell. Choose and record any additional grid, navigation shell, or content-width rule required by the application.
Keyboard interaction, accessible names, focus order, screen-reader announcements, target sizes, and motion need checks in the consuming application.
The bundle has no motion tokens or complete sub-brand color rules. Animation timing, easing, and undocumented category colors remain application decisions unless another authoritative source is supplied.
