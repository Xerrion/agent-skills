# Search

Recorded version: `1.3.0`.

[Local preview](../../assets/components/search.png) · [Design record](search_log.md) · [Figma source](https://www.figma.com/design/cjU0zuiL2r8YXsGmnNxxy2/DS-%7C-Shared?node-id=6419-1539)

Appearance describes the bundled preview. Recorded rules describe the local design record or a named token. The preview canvas does not specify this component's background, spacing, or unseen states. Use recorded values for exact measurements.

## Appearance

Preview shows a wide pill-shaped field with a muted dark fill. A white outlined magnifying glass leads the row. White entered text follows it, with a visible vertical caret. A smaller circular control sits inside the right end of the pill, on a lighter gray surface, with a white X centered inside. The icon, text, and clear control share a horizontal centerline. The field has no visible label or helper text outside it in this example.

## Recorded rules

Search is 44 px high, and its close control uses the 24 px X-Small Icon Button. Version 1.1.0 replaces the previous 12 px Figma padding approach with a fixed 44 px height, so 12 px is not a current universal padding rule. Text uses utility styling; the background uses the recorded weak treatment. Hover and focus are documented, placeholder hover is separate from entered-text hover, and version 1.2.0 adds Active. Version 1.3.0 adds `type=float` for a search bar placed above content. The single preview does not define a distinct float surface or shadow.
