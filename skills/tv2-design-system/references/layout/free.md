# Free product layout

Scope: the Figma page titled `tv2.dk (web) & Free apps`. These values belong to Free and do not replace [Play spacing](play.md).

The complete [local measurement record](../figma/layout-free.json) contains the three layout frames, native auto-layout properties, and variable modes. Figma access is unnecessary.

| Variable | SM (360 frame) | MD (840 frame) | LG (1440 frame) |
| --- | --- | --- | --- |
| Page margin | 12 px | 28 px | 28 px |
| Teaser gap | 8 px | 16 px | 16 px |
| Deck gap | 0 px | 0 px | 0 px |
| Deck padding top | 24 px | 32 px | 32 px |
| Deck padding bottom | 24 px | 32 px | 32 px |

The SM and MD example decks fill their 360 px and 840 px frame widths. LG example decks are 1000 px wide and centered in the 1440 px frame. Each example row contains two equally sized 16:9 media placeholders. These examples do not prescribe two columns for every content type.
The SM frame also has an 8 px page-level gap, while MD and LG bind that gap to the zero deck-gap variable. Keep this distinction when reproducing those exact frames.

The variables have a warning marker in their upstream names. Preserve that provenance and treat this as a pinned layout observation. The source does not establish universal container limits for other TV 2 products or television values for Free.
Use [breakpoint tokens](../foundations/breakpoints.md) for CSS thresholds; the Figma reference frame widths are not breakpoint definitions.

Source: file `cjU0zuiL2r8YXsGmnNxxy2`, page `8449:191`, frames `8645:464`, `8645:510`, and `8645:526`, captured 2026-10-21. [Optional upstream Figma](https://www.figma.com/design/cjU0zuiL2r8YXsGmnNxxy2/DS-%7C-Shared?node-id=8449-191).
