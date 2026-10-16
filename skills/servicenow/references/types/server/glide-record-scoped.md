# GlideRecord: server scoped contracts

API references: [global API](../../sources/api-reference/server-api-reference/glide-record-global.md) and [scoped API](../../sources/api-reference/server-api-reference/glide-record-scoped.md).

For other scoped methods, use the scoped API reference above.
Examples: [task guide](../../glide-record.md).

| Method                                                | Use or constraint                                                                       |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `getElements()`                                       | Get an array of field objects. Distinct from the global `getFields()` collection.       |
| `getLastErrorMessage()`                               | Read the most recent record error, or `null`.                                           |
| `isActionAborted()`                                   | Check the action-abort flag.                                                            |
| `isView()`                                            | Check whether the record came from a view.                                              |
| `isValidEncodedQuery(query)`                          | Validate syntax without executing the query.                                            |
| `isEncodedQueryValid(query)`                          | Deprecated. Applies a valid filter, or adds `sys_idNotValidnull` for an invalid filter. |
| `setCategory(category)`                               | Select the query-routing category. Requires the applicable database configuration.      |
| `addUserQuery(...)` / `addUserEncodedQuery(query)`    | Explicitly enforce user query access where supported.                                   |
| `addUserOrderBy(field)` / `addUserOrderByDesc(field)` | Apply query-access checks to ordering.                                                  |

The documentation also lists `addSystemQuery`, `addSystemEncodedQuery`, `addSystemOrderBy`, and `addSystemOrderByDesc`.
Those APIs explicitly bypass query-access checks for system-level queries. Select them only when that access context is intended; they do not stand for user authorization.
