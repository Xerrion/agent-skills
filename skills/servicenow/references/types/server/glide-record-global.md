# GlideRecord: server global contracts

API references: [global API](../../sources/api-reference/server-api-reference/glide-record-global.md) and [scoped API](../../sources/api-reference/server-api-reference/glide-record-scoped.md).

Examples: [task guide](../../glide-record.md).

Check the API reference for optional parameters and uncommon overloads.

## Construction, retrieval, and iteration

| Signature                               | Purpose                                                                                |
| --------------------------------------- | -------------------------------------------------------------------------------------- |
| `GlideRecord(String tableName)`         | Create an object for the table.                                                        |
| `get(Object name, Object value)`        | One argument tries sys_id, then display value. Two arguments select a field and value. |
| `initialize()`                          | Prepare an empty record for insertion.                                                 |
| `newRecord()`                           | Prepare a record with defaults and a unique ID.                                        |
| `next()`                                | Advance to the next result.                                                            |
| `_next()`                               | Advance when a table field named `next` conflicts with the method.                     |
| `hasNext()`                             | Check for another result without advancing.                                            |
| `find(String columnName, String value)` | Advance to a matching result.                                                          |
| `isNewRecord()`                         | Check whether the record is unsaved.                                                   |
| `isValid()`                             | Check table or retrieval validity.                                                     |
| `isValidField(String columnName)`       | Check whether the table defines a field.                                               |
| `isValidRecord()`                       | Check whether a database record is present.                                            |
| `instanceOf(String className)`          | Check the record's table class.                                                        |
| `operation()`                           | Identify the current database operation.                                               |
| `changes()`                             | Check for changed fields in the record.                                                |

## Filters, ordering, and execution

| Signature                                                                | Purpose                                                                    |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| `addActiveQuery()`                                                       | Filter to active records.                                                  |
| `addInactiveQuery()`                                                     | Filter to inactive records.                                                |
| `addQuery(String name, Object operator, Object value)`                   | Add a condition. Two arguments imply equality.                             |
| `addEncodedQuery(String query, Boolean enforceFieldACL)`                 | Add an encoded condition with the documented ACL option.                   |
| `addNullQuery(String fieldName)`                                         | Filter to empty values.                                                    |
| `addNotNullQuery(String fieldName)`                                      | Filter to populated values.                                                |
| `addJoinQuery(String table)`                                             | Filter through a related table using default join fields.                  |
| `addJoinQuery(String table, String primaryField)`                        | Specify the base join field.                                               |
| `addJoinQuery(String table, String primaryField, String joinTableField)` | Specify both join fields.                                                  |
| `addDomainQuery(Object glideRecord)`                                     | Use the supplied record's domain. Requires the domain plugin. Global only. |
| `addExtraField(String dotWalkedField)`                                   | Prefetch a related field to reduce database round trips.                   |
| `addFunction(Object function)`                                           | Apply a database-function object.                                          |
| `orderBy(String fieldName)`                                              | Sort ascending. Repeated calls add sort fields.                            |
| `orderByDesc(String fieldName)`                                          | Sort descending.                                                           |
| `setLimit(Number limit)`                                                 | Bound the read result.                                                     |
| `chooseWindow(Number firstRow, Number lastRow, Boolean forceCount)`      | Select a row window with optional counting.                                |
| `setNoCount()`                                                           | Suppress a pagination count where supported.                               |
| `query(String field, String value)`                                      | Execute conditions. The optional arguments add a field-value filter.       |
| `_query(String field, String value)`                                     | Execute when a table field named `query` conflicts with the method.        |
| `queryNoDomain(String field, String value)`                              | Execute without domain filtering. Do not use to bypass isolation.          |
| `disableSysIdInOptimization()`                                           | Disable the documented large-sys_id-list optimization.                     |
| `setQueryReferences(Boolean queryReferences)`                            | Control reference display-name matching.                                   |
| `getEncodedQuery()`                                                      | Inspect the accumulated encoded filter.                                    |
| `getRowCount()`                                                          | Get the result count.                                                      |

## Identity, values, and metadata

