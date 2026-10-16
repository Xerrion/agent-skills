# ServiceNow Encoded Queries

Encoded queries are ServiceNow's compact filter language. Use them when a condition builder, URL, reference qualifier, API parameter, or complex GlideRecord filter needs one portable query string. Keep simple programmatic conditions in `addQuery()` calls because their field, operator, and value boundaries are easier to inspect and safer to populate dynamically.

## Build Queries Safely

1. Use the confirmed target table and internal field names. Reuse schema evidence from the current task; inspect only unknown fields.
1. Reuse confirmed field types and stored values. Resolve unknown choices or references before writing. Choice labels are not query values, and reference equality uses a sys_id.
1. Build complex logic in the condition builder when possible, then copy the query from the breadcrumb. This avoids punctuation and grouping mistakes.
1. Treat the complete encoded query as code, not as a place to interpolate untrusted text. Use `addQuery(field, operator, value)` for user-supplied values.
1. Check the selected records before a query-driven write. An automation condition needs verification in its actual evaluation context. Change operators require current and previous values, so an ordinary record-list query cannot test them.
1. Inspect `getEncodedQuery()` when debugging the final GlideRecord query.

```javascript
var grIncident = new GlideRecord("incident");
grIncident.addEncodedQuery("active=true^priorityIN1,2^assignment_groupISNOTEMPTY");
grIncident.setLimit(100);
grIncident.query();
```

Do not concatenate request parameters, form values, catalog variables, email content, or other untrusted strings into `addEncodedQuery()` or `sysparm_query`. Caret separators and operators inside the value can alter the filter. Keep those values separate:

```javascript
var grIncident = new GlideRecord("incident");
grIncident.addQuery("active", true);
grIncident.addQuery("short_description", "CONTAINS", userSearchText);
grIncident.query();
```

## Invalid filters and query access

The global and scoped [GlideRecord contracts](glide-record.md) warn that an invalid encoded term can be dropped from a query.
The remaining valid conditions can then select more records than intended.
An empty encoded query adds no condition and can select every row.
Neither an empty string nor `glide.invalid_query.returns_no_rows` is a reliable write-safety boundary.

Confirm the schema, intended predicate, and affected records before a query-driven write.
Do not silently replace an invalid filter with an empty filter.

The documentation describes explicit user-query ACL APIs separately from ordinary read/write ACL enforcement.
Those checks do not make arbitrary caller-supplied encoded text safe.
Keep caller values in separate arguments and allowlist any caller-selected fields or operators.
Check that the selected API exists in the applicable global or scoped context and supports the required query ACL behavior.

See [primary API sources](sources.md).

## Compose Conditions

| Token | Meaning                                    | Example                                            |
| ----- | ------------------------------------------ | -------------------------------------------------- |
| `^`   | AND                                        | `active=true^caller_idISNOTEMPTY`                  |
| `^OR` | OR within a condition group                | `priority=1^ORpriority=2`                          |
| `^NQ` | Start an alternative top-level query group | `short_descriptionISEMPTY^NQdescriptionISNOTEMPTY` |

Read these examples as:

- `active=true^caller_idISNOTEMPTY`: active is true AND caller is populated.
- `active=true^priority=1^ORpriority=2`: active is true AND priority is 1 or 2.
- `short_descriptionISEMPTY^NQdescriptionISNOTEMPTY`: short description is empty OR description is populated.

Do not insert parentheses into an encoded query. They are not general Boolean-grouping syntax. For logic that is hard to express or review with `^OR` and `^NQ`, use chained `addQuery()` / `addOrCondition()` calls or split the operation into explicit queries.

```javascript
var grIncident = new GlideRecord("incident");
var priorityCondition = grIncident.addQuery("priority", "1");
priorityCondition.addOrCondition("priority", "2");
grIncident.addQuery("active", true);
grIncident.query();
```

Do not assume SQL or JavaScript operator precedence. Generate complex strings in the condition builder and test their result set.

## Common Operators

### All field types

| Label                   | Encoded operator | Example                       |
| ----------------------- | ---------------- | ----------------------------- |
| is                      | `=`              | `active=true`                 |
| is not                  | `!=`             | `state!=7`                    |
| is empty                | `ISEMPTY`        | `assigned_toISEMPTY`          |
| is not empty            | `ISNOTEMPTY`     | `assigned_toISNOTEMPTY`       |
| is anything             | `ANYTHING`       | `short_descriptionANYTHING`   |
| is same as field        | `SAMEAS`         | `caller_idSAMEASassigned_to`  |
| is different from field | `NSAMEAS`        | `caller_idNSAMEASassigned_to` |

`ANYTHING` includes populated, empty, and null values. Use it only when that broad meaning is intentional.

### String and string-choice fields

| Label            | Encoded operator | Example                           |
| ---------------- | ---------------- | --------------------------------- |
| starts with      | `STARTSWITH`     | `short_descriptionSTARTSWITHSAP`  |
| ends with        | `ENDSWITH`       | `short_descriptionENDSWITHoutage` |
| contains         | `LIKE`           | `short_descriptionLIKESAP`        |
| does not contain | `NOT LIKE`       | `short_descriptionNOT LIKESAP`    |
| is one of        | `IN`             | `subcategoryINemail,database`     |
| is not one of    | `NOT IN`         | `subcategoryNOT INemail,database` |
| between          | `BETWEEN`        | `short_descriptionBETWEENq@t`     |
| is empty string  | `EMPTYSTRING`    | `short_descriptionEMPTYSTRING`    |

