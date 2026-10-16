# Access control design

| Task                                   | Read                                                                                        |
| -------------------------------------- | ------------------------------------------------------------------------------------------- |
| Unexpected grant or denial             | [ACL evaluation](#acl-evaluation) and [applicability](#applicability-and-access-conditions) |
| Confidential records or limited fields | [Record and field patterns](#record-and-field-patterns)                                     |
| Attachment access                      | [Attachment protection](#attachment-protection)                                             |
| Missing query results                  | [Security Data Filters](#security-data-filters)                                             |
| ACL creation or migration              | [Management privileges and capture](#management-privileges-and-capture)                     |

API sources: [ACL evaluation][acl], [Deny-unless][deny], and [configuration][configure].

## ACL evaluation

An ACL identifies an object, operation, decision type, and access requirements.
Record access involves table and field checks. A record-level `canRead()` does not establish access to every field.
For data exposed to a user, check field permissions or use the appropriate ACL-aware record API.
See [field permissions](glide-element.md#field-permissions) and [record access](glide-record.md#choose-the-operation).

### Allow-if and matching order

Within an Allow-if ACL, applicable roles, security attributes, conditions, and script requirements must pass.
When multiple Allow-if ACLs match at the same processing point, passing one can satisfy that point.
The table check and field check remain separate requirements. Field-specific, inherited, and wildcard matching affect which ACLs are evaluated.

Two Allow-if rules at the same processing point:

```text
incident.description, Allow-if A: required role passes
incident.description, Allow-if B: restricted audience fails
Result at this point: A can grant access despite B failing.
```

Adding another restrictive Allow-if at that same point does not cancel an existing grant.
This does not mean a wildcard grant overrides every field-specific ACL.
Inspect the matching ACLs and execution trace before selecting a restriction pattern.
Use Allow-if for intended grants. Use an applicable Deny-unless rule when access must fail unless its requirements pass.

**Observed, configuration unrecorded:** A wildcard rule granted access despite a restrictive field-specific rule.
Use an ACL trace to determine which rules match and whether inheritance or configuration explains the result.

### Deny-unless

Where the `decision_type` capability is available, a Deny-unless rule uses `decision_type = 'deny'`.
An applicable failing Deny-unless rule blocks access before Allow-if evaluation.
Passing one Deny-unless rule does not cancel another applicable denial or establish that all access checks pass.

The [Deny-unless][deny] and [general ACL][acl] documentation give conflicting no-match access descriptions.
Check matching rules and security defaults before relying on a passing Deny-unless rule with no matching Allow-if.

`admin_overrides` is an access-design choice.
When enabled, administrators can pass this ACL despite its ordinary restrictions, subject to documented exceptions such as the `nobody` role.
When disabled, administrators may need to pass its condition and script. Administrators can still pass role checks.
Choose the intended behavior explicitly and test both administrator and ordinary-user paths.

### Query ACLs are separate

The documented GlideRecordSecure behavior distinguishes ordinary read/write ACLs from query ACLs.
Query ACL enforcement requires the supported opt-in mechanism described in the relevant API contract.
Confirm method availability and configuration through [record access guidance](glide-record.md#choose-the-operation).

## Applicability and access conditions

| Field        | Purpose                                              | Consequence                                                                                              |
| ------------ | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `applies_to` | Select records to which the ACL applies              | A record outside the filter is outside this ACL's applicability. An empty filter applies to all records. |
| `condition`  | Evaluate an access requirement for an applicable ACL | A false data condition fails that requirement. It is not an alternative applicability filter.            |
| `script`     | Evaluate additional authorization logic              | The script's boolean result participates in the ACL decision.                                            |

Use `applies_to` for applicability where supported.
**Conflicting observation, configuration unrecorded:** A false `condition` appeared to skip a Deny-unless ACL.
The [documented contract][acl] treats a false condition as failure. Inspect an ACL trace if behavior differs.

For example, `u_confidential` below is a **custom boolean field on incident**:

```text
name: incident.*
operation: read
decision_type: deny
applies_to: u_confidential=true^EQ
```

The filter targets confidential incidents. `^EQ` is an optional encoded-query terminator.
An ACL name beginning with `*` cannot use Applies To according to the configuration documentation.
Verify that each filter field exists on the named table.

An unfiltered ACL can be intentional. Its authorization logic must then handle the complete applicable record set.

```text
Incorrect assumption:
  An incident.* Deny-unless rule with no applicability filter
  calls a helper that returns false for ordinary incidents.
  The author expects only confidential incidents to be affected.

Failure:
  Ordinary incidents are also applicable and can be denied.

Correction:
  Set the intended applies_to filter, or deliberately handle
  ordinary incidents in the authorization predicate.
```

## Record and field patterns

`ExampleAccessHelper` is a **custom global Script Include** in these examples.
Its custom `isAuthorized(record)` method implements the application's authorization.
The helper must return a boolean and must not depend on an unchecked client-supplied user identity.
`u_confidential` is a custom boolean field.

### Record-level protection

Use a table-level rule when unauthorized users must not read the record.

```text
name: incident
operation: read
decision_type: deny
applies_to: u_confidential=true^EQ
script: answer = new ExampleAccessHelper().isAuthorized(current);
```

This pattern targets record access, so it does not provide a limited-field view to a denied reader.
The UI may omit a row or show an access error. Do not depend on one specific error message.
Check forms, lists, reports, direct requests, and the APIs used by the application.

ACL script:

```javascript
(function () {
  answer = new ExampleAccessHelper().isAuthorized(current);
})();
```

### Limited-field view

**Observed pattern, matching-rule trace unavailable:** Field-specific Deny-unless rules took precedence over a wildcard rule, permitting selected fields through the denial phase.
Verify precedence in the target configuration. Table access and subsequent Allow-if checks must also pass.

Configuration of the observed pattern:

```text
Wildcard:
  name: incident.*
  operation: read
  decision_type: deny
  applies_to: u_confidential=true^EQ
  script: answer = new ExampleAccessHelper().isAuthorized(current);

Field exception:
  name: incident.number
  operation: read
  decision_type: deny
  applies_to: u_confidential=true^EQ
  script: answer = true;
```

ACL validation can reject the unconditional `answer = true` exception.
Configure the intended role or security attribute requirements and inspect the resulting access trace.
Use the same applicability scope for related exceptions and the wildcard restriction.

| Example fields                                      | Intended limited view                                    | Required check                                                        |
| --------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------- |
| `number`, `state`, `priority`                       | Visible when separately permitted                        | Field exceptions and table access pass.                               |
| `short_description`, `category`, `assignment_group` | Visible only if their contents are safe for the audience | Review the data and each field's authorization.                       |
| `description`, `comments`, `work_notes`             | Restricted                                               | Confirm field and journal access through every supported UI/API path. |
| Other fields                                        | Restricted by the intended wildcard pattern              | Test newly added fields and inherited ACLs.                           |

This pattern uses one wildcard rule and one exception per visible field.
Do not assume journal fields are exempt from field security.

## Attachment protection

Attachments identify their parent through `table_name` and `table_sys_id`.
This pair is not an ordinary reference field that supports parent-field dot-walking.
Existing attachment ACLs may already check parent access. Inspect those rules before adding custom controls.

An incident's custom `u_confidential` field cannot be queried as an attachment field unless the attachment table has its own such field.
Resolve the parent explicitly when its attributes determine attachment authorization.

```text
Incorrect attachment applicability:
  u_confidential=true^EQ
  Assumption: this checks the parent incident's custom field.

Correct applicability for this example:
  table_name=incident^ORtable_name=sc_req_item^EQ
  Parent confidentiality: evaluate after resolving the parent record.
```

Both tables in this example must have the custom `u_confidential` field and compatible custom helper behavior.
Use `applies_to` for table selection where supported. A false `condition` can deny access instead of excluding unrelated attachments.

Illustrative Deny-unless **read** script for attachments within that applicability filter:

```javascript
(function () {
  var tableName = current.getValue("table_name");
  var parentSysId = current.getValue("table_sys_id");
  answer = false;

  // Restrict dynamic table lookup to this example's expected parents.
  if (tableName !== "incident" && tableName !== "sc_req_item") {
    return;
  }

  var parent = new GlideRecord(tableName);
  if (!parent.get(parentSysId)) {
    return; // This example denies an unresolved parent.
  }
  if (!parent.isValidField("u_confidential")) {
    return; // Required custom schema is absent.
  }

  answer =
    parent.getValue("u_confidential") !== "1" ||
    new ExampleAccessHelper().isAuthorized(parent);
})();
```

The script denies access when the parent cannot be resolved.
Choose and test orphan, temporary-upload, and special parent-table behavior for the consuming application.
A passing Deny-unless result still leaves other attachment authorization checks in effect.

Review read, create, write, and delete requirements separately.
A read rule does not establish the result for the other operations. Existing rules may already meet some requirements.
Creation can occur before the parent record exists, so do not copy a read predicate across all operations without analysis.
Each parent lookup adds database work. Measure relevant list and bulk paths.
Check interaction with installed plugin ACLs instead of assuming a particular plugin inventory.
For binary delivery and alternate paths, see [attachment gotchas](platform-gotchas.md#attachment-content-paths).

## Security Data Filters

Security Data Filters constrain query results. Field ACLs can expose selected fields from an accessible record.
A row filter cannot provide that partial-field view.

[Vendor SDF guidance][sdf] describes filters as combined query conditions and says `canRead()` does not check them.
It documents default enforcement for GlideRecordSecure, GlideRecordSandbox, and GlideAggregateSandbox.
Ordinary GlideRecord requires the supported security-feature opt-in for these filters.
Confirm availability and use the documented API when enabling query features.

The [default-filter guide][sdf-default] says filters generally apply after table-level and row ACL checks.
Other diagnostic views describe an evaluation hierarchy at a different level.
Do not model every access path as a universal sequence of SDF, Deny-unless, then Allow-if.

A filter defined on a child table does not automatically constrain queries through its parent table.
Test the tables and access paths through which records can be retrieved.
Filters can reduce returned data, but complex conditions and unindexed fields can also add query cost.
Use data filters with the record and field ACLs required by each access path.

**Unverified:** Attachment records were reported as outside SDF coverage. No reproduction supports a table-wide exclusion.
Check metadata, download, and API paths separately.
Missing query results can reflect a data filter even when a record ACL check succeeds.

## Management privileges and capture

Protected ACL-management operations require the appropriate elevated `security_admin` privilege in the documented administration workflow.
An ordinary administrator session does not automatically establish that elevation.
API or MCP capability depends on the account, session, execution context, and applicable access controls.
Check the operation result and read back the intended configuration.
See [write-failure diagnostics](platform-gotchas.md#acl-management-permissions).

**Observed, capture settings unknown:** ACL records inserted by a Fix Script were absent from `sys_update_xml`.
[Fix Script configuration][fix] documents the Unloadable option for creating Customer Update records.
Verify capture behavior and resulting artifacts for the selected transport. A successful insert alone proves neither capture nor migration.

### Illustrative ES5 creation pattern

Requires a server context with ACL-write permissions, the custom field/helper above, and a caller-supplied boolean `allowAdminOverride`.

```javascript
var acl = new GlideRecord("sys_security_acl");
acl.addQuery("name", "incident.*");
acl.addQuery("operation", "read");
acl.addQuery("decision_type", "deny");
acl.setLimit(1);
acl.query();

if (acl.next()) {
  // A match needs configuration and ownership review, not blind replacement.
  gs.info("A matching ACL exists. Check its configuration.");
} else {
  acl.initialize();
  acl.setValue("name", "incident.*");
  acl.setValue("type", "record");
  acl.setValue("operation", "read");
  acl.setValue("decision_type", "deny");
  acl.setValue("applies_to", "u_confidential=true^EQ");
  acl.setValue("advanced", true);
  acl.setValue("admin_overrides", allowAdminOverride);
  acl.setValue("active", true);
  acl.setValue("script", "answer = new ExampleAccessHelper().isAuthorized(current);");
  var createdId = acl.insert();
  if (!createdId) {
    throw new Error("ACL creation failed. Check authorization and platform errors.");
  }
}
```

The existence check limits duplicate creation in sequential use. It does not resolve concurrent creation or configuration drift.
Multiple legitimate ACLs can share these three lookup values. A real installer needs a stable identity for its own rule.
Keep the ACL script short when a custom Script Include owns complex authorization.
Use the effective script language mode.
See [language-mode gotchas](platform-gotchas.md#fix-script-language-mode).

## Focused verification

1. Compare authorized and unauthorized users, including the intended administrator behavior.
2. Check targeted and non-targeted records, inherited tables, and safe versus sensitive fields.
3. Check each required operation and attachment path, including a missing or not-yet-created parent.
4. Inspect matching ACLs, query ACL settings, SDF enforcement, and data-filter effects through parent-table queries.
5. Confirm the saved configuration and any required captured change records.

[acl]: sources/platform-security/access-control/exploring-access-control-list.md
[deny]: sources/platform-security/access-control/acl-denial-behavior.md
[configure]: sources/platform-security/access-control/configure-acl.md
[sdf]: sources/platform-security/security-data-filters.md
[sdf-default]: sources/platform-security/default-security-filters.md
[fix]: sources/application-development/create-fix-scripts.md
