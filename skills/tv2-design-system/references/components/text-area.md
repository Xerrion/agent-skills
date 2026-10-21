# Text Area

Recorded version: `1.4.0`.

[Local preview](../../assets/components/text-area.png) · [Design record](text-area_log.md) · [Figma source](https://www.figma.com/design/cjU0zuiL2r8YXsGmnNxxy2/DS-%7C-Shared?node-id=4992-1263)

Appearance describes the bundled preview. Recorded rules describe the local design record or a named token. The preview canvas does not specify this component's background, spacing, or unseen states. Use recorded values for exact measurements.

## Appearance

Preview shows a label and smaller helper text above a large rectangular text field. Both align with the field's left edge. The field is wider than it is tall, with a bright light outline and navy interior. Entered text begins near the upper left inside the field, leaving space on the right and below for additional lines. Its corners appear square. The example contains no visible resize handle, counter, or action icon.

## Recorded rules

Tooltip size is 16. The component follows input styling, including its WCAG-related styling update. Hover was added in version 1.4.0. Success feedback uses `check-circle`, and feedback icons use `content.primary`.

The preview supplies a populated text area with a prominent outline. The record does not identify that outline's state. It records hover and success appearances without showing their full treatment in this image.

## Implementation checks

Verify the recorded WCAG input styling against the actual background. Use `stroke.focus.outline` or the TV specific `stroke.focus.outline.tv` token for the applicable focus treatment. Token selection alone does not establish accessibility compliance.
