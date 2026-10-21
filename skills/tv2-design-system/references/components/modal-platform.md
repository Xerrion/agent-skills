# Modal (Platform)

Recorded version: `1.0.0`.

[Local preview](../../assets/components/modal-platform.png) · [Design record](modal-platform_log.md) · [Figma source](https://www.figma.com/design/cjU0zuiL2r8YXsGmnNxxy2/DS-%7C-Shared?node-id=20814-915)

Appearance describes the bundled preview. Recorded rules describe the local design record or a named token. The preview canvas does not specify this component's background, spacing, or unseen states. Use recorded values for exact measurements.

## Appearance

Preview shows a modal centered over a dimmed, blurred backdrop. Its rectangular foreground panel combines a wide promotional image on top with a dark content surface below. The image occupies the full panel width and more than half its height. A small circular close control sits inside the image at the upper right. The promotional title is part of the artwork.

The content area has a left aligned heading above a shorter, smaller paragraph. Both share the same left edge. Two compact pill shaped actions sit side by side beneath the text and are centered as a group. The left action has a muted dark fill and light text; the right action has a white fill and dark text. The body area has visible inset space around its content. This composition has two close actions: the upper right icon and the lower "Luk" button.

## Pinned native measurements

The [local Figma record](../figma/modal-platform.json) contains Modal - Dialog with six actual variants and Modal - Bottom Sheet with three. Captured 2026-10-21. Figma access is unnecessary.

Dialog properties include Breakpoint=SM/MD/LG and Type=Default/Image top. The default shows a close button and hides the customer-center link. The native dialog root declares 16 px padding and gap. Its default wrapper has maximum width 426 px, 24 px vertical gap, and 40 px bottom padding. Header side/top padding is 16 px; content and button groups have 16 px side padding.

The source SM default root currently measures 1522 px wide despite its SM name. Do not infer a mobile viewport width or breakpoint from that anomalous canvas measurement. The wrapper's recorded constraints and the independent breakpoint tokens are the useful evidence.

The default Bottom Sheet root measures 360 px wide; its wrapper fills horizontally, hugs vertically, uses a 24 px gap, and has 40 px bottom padding. The hidden grabber measures 36 × 5 px. Its wrapper radius is mixed; the capture does not establish one uniform corner radius.

Slot descriptions specify content-driven height up to a maximum followed by scrolling, but this capture does not provide a complete numerical maximum-height contract. Focus trapping, Escape, scroll locking, and focus restoration remain implementation requirements. This component has no executable web baseline in this bundle.

## Recorded rules

Version 1.0.0 includes width and padding logic and allows adaptation to different contexts. The bundled record does not provide its calculations or numeric values. The preview supports the image, content, and action arrangement above, without establishing that every modal must use an image, two actions, or this width.
