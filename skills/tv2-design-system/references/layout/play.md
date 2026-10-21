# TV 2 Play spacing

Exact definitions: [play.json](../tokens/play.json).

TV 2 Play defines `teaser.gap`, `deck.gap`, and `page.margin`.
These reference the primitive size tokens.

| Token | Meaning |
| ----- | ------- |
| `teaser.gap` | Space between individual teasers within a content deck |
| `deck.gap` | Vertical space between content decks stacked on a page |
| `page.margin` | Left margin from the screen edge to the content area |

Play also has an `appletv` breakpoint for Apple TV layouts.
In Play, `appletv` targets Apple TV (tvOS), while `tv` covers Android TV and web TV.
Keep these product layout contexts separate even though the foundation's generic `tv` category also includes tvOS.
The product tokens are work in progress and can introduce breaking changes.

| Token         | sm        | md        | lg        | tv         | appletv   |
| ------------- | --------- | --------- | --------- | ---------- | --------- |
| `teaser.gap`  | `size.8`  | `size.12` | `size.16` | `size.40`  | `size.40` |
| `deck.gap`    | `size.32` | `size.32` | `size.56` | `size.80`  | `size.80` |
| `page.margin` | `size.16` | `size.24` | `size.64` | `size.144` | `size.80` |

### Resolved Play spacing

Values below resolve the product aliases through the primitive size tokens. Implement using the named tokens.

| Layout | Gap between teasers | Vertical gap between decks | Left page margin |
| --- | ---: | ---: | ---: |
| `sm` | 8 px | 32 px | 16 px |
| `md` | 12 px | 32 px | 24 px |
| `lg` | 16 px | 56 px | 64 px |
| `tv` | 40 px | 80 px | 144 px |
| `appletv` | 40 px | 80 px | 80 px |

The small layout keeps teasers close together while decks have a larger vertical separation.
Desktop increases both the left inset and the separation between decks; TV layouts increase the spacing further.
`page.margin` specifies the left inset only. These tokens do not prescribe a symmetric right margin, column count, maximum page width, or teaser aspect ratio.
