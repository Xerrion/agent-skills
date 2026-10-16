# ADR Template

Use the repository's established template first. Otherwise, use the form below.
Replace placeholders with evidence or explicit unknowns. Omit inapplicable detail, not material uncertainty.
Use an unnumbered draft title until the identifier is established. Preserve the requested language.

---

# <ADR identifier when known>: <Specific architectural choice>

Status: proposed
Date: \<Actual decision or proposal date, when known>
Decision authority: <Established role or explicit unresolved owner>
Acceptance evidence: \<Pending, or the actual approval/delegation reference>
Related decisions: \<Relevant references, or None>

## Decision

\<Recommend a specific direction and state the decisive reason. For an unresolved choice, label the preferred option provisional and identify the deciding condition.>

## Context and Drivers

\<Describe the problem, current situation, affected boundary, and scope exclusions. Cite consequential facts.>

<State the hard constraints and the drivers that distinguish the options. Identify assumptions and unknowns separately.>

## Alternatives

| Option                              | Fit against the decisive drivers      | Main cost or risk      | Why selected or not selected |
| ----------------------------------- | ------------------------------------- | ---------------------- | ---------------------------- |
| <Current design or smallest change> | <Evidence-based assessment>           | <Concrete consequence> | <Reason>                     |
| <Credible alternative>              | <Assessment against the same drivers> | <Concrete consequence> | <Reason>                     |

<Adjust the option count to the real choice. Explain when the baseline is infeasible.>

## Architectural Contract

\<State the responsibilities, authoritative data owners, allowed dependencies, public contracts, and failure guarantees that the implementation must preserve. Include only what this decision changes or constrains.>

<Distinguish current behaviour from proposed behaviour. Add a compact flow or diagram only when necessary to make a boundary understandable.>

## Consequences

\<Describe the benefits, accepted disadvantages, operational responsibilities, and residual risks. Include the strongest objection and why the recommendation still holds.>

## Transition and Recovery

\<When applicable: describe coexistence, compatibility, data movement, cutover, and rollback or roll-forward. Identify irreversible steps and their required authorization. Otherwise omit this section.>

## Validation

| Invariant or expected outcome | Check and observable success criterion       | Evidence or current status                          |
| ----------------------------- | -------------------------------------------- | --------------------------------------------------- |
| <What must remain true>       | \<Specific inspection, test, or measurement> | \<Observed evidence, supplied evidence, or Not run> |

\<Include workload, environment, thresholds, and ownership when material. Label proposed thresholds and unassigned ownership explicitly.>

## Revisit When

<Name the concrete condition that would invalidate the choice or justify reassessment. State material unresolved evidence and authority needs.>
