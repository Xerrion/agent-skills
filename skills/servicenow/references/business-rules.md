# Business Rules: timing, conditions, and safe changes

Use a Business Rule for server-side behavior associated with a database operation.
Select timing and operations before writing its script.

Sources: [Classic Business Rules](sources/api-reference/business-rules-classic/classic-business-rules.md) and [database-action abortion](sources/api-reference/scripts/abort-database-action-business-rule.md).

## Choose the mechanism and timing

The Business Rules documentation recommends Workflow Studio for new process automation.
Select synchronous validation rules and existing Business Rules according to transaction and application requirements.

| Timing  | Use                                                        | Constraint                                                    |
| ------- | ---------------------------------------------------------- | ------------------------------------------------------------- |
| Before  | Validate or assign fields on `current` before persistence. | Changes save with the original database action.               |
| After   | Act on related records after the original action.          | Do not update `current` again merely to save derived fields.  |
| Async   | Deferred work that need not block the transaction.         | Scheduling and completion order are not guaranteed.           |
| Display | Supply form-load data through `g_scratchpad`.              | Runs after reading the record and before presenting the form. |

Use a before rule for field changes on `current`.
Use an after rule when the action requires the original database operation to complete.
Choose async only when delayed and potentially reordered execution is acceptable.
The need for a sys_id alone does not establish that every insert rule must run after persistence.

Keep Business Rules thin. Put reusable domain logic in a named Script Include.
Retain the platform wrapper in both ES5 and ES2021 modes:

```javascript
(function executeRule(current, previous) {
  // Rule action.
})(current, previous);
```

See [server scripting](scripting.md) for mode selection and Script Include structure.

## Conditions and operations

Use form Filter Conditions for predicates the condition builder can express.
Use the advanced Condition field for the remaining supported predicate.
Keep the action script focused on the action.
Do not describe form conditions as inherently indexed. Index usage depends on the actual query and schema.

| Operation         | Typical use                                                                        |
| ----------------- | ---------------------------------------------------------------------------------- |
| Insert            | Defaults and validation on new records.                                            |
| Update            | Validation or actions on changed records.                                          |
| Insert and Update | Rules that apply to both new and existing records.                                 |
| Delete            | Authorized cleanup or related-record handling.                                     |
| Query             | Usually a before-query filter on the queried table. It affects more than one form. |

Only query rules on the queried table run for that query, according to the Business Rules documentation.
A reference-table query rule does not automatically run merely because its field is referenced.
Before-query filtering is not a substitute for the complete ACL model.

`previous` describes the state before the first update or delete in the execution context.
It is available for supported update and delete contexts, not insert or async scripts.
Guard against `null` before using it.
Do not assume a nested update changes `previous` into the immediately preceding intermediate state.

For an insert-or-change predicate:

```javascript
current.operation() === "insert" || current.assignment_group.changes();
```

Use this fragment in the Condition field.
The insert branch handles initial values explicitly. In a recorded configuration, `changes()` returned false during insertion.
See [insert change detection](platform-gotchas.md) for that observation and its evidence limits.

## Abort a save

Example before-insert/update rule that rejects an empty short description:

```javascript
(function executeRule(current, previous) {
  if (!current.getValue("short_description")) {
    gs.addErrorMessage("Cannot save an incident without a short description.");
    current.setAbortAction(true);
    return;
  }
})(current, previous);
```

`setAbortAction(true)` flags the database action for abortion.
It does not automatically stop execution of the script after that call.
Use an explicit return when later code must not run.
Provide a user-facing error. Do not treat an aborted action as a successful write.

An async rule cannot abort the original transaction.
Check scope restrictions on the abortion API before applying a rule across application boundaries.

## Avoid recursion and hidden processing changes

Do not call `current.update()` inside a before or after rule to persist its own changes.
The extra update can start the rules again.
Do not use `setWorkflow(false)` as a routine workaround for recursion.
That suppresses processing and can change auditing or related behavior.

Set Order deliberately when multiple synchronous rules share timing, table, and operation.
Lower order values run first within the relevant processing stage.
An Order value does not guarantee the completion sequence of async jobs.
Do not use `gs.sleep()` to impose order on synchronous processing.

Rules normally apply across forms, lists, and relevant web-service record operations.
Some application paths bypass that processing, and `setWorkflow(false)` can suppress it.
Identify the actual write paths before claiming that a rule covers every integration.
Business Rule execution also does not automatically establish the initiating user's data permissions.

## Async behavior and races

An async script has no `previous` record.
`changes()`, `changesTo()`, and `changesFrom()` do not provide transition detection inside its script body.
The condition builder and advanced Condition field can support transition checks.
Evaluate the predicate in its supported context rather than moving it into the async body.

Rapid updates can produce out-of-order jobs.
Multiple async rules can overwrite each other's changes.
An order-sensitive action needs a design that accounts for that risk, such as appropriate synchronous processing or events.
Do not assume the queued work represents the latest record state.

The documentation describes `glide.businessrule.async_condition_check` to reevaluate an async condition before execution.
That check does not serialize jobs or provide idempotency.
The documentation also states that newly created async rules can run during upgrades.
Check that lifecycle behavior when creating async rules during an upgrade or application installation.

## Delegation pattern

This illustrative action fragment depends on the custom Script Include `ExampleIncidentUtils`.
It must implement `validate(record)` before the example can run:

```javascript
(function executeRule(current, previous) {
  new ExampleIncidentUtils().validate(current);
})(current, previous);
```

The helper should receive the existing record rather than unnecessarily retrieving it again.
Define whether it sets values, rejects the action, or returns a validation result.
Do not let an unexpected failure become a successful default.
