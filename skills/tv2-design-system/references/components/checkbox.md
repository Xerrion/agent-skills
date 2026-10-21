# Checkbox

Recorded version: `1.3.0`.

[Local preview](../../assets/components/checkbox.png) · [Design record](checkbox_log.md) · [Figma source](https://www.figma.com/design/cjU0zuiL2r8YXsGmnNxxy2/DS-%7C-Shared?node-id=4077-227)

Appearance describes the bundled preview. Recorded rules describe the local design record or a named token. The preview canvas does not specify this component's background, spacing, or unseen states. Use recorded values for exact measurements.

## Appearance

Preview shows a white square control to the left of the first text line, with a dark check mark centered inside. The checkbox aligns with the label at the top of the text block. The label is larger than the supporting paragraph below it. The paragraph wraps across several lines within the text column, leaving the control in its own narrow column.

An underlined blue link sits below the paragraph and starts at the same left edge as the label and paragraph. A small right arrow precedes the link text. The example has no enclosing card outline or separate filled container. Its checked state is communicated by both the square's fill and the check mark.

## Recorded rules

The tooltip size is 16. The label can be toggled off in every state, and card style is an available boolean option. The record adds an error state for a single checkbox and says that focus is described in the developer handoff. Stroke colors use tokens and follow input logic. The bundled preview shows the checked treatment; it does not show the card, unchecked, focus, or error treatments.
