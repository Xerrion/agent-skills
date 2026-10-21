# Button

Recorded version: `2.1.2`.

[Local preview](../../assets/components/button.png) · [Design record](button_log.md) · [Figma source](https://www.figma.com/design/cjU0zuiL2r8YXsGmnNxxy2/DS-%7C-Shared?node-id=2827-29110)

Appearance describes the bundled preview. Recorded rules describe the local design record or a named token. The preview canvas does not specify this component's background, spacing, or unseen states. Use recorded values for exact measurements.

## Appearance

Preview shows a solid white pill with fully rounded ends. A dark single-line label, "Afspil", is centered horizontally and vertically. The visible example has no icon or border that contrasts with the fill. Its width leaves space on both sides of the label.

## Pinned native measurements

The [local Figma record](../figma/button.json) contains 63 actual variants, their property defaults, metric columns, native default tree, and bound variables. Captured 2026-10-21. Figma access is unnecessary.

| Default property | Value |
| --- | --- |
| Size | Medium (default) |
| Type | Default ⚫️ |
| Hieraki | Primary |
| On image | False |
| State | Default |
| Leading icon | Hidden |
| Trailing icon | Visible |

The default variant is `2827:34302`. It is a horizontal, centered pill: height 44 px, radius 99 px, horizontal padding 24 px, declared vertical padding 12 px, gap 8 px, and maximum width 479 px. Text is TV2 Medium, 18 px with 22 px line height. Each icon glyph uses a 20 px frame; its offset wrapper occupies 12 px in the row. The default fill binds `surface.inverted`; text and icon bind `content.inverted`.

Small default variants are 32 px high; X-Small variants are 24 px high. Both declare horizontal padding 16 px, vertical padding 8 px, gap 8 px, and radius 99 px. The native 115 px default width includes the sample label and trailing icon; use content width, not 115 px for all labels.

The declared 44 px height, 12 px top/bottom padding, and 22 px text line do not fit an ordinary CSS content-box calculation. The [web specimen](../../assets/web/specimens/button.html) keeps the measured height and horizontal padding and centers the label. It truncates long labels with an ellipsis within the parent and the native 479 px maximum. Vertical flex centering and truncation are documented web adaptations.

Property options are not a full Cartesian product. Select only a combination listed in `variants`.

## Recorded rules

Medium is the default size. Its `utility.large.medium` text style uses TV2 medium, 18 px text with a 22 px line height outside TV, and 36 px text with a 44 px line height for TV. Small is 32 px high; the compact size is 24 px. A leading icon is off by default. The red variant uses `red.500`, and Brand combines the former Live and Play entry variants. The record recommends one primary button per viewport.

The On Image variant has a disabled state and uses primitive colors without light/dark switching. The preview does not show that treatment. Apply the current 24 px compact size from version 2.1.0; the earlier 1.0.0 entry excluded a historical XS variant and predates this addition.

## Implementation checks

Check the On Image variant against its actual background image. Its primitive colors do not switch with the light or dark theme, so the image determines the resulting contrast.
