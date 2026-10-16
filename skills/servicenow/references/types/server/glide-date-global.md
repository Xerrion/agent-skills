# GlideDate: server global contracts

API references: [global API](../../sources/api-reference/server-api-reference/glide-date-global.md) and [scoped API](../../sources/api-reference/server-api-reference/glide-date-scoped.md).

Examples: [task guide](../../glide-date.md).

| Signature                                                         | Purpose or result                                                   |
| ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| `GlideDate()`                                                     | Construct a date initialized to the current date.                   |
| `getByFormat(String format)`                                      | Return a string using the requested Java date pattern.              |
| `getDayOfMonthNoTZ()`                                             | Return the UTC day of month as a number, 1 through 31.              |
| `getDisplayValue()`                                               | Return the documented UTC display value.                            |
| `getDisplayValueInternal()`                                       | Return internal-format display in the user's time zone.             |
| `getDisplayValueLang(String style)`                               | Return localized display using a style.                             |
| `getDisplayValueLang(String style, String language)`              | Return styled display in a requested language.                      |
| `getMonthNoTZ()`                                                  | Return the UTC month as a number, 1 through 12.                     |
| `getYearNoTZ()`                                                   | Return the UTC year as a number.                                    |
| `parseDate(String date, String language, String country)`         | Parse with the supplied language and country locale. Global source. |
| `setDisplayValue(String asDisplayed)`                             | Set the date from the user's display format and time zone.          |
| `setDisplayValueLang(String date, String style)`                  | Set the date from a styled locale value.                            |
| `setDisplayValueLang(String date, String style, String language)` | Set the date with an explicit style and language.                   |
| `setValue(String o)`                                              | Set the internal-format date.                                       |

## Other global contracts

The global source also documents `getDisplayValueEx(String style)` and `setDisplayValueEx(String date, String style)` for styled display and input. The scoped source documents these methods separately.
