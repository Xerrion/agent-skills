# First-principles Agent Skill

An on-demand decision procedure for engineering agents. It requires the agent to
separate evidence from assumptions, derive necessary behavior, justify mechanisms,
challenge the preferred answer, and report verification honestly.

## Package

```text
first-principles/
├── SKILL.md
├── README.md
├── assets/
│   └── decision-record.md
├── references/
│   └── worked-examples.md
└── evals/
    ├── README.md
    └── evals.json
```

The core works without scripts, additional skills, network access, or external
packages. Evidence gathering uses only the tools the host already permits.
Examples, the template, and evaluations load only when relevant.

The package follows the [Agent Skills format](https://agentskills.io/specification):
a matching directory and skill name, YAML metadata in `SKILL.md`, and relative
resource references. Its main file is 213 lines, below the specification's
recommended 500-line limit; supplementary material stays outside the core.

## Install

Install this skill from the public repository with the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add xerrion/agent-skills --skill first-principles
```

The CLI installs the skill for the selected agent and scope. To install all skills in the repository for Codex:

```bash
npx skills add xerrion/agent-skills --skill '*' --agent codex --yes
```

## On-demand integration

The skill description contains the discovery triggers. Do not copy the full
procedure into every agent prompt or preload all companion files.

Add this rule to the relevant agent's instructions when explicit routing is
needed. It is a snippet to apply locally, not a claim that any agent was edited:

```markdown
## Conditional skill loading

Load `first-principles` through the native skill loader before committing to a
technical decision when the user requests first-principles reasoning, the choice
rests on disputed assumptions, a bug has competing causes, or a proposed rewrite,
dependency, optimization, or architecture change needs justification.

Apply its completion gate to the decision. Treat unavailable evidence as an
explicit limitation, not permission to invent certainty. Keep existing role,
scope, tool permissions, and output requirements. Do not load it for mechanical
edits or simple lookups unless explicitly requested.
```

Example user invocation:

> Load first-principles and evaluate whether this service actually needs a
> message broker. Use the repository's requirements and implementation as
> evidence. Keep the result concise and do not change files.

For delegated work, include the loading requirement in the relevant child's task
and ensure that child can access the skill. Do not assume the parent loading it
means the child has received its instructions.

## What it enforces as instructions

The workflow requires a supported basis, a mechanism tied to requirements, a
credible challenge, and honest verification before a decision is presented as
supported. It allows a conditional conclusion when important evidence is missing.
It does not insist on a particular architecture or on building components from
scratch. It preserves approved constraints and authorized implementation work.

The default output is a compact decision record, adapted to the user's required
format. A detailed file is optional, not a side effect of loading the skill.

## Limits and verification

A text skill is not an execution sandbox or a deterministic enforcement engine.
It cannot guarantee an agent's internal reasoning or compliance. For stronger
control, the host can require observable decision evidence and review it before
accepting a consequential action. That enforcement is outside this package.

Structural checks performed for this package are recorded below. Behavioral
improvement has not been benchmarked. The evaluation cases are proposed tests,
not evidence of model performance; run them against your actual agents.

See [the evaluation guide](evals/README.md) for an evaluation procedure and
[the cases](evals/evals.json) for prompts and expected behavior.

### Packaging checks

- Passed local checks for YAML parsing, permitted frontmatter fields, required
  values, field lengths, matching directory/name, and string-only metadata.
- Passed checks for relative resource links, balanced Markdown fences, UTF-8
  text, evaluation JSON structure, and unique evaluation IDs.
- ZIP integrity and extracted-file byte equality checked during packaging.
- These are local specification-based checks, not a `skills-ref` execution.
- Behavioral tests: not run against a target agent or model.

## Authoring references

Format and loading were checked against the official documentation when creating
this package. The reasoning workflow and fictional examples are original
instructions, not a claim that the format standard mandates this method.

- [Agent Skills overview](https://agentskills.io/home)
- [Agent Skills specification](https://agentskills.io/specification)
- [Skill authoring guidance](https://agentskills.io/skill-creation/best-practices)
- [Skill evaluation guidance](https://agentskills.io/skill-creation/evaluating-skills)
- [OpenCode skill loading](https://opencode.ai/docs/skills/)
