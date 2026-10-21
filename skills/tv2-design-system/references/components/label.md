# Label

Recorded version: `1.2.1`.

[Local preview](../../assets/components/label.png) · [Design record](label_log.md) · [Figma source](https://www.figma.com/design/cjU0zuiL2r8YXsGmnNxxy2/DS-%7C-Shared?node-id=2561-2)

Appearance describes the bundled preview. Recorded rules describe the local design record or a named token. The preview canvas does not specify this component's background, spacing, or unseen states. Use recorded values for exact measurements.

## Appearance

Preview shows a compact yellow rectangle with dark `Breaking` text. The text is centered vertically, with visible inset on each side. The rectangle is wide enough to contain the word and its inset. Its corners appear square, and it has no visible outline, icon, or secondary line.

## Recorded rules

Labels use utility text, and hover is a supported state. The variants include `Neutral Midnight` and `Neutral White`. Medium and Large sizes were added in version 1.2.0. The Live label uses `red.500` from version 1.2.1, replacing `red.525`. These Live and neutral variants are distinct from the yellow Breaking example shown in the preview.

The [utility typography tokens](../tokens/typography.json) provide regular and medium weights at 18/22, 16/20, 14/18, and 12/14 font-size/line-height pairs. The TV counterparts are 36/44, 32/40, 28/36, and 24/28. The component record does not map its Medium and Large size names to a particular utility style, or assign the Breaking preview a specific yellow token. Select those exact values from an explicit variant definition when one is supplied.
