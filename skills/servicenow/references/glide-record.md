# GlideRecord: query, read, and change records

GlideRecord represents records from one server-side table. Build a filter, execute it, and move through the results before reading values.

API references: [global API](sources/api-reference/server-api-reference/glide-record-global.md) and [scoped API](sources/api-reference/server-api-reference/glide-record-scoped.md).

## Contents

- [Choose the operation](#choose-the-operation)
- [Build and execute a query](#build-and-execute-a-query)
- [Values and field access](#values-and-field-access)
- [Validate writes and deletions](#validate-writes-and-deletions)
- [Limits, windows, and counts](#limits-windows-and-counts)
- [Method contracts](#method-contracts)

## Choose the operation

| Need                         | Pattern                                           | Important distinction                                                |
| ---------------------------- | ------------------------------------------------- | -------------------------------------------------------------------- |
| Retrieve an exact sys_id     | `get("sys_id", sysId)`                            | One-argument `get(value)` can fall back to a display-value match.    |
| Retrieve by another field    | `get(field, value)`                               | Check the Boolean result before reading or updating.                 |
| Read matching records        | Conditions, `query()`, then `while (next())`      | `hasNext()` checks availability without advancing.                   |
| Test existence               | Conditions, `setLimit(1)`, `query()`, `hasNext()` | A full count is unnecessary.                                         |
| Count or summarize           | `GlideAggregate`                                  | See [aggregation](glide-aggregate.md).                               |
| Read on behalf of a user     | `GlideRecordSecure`                               | Record access and query access are separate checks.                  |
| Update one existing record   | Successful `get()`, `setValue()`, `update()`      | An update on a nonexistent record can insert instead.                |
| Insert                       | `initialize()`, values, `insert()`                | `newRecord()` also applies defaults and assigns a unique ID.         |
| Filter through another table | `addJoinQuery()`                                  | It adds a subquery. Joined-table fields do not become result fields. |

`GlideRecord` does not automatically provide the same ACL enforcement as `GlideRecordSecure`.
With ordinary GlideRecord, check record permissions and each field exposed to the caller.
See [ACL design](acl-design.md) for the complete access model.

The [GlideRecordSecure guidance](sources/api-reference/scripts/glide-server-apis.md) distinguishes read/write ACLs from query ACLs.
Query ACL enforcement requires explicit opt-in. Do not infer it from the class name.
System-query methods explicitly bypass query ACL checks. Choose query-access behavior for the intended caller and data source.

## Build and execute a query

Illustrative ES2021 server code:

```javascript
const grIncident = new GlideRecord("incident");
grIncident.addQuery("active", true);
grIncident.addQuery("priority", "IN", "1,2");
grIncident.orderByDesc("sys_created_on");
grIncident.setLimit(20);
grIncident.query();

const incidents = [];
while (grIncident.next()) {
  incidents.push({
    sysId: grIncident.getUniqueValue(),
    number: grIncident.getValue("number"),
    priority: grIncident.getValue("priority"),
  });
}
```

Conditions combine with AND. To express an OR group, retain the query-condition object:

```javascript
const grIncident = new GlideRecord("incident");
const priorityCondition = grIncident.addQuery("priority", "1");
priorityCondition.addOrCondition("priority", "2");
grIncident.addQuery("active", true);
grIncident.query();
```

Use [encoded queries](encoded-queries.md) for trusted complex filters.
Use separate `addQuery(field, operator, value)` arguments for untrusted values.
Allowlist any caller-controlled table, field, and operator.

An invalid encoded-query term can disappear from the filter, leaving a broader result set.
The `glide.invalid_query.returns_no_rows` property does not cover every invalid-query case.
An empty encoded string adds no restriction. Never treat it as a safe no-match filter for a write.

The scoped API documents `isValidEncodedQuery(query)` for validation without executing the query.
The deprecated `isEncodedQueryValid(query)` also applies a valid filter, or adds `sys_idNotValidnull` when the filter is invalid. These methods are not interchangeable.
Confirm availability before use. Syntax validation does not establish authorization or the intended affected records.

## Values and field access

| Method              | Result                                                     | Use                                            |
| ------------------- | ---------------------------------------------------------- | ---------------------------------------------- |
| `getValue(field)`   | Stored string, or `null` for an empty or nonexistent field | Comparisons, reference sys_ids, serialization. |
| `getDisplayValue()` | The record's display value                                 | Human-readable labels.                         |
| `getElement(field)` | GlideElement object                                        | Field permissions, metadata, change detection. |
| `getUniqueValue()`  | Primary key, usually `sys_id`                              | Record identity.                               |

Boolean fields return `"1"` or `"0"` from `getValue()`. Neither string should become a Boolean through truthiness.
Use an explicit comparison when the field is known to be Boolean:

```javascript
const isActive = grIncident.getValue("active") === "1";
```

Copy primitive values into arrays or objects. A stored GlideElement remains a platform object rather than a snapshot of its value.
For reference identity, use `getValue("assigned_to")`, not `assigned_to.sys_id`.
Use [GlideElement](glide-element.md) when an object-level field method is needed.

## Validate writes and deletions

| Operation              | Result or hazard                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------- |
| `insert()`             | Returns the inserted sys_id, or `null` on failure.                                                            |
| `update(reason)`       | Returns the saved sys_id, or `null` on failure. It can insert a nonexistent record.                           |
| `deleteRecord()`       | Returns a Boolean indicating success.                                                                         |
| `updateMultiple()`     | Applies the configured values to matching records. It does not provide each saved record as a result.         |
| `deleteMultiple()`     | Deletes matching records. It does not delete their attachments.                                               |
| `setWorkflow(false)`   | Controls Business Rules, script engines, and audits. The documented cascade-delete path ignores this setting. |
| `autoSysFields(false)` | Suppresses system-field updates, including `sys_mod_count`. Dependent functionality can be affected.          |

Check single-record write results and verify persisted values.
Read back the records affected by a bulk operation.
Do not suppress workflow or audit fields as a default performance measure.

The global `autoSysFields()` source warns that suppressing these updates can disrupt Activity Formatter, History Sets, Notifications, and Metrics.
See [lookup and assignment pitfalls](platform-gotchas.md#record-values-and-insert-context) for exact identity, clearing values, and atomic adjustments.
See [query and deletion pitfalls](platform-gotchas.md#query-and-deletion-behavior) for count optimization and processing exceptions.

`setLimit()` is not a deletion cap for `deleteMultiple()`.
Do not combine bulk deletion with `setLimit()` or `chooseWindow()` as a safety boundary.
Do not use `deleteMultiple()` on tables with currency fields. Delete authorized records individually instead.
The documentation also warns against combining `updateMultiple()` with limits or windows on large tables.

Use `setValue()` to define bulk changes. `updateMultiple()` does not support adding multiple journal entries.
Check journal and clearing behavior separately before selecting a bulk API.

Do not call `current.update()` from a Business Rule to persist changes to `current`.
Use a before rule for those changes. See [Business Rules](business-rules.md).
During before-insert processing, a record can have values without passing `isValidRecord()`.
See [the recorded insert pitfalls](platform-gotchas.md#record-values-and-insert-context).

## Limits, windows, and counts

`setLimit(n)` bounds a read result. `chooseWindow(firstRow, lastRow, forceCount)` selects a row window.
Window indices are zero-based. The first index is inclusive and the last is exclusive.
Use a stable order when requesting successive windows.

Calling `setLimit()` after `chooseWindow()` replaces the window.
Windowed queries can trigger an extra `COUNT(*)`.
The documentation describes `setNoCount()` for reads that do not need that count.
A query that already uses `setLimit()` does not need `setNoCount()` for that purpose.

Use `GlideAggregate` for a count-only query.
Calling `getRowCount()` after fetching rows is different from asking the database only for a count.

## Method contracts

Read the [global catalogue](types/server/glide-record-global.md) for global signatures and the [scoped supplement](types/server/glide-record-scoped.md) for documented scoped distinctions.
