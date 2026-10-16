# Client scripts: form behavior and server requests

Use client scripts for interactive validation and dynamic data. Use UI Policies for declarative field behavior.
Neither mechanism establishes server-side authorization or protects writes through every interface.

Sources: [client design guidance](sources/api-reference/scripts/client-script-best-practices.md), [GlideForm](sources/api-reference/glide-form-client.md), and [GlideAjax](sources/api-reference/glide-ajax-client.md).

## Choose the mechanism

| Need                                              | Mechanism                                 | Limit                                                          |
| ------------------------------------------------- | ----------------------------------------- | -------------------------------------------------------------- |
| Mandatory, read-only, or visible field state      | UI Policy                                 | Applies to the configured form context, not all data writes.   |
| Data known when the form loads                    | Display Business Rule and `g_scratchpad`  | Sent once for that form load.                                  |
| Data requested after a field changes              | Asynchronous GlideAjax                    | The callback runs later. Protect against stale results.        |
| Local submit validation                           | `onSubmit` Client Script                  | Returning false blocks that submission.                        |
| List-cell validation                              | `onCellEdit`                              | Form scripts and UI Policies do not automatically cover lists. |
| Invariants across forms, lists, imports, and APIs | Suitable server validation or Data Policy | Select the mechanism for the actual write paths.               |
| Record and field authorization                    | ACLs                                      | Hiding or disabling a field does not deny access.              |

The server's ES2021 setting does not select the browser's JavaScript support.
Default to ES5-compatible client syntax unless the target browser and script-processing context support modern syntax.
Check workspace, Service Portal, mobile, and core-UI API support separately.

## Script types and guards

| Type         | Trigger                                                |
| ------------ | ------------------------------------------------------ |
| `onLoad`     | Form load.                                             |
| `onChange`   | A field value changes, including load-time population. |
| `onSubmit`   | A form submission.                                     |
| `onCellEdit` | List-cell editing.                                     |

For an onChange action that needs a populated value after loading:

```javascript
function onChange(control, oldValue, newValue, isLoading, isTemplate) {
  if (isLoading || newValue === "") {
    return;
  }
  // Action for a populated value.
}
```

The empty-value guard is appropriate only when clearing the field requires no action.
If clearing the field must clear dependent values or messages, handle that branch explicitly.
Use `isTemplate` only when template application needs distinct behavior.
`oldValue` is the value when the form loaded. Comparing it with `newValue` can miss a change back to the original value.

Keep variables inside functions. Unwrapped client variables can collide with other scripts.
Client Script Order runs from lower to higher numbers, but it does not order asynchronous responses.
UI Policies apply after client scripts and can change the field state again.

## Request data with GlideAjax

The client names the processor, sets `sysparm_name`, adds custom `sysparm_` parameters, and requests an asynchronous response.

| Method                   | Callback contract                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------------- |
| `getXML(callback)`       | Callback receives the XML response. Extract its `answer` attribute.                       |
| `getXMLAnswer(callback)` | Callback receives the answer value. Parse JSON only when the endpoint returns JSON.       |
| `getXMLWait()`           | Synchronous. Do not use. It blocks the browser and is unavailable in scoped applications. |

Example onChange script for an incident's `parent` field.
It calls the custom `ExampleIncidentAjax` endpoint shown below, which accepts only incident parents:

```javascript
function onChange(control, oldValue, newValue, isLoading, isTemplate) {
  if (isLoading || newValue === "") {
    return;
  }

  var ga = new GlideAjax("ExampleIncidentAjax");
  ga.addParam("sysparm_name", "getIncidentNumber");
  ga.addParam("sysparm_record_id", newValue);
  ga.getXMLAnswer(function (answer) {
    if (g_form.getValue("parent") !== newValue) {
      return;
    }

    var result;
    try {
      result = JSON.parse(answer);
    } catch (error) {
      g_form.addErrorMessage("Cannot read the parent incident response.");
      return;
    }
    if (!result || result.ok !== true || typeof result.number !== "string") {
      g_form.addErrorMessage("Cannot read the parent incident.");
      return;
    }
    g_form.showFieldMsg("parent", result.number, "info");
  });
}
```

The callback compares the field's current value with the requested value.
That prevents an older response from describing a different current parent.
A field clear is intentionally ignored in this example. Add explicit message cleanup when the form requires it.

An ES5-compatible scoped Script Include for that endpoint:

