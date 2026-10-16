# GlideAggregate: counts, groups, and trends

Use GlideAggregate when the result is a count, sum, average, or grouped summary rather than individual records.
It extends GlideRecord, but each returned row represents an aggregate result.

API references: [global API](sources/api-reference/server-api-reference/glide-aggregate-global.md) and [scoped API](sources/api-reference/server-api-reference/glide-aggregate-scoped.md).

## Choose the aggregate

| Aggregate               | Meaning                                            | Important distinction                                             |
| ----------------------- | -------------------------------------------------- | ----------------------------------------------------------------- |
| `COUNT` without a field | Number of matching records                         | Use this for a record count.                                      |
| `COUNT` with a field    | Count of non-null field values                     | Empty values can change the result.                               |
| `SUM` / `AVG`           | Sum or average of numeric values                   | Parse the returned string only when a numeric result is needed.   |
| `MIN` / `MAX`           | Smallest or largest value                          | Interpret the result according to the field type.                 |
| `STDDEV`                | Population standard deviation                      |                                                                   |
| `GROUP_CONCAT`          | Comma-separated non-null values in ascending order | The result is a string, not an array.                             |
| `GROUP_CONCAT_DISTINCT` | Concatenated values with duplicates removed        | Confirm this aggregate is supported in the effective API context. |

## Count matching records

Illustrative ES2021 server code:

```javascript
const gaIncident = new GlideAggregate("incident");
gaIncident.addQuery("active", true);
gaIncident.addAggregate("COUNT");
gaIncident.query();

let activeCount = 0;
if (gaIncident.next()) {
  activeCount = parseInt(gaIncident.getAggregate("COUNT"), 10);
}
```

`getAggregate()` returns a string. `getRowCount()` counts aggregate result rows, not the underlying incident records.
Use `getAggregate("COUNT")` for the count itself.
Do not fetch all records merely to increment a JavaScript counter.

If totals differ from a record query, inspect [aggregate Query Business Rule processing](platform-gotchas.md#aggregate-queries-can-omit-query-business-rules).

## Group and filter

`addQuery()` filters input records before aggregation.
`groupBy()` defines the result groups.
The global `addHaving()` method filters aggregate results after grouping.

```javascript
const gaIncident = new GlideAggregate("incident");
gaIncident.addQuery("active", true);
gaIncident.addAggregate("COUNT");
gaIncident.groupBy("priority");
gaIncident.query();

const counts = [];
while (gaIncident.next()) {
  counts.push({
    priority: gaIncident.getValue("priority"),
    count: parseInt(gaIncident.getAggregate("COUNT"), 10),
  });
}
```

For a global query that returns only groups with more than five matches, add `addHaving("COUNT", ">", "5")` before `query()`.
For scoped `addHaving()` use, check the scoped API reference. Its availability is not established here.

`orderBy(field)` also adds the field to the group-by list.
Use `orderByAggregate(aggregate, field)` when sorting by an aggregate result.
Do not add a sort field that unintentionally splits one intended group into several groups.
Use `setGroup(false)` when the intended result is an ungrouped aggregate.

## Time trends, windows, and currency

`addTrend(field, interval, numUnits)` groups records into time intervals.
The documentation lists intervals including year, quarter, month, date, week, day-of-week, hour, and minute.
Read the matching source for the accepted interval and unit constraints.
Use `setIntervalYearIncluded()` when day-of-week groups need separate years.
`addBizCalendarTrend()` uses a configured business calendar rather than a normal calendar interval.

`setAggregateWindow(firstRow, lastRow)` restricts the input rows included in the calculation.
Its zero-based first index is inclusive and last index is exclusive.
It changes the dataset being summarized. It is not simply pagination over an unchanged total.

Currency and price aggregation uses reference currency values.
Convert appropriately before displaying session-currency totals.
FX Currency aggregation can return a currency-qualified string such as `USD;134.980000`.
The global source reports a semicolon result when mixed FX currencies cannot be aggregated.
Do not parse that value as an ordinary number or report a successful total.

The scoped API requires GMT/UTC configuration on on-premise database servers.

## Method contracts

Read the [global catalogue](types/server/glide-aggregate-global.md) for global signatures and the [scoped supplement](types/server/glide-aggregate-scoped.md) for documented scoped distinctions.
