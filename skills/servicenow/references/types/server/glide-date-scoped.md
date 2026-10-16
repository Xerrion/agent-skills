# GlideDate: server scoped contracts

API references: [global API](../../sources/api-reference/server-api-reference/glide-date-global.md) and [scoped API](../../sources/api-reference/server-api-reference/glide-date-scoped.md).

For other scoped methods, use the scoped API reference above.
Examples: [task guide](../../glide-date.md).

| Signature                                      | Documented context                                          |
| ---------------------------------------------- | ----------------------------------------------------------- |
| `getValue()`                                   | Scoped source. Read the internal-format date.               |
| `getDisplayValueEx(String style)`              | Scoped source. Styled display.                              |
| `setDisplayValueEx(String date, String style)` | Scoped source. Styled input.                                |
| `subtract(GlideDate start, GlideDate end)`     | Scoped source. Return the date difference as GlideDuration. |

Do not treat a date-only difference as elapsed seconds between two instants.
For elapsed time, use GlideDateTime with an explicit time-zone policy.
