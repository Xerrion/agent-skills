# GlideAggregate: server global contracts

API references: [global API](../../sources/api-reference/server-api-reference/glide-aggregate-global.md) and [scoped API](../../sources/api-reference/server-api-reference/glide-aggregate-scoped.md).

Examples: [task guide](../../glide-aggregate.md).

Check the API reference for optional arguments and context restrictions.

| Signature                                                                             | Purpose                                                       |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| `GlideAggregate(String tableName)`                                                    | Construct an aggregate query.                                 |
| `addAggregate(String agg, String name)`                                               | Add an aggregate, optionally over a field.                    |
| `addEncodedQuery(String query)`                                                       | Add a trusted encoded input filter.                           |
| `addHaving(String name, String operator, String value)`                               | Filter aggregate results.                                     |
| `addHaving(String aggName, String fieldName, String operator, String value)`          | Filter an aggregate over a particular field or attribute.     |
| `addTrend(String fieldName, String timeInterval, Number numUnits)`                    | Group by a time interval.                                     |
| `addBizCalendarTrend(String fieldName, String bizCalendarSysId)`                      | Group by a business-calendar period.                          |
| `getAggregate(String agg, String name)`                                               | Read the current aggregate as a string.                       |
| `getQuery()`                                                                          | Read the filter that selects the current aggregate's records. |
| `getRowCount()`                                                                       | Count aggregate result rows.                                  |
| `getTotal(String agg, String name)`                                                   | Sum an aggregate across its results. Returns a number.        |
| `getValue(String name)`                                                               | Read a group field or dynamic attribute.                      |
| `groupBy(String name)`                                                                | Add a group field or attribute.                               |
| `orderBy(String name)`                                                                | Sort ascending and add the field to grouping.                 |
| `orderByAggregate(String agg, String fieldName)`                                      | Sort by an aggregate and field.                               |
| `query()`                                                                             | Execute the aggregate query.                                  |
| `setAggregateWindow(Number firstRow, Number lastRow)`                                 | Restrict the input-row range.                                 |
| `setGroup(Boolean b)`                                                                 | Enable or disable grouping.                                   |
| `setIntervalYearIncluded(Boolean b)`                                                  | Separate years in day-of-week trends.                         |
| `getDynamicAttributeValue(String fullPath)`                                           | Read an attribute by path.                                    |
| `getDynamicAttributeValue(String dynamicAttributeField, String groupAttrPath)`        | Read an attribute by field and path.                          |
| `getDynamicAttributeDisplayValue(String fullPath)`                                    | Read an attribute display value by path.                      |
| `getDynamicAttributeDisplayValue(String dynamicAttributeField, String groupAttrPath)` | Read an attribute display value by field and path.            |

The global source also documents `setAggregateWorkflow()` and `setCategory()`. These control query processing and routing.
