# Agent skills

Personal and general-purpose skills for coding agents, published in the [Skills CLI](https://github.com/vercel-labs/skills) layout.

## Install

With Node.js 22.20 or later installed, run this in your project to choose which skills and agents to install:

```bash
npx skills add xerrion/agent-skills
```

Install all skills for Codex without prompts:

```bash
npx skills add xerrion/agent-skills --skill '*' --agent codex --yes
```

Install one skill by name:

```bash
npx skills add xerrion/agent-skills --skill architecture-decision
```

Add `--global` to install for your user account. The default installs in the current project.

## Skills

| Skill                                                            | Use it for                                                                                                   |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| [architecture-decision](skills/architecture-decision/SKILL.md)   | Evaluating system boundaries, integration and data ownership, and other costly architecture choices.         |
| [engineering-philosophy](skills/engineering-philosophy/SKILL.md) | Applying engineering principles to implementation, review, research, writing, architecture, and UI work.     |
| [first-principles](skills/first-principles/SKILL.md)             | Evaluating technical choices from evidence, constraints, and invariants.                                     |
| [humanizer-da](skills/humanizer-da/SKILL.md)                     | Editing AI-styled Danish prose to sound natural while preserving facts, uncertainty, and the writer's voice. |
| [wow-addon](skills/wow-addon/SKILL.md)                           | Developing and reviewing WoW addons, including architecture, Lua patterns, events, frames, and API research. |

Each skill loads supporting references as its task requires. The WoW research toolkit describes optional helper tools; these require a separately configured connection.

## Repository layout

```text
skills/
  architecture-decision/SKILL.md
  engineering-philosophy/SKILL.md
  first-principles/SKILL.md
  humanizer-da/SKILL.md
  wow-addon/SKILL.md
```

The Skills CLI discovers skills under `skills/<skill-name>/`. Each directory contains a `SKILL.md` with `name` and `description` in YAML frontmatter. Supporting files stay in that directory and use relative links so they work after installation.

List available skills without installing them:

```bash
npx skills add xerrion/agent-skills --list
```
