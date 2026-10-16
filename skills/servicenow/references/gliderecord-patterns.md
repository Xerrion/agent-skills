# GlideRecord and GlideAggregate patterns

Use these recipes for query design, copied field values, batching, and writes.
See the [GlideRecord guide](glide-record.md), [GlideAggregate guide](glide-aggregate.md), and [sources](sources.md) for the underlying global and scoped contracts.

## JavaScript Mode

The GlideRecord API rules below hold in both ES5 and ECMAScript 2021 mode.
Examples use `var` for compatibility. In ES2021 mode, use `const`/`let` and use `Map`/`Set` where they improve clarity.
See [Server scripting](scripting.md) to confirm an artifact's mode.

## Stored values and field objects

Use `getValue(field)` when you need a stored scalar value, especially when collecting values across rows.
Use `setValue(field, value)` for explicit dynamic field assignment.
The API also documents field-property assignment.
GlideElement methods remain appropriate for permissions, metadata, and change detection.

A query iterator reuses record and field objects. Copy values when retaining data from a row:

```javascript
// Correct: each array entry is the stored value from that row.
var states = [];
var grInc = new GlideRecord("incident");
grInc.addQuery("active", true);
grInc.query();
while (grInc.next()) {
  states.push(grInc.getValue("state"));
}

// Intentionally incorrect for a snapshot of scalar values.
var fieldObjects = [];
var grOther = new GlideRecord("incident");
grOther.addQuery("active", true);
grOther.query();
while (grOther.next()) {
  fieldObjects.push(grOther.state); // Retains a field object, not its copied value.
}
```