```javascript
var ExampleIncidentAjax = Class.create();
ExampleIncidentAjax.prototype = Object.extendsObject(global.AbstractAjaxProcessor, {
  getIncidentNumber: function () {
    var sysId = this.getParameter("sysparm_record_id");
    if (!sysId || !/^[0-9a-f]{32}$/i.test(sysId)) {
      return JSON.stringify({ ok: false });
    }

    var grIncident = new GlideRecordSecure("incident");
    if (
      !grIncident.get("sys_id", sysId) ||
      !grIncident.getElement("number").canRead()
    ) {
      return JSON.stringify({ ok: false });
    }
    return JSON.stringify({
      ok: true,
      number: grIncident.getValue("number"),
    });
  },

  type: "ExampleIncidentAjax",
});
```

The negative result deliberately does not reveal whether an inaccessible record exists.
The client reports it as an error rather than a successful empty value.
Do not return whole records or accept arbitrary caller-selected tables, fields, or encoded queries.

Configure Client callable, the Script Include access ACL, and its application accessibility.
In a scoped app, extend `global.AbstractAjaxProcessor`. In global scope, use the applicable unqualified class.
When calling across scopes, use the Script Include's actual API Name and permitted access settings.
See [Script Include configuration](scripting.md#script-include-configuration-and-access).

## Supply load-time data with scratchpad

A Display Business Rule can publish server data known before the form appears:

```javascript
(function executeRule(current, previous) {
  g_scratchpad.initialState = current.getValue("state");
})(current, previous);
```

A client can read `g_scratchpad.initialState` without another server request.
Scratchpad data does not refresh automatically after a field change.
Use GlideAjax for dynamic requests. Do not put secrets or unauthorized fields in scratchpad.
Check [the observed scratchpad access pitfall](platform-gotchas.md) when ACLs restrict the form.

## Common form methods

| Method                                                 | Use or caution                                                                                                      |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `getValue(field)`                                      | Read the current form value.                                                                                        |
| `setValue(field, value)`                               | Set a field value. It can trigger onChange processing. Avoid repeated self-assignment.                              |
| `setValue(referenceField, sysId, displayValue)`        | Set a reference without a separate display-value lookup.                                                            |
| `getReference(field, callback)`                        | Retrieve a full referenced record asynchronously. Prefer a narrow GlideAjax response when only one value is needed. |
| `setMandatory(field, required)`                        | Change the mandatory state.                                                                                         |
| `setReadOnly(field, readOnly)`                         | Change editability. Resolve a mandatory requirement before making an empty field read-only.                         |
| `setDisplay(field, visible)`                           | Show or hide a field. Hidden space becomes available to other fields.                                               |
| `setVisible(field, visible)`                           | Desktop UI retains hidden space. Portal and mobile can reuse it.                                                    |
| `showFieldMsg(field, message, type)`                   | Show a field-level message. Confirm supported message types in the target UI.                                       |
| `hideFieldMsg(field, clearAll)`                        | Remove field messages.                                                                                              |
| `addInfoMessage(message)` / `addErrorMessage(message)` | Show a form-level message.                                                                                          |
| `clearMessages()`                                      | Remove form informational and error messages.                                                                       |
| `addOption(field, value, label)`                       | Add a choice. Use the stored value and the display label separately.                                                |
| `removeOption(field, value)` / `clearOptions(field)`   | Remove choices. This does not change server-side authorization.                                                     |

Neither hiding method can hide an empty mandatory field.
`setDisplay(false)` hides the field and reuses its layout space. It is not a promise to remove the field from the DOM.
Prefer UI Policies for these field-state changes.

## Submit validation

Example onSubmit validation requiring a description of at least 20 characters:

```javascript
function onSubmit() {
  var description = g_form.getValue("description");
  if (description.length < 20) {
    g_form.showFieldMsg(
      "description",
      "Description must contain at least 20 characters.",
      "error",
    );
    return false;
  }
  return true;
}
```

A later GlideAjax callback cannot retroactively change the return value of `onSubmit()`.
An asynchronous submit workflow needs an explicit pending and resubmission design.
Use server validation for an invariant that must hold outside this form.

For empty reference objects, user-only change listeners, strict read-only fields, or Script Include privacy overrides, read [client pitfalls](platform-gotchas.md#client-and-display-business-rules).

Avoid direct DOM manipulation, synchronous lookups, and scripts on the Global table that load on unrelated pages.
Use supported navigation and messaging APIs for the target UI rather than `window.location`, `alert()`, or `confirm()`.
Verify behavior as a non-admin user and through each supported form or list context.
