# Code Philosophy

Make valid behaviour clear and invalid behaviour explicit.

Apply these principles to the language, runtime, and project contracts. They are not a reason to replace idiomatic code with a preferred style.

[Architecture](architecture.md) governs module boundaries and ownership. [Implementation](implementation.md) governs how changes are performed.

## 1. Early Exit (Guard Clauses)

Handle known preconditions before expensive or irreversible work.

Prefer guard clauses when they reduce nesting and make the main path clearer.

Do not force every function into the same shape. Pattern matching, structured branching, and a single cleanup path can be clearer.

Only check conditions that are meaningful at that point. A postcondition cannot be established before the operation runs.

Preserve cleanup, cancellation, and resource-release guarantees when introducing early returns.

## 2. Parse, Don't Validate (Illegal States Unrepresentable)

Convert untrusted input into a representation that establishes the invariants needed by the next layer.

Use constructors, parsers, schemas, discriminated unions, or equivalent language mechanisms.

A type assertion or cast does not validate runtime data.

Validate at actual trust boundaries. Do not repeat the same structural checks throughout trusted internal code without a reason.

Static types do not establish changing facts such as authorization, freshness, uniqueness, or current account state. Check those where the operation requires them.

Normalize input only when normalization is part of the intended contract. Do not silently repair invalid data into a different request.

## 3. Fail Fast, Fail Loud

Stop an operation when continuing would violate its contract or corrupt state.

Represent expected absence and rejection explicitly. An optional value or result type is valid when absence is part of the contract.

Do not convert unexpected failures into successful-looking defaults.

Handle errors where enough context exists to recover, retry, translate, or report them. Preserve the underlying cause where useful.

Recovery must have an explicit policy. Do not retry indefinitely or catch every error merely to keep execution moving.

Failing an operation does not necessarily mean terminating the process. Match containment to the failure.

Expose useful errors without leaking secrets or unnecessary internal details.

## 4. Intentional Naming & Interfaces

Name values by their meaning, units, and role where ambiguity matters.

Use predicate-style boolean names according to the language and project convention. Clarity matters more than a mandatory prefix.

Make arguments understandable at the call site. Prefer named arguments, options, or domain values when positional flags would be ambiguous.

Do not introduce an options object or enum when the existing call is already clear.

Keep inputs, outputs, mutation, and failure behaviour consistent with the function's contract.

Prefer a clear direct implementation over compact code that hides ordering or side effects.

## 5. Comment Hygiene

Use comments for information the code does not adequately express: rationale, invariants, constraints, compatibility workarounds, or subtle behaviour.

Do not repeat obvious operations in prose.

Public API documentation describes inputs, outputs, side effects, errors, and relevant guarantees.

Keep a durable issue, specification, or decision reference when it explains a non-obvious constraint. Add the essential explanation locally so the link is not the entire comment.

Do not add authorship, change diaries, or unrelated ticket metadata.

Update comments when behaviour changes. A misleading comment is worse than a missing explanation.

## Application

Assess the affected code, not every existing imperfection nearby.

When reviewing, identify a concrete failure or applicable rule violation. A different but equally clear implementation is not a defect.

Do not claim that these principles make all errors impossible. Use types, tests, and runtime checks for the guarantees they actually establish.
