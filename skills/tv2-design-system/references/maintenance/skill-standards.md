# Skill maintenance criteria

Apply these criteria when changing this skill's instructions or tooling. They concern the skill package, not the interfaces it produces.

Keep `name` aligned with the directory and `description` focused on the user's intent and activation boundaries. Document actual runtime requirements in `compatibility`. Load individual references only for the selected task, and keep direct routes to component instructions in `SKILL.md`.

For script changes, retain noninteractive arguments, useful help and errors, distinct exit codes, and bounded stdout. Save full source evidence to a report file when it is large. Run the relevant script tests and [behavioral cases](evaluation.md); record incomplete activation or browser checks separately from successful mechanical checks.

Validate frontmatter with an available current Agent Skills validator, such as `skills-ref validate <skill-directory>`, and validate the local package with `python3 scripts/validate_bundle.py`. The bundled checker covers this package's plain single-line metadata and directory-name contract; it is not a general YAML validator. Older validators can reject the specification's valid `compatibility` field. Check such a discrepancy against the current specification. An optional external validator is maintenance tooling, not a runtime dependency of this skill. Do not infer agent output quality from either format check.

The following upstream guidance is used when maintaining these choices. No live fetch is needed for ordinary skill execution.

| Subject | Source |
| --- | --- |
| Format and loading model | [Overview](https://agentskills.io/home), [specification](https://agentskills.io/specification), [quickstart](https://agentskills.io/skill-creation/quickstart) |
| Instruction scope and disclosure | [Best practices](https://agentskills.io/skill-creation/best-practices) |
| Activation behavior | [Description optimization](https://agentskills.io/skill-creation/optimizing-descriptions) |
| Script interfaces | [Using scripts](https://agentskills.io/skill-creation/using-scripts) |
| Output comparisons | [Evaluation](https://agentskills.io/skill-creation/evaluating-skills) |
