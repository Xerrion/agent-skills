# Section Notice

Recorded version: `1.1.1`.

[Local preview](../../assets/components/section-notice.png) · [Design record](section-notice_log.md) · [Figma source](https://www.figma.com/design/cjU0zuiL2r8YXsGmnNxxy2/DS-%7C-Shared?node-id=5244-34546)

Appearance describes the bundled preview. Recorded rules describe the local design record or a named token. The preview canvas does not specify this component's background, spacing, or unseen states. Use recorded values for exact measurements.

## Appearance

Preview shows a wide, square cornered dark blue notice with a white information symbol at the left. A white message sits to the right and wraps onto three lines. Its continuation lines align with the text column rather than with the icon. The icon aligns near the first text line. All content is inset from the surface edges. The example has no separate heading, close control, link, or action.

## Pinned native measurements

The [local Figma record](../figma/section-notice.json) preserves the four actual types Info, Warning, Error, and Success, their geometry, property defaults, native Info tree, and bound variables. The [native Info screenshot](../../assets/components/section-notice-native.png) is bundled locally. Captured 2026-10-21. Figma access is unnecessary.

Default Info variant `5244:34548` has square corners, 12 px top/bottom padding, 16 px side padding, and 8 px gaps. Its horizontal inner container is content-driven and has maximum width 1000 px. The status icon is 20 × 20 px. The message stack uses regular 14 px text with 18 px line height and an 8 px gap before a separate underlined link. The link's native maximum width is 400 px.

Both the link and dismissal control are shown by default. The sample width is 360 px and height 68 px with one text line and one link line; these are sample dimensions, not a fixed height rule. Let longer text wrap and increase height.

The type selects its `surface.system.*` background and original status glyph. Info binds `content.primary` for its text/icon. Use the original info_circle, warning_triangle, warning_circle, or check_circle artwork.

The [web specimen](../../assets/web/specimens/section-notice.html) keeps a fixed icon column and a wrapping message column. It uses `content.primary` for the link so it remains readable in dark themes; the native link's literal midnight color is recorded in the JSON. Its dismissal control is contained within 32 px, adapting a native 32 px wrapper whose circular child measures 34 px. These are explicit web accessibility and sizing adaptations.

## Recorded rules

Version 1.1.0 provides `info`, `success`, `warning`, and `error` types and sets links to midnight. Version 1.0.0 changes the dark info surface from `blue.800` to `blue.900`. The bundled [color tokens](../tokens/color.json) define `surface.system.info` as `blue.50` in light mode and `blue.900` in dark mode; `blue.900` is `#0f0d52`, and midnight is `#000523`. The preview shows the information composition only. It does not define the icon or arrangement for every feedback type.
