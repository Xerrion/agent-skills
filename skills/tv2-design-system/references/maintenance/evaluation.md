# Behavioral evaluation

Use [evals.json](../../evals/evals.json) after changing instructions, defaults, or resource routing. These tasks evaluate agent behavior and output, separately from the Python script tests. The [Agent Skills evaluation guide](https://agentskills.io/skill-creation/evaluating-skills) explains the comparison method.

1. Snapshot the previous skill outside the installed folder. Create an external workspace such as `tv2-design-system-workspace/iteration-1/<case>/old_skill/outputs/` and `new_skill/outputs/`. Keep results out of the skill package.
2. Run the same case in separate fresh contexts, supplying only the selected skill path, user prompt, permitted input files, and output directory. Read the execution trace as well as the final artifact. Use the previous version as the baseline when refining an existing skill.
3. After inspecting the first outputs, grade specific observable requirements and save `grading.json` with pass/fail, evidence paths, and unverified items. Record actual duration/token usage when the client supplies them. Do not invent missing telemetry or infer browser appearance from source checks.
4. Compare both versions, preserve failures, and change instructions only where the evidence supports it. Re-run affected cases after a correction. Human visual review is still needed for appearance and interaction quality.

The fixtures cover an offline notice page, a design lookup, and source maintenance. The button-change record is a labelled synthetic change to the saved snapshot, not a live Figma update. Script unit tests do not substitute for these runs, and prepared cases do not count as completed evaluations.

For activation behavior, use [trigger-training.json](../../evals/trigger-training.json) and [trigger-validation.json](../../evals/trigger-validation.json). They contain realistic positive prompts and nearby negative prompts. Run each query in a fresh normal client context without explicitly telling it to load this skill. Count activation only when the trace actually reads `SKILL.md`. Repeat runs when estimating activation rates; keep the fixed validation split out of description tuning. A prose classification of the prompts is not an activation test. See [description evaluation guidance](https://agentskills.io/skill-creation/optimizing-descriptions).

Keep the current execution status with the external results. Report separately which cases ran, which checks passed, and which browser or activation checks remain unmeasured.
