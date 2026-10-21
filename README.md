# Agent skills

Reusable skills for coding agents, published in the [Skills CLI](https://github.com/vercel-labs/skills) layout.

## Install

Run this in your project to choose which skills and agents to install:

```bash
npx skills add xerrion/agent-skills
```

Install all skills for Codex without prompts:

```bash
npx skills add xerrion/agent-skills --skill '*' --agent codex --yes
```

Install one skill by name:

```bash
npx skills add xerrion/agent-skills --skill servicenow
```

Add `--global` to install for your user account. The default installs in the current project.

## Skills

| Skill                                                            | Use it for                                                                                                   |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| [architecture-decision](skills/architecture-decision/SKILL.md)   | Evaluating system boundaries, integration and data ownership, and other costly architecture choices.         |
| [engineering-philosophy](skills/engineering-philosophy/SKILL.md) | Applying engineering principles to implementation, review, research, writing, architecture, and UI work.     |
| [first-principles](skills/first-principles/SKILL.md)             | Evaluating technical choices from evidence, constraints, and invariants.                                     |
| [jira-refinement](skills/jira-refinement/SKILL.md)               | Creating and refining Jira Epics, Stories, Tasks, Bugs, Spikes, and Sub-tasks.                               |
| [servicenow](skills/servicenow/SKILL.md)                         | Developing and troubleshooting ServiceNow scripts, queries, ACLs, APIs, and MCP calls.                       |
| [tv2-design-system](skills/tv2-design-system/SKILL.md)           | Building and reviewing TV 2 interfaces and HTML emails with bundled tokens, fonts, and artwork.              |
| [wow-addon](skills/wow-addon/SKILL.md)                           | Developing and reviewing WoW addons, including architecture, Lua patterns, events, frames, and API research. |

Each skill loads supporting references as its task requires. The ServiceNow skill includes local API sources and type declarations. ServiceNow MCP tools require a separately configured connection.

## Repository layout

```text
skills/
  architecture-decision/SKILL.md
  engineering-philosophy/SKILL.md
  first-principles/SKILL.md
  jira-refinement/SKILL.md
  servicenow/SKILL.md
  tv2-design-system/SKILL.md
  wow-addon/SKILL.md
```

The Skills CLI discovers skills under `skills/<skill-name>/`. Each directory contains a `SKILL.md` with `name` and `description` in YAML frontmatter. Supporting files stay in that directory and use relative links so they work after installation.

List available skills without installing them:

```bash
npx skills add xerrion/agent-skills --list
```

ServiceNow reference materials include their [copyright and license notice](skills/servicenow/references/servicenow-docs-notice.txt) and [Apache 2.0 license text](skills/servicenow/references/apache-2.0.txt).
