# Server scripting and Script Includes

Sources: [JavaScript modes](sources/api-reference/scripts/javascript-modes.md), [feature support](sources/api-reference/scripts/javascript-engine-feature-support.md), and [Script Includes](sources/api-reference/scripts/script-includes.md).

Read by task:

- [JavaScript modes](#javascript-mode-es5-or-es2021) for syntax and semantic dependencies.
- [Script Include pattern](#script-include-pattern) and [configuration](#script-include-configuration-and-access) for callable classes and functions.
- [Wrappers](#iife-wrappers-by-context) and [example naming](#example-naming) for script containers.
- [Error handling](#error-handling) and [API cautions](#api-and-security-cautions) for failure and access behavior.
- [Templates](#script-include-templates) for illustrative ES5 and ES2021 implementations.

## JavaScript Mode: ES5 or ES2021

Use the effective JavaScript mode of the application and individual artifact.
Use ES5-compatible syntax when the effective mode is unknown or compatibility requires it.
Confirm the mode when using modern syntax, diagnosing mode-dependent behavior, or reporting the setting.
Reuse mode evidence already established for the task.
An ES5-compatible wrapper alone does not require another lookup.

### Select the effective mode

Check the artifact's effective mode. Application defaults do not establish an existing artifact's configuration:

| Mode                   | Default or use                                                              | Constraint                                                       |
| ---------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| ECMAScript 2021 (ES12) | Default for new scoped applications.                                        | A subset of modern JavaScript, not a browser or Node.js runtime. |
| ES5 Standards          | Default for new global applications. Also available in scoped applications. | Modern syntax requires a supported per-script override.          |
| Compatibility          | Legacy scripts that need older behavior.                                    | Do not assume modern library or language semantics.              |

The JavaScript modes documentation describes ES2021 support for individual global scripts, without application-level selection.
The documentation also describes newly created scripts as enabling ES2021 by default, regardless of the application's mode.
Check the actual script instead of inferring its mode from the application's default or its creation date.

| Setting          | Where to check                                                                   |
| ---------------- | -------------------------------------------------------------------------------- |
| Application mode | The scoped application's JavaScript mode.                                        |
| Script override  | **Turn on ECMAScript 2021 (ES12) mode** above the script field, where supported. |

A recorded configuration used `sys_es_latest_script` for per-script mode metadata.
Confirm that table and its fields in the target configuration.
An XML-only transfer was observed without the associated toggle.
Check the effective target mode when transferring syntax that depends on it.
See [capture and execution gotchas](platform-gotchas.md) when exported artifacts behave differently after transfer.

Switching modes can change behavior even when a script still parses.
Test the affected inputs and library behavior after a mode change.
The mode name alone is not evidence that every feature of that ECMAScript edition is supported.

### Features documented in ES2021 mode

Check the feature matrix for an unusual feature or semantic dependency.
Feature support can depend on the execution context and effective mode.
The vendor distinguishes these statuses:

| Status        | Meaning                                                                                   |
| ------------- | ----------------------------------------------------------------------------------------- |
| Supported     | ServiceNow tested and validated that feature in the documented configuration.             |
| Not Supported | ServiceNow did not validate it. This is not proof that every invocation throws.           |
| Disallowed    | The platform rejects the feature for programming-model, security, or performance reasons. |

- Declarations and functions: `let`, `const`, arrow functions, default and rest parameters, spread, destructuring (declarations, assignment, parameters), block-level function declarations
- Literals: template literals including tagged templates, object shorthand and computed keys, numeric separators, binary and octal literals
- Operators: `?.`, `??`, `||=`, `&&=`, `??=`, `**`
- Control flow: `for...of`, optional catch binding (`catch {}`), generators and `yield*`
- Async: `async`/`await` in function declarations, function expressions, arrow functions, and object-literal methods; `Promise.all/race/allSettled/any/finally`; `AggregateError`
- Collections and types: `Map`, `Set`, `WeakMap`, `WeakSet`, `Symbol` and well-known symbols, typed arrays, `BigInt`, `Proxy`, `globalThis`
- Built-in methods: `Object.assign/values/entries/fromEntries/is`, `Array.from/of/includes/find/findIndex/flat/flatMap/fill`, `String.padStart/padEnd/trimStart/trimEnd/replaceAll/matchAll/repeat/includes`
- RegExp: named capture groups, lookbehind assertions, `s`/`u`/`y` flags, Unicode property escapes
- `class` declarations and expressions, including `extends`, `super`, static members, and accessors

### Features to avoid even in ES2021 mode

Consult the feature matrix to distinguish unvalidated features from explicitly disallowed features:

- The entire `Reflect` namespace
- `async` methods inside a `class` body. Put async work in a supported object-literal method or arrow function.
- Async iterators, async generators, `for await...of`
- Lexical `new.target` binding inside arrow functions. The matrix separately lists class `new.target` as supported.
- Subclassing built-ins (`Array`, `Error`, `Map`, `Set`, `Promise`, `RegExp`, `Function`, `Number`, `String`, `Boolean`)
- `WeakRef`, `FinalizationRegistry`, `SharedArrayBuffer`, `Atomics`
- `generator.throw()` and `generator.return()`
- `new Function()` built with modern syntax (default parameters, destructuring, rest)
- Proper tail calls. Deep recursion can still overflow.

### Semantics that need individual checks

The matrix marks these semantic subfeatures as unvalidated or disallowed. That status does not prove a particular observed runtime result:

- Temporal dead zone: `let`/`const` entries are unvalidated. Declare before use instead of depending on the failure behavior.
- Implicit strict mode inside `class` bodies: the matrix marks it unvalidated. Use an explicit directive in a supported function context when strict semantics matter.
- `Function.prototype.toString` returning original source text
- Own-property order for `Object.assign`, `JSON.stringify`, and `JSON.parse`
- `Array.prototype.includes` on array-likes. Do not assume generic behavior here.
- `Number('0b1010')` and `Number('0o17')`. Literal support does not establish the same string-coercion behavior.
- Unicode escape sequences in identifiers and property keys
- Well-formed `JSON.stringify`. Do not assume lone surrogates are escaped.

### What the mode does not change

Language mode does not select the platform API, caller permissions, application accessibility, or script container.
Use the wrapper required by that container and the applicable global or scoped API contract.

### ES5 compatibility

These apply only until you have confirmed ES2021 mode is on for the artifact:

- Do not use `let`, `const`, arrows, template literals, classes, destructuring, spread, `?.`, `??`, or `async`/`await` in ES5 mode.
- Do not rely on `Map`, `Set`, `Promise`, or `Symbol` in ES5 mode.
- Use compatible alternatives to `Object.assign`, `Array.prototype.includes`, and `String.prototype.padStart` in ES5 mode.

## Script Include Pattern

ES5-compatible Script Include using `Class.create()`, `prototype`, and `type`:

```javascript
var MyUtil = Class.create();
MyUtil.prototype = {
  initialize: function () {},

  doSomething: function (param) {
    // implementation
  },

  type: "MyUtil",
};
```

For inheritance, use `Object.extendsObject`. The following fragment assumes global scope:

```javascript
var ChildUtil = Class.create();
ChildUtil.prototype = Object.extendsObject(AbstractAjaxProcessor, {
  doSomething: function (param) {
    // implementation
  },

  type: "ChildUtil",
});
```

A scoped AJAX processor extends `global.AbstractAjaxProcessor`. See the [client/server example](client-scripts.md#request-data-with-glideajax).
Retain this structure when extending a platform prototype such as `AbstractAjaxProcessor`.
The same structure permits modern method bodies when the effective mode supports them:

```javascript
var MyUtil = Class.create();
MyUtil.prototype = {
  initialize: function () {
    this.LOG_PREFIX = "[MyUtil] ";
  },

  summarize: function (userNames = []) {
    const labels = userNames.map((name) => name ?? "Unknown");
    return `${labels.length} user(s): ${labels.join(", ")}`;
  },

  type: "MyUtil",
};
```

The documented Script Include contract also permits a classless function whose name matches the record name.
The Script Include documentation does not establish every ES class loading and inheritance combination.
Use the documented prototype pattern by default when interoperability with platform inheritance matters.

## Script Include configuration and access

| Setting                              | Meaning                                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------------------- |
| Name                                 | Must match the class, prototype, and `type`, or the function name for an on-demand include. |
| API Name                             | The identifier used by out-of-scope callers.                                                |
| Active                               | Enables loading and use.                                                                    |
| Accessible from                      | Limits which application scopes may call the include.                                       |
| Client callable / Glide AJAX enabled | Exposes it to supported client request paths. The caller must satisfy its associated ACL.   |
| Sandbox enabled                      | Makes it available to sandboxed scripts. Enable only when the task requires it.             |

Client callable does not make returned records or fields authorized.
Validate request parameters and apply the appropriate data ACLs inside the server method.
Return only the required values. Do not expose credentials or whole GlideRecord objects.
See [client/server examples](client-scripts.md#request-data-with-glideajax).

## IIFE Wrappers by Context

Use the correct wrapper per script context:

- **REST API (Scripted REST Resource):** `(function process(request, response) { ... })(request, response);`
- **Widget Server Script:** `(function() { ... })();`
- **Widget Client Script:** `function() { ... }`
- **Email Script:** `(function runMailScript(current, template, email, email_action, event) { ... })(current, template, email, email_action, event);`
- **Transform Script:** `(function transformEntry(source, map, log, target) { ... })(source, map, log, target);`

## Example naming

- Declarations: `var` in ES5 mode. In ES2021 mode use `const` by default and `let` only where the binding is reassigned
- Variables and functions: `camelCase`
- GlideRecord variables: `gr` prefix (e.g., `grIncident`, `grUser`)
- GlideAggregate variables: `ga` prefix (e.g., `gaCount`)
- Constants: `UPPER_SNAKE_CASE`
- Script Include names: `PascalCase` matching the class name exactly

## Error Handling

Use consistent logging with class and method context:

```javascript
gs.error("[MyScriptInclude.methodName] Processing failed.");
gs.warn("[MyScriptInclude.methodName] Invalid processing state.");
gs.info("[MyScriptInclude.methodName] Processing complete.");
```

The `{0}` substitution works in both modes when the supplied values are safe to log.
Do not log raw request values, credentials, personal data, or unsanitized exception text.

## JSDoc Conventions

Document Script Includes with JSDoc:

```javascript
/**
 * Utility for managing incident escalation logic.
 * @class IncidentEscalation
 */

/**
 * Escalates an incident based on priority and age.
 * @param {string} incidentSysId - sys_id of the incident to escalate
 * @param {number} priority - Target priority level (1-5)
 * @returns {boolean} True if escalation was successful
 */
```

## API and security cautions

These rules apply in every mode:

- For reference sys_ids, use `getValue('reference_field')`.
- **No `gs.nowDateTime()`** in scoped apps. Use GlideDateTime and choose stored UTC or local display deliberately. See [dates and times](date-time.md).
- Do not evaluate untrusted input as code.
- Write stored values with `gr.setValue('field', value)`.
- Read stored values with `gr.getValue('field')`. GlideElement methods remain appropriate for field-specific behavior.
- Do not call `current.update()` to persist a Business Rule's changes to `current`.
- Use asynchronous GlideAjax rather than synchronous client/server calls.

## Hardcoded sys_ids

A literal sys_id can identify an application-owned record that is delivered consistently with the application.
Establish that the record retains the same identity across the intended targets before relying on the constant.
A sys_id copied from an example or independently created local data does not establish portability.

Prefer a named constant so the purpose is clear at each call site. Use a system property when administrators must configure the reference per instance. Use a lookup when the target is instance-specific data or is created independently on each instance and therefore does not share a stable sys_id.

## Script Include templates

Illustrative templates for a class-based Script Include. Replace the placeholder names and descriptions:

```javascript
/**
 * <Description of what this utility does>.
 * @class <ClassName>
 */
var ClassName = Class.create();
ClassName.prototype = {
  initialize: function () {
    this.LOG_PREFIX = "[ClassName] ";
  },

  /**
   * <Method description>.
   * @param {string} param1 - <description>
   * @returns {string} The validated string.
   */
  methodName: function (param1) {
    if (typeof param1 !== "string") {
      throw new Error("param1 must be a string.");
    }
    return param1;
  },

  type: "ClassName",
};
```

ES2021 method body in the same Script Include structure:

```javascript
/**
 * <Description of what this utility does>.
 * @class <ClassName>
 */
var ClassName = Class.create();
ClassName.prototype = {
  initialize: function () {
    this.LOG_PREFIX = "[ClassName] ";
  },

  /**
   * <Method description>.
   * @param {string} param1 - <description>
   * @param {string} [fallback] - <description>
   * @returns {string} The validated string or fallback.
   */
  methodName: function (param1, fallback = "") {
    const value = param1 ?? fallback;
    if (typeof value !== "string") {
      throw new Error("value must be a string.");
    }
    return value;
  },

  type: "ClassName",
};
```

Do not add a broad catch that converts an unexpected failure into `false`, an empty value, or another success-shaped result.
Catch only where the caller can report or recover from the specific failure.
