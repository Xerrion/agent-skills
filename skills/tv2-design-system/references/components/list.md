# List

Recorded version: `1.5.0`.

[Local preview](../../assets/components/list.png) · [Design record](list_log.md) · [Figma source](https://www.figma.com/design/cjU0zuiL2r8YXsGmnNxxy2/DS-%7C-Shared?node-id=4733-5554)

Appearance describes the bundled preview. Recorded rules describe the local design record or a named token. The preview canvas does not specify this component's background, spacing, or unseen states. Use recorded values for exact measurements.

## Appearance

Preview shows four equal width rows stacked vertically with narrow gaps. Each row has a flat dark surface, square corners, a white leading icon, left aligned label text, and a white right facing chevron near the right edge. The icon column, labels, and chevrons line up across rows. Icons, text, and trailing content are vertically centered within each row. The longer label remains on one line in this example.

The first row includes a muted numeric count between its label and chevron. The second places a white number inside a red circular notification badge in that trailing region. The other rows leave this region empty. No group heading, hover treatment, or dismiss control appears in the preview.

## Recorded rules

Version 1.5.0 sets left and right padding to 12 px and the gap to 12 px, replacing 16 px values. The record does not identify which internal layout gap this change applies to. It also adds top and bottom padding to List Group for dropdown and similar contexts without specifying those padding values. Version 1.2.0 sets header bottom padding to `size.8`, which is 8 in [size tokens](../tokens/size.json), and list bottom padding to 0. Version 1.1.0 replaces a 3 px gap with 4 px and attaches spacing to size tokens; that older adjustment does not override the later 12 px gap rule.

Version 1.2.1 sets the notification dot to `red.500`, which is `#EB050F` in [color tokens](../tokens/color.json). Version 1.3.0 adds a hover layer using `surface.state.hover` over the existing background. The token maps to `opacity.midnight.200` in light mode and `opacity.white.400` in dark mode. Version 1.3.1 adds a dismissible List Element; version 1.4.0 shows that dismiss control only on hover and allows the chevron to be hidden. The source's word "darkens" describes its hover intent; retain the actual theme token mapping when implementing the layer.

Make dismissal discoverable and operable with keyboard focus and touch as well. This is an implementation adaptation to the recorded hover treatment.
