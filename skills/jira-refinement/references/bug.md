# Bug

A Bug describes existing behaviour that differs from expected behaviour.
Separate observed facts from suspected causes. Do not invent reproduction steps, causes, environment details, or evidence.
Keep relevant environment fields. Omit browser or device fields only when they do not apply.
If reproduction is unknown, state that gap separately and use the available observations.
Expected behaviour and evidence must make the correction verifiable. Remove secrets and personal data from evidence.

## Template

```markdown
<Short description of the problem>

## Environment

- Environment: <Production / Test / Development>
- Version/build: <Version>
- Browser/client: <If relevant>
- OS/device: <If relevant>

## Steps to Reproduce

1. <Known step>
2. <Known step>

## Actual Result

<What happens?>

## Expected Result

<What should happen?>

## Impact

<Who or what is affected, and how?>

## Evidence

<Safe screenshots, logs, request IDs, traces, or links>
```
