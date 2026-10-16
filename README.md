# ServiceNow skills

Agent instructions for ServiceNow development, troubleshooting, and API lookup. Install with the [Skills CLI](https://github.com/vercel-labs/skills).

## Install

Install from GitHub:

```bash
npx skills add xerrion/servicenow-skills --skill servicenow
```

Node.js and npm must be available. The CLI lets you select your coding agent and installation scope.

Install for a specific agent, such as Codex or OpenCode:

```bash
npx skills add xerrion/servicenow-skills --skill servicenow --agent codex
npx skills add xerrion/servicenow-skills --skill servicenow --agent opencode
```

Add `--global` to make the skill available across projects. Omit it to install in the current project.

## Available skill

| Skill | Use it for |
| --- | --- |
| [servicenow](skills/servicenow/SKILL.md) | Scripts, Business Rules, Client Scripts, GlideRecord, encoded queries, date handling, ACLs, API contracts, and MCP interaction. |

The skill loads task-specific references as needed. Local API sources and type declarations are included in the installation. ServiceNow MCP tools require a separately configured connection.

## Repository layout

```text
skills/
  servicenow/
    SKILL.md
    references/
      sources/
      types/
      ...
```

Each installable skill lives in `skills/<skill-name>/` and has a `SKILL.md` with `name` and `description` in YAML frontmatter. Keep supporting files inside that directory and use relative links so they work after installation.

The Skills CLI discovers this layout directly. This repository does not need an npm package or a custom installer.

## Try the local version

From this repository's root directory:

```bash
npx skills add . --skill servicenow
```

List the skills available locally without installing them:

```bash
npx skills add . --list
```

Check the GitHub source:

```bash
npx skills add xerrion/servicenow-skills --list
```

## Bundled source notices

ServiceNow reference materials include their existing [copyright and license notice](skills/servicenow/references/servicenow-docs-notice.txt) and [Apache 2.0 license text](skills/servicenow/references/apache-2.0.txt).
