---
name: engineering-philosophy
description: Apply engineering principles when implementing or reviewing code, researching technical facts, writing documentation or agent instructions, and designing architecture or UI. Selects on-demand guidance for implementation, review, research, writing, code, architecture, and frontend work.
---

# Engineering Philosophy

Select the disciplines needed for the current task. This skill is a routing guide, not a universal checklist.
Keep responsibilities separate even when several disciplines apply together.

## Authority and Scope

The active agent and task define permissions, scope, Git policy, delegation, and output format.
Neither this skill nor its references expand that authority.

Reading implementation guidance does not authorize edits, tests, commits, or publishing.
A read-only review remains read-only. A research or writing task does not become an implementation task.
Apply project contracts before stylistic defaults. These principles do not authorize unrelated work.

## Select and Read References

1. Identify the current activity and affected behaviour.
1. Include references explicitly required by the active agent.
1. Select additional references from the tables below when their conditions apply.
1. Read each selected reference before the corresponding work. Do not merely name it as loaded.
1. Reconsider the selection if the task changes. Reuse references already read unless their contents changed.

All paths below are relative to the `engineering-philosophy` skill directory.
A generated instruction copy does not change that base directory.
These are reference files, not independently loadable skills.

Load several references when needed, but do not load all seven automatically.
A reference can link to another discipline without requiring that discipline for every task.
Read a linked reference when its guidance is needed, not merely because a link exists.

### How the Work Is Performed

| Discipline     | Read when                                                                                   | Reference                                      |
| -------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Implementation | Implementing or verifying software changes, including configuration and agent instructions. | [Implementation](references/implementation.md) |
| Review         | Reviewing code, patches, files, or prior findings.                                          | [Review](references/review.md)                 |
| Research       | Resolving external facts, API behaviour, compatibility, or technology choices.              | [Research](references/research.md)             |
| Writing        | Producing or revising durable technical prose or agent-facing instructions.                 | [Writing](references/writing.md)               |

### What the Result Should Satisfy

| Discipline   | Read when                                                                                            | Reference                                  |
| ------------ | ---------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| Code         | Implementing or inspecting logic, transformations, validation, state transitions, or error paths.    | [Code](references/code.md)                 |
| Architecture | Designing or inspecting boundaries, ownership, dependencies, interfaces, or cross-component effects. | [Architecture](references/architecture.md) |
| Frontend     | Designing or inspecting UI, styling, accessibility, interaction, or responsive behaviour.            | [Frontend](references/frontend.md)         |

Activity and result disciplines combine. For example, a UI implementation can require Implementation, Code, and Frontend.
A code review uses Review and relevant result disciplines without inheriting implementation duties.
A documentation-only task can use Writing without loading Code or Frontend.

## Ownership and Reporting

Each reference owns its discipline. Do not duplicate its rules in this entry point or in agent definitions.
`code-review` remains the separate owner of the review procedure, severity thresholds, verdicts, and report format.
`asd-ste100` remains separate and owns its applicable controlled-language rules.

Use only relevant principles from references actually read. Do not create a seven-discipline compliance report by default.
Follow the active agent's report format. Distinguish observed evidence, supplied results, and unverified assumptions.
If a required reference is unavailable, name it and explain the resulting limitation. Do not claim to have applied unread guidance.
