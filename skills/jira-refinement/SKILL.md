---
name: jira-refinement
description: Create, rewrite, or refine Jira issues. Use for Epics, Stories, Tasks, Bugs, Spikes, investigations, and Sub-tasks, including issue-type selection, decomposition, acceptance criteria, and Done When checks. Loads only the reference needed for each issue type.
---

# Jira Refinement

Make work understandable, appropriately scoped, and verifiable. Start with the intended outcome, not a template.
This skill owns the shared drafting rules and type-specific templates. The active agent owns Jira tool use and its response format.

## Workflow

1. Read the supplied context. For existing issues, inspect relevant descriptions, comments, parents, children, links, and project requirements when available.
1. Identify the observable outcome. Separate known facts, dependencies, assumptions, conflicts, and material open questions.
1. Assess the issue type and scope. Explain proposed type changes or splits before drafting their replacement structure.
1. Read the matching reference below. For mixed work, read each reference only when drafting that type.
1. Draft the smallest useful issue. Use the reference template as a starting point, not a list of mandatory sections.
1. Check facts, scope, and completion criteria. Present the draft and material questions before any Jira write.

## Select a Reference

Resolve reference paths from the `jira-refinement` skill directory. A generated instruction copy does not change that base directory.
Do not load all references for a single issue. Read the selected reference before using its template.

| Type     | Use when                                                                              | Reference                          |
| -------- | ------------------------------------------------------------------------------------- | ---------------------------------- |
| Epic     | A larger outcome needs multiple meaningful child outcomes.                            | [Epic](references/epic.md)         |
| Story    | A user or stakeholder needs an independently verifiable outcome.                      | [Story](references/story.md)       |
| Task     | Technical, operational, administrative, or enabling work has a concrete deliverable.  | [Task](references/task.md)         |
| Bug      | Existing behaviour differs from expected behaviour.                                   | [Bug](references/bug.md)           |
| Spike    | An investigation must produce knowledge or a decision before implementation planning. | [Spike](references/spike.md)       |
| Sub-task | A small execution step belongs to a parent and needs separate tracking.               | [Sub-task](references/sub-task.md) |

Choose by the work's purpose, not only its current Jira type.
If the project lacks a Spike type, use a Task with the Spike reference. Do not use the implementation Task template.
If the type is unclear, ask only for information that could change the choice.

## Shared Drafting Rules

- Preserve supported facts and established terminology. State conflicts instead of silently choosing a source.
- Keep missing information separate from the draft. Do not turn assumptions into acceptance criteria.
- Ask only questions that affect scope, acceptance, ownership, sequencing, risk, or planning.
- Do not invent personas, owners, dates, estimates, dependencies, evidence, or technical requirements.
- Write observable acceptance criteria or Done When checks. Replace vague claims such as "works correctly" with results the team can check.
- Keep technical constraints when supported by context. Do not design an implementation merely to complete a template.
- Use short sentences and concrete terms. Do not add emojis, empty headings, filler, or duplicated context.
- Omit template sections without useful content. Report missing material facts as open questions instead of filling placeholders with guesses.
- Remove secrets and personal data from evidence. Use safe references to restricted evidence when needed.

## Scope and Readiness

Keep steps together when they serve one outcome without useful independent results.
Split only for meaningful differences in outcome, ownership, timing, acceptance, risk, uncertainty, or parallel work.
Do not create an Epic for sequential steps. Use Sub-tasks only when separate execution tracking helps.

Use the project's Definition of Ready when available. Otherwise, check outcome clarity, verifiable completion, bounded scope, dependencies, and material questions.
An Epic needs sufficient clarity for decomposition, not sprint-sized scope. A Spike needs an agreed timebox before declaring it ready.
Missing material information does not prevent a useful draft. Expose the gap without inventing an answer or claiming readiness.

## Approval and Reporting

The team estimates work. The Product Owner owns priority and product decisions.
Do not set story points, priority, or sprint capacity. Do not invent owners or dates, or remove issues.

Before any Jira write:

1. Show the proposed text, issue types, and relationships. For existing issues, make meaningful changes clear.
1. Get explicit approval for those changes.
1. Apply only the approved changes through permitted tools.

Do not write implementation code as part of refinement. If Jira tools are unavailable, return the proposed text and state it was not saved.
After a write, check the result before reporting issue keys and changes. Identify failed or unapplied changes and remaining material questions.

Use the active agent's response format when specified. Otherwise, show the recommended type, brief rationale, proposed Jira text, and material questions.
Do not add an agile framework scorecard unless requested.
