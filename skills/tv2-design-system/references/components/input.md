# Input

Recorded version: `1.2.0`.

[Local preview](../../assets/components/input.png) · [Design record](input_log.md) · [Figma source](https://www.figma.com/design/cjU0zuiL2r8YXsGmnNxxy2/DS-%7C-Shared?node-id=4040-146)

Appearance describes the bundled preview. Recorded rules describe the local design record or a named token. The preview canvas does not specify this component's background, spacing, or unseen states. Use recorded values for exact measurements.

## Appearance

Preview shows a single text column: label, helper text, then one wide empty input rectangle. The label and helper text share the field's left edge. The label is more prominent than the helper text. The field has a muted light outline and a navy interior that visually matches the surrounding canvas. Its corners appear square. No text, icon, or trailing action is visible inside the field.

## Pinned native measurements

The [local Figma record](../figma/input.json) contains the Input set's seven actual states: Default, Active, Filled, Success, Error, Disabled, and Hover. It also preserves two internal helper sets. Captured 2026-10-21. Figma access is unnecessary.

Default variant `4040:176` shows label and helper text. Required text, tooltip, leading icon, trailing icon, and placeholder are hidden by default. The native sample is 300 px wide; the 90 px overall height consists of the 38 px label/helper group, 8 px gap, and 44 px field.

The label/helper group has zero vertical gap. Helper text is TV2 Regular 14 px with 18 px line height. The field has square corners, a 1 px `stroke.input.default` border, and a 44 px wrapper with declared 12 px padding on all sides and 8 px internal gap. Required text, when shown, has 4 px top padding and uses 12/14 px regular text.

The capture stops above the label and editable-text descendants, so their typography is not measured here. The [web specimen](../../assets/web/specimens/input.html) chooses `utility.medium.medium` for the label and `utility.medium.regular` for editable text as explicit web conventions, and keeps the field at 44 px. Do not describe those choices as extracted Figma facts.

## Recorded rules

The label and helper text gap is 0, changed from 4 in version 1.0.1. The info icon size is 16. Version 1.1.0 adds a stroke because a field distinguished only by its background did not meet the recorded contrast requirement. The selected stroke passes 3:1 contrast against the three standard background colors. Hover uses the hover token. Version 1.1.1 removes leftover background colors.

The preview shows an empty outlined field. Its label, helper, and field order can be reproduced directly. The record establishes a hover treatment but does not provide its exact token name or show a hover, populated, error, disabled, or focus comparison here.

## Implementation checks

Verify the field stroke against each actual background. The recorded 3:1 requirement concerns WCAG 1.4.11. Use `stroke.focus.outline` or the TV specific `stroke.focus.outline.tv` token for the applicable focus treatment. Token selection alone does not establish accessibility compliance.
