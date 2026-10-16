# Review Philosophy

A review is a set of claims about an identified implementation.

Make those claims specific, supported, and useful to the author.

`code-review` owns the review method, severity thresholds, verdict rules, and report format. Do not redefine them here.

This reference does not expand the active reviewer's permissions.

## 1. Evidence Before Verdict

Connect each finding to a location, triggering condition, and observable consequence or applicable requirement.

Trace enough of the code path to support the claim.

Look for evidence that disproves the suspected issue, including caller guarantees, guards, framework behaviour, and tests.

Distinguish direct observation, supplied evidence, and static inference.

A proposed reproduction is not an executed reproduction. An author assertion is not independent confirmation.

## 2. Calibrate Impact and Confidence

Impact describes the consequence. Confidence describes the strength of the evidence.

Use the tier criteria and confidence rules from `code-review`. Do not introduce another scale or pretend that confidence estimates are measured probabilities.

State material uncertainty without hiding the potential consequence.

Do not retain unsupported speculation by relabeling it as a minor issue.

Place consequential unresolved assumptions under Verification with the evidence needed to resolve them.

## 3. Correctness Over Preference

Distinguish defective behaviour from code that could be written differently.

A blocking finding requires the evidence and impact defined by `code-review`.

Missing tests, unusual structure, or a philosophy deviation does not automatically establish a behavioural defect.

A test gap can violate an explicit project requirement. Cite that requirement rather than inventing one.

Do not use review to redesign a valid implementation into your preferred style.

## 4. Scope Discipline

For a change review, report defects introduced or exposed by the change.

Inspect surrounding code to understand reachability, contracts, and impact. That inspection does not turn unrelated existing debt into the review target.

For an explicit snapshot review, existing defects in the requested files, directory, or snippet are in scope.

For re-review, check earlier findings, their fixes, and affected paths. Report new supported defects without repeating settled preferences.

State material exclusions and missing evidence. Do not present partial coverage as a complete review.

## 5. Pattern Over Taste

Apply relevant project contracts and conventions before general preferences.

A named philosophy principle is not sufficient evidence by itself. Explain how the actual implementation violates an applicable requirement.

Keep optional refactoring separate from defects. State its concrete benefit and the evidence that behaviour is preserved.

Combine findings with the same root cause. Prefer a small actionable correction over an unsolicited rewrite.

No finding quota applies. No praise quota applies.

## Before Returning

Remove unsupported claims, duplicates, invented locations, and preference-only findings.

Ensure the verdict follows `code-review` and remains limited to the stated scope.

Approval does not certify that tests passed or that the system contains no defects.