Call `query()` after constructing a query and before iterating its result set.
A successful `get()` already retrieves a record and does not need a second query.
For user-facing reads, apply the [record and field access checks](glide-record.md#choose-the-operation).

## Query Patterns

### Basic Query

```javascript
var gr = new GlideRecord("incident");
gr.addQuery("state", "1"); // equals
gr.addNotNullQuery("assigned_to"); // field is not empty
gr.addActiveQuery(); // active=true
gr.orderByDesc("sys_created_on");
gr.setLimit(10);
gr.query();
while (gr.next()) {
  // process
}
```

### Encoded Query (Complex Conditions)

Read [Encoded queries](encoded-queries.md) whenever constructing, translating, reviewing, or debugging an encoded query.
That reference covers operators, `^OR`/`^NQ` composition, date formulas, and injection safety.

```javascript
var gr = new GlideRecord("incident");
gr.addEncodedQuery("state=1^priority<=2^assignment_groupISNOTEMPTY");
gr.query();
while (gr.next()) {
  // process
}
```

Use `addEncodedQuery()` when:

- You have complex OR conditions
- The query is a trusted, server-owned string copied from a tested filter

Do not pass client-supplied `sysparm_query` or another URL parameter to `addEncodedQuery()`. Do not concatenate user input into an encoded query. Reconstruct allowed conditions with `addQuery(field, operator, value)` so the caller cannot introduce encoded-query separators, operators, or fields.

### Reference Field Queries

```javascript
// Copy the stored reference sys_id.
var assignedTo = gr.getValue("assigned_to"); // returns sys_id string

// Avoid retaining this GlideElement when you need a copied sys_id.
var assignedTo = gr.assigned_to.sys_id; // unnecessary, getValue already returns sys_id

// Query by reference field
var grTask = new GlideRecord("task");
grTask.addQuery("assigned_to", userId); // pass sys_id directly
grTask.query();
```

## Existence Checks

For a query that only checks existence, use `setLimit(1)`.
Use `get()` when you also need a matching record.

```javascript
// Bounded existence check. The caller supplies trusted table and field names.
function recordExists(table, field, value) {
  var gr = new GlideRecord(table);
  gr.addQuery(field, value);
  gr.setLimit(1);
  gr.query();
  return gr.hasNext();
}

// Retrieve a record when its values are needed.
var gr = new GlideRecord("sys_user");
if (gr.get("user_name", "admin")) {
  // gr is now populated with the record
  var name = gr.getValue("name");
}

// Intentionally inefficient for an existence-only question: no result limit.
var gr = new GlideRecord("incident");
gr.addQuery("active", true);
gr.query();
if (gr.next()) {
  // The query has no explicit bound although only one result is needed.
  // ...
}
```

## GlideAggregate (Counts, Sums, Averages)

Use GlideAggregate when you only need a database aggregate.
If the task already needs every matching row, counting processed rows may be appropriate.
`getRowCount()` and aggregation have different query costs and access semantics.

```javascript
// Correct: count with GlideAggregate
var ga = new GlideAggregate("incident");
ga.addQuery("active", true);
ga.addAggregate("COUNT");
ga.query();
if (ga.next()) {
  var count = parseInt(ga.getAggregate("COUNT"));
}

// Correct: count grouped by field
var ga = new GlideAggregate("incident");
ga.addQuery("active", true);
ga.addAggregate("COUNT");
ga.groupBy("priority");
ga.query();
while (ga.next()) {
  var priority = ga.getValue("priority");
  var count = parseInt(ga.getAggregate("COUNT"));
  gs.info("Priority {0}: {1} incidents", priority, count);
}

// Correct: average
var ga = new GlideAggregate("incident");
ga.addAggregate("AVG", "reassignment_count");
ga.query();
if (ga.next()) {
  var avgReassign = ga.getAggregate("AVG", "reassignment_count");
}

// Intentionally inefficient when count is the only required result.
var gr = new GlideRecord("incident");
gr.addQuery("active", true);
gr.query();
var count = 0;
while (gr.next()) {
  count++; // WRONG: use GlideAggregate instead
}
```

## Avoid repeated queries in loops

Repeated dependent queries can create an N+1 workload.
Batch related identifiers when the task permits it. A bounded dependent query can still be necessary for a particular operation.

```javascript
// Intentionally inefficient N+1 lookup.
var grInc = new GlideRecord("incident");
grInc.addQuery("active", true);
grInc.query();
while (grInc.next()) {
  var grUser = new GlideRecord("sys_user"); // QUERY IN LOOP!
  grUser.get(grInc.getValue("assigned_to"));
  // ...
}

// Batch query, then lookup.
var userMap = {};
var grInc = new GlideRecord("incident");
grInc.addQuery("active", true);
grInc.query();

// Collect unique user sys_ids
var userIds = [];
while (grInc.next()) {
  var userId = grInc.getValue("assigned_to");
  if (userId && userIds.indexOf(userId) === -1) {
    userIds.push(userId);
  }
}

// Single batch query for all users
if (userIds.length > 0) {
  var grUser = new GlideRecord("sys_user");
  grUser.addQuery("sys_id", "IN", userIds.join(","));
  grUser.query();
  while (grUser.next()) {
    userMap[grUser.getUniqueValue()] = grUser.getValue("name");
  }
}

// Now use the map for lookups (no queries)
grInc = new GlideRecord("incident");
grInc.addQuery("active", true);
grInc.query();
while (grInc.next()) {
  var userName = userMap[grInc.getValue("assigned_to")] || "Unassigned";
}
```

An ES2021 fragment of the same batch pattern uses `Set` and `Map`.
`someUserId` represents a previously obtained reference sys_id:

```javascript
const userIds = new Set();
const grInc = new GlideRecord("incident");
grInc.addQuery("active", true);
grInc.query();
while (grInc.next()) {
  const userId = grInc.getValue("assigned_to");
  if (userId) {
    userIds.add(userId);
  }
}

const userNames = new Map();
if (userIds.size > 0) {
  const grUser = new GlideRecord("sys_user");
  grUser.addQuery("sys_id", "IN", [...userIds].join(","));
  grUser.query();
  while (grUser.next()) {
    userNames.set(grUser.getUniqueValue(), grUser.getValue("name"));
  }
}

// Lookups are now in-memory
const displayName = userNames.get(someUserId) ?? "Unassigned";
```

## Factory Methods (Prefer Over Manual Conditions)

```javascript
gr.addActiveQuery(); // instead of addQuery('active', true)
gr.addNotNullQuery("assigned_to"); // instead of addQuery('assigned_to', '!=', '')
gr.addNullQuery("closed_at"); // instead of an encoded ISEMPTY condition
gr.addJoinQuery("sys_user_grmember", "assigned_to", "user"); // join queries
```

## Update/Insert/Delete Patterns

| Operation         | Pattern                                                                      | Check                                                                           |
| ----------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Update one record | Successful `get()`, assign values, then `update()`.                          | Check the returned sys_id and persisted values.                                 |
| Insert            | `initialize()`, assign values, then `insert()`.                              | Check the inserted sys_id. Account for defaults and mandatory fields.           |
| Delete one record | Retrieve an authorized record, then `deleteRecord()`.                        | Check its Boolean result and verify absence.                                    |
| Bulk update       | Confirm the filter, assign with `setValue()`, then `updateMultiple()`.       | Verify the intended affected set. It does not return each saved record.         |
| Bulk delete       | Check the complete filter and selected record set before `deleteMultiple()`. | A read limit does not cap deletion. Attachments are not deleted by this method. |

Do not use `deleteMultiple()` on currency tables.
Do not rely on `setLimit()` or `chooseWindow()` to constrain a bulk deletion.
The documentation also warns against using limits or windows with bulk updates on large tables.
See [write and deletion contracts](glide-record.md#validate-writes-and-deletions).

## Performance Tips

| Need                     | Approach                                   | Constraint                                                           |
| ------------------------ | ------------------------------------------ | -------------------------------------------------------------------- |
| Bounded read             | `setLimit()`                               | It bounds records, not a field projection or bulk deletion.          |
| Pagination               | Stable ordering and `chooseWindow()`       | Windows can trigger an additional count query.                       |
| Avoid a pagination count | `setNoCount()` where supported             | A read already using `setLimit()` does not need it for that purpose. |
| Count only               | GlideAggregate                             | `getRowCount()` after fetching records is a different workload.      |
| Related values           | Batch referenced sys_ids, then use a map   | Bound or chunk the collected IDs for the actual workload.            |
| Repeated filters         | Inspect the predicate and relevant indexes | An encoded string does not make the query indexed by itself.         |

The GlideRecord contracts do not establish `setFields()` or `chooseWindowQuery()` as supported methods.
Do not present them as supported field-selection APIs without additional evidence.
`setWorkflow(false)` and `autoSysFields(false)` change processing and history. They are not default performance tips.
