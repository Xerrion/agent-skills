# Decision: <specific question>

Use this template only when a substantial decision needs a record and the task
does not already prescribe a format. Remove the instructions and irrelevant
rows. Do not invent facts to populate fields. Creating a persistent file still
requires authorization.

## Decision

<Recommended mechanism or diagnosis. State whether it is supported, conditional,
or unresolved. Describe the scope, not a universal rule.>

## Basis

| Kind       | Premise                               | Source or status                                   | Effect on the decision  |
| ---------- | ------------------------------------- | -------------------------------------------------- | ----------------------- |
| Fact       | <observation or supplied fact>        | <source, scope, and whether independently checked> | <why it matters>        |
| Constraint | <binding requirement>                 | <requirement source>                               | <what it rules out>     |
| Invariant  | <property to preserve>                | <requirement it follows from>                      | <how it can be checked> |
| Assumption | <material unknown used provisionally> | <unverified>                                       | <what changes if false> |
| Preference | <negotiable goal, if relevant>        | <who prefers it>                                   | <how it breaks a tie>   |

## Necessary behavior and mechanism

| Required behavior | Why it is necessary               | Proposed mechanism   | Check               |
| ----------------- | --------------------------------- | -------------------- | ------------------- |
| <behavior>        | <supporting premise or invariant> | <how it is provided> | <observable result> |

<Include a short calculation or model only when it materially affects the choice.
State units and assumptions. Explain the delta from the existing system.>

## Alternative and trade-off

<The strongest plausible alternative, evaluated against the same constraints.
Explain what the chosen option gains, what it gives up, and why the trade-off is
acceptable. Include keeping the current solution when it is plausible.>

## Verification

| Status   | Evidence or proposed check            | Result or remaining uncertainty |
| -------- | ------------------------------------- | ------------------------------- |
| Observed | <actual inspection or executed check> | <result and scope>              |
| Inferred | <conclusion and its premises>         | <limits of the inference>       |
| Not run  | <check not performed>                 | <what cannot yet be claimed>    |

**Revisit when:** <observable condition that changes the decision>.

**Next authorized action:** <implementation, bounded experiment, further
inspection, or escalation of a specific blocking constraint>.