| Signature                        | Purpose                                                                     |
| -------------------------------- | --------------------------------------------------------------------------- |
| `getUniqueValue()`               | Read the primary key.                                                       |
| `getValue(String fieldName)`     | Read a stored field value.                                                  |
| `getDisplayValue(String name)`   | Read a display value, including documented dynamic-attribute forms.         |
| `getElement(String fieldName)`   | Get the GlideElement for a field.                                           |
| `getED()`                        | Read the element descriptor.                                                |
| `getAttribute(String fieldName)` | Read dictionary attributes.                                                 |
| `getFields()`                    | Return a Java ArrayList of fields. Do not assume a native JavaScript array. |
| `getTableName()`                 | Read the table name.                                                        |
| `getRecordClassName()`           | Read the record's concrete table class.                                     |
| `getClassDisplayValue()`         | Read the table label.                                                       |
| `getLabel()`                     | Read the field label.                                                       |
| `getPlural()`                    | Read the plural table label.                                                |
| `getLink(Boolean noStack)`       | Build a record link.                                                        |
| `getEscapedDisplayValue()`       | Read the escaped display value for Jelly.                                   |
| `getRelatedLists()`              | Inspect related-list names and labels.                                      |
| `getRelatedTables()`             | Inspect referenced-table names and labels.                                  |
| `hasAttachments()`               | Check attachment presence.                                                  |
| `canCreate()`                    | Check permission to insert.                                                 |
| `canRead()`                      | Check permission to read the current record.                                |
| `canWrite()`                     | Check permission to update.                                                 |
| `canDelete()`                    | Check permission to delete.                                                 |

## Mutation and processing controls

| Signature                                    | Purpose                                                                 |
| -------------------------------------------- | ----------------------------------------------------------------------- |
| `setValue(String name, Object value)`        | Assign a stored value.                                                  |
| `setDisplayValue(String name, Object value)` | Assign by a display value. Resolve ambiguous references carefully.      |
| `addValue(String field, Number value)`       | Apply an atomic numeric adjustment at database level.                   |
| `applyEncodedQuery(String queryString)`      | Assign values described by an encoded query. This is not a read filter. |
| `applyTemplate(String template)`             | Apply a named template. An absent template makes no change.             |
| `insert()`                                   | Insert and return the new sys_id.                                       |
| `insertWithReferences()`                     | Insert the record and related records.                                  |
| `update(Object reason)`                      | Save changes with an optional audit reason.                             |
| `updateMultiple()`                           | Apply changes to the matching set.                                      |
| `updateWithReferences(Object reason)`        | Save the record and related records.                                    |
| `deleteRecord()`                             | Delete the current record.                                              |
| `deleteMultiple()`                           | Delete the matching set.                                                |
| `setAbortAction(Boolean b)`                  | Flag the next database action for abortion.                             |
| `setForceUpdate(Boolean force)`              | Save even when fields are unchanged.                                    |
| `setWorkflow(Boolean e)`                     | Control Business Rule processing and documented related effects.        |
| `setUseEngines(Boolean e)`                   | Control approval and assignment engines.                                |
| `autoSysFields(Boolean e)`                   | Control automatic system-field updates.                                 |
| `setNewGuid()`                               | Generate and assign a new sys_id.                                       |
| `setNewGuidValue(String guid)`               | Assign the supplied sys_id for insertion.                               |

## Dynamic attributes and cursor location

Dynamic-attribute access requires the documented `dynamic_schema_reader` or `dynamic_schema_writer` role.
Confirm the field and attribute-path grammar before use. These methods do not grant additional permissions.

| Signature                                                                                           | Purpose                                             |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| `getDynamicAttribute(String fullPath)`                                                              | Retrieve an attribute object by path.               |
| `getDynamicAttribute(String dynamicAttributeField, String groupAttrPath)`                           | Retrieve an attribute object by field and path.     |
| `getDynamicAttributeValue(String fullPath)`                                                         | Read an attribute value by path.                    |
| `getDynamicAttributeValue(String dynamicAttributeField, String groupAttrPath)`                      | Read an attribute value by field and path.          |
| `getDynamicAttributeDisplayValue(String fullPath)`                                                  | Read an attribute label by path.                    |
| `getDynamicAttributeDisplayValue(String dynamicAttributeField, String groupAttrPath)`               | Read an attribute label by field and path.          |
| `setDynamicAttributeValue(String fullPath, Object value)`                                           | Write an attribute value by path.                   |
| `setDynamicAttributeValue(String dynamicAttributeField, String groupAttrPath, Object value)`        | Write an attribute value by field and path.         |
| `setDynamicAttributeDisplayValue(String fullPath, Object value)`                                    | Write an attribute display value by path.           |
| `setDynamicAttributeDisplayValue(String dynamicAttributeField, String groupAttrPath, Object value)` | Write an attribute display value by field and path. |
| `setDynamicAttributeValues(String dynamicAttributeField, GlideDynamicAttributeStore values)`        | Copy staged attributes into the field.              |
| `getLocation()`                                                                                     | Read the current row location.                      |
| `getRowNumber()`                                                                                    | Read the saved or specified row number.             |
| `setLocation(Number rowNumber)`                                                                     | Move to a row location.                             |
| `saveLocation()`                                                                                    | Save the current row location.                      |
| `restoreLocation()`                                                                                 | Return to the saved location.                       |
