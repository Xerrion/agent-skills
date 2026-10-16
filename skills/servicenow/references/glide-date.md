# GlideDate: date-only values and formatting

Use GlideDate for a date without a time of day.
Use [GlideDateTime](date-time.md) for timestamps, elapsed time, and time-zone-aware arithmetic.

API references: [global API](sources/api-reference/server-api-reference/glide-date-global.md) and [scoped API](sources/api-reference/server-api-reference/glide-date-scoped.md).
Global and scoped locale methods have different overloads.

## Stored values and display values

| Need                         | Method                                                   | Format and context                                                                |
| ---------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Set a stored date            | `setValue(value)`                                        | Internal `yyyy-MM-dd` format and system time zone, UTC by default.                |
| Read the stored date         | `getValue()`                                             | Explicitly documented in the scoped source. Internal format and system time zone. |
| Render a pattern             | `getByFormat(format)`                                    | Uses Java SimpleDateFormat tokens.                                                |
| Read the normal display      | `getDisplayValue()`                                      | Documented as UTC. Distinct from GlideDateTime display semantics.                 |
| Read internal-format display | `getDisplayValueInternal()`                              | `yyyy-MM-dd` in the current user's time zone.                                     |
| Read calendar components     | `getDayOfMonthNoTZ()`, `getMonthNoTZ()`, `getYearNoTZ()` | UTC components. The month is 1 through 12.                                        |
| Parse user-entered display   | `setDisplayValue(value)`                                 | Current user's display format and time zone.                                      |

Do not send an ambiguous date such as `02/03/2026` to an API without a known input format and locale.
Use internal values for storage and explicit display methods for presentation.

Illustrative ES2021 server code:

```javascript
const date = new GlideDate();
date.setValue("2026-10-06");
const formatted = date.getByFormat("dd-MM-yyyy");
```

The explicit formatting result is `06-10-2026`.

Java format tokens are case-sensitive:

| Token  | Meaning                                                           |
| ------ | ----------------------------------------------------------------- |
| `yyyy` | Calendar year.                                                    |
| `MM`   | Month number. Lowercase `mm` means minutes in date/time patterns. |
| `dd`   | Day of month.                                                     |
| `EEEE` | Weekday name.                                                     |

## Locale and style

The documented styles are `short`, `medium`, `long`, and `full`.
Language and locale determine text and ordering. A short date can place month or day first.
The global language-aware methods document case-insensitive styles and a `medium` fallback for an unrecognized style.
Prefer a known style rather than relying on that fallback.

The global API lists one- and two-argument `getDisplayValueLang()` overloads.
The scoped API lists `getDisplayValueLang(String style, String language)`.
Confirm the target scope before using the shorter global form.

`getDisplayValueEx(style)` and `setDisplayValueEx(date, style)` have separate global and scoped contracts.
Use the matching API reference for the target scope.

Do not parse localized output into an integration timestamp.
For timestamps, pair the explicit storage and display contracts in [date and time guidance](date-time.md).

## Method contracts

Read the [global catalogue](types/server/glide-date-global.md) for global signatures and the [scoped supplement](types/server/glide-date-scoped.md) for documented scoped distinctions.
