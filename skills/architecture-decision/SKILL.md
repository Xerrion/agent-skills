---
name: architecture-decision
description: Resolve consequential software design choices and produce evidence-backed architecture decision records (ADRs). Use when choosing system boundaries, data ownership, integration or consistency models, platform dependencies, or costly-to-reverse designs; comparing architectural alternatives; or revisiting an existing ADR. Distinguishes technical recommendations from approval and implementation authority.
---

# Architecture Decision

Turn an architectural question into a specific, justified, verifiable decision.

This skill owns the decision method, record lifecycle, and deliverable. `engineering-philosophy` owns the shared design and writing principles. The active agent and task own permissions, delegation, and output intent.

## 1. Establish the Decision

State the question, affected system, required outcome, and scope exclusions.

A decision merits an ADR when it materially affects cross-component contracts, quality requirements, ownership, trust, operations, dependencies, or future change cost.

Do not require an ADR for routine local design. Return `no-adr-needed` with the answer and brief rationale unless the caller explicitly requests a formal record.

Identify related decisions. Separate independently reversible choices into separate records, but do not fragment one coherent decision into an ADR for every implementation step.

For an existing ADR, establish whether the task is clarification, reassessment, or replacement. Do not silently convert a historical explanation into a new recommendation.

## 2. Establish Context and Drivers

Read applicable instructions, relevant accepted decisions, and enough implementation evidence to understand the affected boundaries.

Establish what exists before describing what should exist. For greenfield work, use supplied requirements and label the absence of implementation evidence.

Separate:

- Hard constraints: required contracts, policies, compatibility, data rules, or explicit limits.
- Decision drivers: the qualities and trade-offs that distinguish viable options.
- Assumptions: unverified conditions on which the recommendation depends.

Determine which drivers matter most. Infer a provisional priority only when defensible, and label it. Ask for authority when an unresolved priority would materially change product behaviour, cost, or risk acceptance.

Make vague goals concrete. For performance or reliability requirements, identify the workload, failure scenario, observable result, and threshold when known. Label an invented-for-discussion threshold as proposed, never as a requirement.

Do not manufacture traffic, service-level objectives, deadlines, team capacity, costs, or future requirements to justify a design.

## 3. Resolve Decision-Changing Unknowns

Investigate uncertainties that could change feasibility, ranking, safety, or implementation scope.

Prefer local evidence for the current system. Use primary documentation for external behaviour and check the relevant version and environment.

Distinguish direct observation, supplied evidence, inference, and an untested hypothesis. A vendor capability does not establish that the local configuration enables it.

Stop research when the evidence supports the decision or further reading is unlikely to change it.

When measurement is necessary, define a bounded experiment: question, representative workload, comparison baseline, observable result, pass/fail criterion, and how the result changes the choice.

Do not claim the experiment ran. Return the specific evidence request when execution or source access is outside the active agent's permissions.

## 4. Compare Credible Options

Consider retaining the current design and the smallest sufficient change. Explain when either fails a hard constraint.

Compare only plausible alternatives. Do not invent weak candidates to make a favourite win, require a fixed option count, or research every product in a category.

Evaluate options against the same decision drivers. Include relevant migration effort, operational ownership, failure handling, recurring cost, coupling, and reversibility.

Reject hard-constraint violations explicitly. Do not average them away with a weighted score.

Prefer qualitative comparisons with concrete reasons. Use numerical scoring only when its inputs and weights are defensible; expose sensitivity to uncertain inputs.

A technology's popularity, a named architecture pattern, or claimed scalability is not a project-specific benefit by itself.

## 5. Challenge the Preferred Option

Trace the important success path and the most consequential credible failure path across the proposed boundaries.

Consider only relevant concerns:

- Ownership and contracts: authoritative state, allowed dependencies, compatibility, transactions, and lifecycle ownership.
- Failure and recovery: partial completion, duplicate delivery, ordering, retries, timeouts, cancellation, overload, and repair.
- Security and privacy: trust boundaries, authorization, isolation, sensitive data, and credible abuse paths.
- Operation and change: deployment, observability, resource bounds, capacity evidence, migration, ongoing support, and exit cost.

Use the Architecture reference for design principles rather than reproducing its laws here.

State the strongest objection to the recommendation and the evidence that could overturn it. Check whether a simpler option satisfies the same constraints.

For risky transitions, describe coexistence and recovery. Identify the point beyond which rollback is unsafe or impossible. Use a roll-forward or repair strategy when reversal would lose data or break compatibility.

