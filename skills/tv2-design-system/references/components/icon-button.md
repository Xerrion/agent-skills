# Icon Button

Recorded version: `1.2.1`.

[Local preview](../../assets/components/icon-button.png) · [Design record](icon-button_log.md) · [Figma source](https://www.figma.com/design/cjU0zuiL2r8YXsGmnNxxy2/DS-%7C-Shared?node-id=2827-29109)

Appearance describes the bundled preview. Recorded rules describe the local design record or a named token. The preview canvas does not specify this component's background, spacing, or unseen states. Use recorded values for exact measurements.

## Appearance

Preview shows a white circular button with a dark right-arrow glyph centered inside it. A separate white label sits to its right, outside the circle. The circle and label align around a common horizontal centerline. The preview's circular surface is visually distinct from the pill shape of the text Button.

## Pinned native measurements

The [local Figma record](../figma/icon-button.json) contains 72 actual variants and all owning-set property defaults. Captured 2026-10-21. Figma access is unnecessary.

The default `8576:2620` is Icon only, On image=False, Medium (default), Primary, State=Default. Its outer frame is 44 × 44 px. The circular child is 44 × 44 px with radius 99 px, padding 12 px, and a 20 × 20 px glyph. Fill binds `surface.inverted`; glyph binds `content.inverted`.

Icon-only Small variants are 32 × 32 px and X-Small variants are 24 × 24 px. Label below and Label right are distinct recorded variants; their overall dimensions include their label and must not be replaced by the icon-only measurements.

The [web specimen](../../assets/web/specimens/icon-button.html) implements the default icon-only form. Supply a meaningful accessible control name. The recorded historical `content.primary` description below does not override the native default's `content.inverted` binding.

## Recorded rules

Medium is the default size; Small is 32 px and X-Small is 24 px. Version 1.2.1 sets the X-Small glyph to 12 px, replacing its previous 16 px glyph. Primary uses the recorded `surface.inverted` and `content.primary` roles. There is no tertiary variant. The label placement visible here does not define every supported label arrangement.
