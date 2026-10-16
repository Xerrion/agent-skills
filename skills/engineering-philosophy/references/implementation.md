# Implementation Philosophy

Implement the requested behaviour with evidence appropriate to its risk.

This reference governs the act of changing software. [Code](code.md) and [Architecture](architecture.md) govern the resulting code and structure.

The active agent and task define permissions, Git policy, and reporting format. This reference does not expand them.

## 1. Understand Before Change

Establish the current behaviour, requested behaviour, acceptance criteria, and relevant constraints before editing.

Read applicable project instructions and enough implementation context to identify the affected paths and invariants.

Distinguish explicit requirements from assumptions. Do not turn an implementation guess into a product requirement.

Stop discovery when the change surface and verification approach are sufficiently clear. Expand it only to resolve a consequential uncertainty.

## 2. Verify Before Assume

Verify assumptions whose failure would invalidate the implementation.

Use defining source, installed types, versioned documentation, generated schemas, or executable evidence as appropriate.

A manifest or lockfile establishes dependency identity and version. It does not establish that a particular method exists or behaves as expected.

Reuse supplied evidence when its source, version, and applicability are clear. Recheck stale, conflicting, or consequentially incomplete evidence.

Do not manually reread every familiar symbol as a ritual. Verification effort follows uncertainty and consequence.

## 3. Sweep the Impact Surface

Trace consumers when changing names, signatures, paths, schemas, configuration, or observable behaviour.

Consider callers, implementations, tests, serialization, persisted data, generated artifacts, documentation, and external integrations where relevant.

Combine repository searches with semantic inspection. Text search cannot establish complete compatibility by itself.

Account for relevant matches. Do not delete historical references, migrations, or compatibility aliases merely because they contain an old name.

Name consumers outside the available evidence. Do not claim they were checked.

## 4. Make the Smallest Coherent Change

Classify work as:

- **Required:** Directly implements the requested outcome.
- **Induced:** Necessary to integrate the change, preserve an invariant, or prevent a regression caused by it.
- **Adjacent:** Useful but independent improvement.

Implement Required and Induced work. Record Adjacent work separately.

A supporting refactor is justified when it makes the requested implementation correct and coherent. A philosophy preference alone is insufficient.

Minimize justified scope, not line count. Preserve unrelated work and avoid formatting churn.

## 5. Verify Behaviour and Report Evidence

Choose checks according to the changed behaviour and plausible failure paths.

For bug fixes, establish a failing reproduction when practical and safe. Confirm that it fails for the relevant reason, not an unrelated setup error.

Use focused checks during implementation. Expand to integration checks, builds, broader suites, or runtime inspection when risk or project policy requires them.

A passing command proves only what it actually checked. Inspect test scope, assertions, discovery, and skipped cases.

Reuse results only while relevant source, tests, dependencies, configuration, runtime, and environmental assumptions remain valid.

Use these result labels consistently:

| Result  | Meaning                                                              |
| ------- | -------------------------------------------------------------------- |
| PASS    | The stated check completed and met its stated expectation.           |
| FAIL    | The check ran and did not meet that expectation.                     |
| FLAKY   | Observed outcomes were inconsistent. Preserve both results.          |
| NOT RUN | The check is relevant but was omitted, blocked, or did not complete. |
| N/A     | The check does not apply. State why when not obvious.                |

For executed checks, report the exact command or action and observed evidence.

For supplied results, identify their source and applicable revision. For static reasoning, identify the inspected evidence.

Do not invent commands, output, test counts, or verification claims.

A missing required check remains a completion gap. Review approval, a commit, or confidence does not replace it.

## 6. Review the Final Change

Inspect the complete scoped change after the last edit affecting it.

Include staged and unstaged changes, new files, deletions, and generated output. Do not rely on one diff command that omits part of the work.

Check correctness, scope, compatibility, error paths, stale instructions, temporary scaffolding, and accidental edits.

Confirm that verification applies to the final relevant state. Hooks and generators can change that state.

Before reporting completion, connect each acceptance criterion to implementation and evidence. State any remaining limitation explicitly.