Use stored choice values in `IN` and `NOT IN`, not their display labels.

### Numeric and integer-choice fields

| Label                          | Encoded operator     | Example                                            |
| ------------------------------ | -------------------- | -------------------------------------------------- |
| less than                      | `<`                  | `reassignment_count<2`                             |
| greater than                   | `>`                  | `reassignment_count>2`                             |
| less than or equal             | `<=`                 | `reassignment_count<=2`                            |
| greater than or equal          | `>=`                 | `reassignment_count>=2`                            |
| between, inclusive             | `BETWEEN`            | `reassignment_countBETWEEN1@3`                     |
| greater than field             | `GT_FIELD`           | `reassignment_countGT_FIELDreopen_count`           |
| less than field                | `LT_FIELD`           | `reassignment_countLT_FIELDreopen_count`           |
| greater than or equal to field | `GT_OR_EQUALS_FIELD` | `reassignment_countGT_OR_EQUALS_FIELDreopen_count` |
| less than or equal to field    | `LT_OR_EQUALS_FIELD` | `reassignment_countLT_OR_EQUALS_FIELDreopen_count` |

Operator availability can differ between numeric fields and integer-backed choice fields. If the condition builder does not offer `<=` or `>=` for the selected field, use a supported scripted condition or a direct GlideRecord condition rather than forcing the encoded form.

### Reference fields

| Intent                           | Example                                      |
| -------------------------------- | -------------------------------------------- |
| equals a record                  | `caller_id=0123456789abcdef0123456789abcdef` |
| is populated                     | `caller_idISNOTEMPTY`                        |
| display value starts with text   | `caller_idSTARTSWITHDon`                     |
| same record as another reference | `caller_idSAMEASassigned_to`                 |
| dynamic filter option            | `caller_idDYNAMIC<filter-option-sys-id>`     |

The 32-character identifier above is fictional. For equality, use the referenced record sys_id. Text operators act on the reference display value. Dynamic-filter identifiers are instance records, so copy the generated condition from the condition builder instead of hardcoding an identifier from another instance. Not every operator is available for every reference type.

### Boolean fields

Use `field=true`, `field=false`, `fieldISEMPTY`, or `fieldISNOTEMPTY`. Remember that `active!=true` can include false, empty, and null values; it is broader than `active=false`.

## Date and Time Operators

Prefer condition-builder-generated date queries. Date ranges use `@` to separate operands and often contain a trusted `javascript:` expression evaluated by ServiceNow.

| Intent                                    | Example                                                                    |
| ----------------------------------------- | -------------------------------------------------------------------------- |
| today                                     | `sla_dueONToday@javascript:gs.daysAgoStart(0)@javascript:gs.daysAgoEnd(0)` |
| before today                              | `sla_due<javascript:gs.daysAgoStart(0)`                                    |
| at or before today                        | `sla_due<=javascript:gs.daysAgoEnd(0)`                                     |
| after today                               | `sla_due>javascript:gs.daysAgoEnd(0)`                                      |
| yesterday through today                   | `sla_dueBETWEENjavascript:gs.daysAgoStart(1)@javascript:gs.daysAgoEnd(0)`  |
| more recent than one hour ago             | `sla_dueRELATIVEGT@hour@ago@1`                                             |
| older than one hour ago                   | `sla_dueRELATIVELT@hour@ago@1`                                             |
| same day as another field                 | `sla_dueSAMEASactivity_due@day`                                            |
| more than one day before another field    | `sla_dueMORETHANactivity_due@day@before@1`                                 |
| less than three days before another field | `sla_dueLESSTHANactivity_due@day@before@3`                                 |

Never place user input inside a `javascript:` expression. Date tokens and trend operators can vary with field type and platform support, so copy them from a tested condition builder when available.

## Change, Tag, and Special Operators

Change operators apply only in contexts that have current and previous values, such as notification conditions:

| Intent               | Example             |
| -------------------- | ------------------- |
| field changes        | `stateVALCHANGES`   |
| changes from value 4 | `stateCHANGESFROM4` |
| changes to value 4   | `stateCHANGESTO4`   |

Tag queries are generated structures that include the tag record sys_id:

- Has tag: `sys_tags.<tag-sys-id>=<tag-sys-id>`
- Does not have tag: `sys_tags.<tag-sys-id>DOESNOTHAVE<tag-sys-id>`
- Excludes tag: `sys_tags.<tag-sys-id>EXCLUDING<tag-sys-id>`

Generate tag queries in the condition builder. Do not copy tag sys_ids across instances without resolving the corresponding tag record.

## Translation Workflow

When translating plain language or condition-builder rows into an encoded query:

1. Write the intended Boolean expression in words.
1. Resolve labels to internal field names and stored values.
1. Select operators that the target field type supports.
1. Separate AND conditions with `^`.
1. Use `^OR` for alternatives in one group and `^NQ` for a new top-level alternative.
1. Generate or verify the result in the condition builder.
1. Return both the encoded query and a one-sentence reading of it.

Example request: "Active incidents where priority is High or Critical and assignment group is populated."

```text
active=true^priorityIN1,2^assignment_groupISNOTEMPTY
```

Meaning: active is true, priority is 1 or 2, and assignment group is populated.
