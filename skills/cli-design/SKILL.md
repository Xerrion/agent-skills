---
name: cli-design
description: Design, implement, and review command-line interfaces for human users and automation. Use for command and flag design, help, output and exit contracts, configuration, diagnostics, networking, installation, updates, and CLI compatibility across languages, frameworks, shells, and operating systems.
---

# CLI Design

Build a predictable interface for terminals, scripts, and long-lived installations. Base decisions on user tasks and the existing public contract.

## Establish the contract

1. Identify primary tasks, intended users, automation consumers, and compatibility commitments. Inspect the parser, help, tests, documentation, and release conventions when available.
2. Identify supported operating systems, shells, terminal capabilities, installation channels, filesystem permissions, and network restrictions. State assumptions when the project leaves these open.
3. Match the requested scope. For a small fix, inspect affected behavior. For a new CLI, sketch discovery, a common successful task, a recoverable mistake, and unattended use before choosing implementation details.
4. Define each affected command's inputs, defaults, output format and destination, exit meaning, interaction requirements, side effects, and failure recovery. Use a compact table or examples when useful.

Preserve established names, schemas, precedence rules, and exit meanings unless the requested change includes migration. Treat behavior consumed by scripts as a public interface even when originally undocumented.

## Read the relevant guidance

Read only the references needed for the task:

| Work | Reference |
| --- | --- |
| Commands, help, input, output, interaction, configuration | [Interface contracts](references/interface-contracts.md) |
| Diagnostics, networking, security, performance, analytics, distribution, versioning | [Runtime and lifecycle](references/runtime-and-lifecycle.md) |
| Implementation checks, regression cases, interface audits | [Validation](references/validation.md) |
| Attribution, coverage, and source limitations | [Sources](references/sources.md) |

## Keep decisions portable

- Specify observable behavior before selecting a parser, runtime, packaging tool, or test framework. Adapt to the project's stack.
- Distinguish a general contract from its platform implementation. Map paths, credentials, subprocess invocation, terminal detection, cancellation, and installation to supported native capabilities.
- Determine capabilities independently. Redirected output does not establish whether input can be interactive; interactive input does not justify formatting redirected output.
- Use plain text and explicit arguments as a dependable baseline. Add richer presentation or interactive convenience where useful.
- Follow relevant ecosystem conventions. Do not require every CLI to implement all platforms, channels, formats, or optional features discussed here.
- Keep examples shell neutral where possible. Label shell-specific quoting and redirection.

## Implement or review

For implementation, turn the affected contract into code, focused behavioral checks, and matching help or documentation. Separate parsing and presentation from the operation sufficiently to exercise them independently; avoid imposing a particular architecture on a small utility.

For review, lead with reproducible findings. Provide the invocation or environment, observed behavior, user impact, and smallest useful correction. Distinguish defects, compatibility risks, and optional improvements. Mark unavailable evidence as unverified.

Select checks from the validation reference proportional to the change. Report what ran and what remains unverified. Do not claim cross-platform compatibility from a single-platform run.

## Deliver the result

Show the implemented behavior or proposed interface, significant tradeoffs, validation evidence, and any migration or remaining limitation. Keep changes within scope; avoid adding telemetry, self-updating, SDK bindings, or distribution channels merely because the guide discusses them.

Combine [Better CLI's design guides](https://bettercli.org/design/) with the additional primary sources mapped in the sources reference. Use the bundled guidance offline. Consult original pages or current platform documentation when implementation details need verification. Distinguish formal requirements, ecosystem conventions, and project-specific choices.
