# Dates and times: storage, display, and arithmetic

Use GlideDate for calendar dates and GlideDateTime for instants that include a time.
Decide whether an operation means a local calendar change or an elapsed duration before choosing a method.

Sources: [scoped GlideDateTime API](sources/api-reference/server-api-reference/glide-date-time-scoped.md) and [date-format guidance](sources/api-reference/scripts/glide-server-apis.md).

## Storage and display are different contracts

| Method                           | Format                                      | Time-zone context                                                 |
| -------------------------------- | ------------------------------------------- | ----------------------------------------------------------------- |
| `getValue()`                     | `yyyy-MM-dd HH:mm:ss`                       | UTC. Use for stored values and integration payloads.              |
| `getDisplayValue()`              | Current user's display format               | Current user's time zone. Use for presentation.                   |
| `getDisplayValueInternal()`      | `yyyy-MM-dd HH:mm:ss`                       | Current user's time zone. Internal format does not mean UTC here. |
| `getNumericValue()`              | Number of milliseconds since the Unix epoch | An absolute instant.                                              |
| `setValue(value)`                | Prefer explicit `yyyy-MM-dd HH:mm:ss` input | A string in this form means UTC.                                  |
| `setDisplayValueInternal(value)` | `yyyy-MM-dd HH:mm:ss`                       | Interpret as the current user's local time.                       |
| `setValueUTC(value, format)`     | Supplied explicit date pattern              | Interpret as UTC. Use for a known nonstandard input format.       |

Do not assign a user's display value to a stored timestamp as if it were UTC.
Do not infer time zone from the string's shape.
Avoid parsing ambiguous month/day strings through constructor fallback rules.

The GlideDateTime constructor documentation does not accept the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.
Do not assume an arbitrary ISO timestamp is a valid GlideDateTime constructor argument.
Convert it through an explicitly supported format and offset policy.

## Construct and validate

| Signature                            | Meaning                                                             |
| ------------------------------------ | ------------------------------------------------------------------- |
| `GlideDateTime()`                    | Current date and time.                                              |
| `GlideDateTime(String value)`        | Initialize from a UTC date/time string. Prefer the internal format. |
| `GlideDateTime(GlideDateTime value)` | Copy another object.                                                |
| `isValid()`                          | Check whether the object contains a valid date and time.            |

Illustrative ES2021 server code:

```javascript
const timestamp = new GlideDateTime("2026-10-06 08:00:00");
if (!timestamp.isValid()) {
  throw new Error("Invalid timestamp.");
}
const storedValue = timestamp.getValue();
const displayValue = timestamp.getDisplayValue();
```

The source is a UTC value. The display value depends on the current user.
Check untrusted inputs against the accepted format before constructing the object.
`isValid()` does not resolve an ambiguous format or establish which time zone the caller intended.

For setter exceptions, day-of-month clamping, or week-number conventions, read [date parsing and calendar pitfalls](platform-gotchas.md#date-parsing-and-calendar-behavior).

## Choose calendar or elapsed-time arithmetic

| Requirement                                   | Method                               | Consequence                                    |
| --------------------------------------------- | ------------------------------------ | ---------------------------------------------- |
| Same local clock time on another calendar day | `addDaysLocalTime(days)`             | Uses local calendar values.                    |
| Change the UTC calendar day                   | `addDaysUTC(days)`                   | Uses UTC calendar values.                      |
| Add a fixed elapsed interval                  | `addSeconds(seconds)`                | Express the interval in seconds.               |
| Subtract an elapsed interval                  | `subtract(milliseconds)`             | This overload uses milliseconds, not seconds.  |
| Compare absolute instants                     | `getNumericValue()`                  | Compare numbers rather than localized strings. |
| Compute a duration                            | `GlideDateTime.subtract(start, end)` | Returns GlideDuration.                         |

Across daylight-saving transitions, a local calendar day need not equal 24 elapsed hours.
Use `addDaysLocalTime(1)` for a local-calendar requirement.
Use `addSeconds(86400)` only when the requirement is exactly 24 elapsed hours.

```javascript
const start = new GlideDateTime("2026-10-06 08:00:00");
const nextLocalDay = new GlideDateTime(start);
nextLocalDay.addDaysLocalTime(1);

const after24Hours = new GlideDateTime(start);
after24Hours.addSeconds(86400);
```

These objects express different requirements. Do not replace one method with the other as a refactoring.
Choosing local-calendar arithmetic does not make local display strings appropriate for UTC storage.

## Focused verification cases

- An internal UTC value survives a storage and read-back cycle.
- Different user time zones change display values without changing the stored instant.
- Input containing an ambiguous day and month is rejected or parsed through a known explicit format.
- A local-day rule preserves the intended local clock time across daylight-saving transitions.
- An elapsed-duration rule preserves the intended milliseconds across those transitions.
- Empty date fields do not silently become the current time.

See [GlideDate](glide-date.md) for date-only values.
