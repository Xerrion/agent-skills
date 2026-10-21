# Platform breakpoints

Exact definitions: [breakpoint.json](../tokens/breakpoint.json).

Design the `sm` layout first.
The same breakpoint names use different units and values across platforms.

| Breakpoint | Web (px) | iOS size class | Android (dp) |
| ---------- | -------: | -------------- | ------------ |
| `sm`       |        0 | compact        | 0            |
| `md`       |      680 | regular        | 600          |
| `lg`       |     1024 | regular        | 840          |
| `xl`       |     1440 | regular        | 1024         |
| `2xl`      |     1920 | regular        | 1280         |
| `tv`       |     1920 | tvOS           | television   |

iOS values are UIKit size classes, not pixel thresholds.
Android values are density-independent pixels.
In Figma, an `sm` frame represents responsive web, Android mobile, and iOS compact layouts.
The table follows the bundled JSON, including its native `xl` and `2xl` entries.
The source's breakpoint prose describes those two names as web-only; use the JSON values when the sources disagree.

### Web layout ranges

| Layout | Width range | Recorded context |
| --- | --- | --- |
| `sm` | Below 680 px | Default responsive web and compact mobile layout |
| `md` | From 680 px to below 1024 px | Tablet and larger phones in landscape |
| `lg` | From 1024 px to below 1440 px | Desktop and larger tablets |
| `xl` | From 1440 px to below 1920 px | Wider desktop layout |
| `2xl` | From 1920 px | Wider desktop layout |

The `tv` category also records a 1920 px web threshold. Select it for an intended television interface rather than automatically applying TV typography to a wide desktop browser.
Typography and responsive sizes provide `sm`, `md`, `lg`, and `tv` values, with no separate `xl` or `2xl` values.
Keep the `lg` value for wider desktop layouts unless the application has an explicit additional mapping.
