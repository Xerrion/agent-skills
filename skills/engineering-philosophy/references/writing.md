# Writing Philosophy

Help the intended reader find, understand, and use the information they need.

This reference governs content decisions and document structure. Use `asd-ste100` for its applicable controlled-language rules rather than duplicating them here.

The active task defines whether to edit files or return text. Writing guidance does not grant additional tool or editing permissions.

## 1. Reader Need First

Identify the reader, their relevant knowledge, and the question, task, or decision the document supports.

Choose a structure that serves that purpose.

Tutorials teach through practice. How-to guides support tasks. References provide exact facts. Explanations develop understanding.

A README may orient readers and link to several forms. Do not force every document into a single universal outline.

Lead with what the reader needs next. Explain why first when that explanation helps them decide or act.

Do not add a motivation section when the heading and context already establish the need.

## 2. Progressive Disclosure Without Hidden Requirements

Provide essential scope, prerequisites, conditions, and risks before they affect an action or decision.

Defer optional depth, not information required for correct use.

Use descriptive headings and meaningful links. Support readers who arrive at a section through search or a direct link.

Present a complete primary path before uncommon alternatives when the task permits it.

Keep necessary context local. Do not require readers to reconstruct a procedure from scattered references.

## 3. Stable, Audience-Appropriate Terminology

Use a consistent term for each concept.

Preserve exact identifiers, configuration keys, paths, commands, and interface labels when referring to them.

Explain the relationship between public and internal terminology where needed. Do not expose internal names merely because they appear in the source.

Define unfamiliar terms when understanding matters, even if the term appears only once.

Introduce an abbreviation only when it helps subsequent reading. Do not expand familiar terms mechanically.

Prefer literal, precise wording. Do not replace a useful technical term with a vague simplification.

## 4. Ground Claims and State Their Limits

Verify consequential claims against evidence appropriate to them.

Distinguish current behaviour, required behaviour, recommendations, and proposals.

Check the applicable version and environment. Existing prose and historical design notes are sources to assess, not automatic proof.

State units, defaults, boundaries, and failure behaviour when they affect interpretation.

Do not invent capabilities, guarantees, performance claims, or design rationale.

Omit unsupported optional claims. Disclose uncertainty that affects the reader's decision or ability to complete the task.

Keep verification-session details in the handoff unless they belong in the durable document.

## 5. Make Instructions and Examples Usable

Provide the context needed to perform the action.

Identify prerequisites, environment, working directory, permissions, and replacement values where relevant.

Explain how to recognize success and recover from important failures.

A runnable example must be complete for its stated purpose. Label fragments, pseudocode, omissions, and illustrative output clearly.

Test examples when execution is authorized and practical. Otherwise, state the verification limitation in the handoff.

Do not invent observed output or imply that an example ran successfully.

Use safe values and preserve relevant security requirements. Do not shorten an example by hiding a dangerous assumption.

## 6. Edit for Clarity and Maintainability

Remove padding, promotional language, repetitive introductions, and unrelated explanations.

Preserve necessary context, qualifications, and consequences. Minimum word count is not the objective.

Choose paragraphs, lists, tables, and diagrams according to the information they convey.

Keep changing facts and behavioural rules in a canonical location. Reference them rather than creating competing copies.

Repeat essential reader context when it prevents misunderstanding.

For agent-facing instructions, make the trigger, action, authority boundary, and expected result explicit. Distinguish requirements from defaults and examples.

Avoid restating another skill's method, thresholds, or numbered principles inside an agent. Reference the owning skill instead.

Update affected documentation with the behaviour it describes. Preserve historical records as historical records.

## Before Handoff

Read the finished document from the reader's perspective.

Check terminology, examples, links, and rendered structure when available.

Confirm that the result answers the intended question and does not contain contradictory instructions or unsupported claims.

Do not claim full ASD-STE100 conformance merely because the companion skill was applied.
