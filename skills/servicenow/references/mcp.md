# MCP interaction and recovery

Use the tool schemas exposed by the current integration. The names below apply when those schemas match.
Discover the callable path before invoking a tool. For prepared payloads, use the unqualified name until that path is known.

## Discover and call tools

1. Check the tool schema and description for argument types and action-specific requirements.
2. Pass arrays and objects as native values. Encode them as strings only when the schema requires strings.
3. Await dependent calls in order. Omit unused optional arguments.

## Select the operation

| Need                                            | Tool and selection                                   |
| ----------------------------------------------- | ---------------------------------------------------- |
| Read one known record or list matching records  | `query` with `sys_id`, or `encoded_query` for a list |
| Read an artifact and discover its script fields | `record_read` with exactly one of `sys_id` or `name` |
| Inspect table fields or resolve choice values   | `describe` or `resolve_choice`                       |
| Inspect a flow or check its reported status     | `flow` with the relevant discovered action           |
| Stage and apply an authorized change            | The family preview, then `mutation_apply`            |

## Read records and limits

Use an explicit native projection such as `fields: ["sys_id", "short_description"]`.
For `query`, list mode requires `fields`. Use `fields: "*"` only when all masked fields are needed.
Exact `sys_id` mode defaults to identity/update metadata. Other filters do not constrain that exact lookup.
Do not combine an exact lookup with list filters to enforce a condition.

For a list, pass `encoded_query` as a string and use bounded `limit` and `offset` values.
Pass `aggregate`, `group_by`, and `resolve_labels` as native arrays when needed.
For `record_read`, omitted or empty `fields` includes compact metadata and discovered script fields.
Reuse its `script_fields` result instead of rediscovering those fields.

Check `pagination`, `warnings`, and `truncation` before treating results as complete.
An empty result means no visible match within the returned scope, not proof that a record does not exist.
Date-bound rejections can come from integration configuration. Add a relevant date constraint when required by the tool.

## Construct record payloads

`record_preview` selects the operation with `action: "create"`, `action: "update"`, or `action: "delete"`.
It accepts `data` as a native object of field-value pairs, not a JSON string.
Create requires `data` and forbids `sys_id`. Update requires both. Delete requires `sys_id` and forbids `data`.
Omit unchanged fields from updates.
For each changed script or markup field, pass the complete new content as its string value.
Pass script contents as the field value. A local path does not load the file.

## Preview and apply

1. Read the target state. Before creation, check for a conflicting record identity.
2. Call the family preview. Check the target, differences, limitations, and expiry.
3. Apply the intended change with `mutation_apply(preview_token)`.
4. Read the saved target. Check update-set capture separately when required.

Preview stages a change without mutating ServiceNow. The token identifies staged content, not user approval.
Tokens are single-use and expire after 300 seconds.
Every apply attempt consumes its token, including rejection, cancellation, or failure.
An expired or consumed token requires a fresh preview. Reconcile an unknown write outcome before staging another change.

### Flow context and readback

Creation requires an explicit `scope` sys_id or `global`.
For strict context binding, supply `expected_scope` and `expected_update_set` together.
Binding an existing flow also requires `expected_revision`, taken from `sys_mod_count` in `flow` with `action: "status"`.
Binding checks the current context. It does not switch the application or update set.
Pass `edits` as an ordered native array and `inputs` as a native object when the selected action requires them.

The flow adapter supports inactive, unpublished drafts through an undocumented upstream API.
`flow` with `action: "inspect"` reads persisted configuration. `action: "validate"` performs local semantic validation without saving or running it.
Catalog discovery does not establish adapter support or successful execution.
Readback checks saved state. It does not prove activation, execution, asynchronous behavior, or an external integration's result.
Flow-header update-set capture does not prove child-artifact capture. Report the returned capture coverage and limitations.

## Handle structured errors

Check `status` before using `data`. For errors, inspect `error.code`, `message`, `phase`, and `operation` when present.

| Error detail                             | Response                                                                                                                   |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `missing_arguments`                      | Supply missing tool arguments at their schema-defined locations. Do not add them as record fields.                         |
| `missing_fields`                         | Supply the missing mandatory record fields in `data` for a record mutation. Do not confuse them with tool arguments.       |
| `invalid_fields`                         | Check each `field` and `expected` type. Correct the argument against the live schema, including native arrays and objects. |
| Input rejection or preview failure       | Correct the request. These failures do not commit the requested mutation.                                                  |
| Expired token or changed-state rejection | Inspect the reason and obtain a fresh preview. Never reuse the previous token.                                             |

A timeout, ambiguous apply error, or `UNKNOWN_OUTCOME` does not establish rollback.
Do not retry the write automatically or immediately prepare another mutation.
Read the exact target and relevant returned identifiers to reconcile the remote outcome first.
If read access cannot establish the outcome, report the uncertainty and stop.
Share only sanitized error evidence. Keep secrets, payloads containing personal data, and preview tokens out of logs and reports.
