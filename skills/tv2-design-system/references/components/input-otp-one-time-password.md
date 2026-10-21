# Input OTP (One time password)

Recorded version: `1.2.0`.

[Local preview](../../assets/components/input-otp-one-time-password.png) · [Design record](input-otp-one-time-password_log.md) · [Figma source](https://www.figma.com/design/cjU0zuiL2r8YXsGmnNxxy2/DS-%7C-Shared?node-id=4091-547)

Appearance describes the bundled preview. Recorded rules describe the local design record or a named token. The preview canvas does not specify this component's background, spacing, or unseen states. Use recorded values for exact measurements.

## Appearance

Preview shows a label and helper text above a horizontal row of six separate character boxes. The text block begins at the first box's left edge. The boxes have the same tall rectangular proportions, are evenly separated, and share top and bottom alignment. Each box holds one centered character.

The first three boxes contain `3`, `3`, and `0`; the remaining boxes are empty. The third box has a brighter, thicker outline than the other five. All boxes have navy interiors. This gives a visible distinction between the emphasized box and the surrounding boxes while retaining the row's geometry. The image does not label the interaction state represented by that emphasis.

## Recorded rules

Tooltip size is 16. Tooltip placement follows the other input fields, and the label uses Figma's hug sizing rather than fill sizing. The component follows input stroke logic. The preview establishes the six-box composition shown here; it does not establish that every OTP use must contain six characters.
