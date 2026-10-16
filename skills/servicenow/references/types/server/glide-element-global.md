# GlideElement: server global contracts

API references: [global API](../../sources/api-reference/server-api-reference/glide-element-global.md) and [scoped API](../../sources/api-reference/server-api-reference/glide-element-scoped.md).

Examples: [task guide](../../glide-element.md).

Check the API reference for optional parameters and detailed return types.

## Access, changes, and values

| Signature                                            | Purpose                                           |
| ---------------------------------------------------- | ------------------------------------------------- |
| `canCreate()`                                        | Check field permission for creation.              |
| `canRead()`                                          | Check field permission for reading.               |
| `canWrite()`                                         | Check field permission for writing.               |
| `hasRightsTo(String operationName)`                  | Check permission for the named operation.         |
| `changes()`                                          | Check whether the field changed.                  |
| `changesFrom(Object value)`                          | Match the previous value of a change.             |
| `changesTo(Object value)`                            | Match the new value of a change.                  |
| `getValue()`                                         | Read the stored value.                            |
| `toString()`                                         | Copy the value as a string.                       |
| `nil()`                                              | Check for null or an empty string.                |
| `hasValue()`                                         | Check for a populated value.                      |
| `getDisplayValue(Number maxChar)`                    | Read display text with optional truncation.       |
| `getDisplayValueExt(Number maxChar, String nullSub)` | Read display text with an empty-value substitute. |
| `getDisplayValueLang(String language)`               | Read display text in a requested language.        |
| `getChoiceValue()`                                   | Read the selected choice label.                   |
| `getChoices(String dependent)`                       | Read available base-table choice values.          |
| `getElementValue(String value)`                      | Read the specified element's value.               |
| `getRefRecord()`                                     | Retrieve the referenced record.                   |
| `getJournalEntry(Number mostRecent)`                 | Read the latest entry or all journal entries.     |

## Dictionary and object metadata

| Signature                                   | Purpose                                     |
| ------------------------------------------- | ------------------------------------------- |
| `getAttribute(String attributeName)`        | Read a dictionary attribute.                |
| `getBooleanAttribute(String attributeName)` | Read a Boolean dictionary attribute.        |
| `hasAttribute(String attributeName)`        | Check whether an attribute exists.          |
| `getBaseTableName()`                        | Read the field's base table.                |
| `getDependent()`                            | Read the field on which this field depends. |
| `getDependentTable()`                       | Read the dependency table.                  |
| `getED()`                                   | Read the element descriptor.                |
| `getGlideObject()`                          | Read the platform object behind the value.  |
| `getGlideRecord()`                          | Read the associated GlideRecord.            |
| `getLabel()`                                | Read the field label.                       |
| `getLabelLang(String language)`             | Read the field label in a language.         |
| `getName()`                                 | Read the field name.                        |
| `getTableName()`                            | Read the containing table name.             |
| `getFieldStyle()`                           | Read field CSS styling.                     |
| `getStyle()`                                | Read value CSS styling.                     |

## Formatting, mutation, and diagnostics

| Signature                                         | Purpose                                                      |
| ------------------------------------------------- | ------------------------------------------------------------ |
| `getEscapedValue()`                               | Read the escaped value. Confirm the output context.          |
| `getHTMLValue(Number maxChars)`                   | Read HTML-format output with optional truncation.            |
| `getHTMLValueExt(Number maxChar, String nullSub)` | Read HTML output with an empty-value substitute.             |
| `getTextAreaDisplayValue()`                       | Read the display value with HTML escaping.                   |
| `getXHTMLValue()`                                 | Read XHTML output.                                           |
| `getXMLValue()`                                   | Read XML output.                                             |
| `setValue(Object value)`                          | Assign a stored value.                                       |
| `setDisplayValue(Object displayValue)`            | Assign a display value.                                      |
| `setInitialValue(Object value)`                   | Assign the initial field value.                              |
| `setJournalEntry(String entry, String userName)`  | Append a journal entry and author.                           |
| `dateNumericValue()`                              | Read the numeric duration-field representation.              |
| `setDateNumericValue(Number milliseconds)`        | Assign the numeric duration-field representation.            |
| `setError(String message)`                        | Add a field error.                                           |
| `getError()`                                      | Read the associated error.                                   |
| `debug(Object o)`                                 | Add an object debug message. Never include sensitive values. |
| `getDebugCount()`                                 | Count logged debug messages.                                 |

## Dynamic-schema metadata

The global API documents `getDynamicAttribute()`, `getDynamicNamespace()`, and `getDynamicNamespaceName()` for dynamic-schema metadata.
Confirm dynamic-schema support and configuration before use.
