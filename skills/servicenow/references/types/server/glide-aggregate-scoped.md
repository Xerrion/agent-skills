# GlideAggregate: server scoped contracts

API references: [global API](../../sources/api-reference/server-api-reference/glide-aggregate-global.md) and [scoped API](../../sources/api-reference/server-api-reference/glide-aggregate-scoped.md).

For other scoped methods, use the scoped API reference above.
Examples: [task guide](../../glide-aggregate.md).

The scoped API documents `addQuery`, `addNullQuery`, `addNotNullQuery`, `hasNext`, `next`, `getTableName`, and `getEncodedQuery`.
It uses `getAggregateEncodedQuery()` for the query selecting the current aggregate's records.
Do not assume the global `getQuery()` spelling applies to a scoped script.

Both APIs document `setAggregateWorkflow()` and `setCategory()`.
The scoped source also documents `orderByDesc()`.
These methods control query processing or routing. They do not grant access to additional data.
An internal aggregate query is not evidence that a caller may see its totals.
