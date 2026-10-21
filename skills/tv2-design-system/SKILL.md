---
name: tv2-design-system
description: Use this skill when creating, styling, reviewing, or repairing TV 2 or TV2 interfaces and HTML emails, including components, light/dark themes, typography, layouts, icons, and logos. Also use when maintaining this skill from TV 2 design-system sources. Supplies TV 2 design rules and original artwork offline. Backend logic and deployment alone are outside its scope.
compatibility: Asset export and checks require Python 3.10+ with its standard library. Repository refresh also requires Git. Figma refresh requires authorized Figma access; ordinary design use works offline.
---

# TV 2 design system

Use the bundled references, tokens, fonts, and artwork. Ordinary use needs no Figma account, network, source checkout, or other skill.
Resolve resources from this skill folder. Commands below run from that folder; when working elsewhere, invoke the script by its resolved path.
Copy output assets into the consuming application's static directory. Local skill paths are not deployed web URLs.

## Select the task

| Request | Action |
| --- | --- |
| Explain a token, component, or layout | Read only that topic's reference. No asset export or source maintenance is needed. |
| Review an existing interface | Read the relevant references and inspect the supplied implementation. Generate assets only if fixing it requires them. |
| Implement a web interface | Follow the web workflow below. |
| Create an HTML email | Use the [email reference](references/implementation/email.md); inline resolved values for the delivery environment. |
| Refresh repository or Figma sources | Use [repository maintenance](references/maintenance/repository-refresh.md) or [Figma maintenance](references/maintenance/figma-refresh.md). |
| Evaluate this skill after changing it | Use [behavioral evaluation](references/maintenance/evaluation.md). |

When editing this skill's instructions or tooling, apply the [skill maintenance criteria](references/maintenance/skill-standards.md).

## Web workflow

1. Keep the requested platform, product, theme, and existing application conventions. Use [web-default](references/implementation/default-profile.md) only for unspecified choices.
2. Export with `python3 scripts/build_web_assets.py --output <application-assets-directory>`. Load the generated token CSS before the [web baseline](references/implementation/web-baseline.md). Reuse its specimens for Button, Icon Button, Input, Section Notice, and Snackbar; adapt markup to the requested framework.
3. Read the selected component reference below. Use its local measurements, preview, and design record. Foundation JSON defines token values; native Figma records define captured geometry. Keep local web adaptations identifiable.
4. Preserve semantic color bindings, complete typography, and original artwork. Use [icon masks](references/implementation/icon-rendering.md) for monochrome icons that follow text color. Select an actual recorded variant; property options do not imply every combination exists.
5. Check the result in the application using [implementation verification](references/implementation/verification.md). Fix relevant failures before reporting completion. Run bundle validation when the skill itself changes, rather than for every interface lookup.

## Components

Each link opens one component. Its local preview and design record remain usable without Figma.

| Component | Component |
| --- | --- |
| [Accordion](references/components/accordion.md) | [Button](references/components/button.md) |
| [Button Group](references/components/button-group.md) | [Carousel Dots](references/components/carousel-dots.md) |
| [Checkbox](references/components/checkbox.md) | [Countdown](references/components/countdown.md) |
| [Flag](references/components/flag.md) | [Form Group Header](references/components/form-group-header.md) |
| [Icon](references/components/icon.md) | [Icon Button](references/components/icon-button.md) |
| [Icon Marker, deprecated](references/components/icon-marker.md) | [Input](references/components/input.md) |
| [Input OTP](references/components/input-otp-one-time-password.md) | [Label](references/components/label.md) |
| [List](references/components/list.md) | [Logo](references/components/logo.md) |
| [Media Tag](references/components/media-tag.md) | [Modal](references/components/modal-platform.md) |
| [Placeholder Image](references/components/placeholder-image.md) | [Progress Indicator](references/components/progress-indicator.md) |
| [Progress Slider](references/components/progress-slider.md) | [Radio Button](references/components/radio-button.md) |
| [Search](references/components/search.md) | [Section Notice](references/components/section-notice.md) |
| [Segmented Control](references/components/segmented-control.md) | [Select](references/components/select.md) |
| [Snackbar](references/components/snackbar.md) | [Spinner](references/components/spinner.md) |
| [Switch](references/components/switch-platform.md) | [System Banner](references/components/system-banner.md) |
| [Text Area](references/components/text-area.md) | [Validation Summary](references/components/validation-summary.md) |

## Foundations and resources

| Need | Reference |
| --- | --- |
| Source authority and coverage | [Sources](references/governance/sources.md) |
| Design principles | [Principles](references/governance/principles.md) |
| Colors | [Primitives](references/foundations/color-primitives.md), [semantic roles](references/foundations/color-semantic.md), [election colors](references/foundations/election-colors.md) |
| Typography | [Styles](references/foundations/typography.md), [font files](references/artwork/fonts.md), [web font loading](references/implementation/web-fonts.md) |
| Size and thresholds | [Spacing](references/foundations/spacing.md), [breakpoints](references/foundations/breakpoints.md) |
| Product layout | [Free](references/layout/free.md), [Play](references/layout/play.md) |
| Composition | [Surfaces](references/layout/surfaces.md), [composition index](references/layout/composition.md) |
| Artwork browsing | [Icons](references/artwork/icons.md), [logos](references/artwork/logos.md), [flags](references/artwork/flags.md), [illustrations](references/artwork/illustrations.md) |
| Web integration | [Asset export](references/implementation/web-assets.md), [baseline index](references/implementation/web-baseline.md) |
| Raw measurement interpretation | [Figma record format](references/implementation/figma-records.md) |
| Staged source changes | [Candidate review](references/maintenance/staged-review.md) |

Locate a single artwork file by its exact filename under `assets/`; open a family catalog when browsing options.
Each prose reference covers one topic or one component. Index files contain navigation only. Link related topics instead of merging them.

## Scripts

All Python scripts use the standard library and accept `--help`. Each linked guide describes that script's output and exit codes.

| Script | Use |
| --- | --- |
| `scripts/build_web_assets.py` | [Export assets](references/implementation/web-assets.md), or check an existing export with `--check`. |
| `scripts/validate_bundle.py` | [Validate the bundle](references/implementation/bundle-validation.md), including metadata, links, pinned files, and fixtures. |
| `scripts/maintain_sources.py` | [Compare sources](references/maintenance/repository-refresh.md) and stage a separate candidate. Read maintenance guidance before using it. |

## Constraints

- Use the bundled TV2 fonts and original artwork. Failed font or artwork loading is an implementation defect.
- Keep token values unchanged. Election colors retain their recorded NAVL coordination requirement.
- Figma frame widths are sample dimensions. Use breakpoint tokens for CSS thresholds, and select TV mode explicitly rather than inferring it from a wide screen.
- The executable web baseline covers five components. Other components have local appearance and history; previews alone do not establish complete behavior or accessibility.
- Refresh upstream sources only when requested. Figma links identify evidence; regular implementations use the saved local records.
