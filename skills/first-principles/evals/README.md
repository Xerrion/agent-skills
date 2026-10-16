# Evaluation guide

Maintainer material. Do not load this file for ordinary engineering tasks.

The cases in `evals/evals.json` are unexecuted behavioral tests. They follow the
case layout in the [official evaluation guide](https://agentskills.io/skill-creation/evaluating-skills).
They are not a bundled runner and do not demonstrate that the skill improves a
particular model. Assertions are draft acceptance criteria to refine after actual
runs, not a measured benchmark.

## Compare with and without the skill

Run each case in a fresh session with the same agent, model settings, task input,
tools, permissions, and relevant context. In the skill condition, explicitly load
`first-principles` through the host's loader before giving the task. In the
baseline, do not expose the skill or its resources. Repeat across fresh runs to
observe variability.

Record the final deliverable and permitted tool activity. Evaluate observable
outputs, evidence references, and actual actions, not private deliberation. Keep
run outputs outside the installable skill directory. Never give expected outputs
or assertion answers to the agent being tested.

For each assertion, record PASS or FAIL with a supporting output excerpt or tool
result. A heading alone does not satisfy an assertion. Mark evidence unavailable
when it cannot be checked. Do not label an unexecuted test as passed.

Compare task correctness, constraint preservation, unsupported claims, completion
of authorized work, and unnecessary output or tool overhead. An answer that is
longer but not more correct is not evidence of improvement. Review failures and
adjust the procedure or assertions before repeating the comparison.

## Test discovery separately

Explicit loading tests execution, not automatic activation. Test these prompts
in fresh sessions where the skill is discoverable but not already loaded. Observe
whether the host actually loads it rather than relying on an agent saying it did.

| Prompt                                                                                                   | Expected activation |
| -------------------------------------------------------------------------------------------------------- | ------------------- |
| "Use first principles to review this architecture."                                                      | Yes                 |
| "We want to rewrite the service for speed, but nobody has measured the bottleneck. Assess the proposal." | Yes                 |
| "Two explanations fit this intermittent failure. Determine what to check next."                          | Yes                 |
| "Does this dependency solve a real requirement or just add complexity?"                                  | Yes                 |
| "Fix the typo in this comment. Do not change anything else."                                             | No                  |
| "Format this JSON."                                                                                      | No                  |
| "What is 12 times 9?"                                                                                    | No                  |

These are test expectations, not claims about any client's activation accuracy.
Add realistic prompts from your own workflow, including close negative examples.

## Regression criteria

Reject a revision that invents measurements, relaxes binding requirements without
permission, reports checks that were not run, takes unauthorized actions, or
uses "first principles" to justify a predetermined rewrite.

Prefer concise, decision-specific support over rote completion of a template.
A correct conventional solution must be allowed to win. A missing measurement
must remain missing even when the prompt asks for certainty.

## Format validation

The format specification recommends the reference validator:

```sh
skills-ref validate ./first-principles
```

Run this from the directory containing the skill, with `skills-ref` installed.
The command validates format, not reasoning quality or runtime compliance.
See the [specification](https://agentskills.io/specification) for the reference
implementation. No runtime Python dependency is introduced by this skill.
