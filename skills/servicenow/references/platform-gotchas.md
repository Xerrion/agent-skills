# Platform gotchas

Read the entry matching the symptom or execution context.

| Symptom or task                                                                       | Read                                                                      |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Identity lookup, field clearing, counters, Boolean, membership, or insert logic fails | [Record values and insert context](#record-values-and-insert-context)     |
| Counts disagree, methods fail, or cascade deletion triggers rules                     | [Query and deletion behavior](#query-and-deletion-behavior)               |
| State leaks, roles appear stale, or user context changes                              | [Session and impersonation](#session-and-impersonation)                   |
| Client callbacks, change listeners, privacy, or display data behave unexpectedly      | [Client and Display Business Rules](#client-and-display-business-rules)   |
| Parsing throws, a day changes, or week numbers differ                                 | [Date parsing and calendar behavior](#date-parsing-and-calendar-behavior) |
| Fix Script syntax, update capture, or ACL writes fail                                 | [Fix Scripts and metadata](#fix-scripts-and-metadata)                     |
| Attachment uploads fail or authorization differs from parent access                   | [Attachments](#attachments)                                               |

Use [API lookup](glide-api.md) for signatures and [ACL design](acl-design.md) for access-control decisions.

## Record values and insert context

### Single-argument get can match a display value

**Documented:** Both [global](sources/api-reference/server-api-reference/glide-record-global.md#gliderecord---getobject-name-object-value) and [scoped](sources/api-reference/server-api-reference/glide-record-scoped.md#scoped-gliderecord---getobject-name-object-value) `get(value)` first search by `sys_id`, then try the display value if no record is found.
A successful single-argument call therefore does not prove that the input matched a `sys_id`.
For an exact identity lookup, name the field and handle a false result:

```javascript
// Comparison fragments. recordSysId is caller input.
gr.get(recordSysId); // Can fall back to matching a display value.
if (gr.get("sys_id", recordSysId)) {
  // Use the record only after the explicit identity lookup succeeds.
}
```

### Null is not the documented bulk-clear value

**Documented global behavior:** Passing `null` to [`setValue()`](sources/api-reference/server-api-reference/glide-record-global.md#gliderecord---setvaluestring-name-object-value) leaves the field unchanged without throwing an error.
The [`updateMultiple()` contract](sources/api-reference/server-api-reference/glide-record-global.md#gliderecord---updatemultiple) documents the literal string `'NULL'` for clearing existing field values.
These are different inputs. Keep this bulk-update rule distinct from single-record, journal, and field-specific behavior.

```javascript
// Global server fragments. gr already has the intended bulk-update query.
// Incorrect when the intent is to clear existing descriptions.
gr.setValue("description", null);
gr.updateMultiple();

// Documented bulk-clear form for the same selected records.
gr.setValue("description", "NULL");
gr.updateMultiple();
```

### Counter updates can lose concurrent increments

**Documented global behavior:** Reading a number, adding locally, and saving it can overwrite another transaction's increment.
[`addValue(field, amount)`](sources/api-reference/server-api-reference/glide-record-global.md#gliderecord---addvaluestring-field-number-value) performs the addition atomically in the database when `update()` runs.
It only applies to numeric fields, and the in-memory record must be explicitly reloaded to observe the new value.
A preceding `setValue()` for the same field prevents `addValue()` from being processed and logs an error.
With `insert()`, the amount initializes the field instead of incrementing an existing row.
For a custom counter such as `u_count`, choose one write strategy and distinguish the database result from the loaded object's value.

### Boolean storage values

For a boolean field, the documented GlideRecord `getValue()` result uses string storage values `'1'` and `'0'`.
Comparing that result with `'true'` misses a checked value.
Comparison fragments for the **custom boolean field** `u_some_flag`:

```javascript
// Incorrect for a boolean field's storage value.
if (gr.getValue("u_some_flag") === "true") {
  // This does not match the stored true value.
}

// Correct comparison for the boolean storage contract.
if (gr.getValue("u_some_flag") === "1") {
  // The field is true.
}
```

Display values serve presentation and can depend on field type and locale.
**Observed:** A Boolean display value returned textual true/false. Use stored values for Boolean logic.
See [field values](glide-element.md) and [record contracts](glide-record.md).

### Before-insert record guards

**Observed:** A helper guarded by `isValidRecord()` rejected a populated `current` from a before-insert Business Rule.
The same helper worked after insert and on update.
The [scoped GlideRecord contract][record] defines this method in terms of a record returned by query/get.
It does not document a general validity check for every new-record execution context.

A helper that accepts new records must validate its required table and fields without requiring a fetched row.

Helper fragments:

```javascript
// Incorrect when the helper must also accept before-insert records.
function inspectRecord(gr) {
  if (!gr || !gr.isValidRecord()) return null;
  // Process a fetched record.
}

// A guard compatible with the helper's new-record input contract.
function inspectNewOrFetchedRecord(gr) {
  if (!gr) return null;
  // Validate required table and fields before using them.
}
```

A null guard alone does not prove that an object has the expected table or required values.
Retain those validations according to the helper's contract.

### Insert handling and changes()

**Observed:** A before-insert rule guarded only by `current.assignment_group.changes()` missed inserts.
The field initialization sequence was unrecorded. Insert behavior can depend on that sequence.

[GlideElement documentation][element] describes internal change tracking and its Business Rule lifecycle.
It also describes unchanged initialized/read records. These conditions differ from an arbitrary insert path.
The absence of `previous` was a proposed cause, not a confirmed explanation.

When the requirement includes every insert and selected updates, express it directly:

```javascript
// Insufficient for the stated requirement without proving insert behavior.
current.assignment_group.changes();

// Explicitly includes inserts and updates that change the field.
current.operation() === "insert" || current.assignment_group.changes();
```

These are condition fragments, not standalone scripts.
Configure the Business Rule's operation flags consistently with the expression.
Verify before/after behavior separately. Do not use `changes()` in ACL scripts, where the documented API does not support it.

### Group membership and active filters

**Observed schema:** `sys_user_grmember` had no `active` field. An `addActiveQuery()` call returned no memberships in that configuration.
A missing-field query does not have a universal empty-result guarantee. Invalid-query handling can omit a condition or reject a query.
Check the actual dictionary, including custom fields, before using an active filter.

To select memberships whose referenced users are active, check the user record explicitly:

```javascript
// Illustrative ES2021 server code. groupSysId is caller input.
const membership = new GlideRecord("sys_user_grmember");
membership.addQuery("group", groupSysId);
membership.query();

while (membership.next()) {
  const user = new GlideRecord("sys_user");
  if (user.get(membership.getValue("user")) && user.getValue("active") === "1") {
    // This membership references an active user.
  }
}
```

For large result sets, evaluate the query cost and a supported reference-field filter.

## Query and deletion behavior

### Large sys_id lists can produce an incorrect row count

**Documented server behavior:** For a `sys_id IN` list exceeding `glide.db.first_pass_sys_id_list_size.max`, [`getRowCount()` may be incorrect](sources/api-reference/server-api-reference/glide-record-global.md#gliderecord---disablesysidinoptimization).
The documented default threshold is 100.
Both the [global](sources/api-reference/server-api-reference/glide-record-global.md#gliderecord---disablesysidinoptimization) and [scoped](sources/api-reference/server-api-reference/glide-record-scoped.md#scoped-gliderecord---disablesysidinoptimization) APIs document `disableSysIdInOptimization()` for that record query.
Call it before querying when this optimization affects the count. Changing the system property's threshold affects all GlideRecords.
For this large-list path, the [`getRowCount()` instructions](sources/api-reference/server-api-reference/glide-record-global.md#gliderecord---getrowcount) also require `next()` before reading the count.
Do not treat the `next()` condition as a general rule for every row-count call.

### Cascade deletion can ignore the workflow flag

**Documented global behavior:** The [`deleteMultiple()` documentation](sources/api-reference/server-api-reference/glide-record-global.md#gliderecord---deletemultiple) says prior `setWorkflow()` calls on the same object are ignored when `deleteMultiple()` or `deleteRecord()` performs cascade deletion.
Do not rely on `setWorkflow(false)` alone to predict which Business Rules run for cascaded records.
Check the actual cascade relationships and affected rule behavior for the chosen operation.
This exception concerns cascade deletion, not every update or delete.

### Dot-walked filters are not supported bulk-delete boundaries

**Documented global behavior:** [`deleteMultiple()`](sources/api-reference/server-api-reference/glide-record-global.md#gliderecord---deletemultiple) does not support dot-walking and warns that using it on referenced tables can delete all records in the table.
A dot-walked filter that works for record retrieval is therefore not a supported boundary for this bulk-delete method.
Use supported base-table conditions or explicitly resolve the intended records before choosing a deletion path.
Do not generalize this global method's documented limitation to every query or scoped API.

### Aggregate queries can omit Query Business Rules

**Documented:** [Global](sources/api-reference/server-api-reference/glide-aggregate-global.md#glideaggregate---setaggregateworkflowboolean-workflow) and [scoped](sources/api-reference/server-api-reference/glide-aggregate-scoped.md#scoped-glideaggregate---setaggregateworkflowboolean-workflow) `setAggregateWorkflow()` default to `false`.
Use `setAggregateWorkflow(true)` when the aggregate query must run Query Business Rules.
The documented session-level workflow setting overrides this flag: a disabled session workflow prevents those rules from running even when the aggregate flag is true.
When aggregate totals differ from a record query, compare these settings and the Query Business Rules' filters.
This switch controls Business Rule execution. It does not establish which ACL checks apply to the operation.

### Table fields can hide query and iteration methods

**Documented:** A field named `next` can make `next()` fail, and a field named `query` can make `query()` fail.
The global alternatives are [`_next()`](sources/api-reference/server-api-reference/glide-record-global.md#gliderecord---_next) and [`_query()`](sources/api-reference/server-api-reference/glide-record-global.md#gliderecord---_querystring-field-string-value).
The scoped contracts document the same [`_next()`](sources/api-reference/server-api-reference/glide-record-scoped.md#scoped-gliderecord---_next) and [`_query()`](sources/api-reference/server-api-reference/glide-record-scoped.md#scoped-gliderecord---_querystring-field-string-value) workarounds.
Inspect the table dictionary when a method fails only on a particular table before changing the query or loop logic.

## Session and impersonation

### Session role lists do not refresh during the session

**Documented global behavior:** [`gs.getSession().getRoles()`](sources/api-reference/server-api-reference/glide-session-global.md#glidesession---getroles) does not reflect role changes made during the current user session.
The user must log out and log back in to obtain an updated list through this method.
When testing a role change, compare a fresh session before concluding that the change failed.
This is a contract for the returned session role list, not a claim about every authorization API or cache.

### Mobile users can have non-interactive sessions

**Documented global behavior:** [`isInteractive()`](sources/api-reference/server-api-reference/glide-session-global.md#glidesession---isinteractive) returns `false` for user sessions in both the classic and current mobile applications.
A human using the mobile app can therefore follow a branch intended for non-interactive sessions.
Do not use this flag alone to distinguish human activity from integrations or as an authorization decision.

### Session data outlives an iteration

The [GlideSession API][session] stores client data in the session.
It is not transaction-local state.
**Observed:** Test iterations in one Fix Script reused a value from a previous iteration.

Reset only the keys owned by the workflow, and account for other work sharing the session.
**Observed, execution context unknown:** `clearClientData()` returned `Can't find method`.
The global API documents `clearClientData(name)`; check availability in the current scope and context.

```javascript
// Documented global operation when available in this context.
gs.getSession().clearClientData("example_mode");

// Reset workaround when clearClientData is unavailable.
gs.getSession().putClientData("example_mode", "");
```

An empty value and an absent value are different states.
Use the workaround only if the consumer treats an empty value as a reset.
Do not store credentials or sensitive records in session client data.

### Session string comparisons

**Observed:** Strict equality on a `getClientData()` result failed despite identical displayed text.
A Java string wrapper was suspected; the actual type and engine configuration are unknown.
The documented return type is `String`.

Normalize a retrieved value when the consuming code needs a native JavaScript string, while preserving missing-data semantics:

```javascript
// Direct comparison before normalization.
if (gs.getSession().getClientData("example_mode") === "test") {
  // The observed comparison did not match.
}

// Explicit normalization, with null preserved.
const rawMode = gs.getSession().getClientData("example_mode");
const mode = rawMode == null ? null : String(rawMode);
if (mode === "test") {
  // Compare normalized text.
}
```

Loose equality also converts values. Prefer explicit normalization when a native string is required.
The fragments above require ES2021 mode.

### Restore impersonation explicitly

**Observed:** A test using an `unimpersonate()` call did not reliably restore the original user.
Subsequent code could therefore run as the wrong user.
That method is not listed in the documented global GlideImpersonate contract.

The [global API][impersonate] documents calling `impersonate(originalUserId)` to restore the administrator.
Capture the original identity before the change and restore it in `finally`.
Impersonation requires the documented capabilities. Actions are attributed to the impersonated user.

```javascript
// Illustrative global server fragment. testUserSysId is caller input.
var originalUserId = gs.getUserID();
var impersonator = new GlideImpersonate();
if (!impersonator.canImpersonate(testUserSysId)) {
  throw new Error("The selected user cannot be impersonated in this context.");
}
try {
  impersonator.impersonate(testUserSysId);
  // Test behavior as the selected user.
} finally {
  impersonator.impersonate(originalUserId);
}
```

**Undocumented workaround:** `gs.getSession().impersonate()` was used with the same restoration pattern.
That method is absent from the public GlideSession contract. Prefer the documented GlideImpersonate API.
Confirm the restored identity before continuing a multi-user test sequence.

## Client and Display Business Rules

### A Script Include can override the global privacy setting

**Documented:** A Glide AJAX enabled Script Include's [`isPublic()` result takes precedence](sources/api-reference/scripts/script-includes.md#change-privacy-on-a-single-glide-ajax-enabled-script-include) over `glide.script.ccsi.ispublic`.
An include returning `true` remains public even when the property is `false`.
The [public privacy setting](sources/api-reference/scripts/script-includes.md#public-privacy-setting) allows unauthenticated callers to invoke the include through an appropriate HTTP request.
Review the include's own method when diagnosing unexpected access. The global property alone does not establish its privacy.
Script Include access ACLs and authorization for returned records remain separate checks. Public privacy alone does not authorize the caller to read arbitrary data.

### A missing client reference can still return an object

**Documented:** [`g_form.getReference()`](sources/api-reference/glide-form-client.md#glideform---getreferencestring-fieldname-function-callback) returns an initialized GlideRecord when the reference cannot be found, with `currentRow = -1` and `rows.length = 0`.
A truthy callback argument alone does not prove that a referenced row exists.
Check that the returned record contains the expected identity and required data before using it.
Keep that check inside the callback when using the asynchronous form.

### User-change listeners miss programmatic changes

**Documented:** [`g_form.onUserChangeValue()`](sources/api-reference/glide-form-client.md#glideform---onuserchangevaluefunction-fn) runs for changes made by a user, excluding changes from Client Scripts, UI Policies, and other programmatic interactions.
It also does not support journal fields or Service Catalog items in the classic environment.
If the same logic must run after a script changes a value, call shared logic from that script instead of expecting this listener to detect the change.

### Strict read-only fields ignore client value writes

**Documented:** [`g_form.setValue()`](sources/api-reference/glide-form-client.md#glideform---setvaluestring-fieldname-string-value-string-displayvalue) and [`clearValue()`](sources/api-reference/glide-form-client.md#glideform---clearvaluestring-fieldname) cannot update strict read-only fields.
The field remains unchanged and the browser console receives a warning.
When the client branch executes but the value does not change, inspect this field security setting and the console before attributing the failure to an onChange guard or asynchronous ordering.

### Client Script behavior differs by user

**Observed:** An onLoad Client Script configured for Desktop did not execute for an administrator but worked for an ordinary user.
The cause is unknown; an administrator bypass was suspected but not established.

Check the active flag, table, UI type, view, conditions, client errors, and tested user context.
Compare the same supported interface for both users.
**Observed workaround:** A Display Business Rule used `gs.addInfoMessage()` or `gs.addErrorMessage()` for server-originated feedback.
Message delivery depends on the execution path and UI.
Client feedback is not an access-control mechanism.

### Missing g_scratchpad under restricted access

**Observed:** Display Business Rules encountered an undefined `g_scratchpad` during a test with restrictive Deny-unless field ACLs.
Multiple rules on the table were affected. The cause and exact configuration are unknown.

An unguarded reference can throw when the variable is absent:

```javascript
// Incorrect in a context where g_scratchpad is undefined.
g_scratchpad.exampleMessage = "Review required";

// Guard the optional transport object.
if (typeof g_scratchpad !== "undefined") {
  g_scratchpad.exampleMessage = "Review required";
}
```

The guard prevents that exception. It does not supply the missing data to the client.
Decide whether the consuming client can continue without it, and test the affected UI path.
Do not place data in scratchpad unless the intended reader may receive it.

### Display Business Rule stored choice

**Observed schema:** The Display label for `sys_script.when` corresponded to `before_display`.
A query using the label-shaped value `display` missed those records.
Verify the stored choice value when inspecting a different schema or configuration.

```javascript
// Incorrect for the observed stored choice.
const wrongQuery = new GlideRecord("sys_script");
wrongQuery.addQuery("when", "display");
wrongQuery.query();

// Query the stored choice, not its display label.
const displayRules = new GlideRecord("sys_script");
displayRules.addQuery("when", "before_display");
displayRules.query();
```

## Date parsing and calendar behavior

### Explicit date parsers can throw before a validity check

**Documented scoped behavior:** [`setDisplayValue(value, format)`](sources/api-reference/server-api-reference/glide-date-time-scoped.md#scoped-glidedatetime---setdisplayvaluestring-value-string-format) and [`setValueUTC(dt, format)`](sources/api-reference/server-api-reference/glide-date-time-scoped.md#scoped-glidedatetime---setvalueutcstring-dt-string-format) throw a runtime exception when the value does not match the format.
An `isValid()` call after the setter cannot handle an exception that already interrupted execution.
Catch the exception around parsing, then use `getErrorMsg()` for the parser's diagnostic if needed.
The display setter uses the current user's time zone. The UTC setter uses UTC.
Choose the parser and format from the input contract before validating the result.

### Day-of-month setters clamp to the month's end

**Documented scoped behavior:** [`setDayOfMonthLocalTime()`](sources/api-reference/server-api-reference/glide-date-time-scoped.md#scoped-glidedatetime---setdayofmonthlocaltimenumber-day) and [`setDayOfMonthUTC()`](sources/api-reference/server-api-reference/glide-date-time-scoped.md#scoped-glidedatetime---setdayofmonthutcnumber-day) accept days from 1 to 31.
When the requested day exceeds the number of days in the selected month, they use the month's last day.
Setting day 31 in a shorter month therefore does not establish that day 31 was accepted unchanged.
If an exact calendar day is required, compare the resulting day or validate against `getDaysInMonthLocalTime()` or `getDaysInMonthUTC()` in the same time context.

### Week numbers use Sunday and the January 1 week

**Documented scoped behavior:** [`getWeekOfYearLocalTime()`](sources/api-reference/server-api-reference/glide-date-time-scoped.md#scoped-glidedatetime---getweekofyearlocaltime) and [`getWeekOfYearUTC()`](sources/api-reference/server-api-reference/glide-date-time-scoped.md#scoped-glidedatetime---getweekofyearutc) use weeks beginning on Sunday.
The first week is the week containing at least one day of the new year, including January 1.
Do not assume ISO week numbering when comparing these values with reports or external calendar libraries.
The local and UTC variants also evaluate the date in different time zones.
Test year-boundary dates against the required calendar convention.

## Fix Scripts and metadata

### Fix Script language mode

**Observed:** A Fix Script rejected syntax that worked in another server artifact, including a template literal with an `Unexpected token` error.
The effective language mode was not recorded.

[JavaScript mode documentation][modes] describes application and individual script settings.
Inspect the effective context and supported syntax before attributing a parse error to the artifact type alone.
Use ES5 syntax when the execution context requires it.

| Unsupported syntax in a legacy context | ES5 form for the same intended task                                           |
| -------------------------------------- | ----------------------------------------------------------------------------- |
| `const` or `let`                       | `var`, with different scope behavior reviewed                                 |
| Template literal or arrow function     | String concatenation or a traditional function, with `this` behavior reviewed |
| Destructuring or optional chaining     | Explicit property assignments and null checks                                 |
| `for...of` or array-copy spread        | An indexed loop, or `Array.prototype.slice.call(arrayLike)` for an array copy |
| `class`                                | The platform `Class.create()` pattern where that API is available             |

Array-copy replacement does not cover object spread or argument spread.
A syntax substitution can change semantics, so verify the rewritten operation as well as parsing.

### Missing update capture

**Observed:** ACL records created through GlideRecord in a Fix Script were not found in `sys_update_xml` afterward.
Capture settings are unknown.
[Fix Script configuration][fix] documents the Unloadable option to create Customer Update records.

Check the option, the affected record type, execution completion, and resulting Customer Update records.
A successful write alone does not establish transport coverage.

Existence-check fragment before creation:

```javascript
// Illustrative fragment. u_example_record is a custom table.
var acl = new GlideRecord("sys_security_acl");
acl.addQuery("name", "u_example_record");
acl.addQuery("operation", "read");
acl.setLimit(1);
acl.query();
if (!acl.hasNext()) {
  // Prepare the complete owned ACL configuration before insertion.
}
```

An existence query alone does not distinguish different ACLs with the same name and operation, correct drift, or prevent concurrent duplicates.
See the fuller [creation pattern](acl-design.md#illustrative-es5-creation-pattern).

### ACL management permissions

[ACL administration documentation][acl] requires elevated `security_admin` privileges for protected creation and update operations.
A normal administrator session does not itself prove that this elevation is active.
An account also needs applicable table, scope, and channel permissions for the chosen operation.

**Observed:** An integration-context ACL write returned a falsy result without a useful accompanying error.
Inspect the response, platform errors, actual session privileges, and resulting record.
Do not infer success from the absence of an exception.

## Attachments

### Multipart uploads require metadata before the file

**Documented:** [`POST /now/attachment/upload`](sources/api-reference/rest-apis/attachment-rest-api.md#attachment---post-nowattachmentupload) requires `table_name` and `table_sys_id` in the multipart body, not URL parameters.
The file must occupy the final part, after the metadata.
The [mandatory-value instructions](sources/api-reference/rest-apis/attachment-rest-api.md#post-multipart-mandatory-values) also require the file's `Content-Type` inside the file part.
The overall request's `multipart/form-data` content type does not replace that file content type.
Check the generated multipart body when an HTTP library constructs the request.

### An attachment 404 can mean missing or inaccessible

**Documented:** For [`GET /now/attachment/{sys_id}`](sources/api-reference/rest-apis/attachment-rest-api.md#attachment---get-nowattachmentsys_id), a 404 can mean the attachment does not exist or the current user cannot access it.
For [`POST /now/attachment/file`](sources/api-reference/rest-apis/attachment-rest-api.md#attachment---post-nowattachmentfile), a 404 can mean the specified parent record does not exist or is inaccessible.
Do not infer deletion or a bad identifier from either response alone.
Compare the caller's access and the target record through an authorized diagnostic path.
These descriptions apply to those endpoints. They do not define every attachment endpoint's status behavior.

### Resolve the parent record

The standard attachment relationship uses `table_name` and `table_sys_id`.
There is no ordinary parent reference to dot-walk in this relationship.
A custom reference field, if present, is a separate schema feature.

```javascript
// Illustrative ES2021 server fragment. incidentSysId is caller input.
const attachment = new GlideRecord("sys_attachment");
attachment.addQuery("table_name", "incident");
attachment.addQuery("table_sys_id", incidentSysId);
attachment.query();

while (attachment.next()) {
  const parent = new GlideRecord("incident");
  if (parent.get(attachment.getValue("table_sys_id"))) {
    // Apply the operation's parent authorization checks.
  }
}
```

When resolving arbitrary attachment parents, validate the table against the application's supported parent types before constructing a dynamic GlideRecord.
See [attachment protection](acl-design.md#attachment-protection) for applicability and operation distinctions.

### Attachment content paths

`sys_attachment_doc` stores attachment content chunks associated with attachment metadata.
**Recorded observation:** Denying the parent `sys_attachment` read blocked content through the tested attachment delivery path.
Endpoint coverage is unknown. Other table-access and custom integration paths require separate checks.
The [Attachment API][attachment] documents permissions for its endpoints. It does not establish access control for arbitrary custom scripts.
Test the actual download path, direct APIs, and any separately exposed content tables or custom endpoints.
Decide whether additional controls are needed from those access paths and existing ACLs.
Do not add redundant rules merely because metadata and content use separate tables, or omit necessary rules because one download test passed.

[record]: sources/api-reference/server-api-reference/glide-record-scoped.md
[element]: sources/api-reference/server-api-reference/glide-element-global.md
[session]: sources/api-reference/server-api-reference/glide-session-global.md
[impersonate]: sources/api-reference/server-api-reference/glide-impersonate-global.md
[modes]: sources/api-reference/scripts/javascript-modes.md
[fix]: sources/application-development/create-fix-scripts.md
[acl]: sources/platform-security/access-control/exploring-access-control-list.md
[attachment]: sources/api-reference/rest-apis/attachment-rest-api.md
