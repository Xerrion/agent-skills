# GlideElement: field values, permissions, and changes

A GlideElement represents one field on a GlideRecord.
Use its methods for field-specific behavior. Use `GlideRecord.getValue()` when you only need a stored string.

API references: [global API](sources/api-reference/server-api-reference/glide-element-global.md) and [scoped API](sources/api-reference/server-api-reference/glide-element-scoped.md).

## Choose a value representation

| Need                         | Method                                       | Result                                                    |
| ---------------------------- | -------------------------------------------- | --------------------------------------------------------- |
| Stored value                 | `gr.getValue(field)` or `element.getValue()` | A string representation of the database value.            |
| Display text                 | `element.getDisplayValue()`                  | A label, reference display value, or formatted date.      |
| Choice label                 | `element.getChoiceValue()`                   | The label for the selected choice, not its stored value.  |
| Copy into an array or object | A stored string or `element.toString()`      | A primitive snapshot rather than a retained field object. |
| Check empty                  | `element.nil()`                              | True for null or an empty string.                         |
| Inspect metadata             | `element.getED()`                            | An element descriptor, not the field's data.              |

Do not use a display value as a record key.
For a reference sys_id, use the parent record's `getValue(referenceField)`.
Check Boolean strings explicitly. `"0"` is a nonempty string and therefore truthy in JavaScript.

## Field permissions

`gr.canRead()` checks record access. `gr.getElement(field).canRead()` checks field access.
A readable record can still contain fields the caller may not read.
Apply the relevant record and field checks before exposing data through GlideAjax, widgets, or REST.

```javascript
const grIncident = new GlideRecord("incident");
if (grIncident.get(sysId) && grIncident.canRead()) {
  const element = grIncident.getElement("short_description");
  if (element.canRead()) {
    const description = grIncident.getValue("short_description");
    // Pass the value only to the authorized caller.
  }
}
```

For this server-side fragment, supply a validated incident sys_id and an authorized response path.
Field methods do not replace the broader [ACL evaluation model](acl-design.md).

## Change detection

| Method               | Meaning                                                              |
| -------------------- | -------------------------------------------------------------------- |
| `changes()`          | The field value changed in the current supported transition context. |
| `changesFrom(value)` | The field changed from the supplied previous value.                  |
| `changesTo(value)`   | The field changed to the supplied new value.                         |

The documented `changes()` contract excludes journal fields and does not support calls from ACL scripts.
Async Business Rule scripts lack the previous record and cannot use these methods for transition detection.
Their condition context is different. See [Business Rule conditions](business-rules.md#conditions-and-operations).

During insert, `changes()` has been observed to miss initially set values. Affected fields and execution contexts are unconfirmed.
For logic that must cover both insertion and updates, account for the operation explicitly:

```javascript
current.operation() === "insert" || current.assignment_group.changes();
```

Use this expression in a Business Rule condition. GlideElement method calls differ from reading values through direct dot notation.
See [the insert pitfalls](platform-gotchas.md#record-values-and-insert-context) for their observed scope.

## References and journal fields

`getRefRecord()` retrieves the referenced GlideRecord.
An empty reference returns an empty GlideRecord object rather than `null`.
Check `isValidRecord()` before treating it as a retrieved database row.
Avoid repeating reference retrieval inside a loop. Batch the referenced IDs when practical.
Do not assume the retrieved record inherits your caller's authorization.

`getJournalEntry(1)` returns the most recent entry.
`getJournalEntry(-1)` returns all entries separated by blank lines.
The text contains the field label, timestamp, and user display name, not just the note body.
Do not parse it as structured audit data or send it to logs.

`setJournalEntry(entry, userName)` adds an entry with an author.
The author parameter changes the attribution of the journal entry.
For bulk journal updates, see [GlideRecord write behavior](glide-record.md#validate-writes-and-deletions).

## Dates, choices, and escaped output

`dateNumericValue()` and `setDateNumericValue()` expose the documented duration-field numeric representation.
Read the field's type before treating its value as an absolute timestamp.
Use [date and time guidance](date-time.md) for GlideDateTime calculations.

`getChoices(dependent)` returns the base table's choice values, not necessarily an extended table's complete choices.
Resolve choices against the actual target table.
Do not assume the returned Java collection is a native JavaScript array.

The HTML, XHTML, XML, and escaped-value methods serve different output formats.
Select the method for the actual sink. A formatted display value is not an HTML-escaping guarantee.
Avoid direct DOM insertion of unchecked display text.

## Method contracts

Read the [global catalogue](types/server/glide-element-global.md) for global signatures and the [scoped supplement](types/server/glide-element-scoped.md) for documented scoped distinctions.