Describe current, transitional, and target states only when their differences matter. Do not produce a diagram merely to decorate the decision.

## 6. Decide

Recommend one direction when the evidence supports it. Name the decisive driver and the cost or limitation the team would accept.

Proceed under disclosed assumptions when they do not invalidate a safe recommendation. Do not block on immaterial unknowns.

When a material assumption remains unresolved, state the provisional preference and the exact condition that would change it. Do not present it as an unconditional commitment.

When no option satisfies the hard constraints, say so. Identify the smallest constraint change or experiment needed; do not quietly weaken the requirements.

Use one task outcome:

| Outcome           | Meaning                                                                                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `recommended`     | A specific recommendation is supported within the stated constraints and assumptions. Normal approval may still be pending.                                          |
| `needs-evidence`  | A named evidence gap prevents a reliable selection. Include the provisional preference and resolving check when possible.                                            |
| `needs-authority` | A material requirement, exception, or risk decision must be resolved by an authorized person. Explain the technical recommendation and the precise authority needed. |
| `no-adr-needed`   | The question is routine local design. Answer it without imposing a formal architecture process.                                                                      |

These outcomes describe the task result, not ADR approval, implementation completion, or code-review verdicts.

## 7. Record the Decision

Use the repository's ADR convention when one exists. Otherwise, read [the ADR template](references/adr-template.md) and adapt it to the decision.

A record must preserve the question, context, decisive drivers, chosen direction, credible alternatives, accepted disadvantages, uncertainty, and validation conditions. Keep it short enough to maintain.

One record contains one coherent architectural decision. Link related records rather than copying their rationale.

If no storage convention exists, suggest `docs/decisions/`. Inspect existing numbering before proposing a final identifier. A suggested path is not a saved file.

### Lifecycle and Authority

Default a new ADR to `proposed`.

Use `accepted` only when acceptance is evidenced by the designated authority or the project explicitly delegates that decision to the caller or active agent. Record the basis of acceptance. A request to recommend, draft, or evaluate is not acceptance.

A selected technical option may remain `proposed` pending normal approval. Do not use `needs-authority` merely because that approval has not happened yet.

Follow the project's remaining lifecycle states. Without a convention, use `rejected`, `deprecated`, and `superseded` where appropriate.

Preserve accepted historical rationale. A materially changed decision gets a new record with a supersession relationship. The old record remains available; an authorized writer updates its status and replacement link when the new decision is accepted.

An implementation that contradicts an ADR does not automatically supersede it. Establish whether the implementation, the recorded decision, or the governing requirement needs correction.

Acceptance does not establish implementation, operational verification, or permission to deploy.

### Evidence and Confirmation

Cite consequential claims next to the context or rationale they support. Use durable repository references and version-specific external sources where available.

Do not use inaccessible session identifiers as the only evidence in a durable ADR. Retain links to the underlying sources or attribute supplied evidence clearly.

Define checks that confirm both architectural conformance and the promised outcome. Connect each important invariant to an observable check.

Use project-supported commands only when known. Otherwise, describe the test or inspection without inventing executable instructions.

Mark future checks as not run. Identify the owner by established role when known, or leave ownership unresolved. Do not assign work to an uninvolved person.

Define a concrete revisit trigger: a failed validation, changed constraint, measured threshold, or relevant dependency change. "Revisit when needed" is not useful.

## Deliverable

Follow an explicit caller format. Otherwise, lead with a compact decision brief:

- Recommendation: the selected direction and decisive reason, or the unresolved choice.
- Outcome: one of the four task outcomes.
- Scope: affected boundary and important exclusions.
- Confidence: high, medium, or low, with the evidence and assumptions that justify the label. Do not present this as a measured probability.

For a material decision, return the completed ADR. When selection remains blocked, keep it proposed and label the choice provisional or unresolved.

Add a short handoff only when needed. Identify binding constraints, unresolved evidence or authority, and the next responsible role. Reference the ADR instead of repeating its contents.

Do not turn the handoff into a phased implementation plan, a code-review report, or an unsolicited patch.

For `no-adr-needed`, return the answer, outcome, and rationale without empty template sections unless the caller requested the record.

## Final Check

Confirm that the result answers the actual decision, identifies a preferred option when supportable, and explains why the strongest alternative was not selected.

Check hard constraints, existing decisions, operational consequences, verification claims, acceptance authority, and scope boundaries.

Remove invented facts, decorative scores, unnecessary layers, duplicated rationale, and claims that unperformed work is complete.
