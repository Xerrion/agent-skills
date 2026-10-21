# Type styles

Exact definitions: [typography.json](../tokens/typography.json).

Select the complete style for the element's role, including its font type, size, and line height.
Use the [mapped TV2 font face](../artwork/fonts.md) for each style. Product interfaces must use the TV2 typeface.
The size categories use the [platform breakpoints](breakpoints.md).

The JSON defines 35 styles.
Font sizes are in pixels.
Relative line heights become unitless CSS values, such as `line-height: 1.4`.
Absolute line heights become pixel values, such as `line-height: 20px`.
Preserve that distinction when implementing the styles.

### Headings

| Style | Font type | sm | md | lg | tv | Line height |
| ----- | --------- | -: | -: | -: | -: | ----------: |
| `heading.3xlarge` | `bold` | 36 | 48 | 60 | 76 | 1.1 |
| `heading.2xlarge` | `bold` | 32 | 42 | 48 | 60 | 1.1 |
| `heading.xlarge` | `bold` | 28 | 32 | 36 | 54 | 1.1 |
| `heading.large` | `bold` | 24 | 28 | 32 | 42 | 1.1 |
| `heading.medium` | `bold` | 18 | 20 | 20 | 32 | 1.1 |
| `heading.small` | `bold` | 16 | 18 | 18 | 28 | 1.1 |
| `heading.xsmall` | `bold` | 14 | 16 | 16 | 24 | 1.1 |

### Accents

| Style | Font type | sm | md | lg | tv | Line height |
| ----- | --------- | -: | -: | -: | -: | ----------: |
| `accent.xlarge` | `light` | 32 | 36 | 48 | 60 | 1.2 |
| `accent.large` | `light` | 28 | 32 | 36 | 54 | 1.2 |
| `accent.medium` | `light` | 24 | 28 | 32 | 42 | 1.2 |
| `accent.small` | `light` | 20 | 24 | 24 | 36 | 1.2 |
| `accent.xsmall` | `light` | 18 | 20 | 20 | 32 | 1.2 |

### Body

| Style | Font type | sm | md | lg | tv | Line height |
| ----- | --------- | -: | -: | -: | -: | ----------: |
| `body.large` | `regular` | 18 | 18 | 18 | 36 | 1.4 |
| `body.large.bold` | `bold` | 18 | 18 | 18 | 36 | 1.4 |
| `body.large.italic` | `regularItalic` | 18 | 18 | 18 | 36 | 1.4 |
| `body.medium` | `regular` | 16 | 16 | 16 | 32 | 1.4 |
| `body.medium.bold` | `bold` | 16 | 16 | 16 | 32 | 1.4 |
| `body.medium.italic` | `regularItalic` | 16 | 16 | 16 | 32 | 1.4 |
| `body.small` | `regular` | 14 | 14 | 14 | 28 | 1.4 |
| `body.small.bold` | `bold` | 14 | 14 | 14 | 28 | 1.4 |
| `body.small.italic` | `regularItalic` | 14 | 14 | 14 | 28 | 1.4 |

### Utility

`value` and `absolute` apply to non-TV layouts; `tvvalue` and `tvabsolute` apply to TV layouts.

| Style | Font type | Size | Line height | TV size | TV line height |
| ----- | --------- | ---: | ----------: | ------: | -------------: |
| `utility.large.regular` | `regular` | 18 | 22px | 36 | 44px |
| `utility.large.medium` | `medium` | 18 | 22px | 36 | 44px |
| `utility.medium.regular` | `regular` | 16 | 20px | 32 | 40px |
| `utility.medium.medium` | `medium` | 16 | 20px | 32 | 40px |
| `utility.small.regular` | `regular` | 14 | 18px | 28 | 36px |
| `utility.small.medium` | `medium` | 14 | 18px | 28 | 36px |
| `utility.xsmall.regular` | `regular` | 12 | 14px | 24 | 28px |
| `utility.xsmall.medium` | `medium` | 12 | 14px | 24 | 28px |

### Markers

| Style | Font type | sm | md | lg | tv | Line height |
| ----- | --------- | -: | -: | -: | -: | ----------: |
| `marker.xsmall` | `medium` | 12 | 14 | 14 | 24 | 1.1 |
| `marker.small` | `medium` | 14 | 16 | 16 | 24 | 1.1 |
| `marker.medium` | `medium` | 16 | 18 | 18 | 32 | 1.1 |
| `marker.large` | `medium` | 20 | 24 | 24 | 32 | 1.1 |
| `marker.xlarge` | `medium` | 24 | 28 | 28 | 36 | 1.1 |
| `marker.2xlarge` | `medium` | 28 | 32 | 32 | 42 | 1.1 |
