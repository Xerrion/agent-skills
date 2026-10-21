# Snackbar

Recorded version: `1.2.0`.

[Local preview](../../assets/components/snackbar.png) · [Design record](snackbar_log.md) · [Figma source](https://www.figma.com/design/cjU0zuiL2r8YXsGmnNxxy2/DS-%7C-Shared?node-id=19525-1042)

Appearance describes the bundled preview. Recorded rules describe the local design record or a named token. The preview canvas does not specify this component's background, spacing, or unseen states. Use recorded values for exact measurements.

## Appearance

Preview shows a long neutral dark bar with rounded corners and a soft shadow beneath it. A white circular check symbol sits at the left, followed by a single line of white message text. The symbol and text are vertically centered. The bar has inset space on both ends and contains no visible action or close control. Its rounded outline and shadow separate it from the surrounding dark presentation canvas.

## Pinned native measurements

The [local Figma record](../figma/snackbar.json) contains standalone component `19525:1695`, its default properties, native tree, variable modes, and Shadow Float effect. Captured 2026-10-21. Figma access is unnecessary.

The default shows a 20 px leading check_circle icon, with headline and dismissal hidden. The sample is 328 × 60 px, uses a horizontal layout, padding 12 px on every side, gap 8 px, and radius 12 px. Content uses regular 14/18 px text. When shown, the headline uses `heading.small` and the text stack has a 4 px gap.

Fill binds `surface.elevation.float`; content binds `content.primary`. Shadow Float is a drop shadow with offset x=0 px, y=8 px, blur=16 px, spread=0 px, and color bound to `surface.effect.shadow`. Keep the neutral surface and shadow binding in both themes.

The [web specimen](../../assets/web/specimens/snackbar.html) keeps the captured 328 px width, shrinks to fit a narrower parent, and grows in height with its content. Its contained 32 px dismissal control is an explicit web adaptation when dismissal is enabled. Placement, dismissal timing, live-region policy, and application message text are not specified by this static Figma component.

## Recorded rules

Version 1.0.0 uses Snackbar for passive feedback in the defined neutral standard color. Keep that neutral color; use Section Notice for a message specific to an element or section. Version 1.0.1 makes dismissal use the icon only Icon Button variant. Version 1.1.0 adds an optional headline and corrects single line text layout.

Version 1.2.0 sets the headline to `heading.small`, changes the shadow to `Shadow Float`, adds `radius s`, and sets left and right padding to 12 px, replacing 16 px. [Typography tokens](../tokens/typography.json) define `heading.small` as TV2 bold, weight 700, with a 1.1 relative line height and sizes 16 at `sm`, 18 at `md` and `lg`, and 28 at `tv`. Apply this style to the headline property. The preview contains a message without a separate headline. The bundled tokens do not provide complete numeric definitions for `Shadow Float` or `radius s`.
