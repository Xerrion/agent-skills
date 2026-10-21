# Sources and adaptation

Base this skill on [Better CLI: Design](https://bettercli.org/design/), supplemented by the primary sources below. Review date: 2026-10-21. Consult these Better CLI guides for the initial rationale:

| Topic | Original guide |
| --- | --- |
| Help | [CLI Help pages](https://bettercli.org/design/cli-help-page/) |
| Presentation | [Colors and formatting](https://bettercli.org/design/using-colors-in-cli/) |
| Settings | [Configuration](https://bettercli.org/design/configuration/) |
| Outcomes | [Exit codes](https://bettercli.org/design/exit-codes/) |
| Messages | [Messaging](https://bettercli.org/design/messaging/) |
| Troubleshooting | [Debugging](https://bettercli.org/design/debugging/) |
| Transport | [Networking](https://bettercli.org/design/cli-networking/) |
| Responsiveness | [Performance](https://bettercli.org/design/performance/) |
| Data collection | [Collecting analytics](https://bettercli.org/design/collecting-analytics/) |
| Trust | [Security considerations](https://bettercli.org/design/security-considerations/) |
| Installation | [Distribution and installation](https://bettercli.org/design/distribution/installation/) |
| Installers | [Self-executing installation scripts](https://bettercli.org/design/distribution/self-executing-installer/) |
| Updates | [Auto-updating CLI applications](https://bettercli.org/design/distribution/auto-updating-cli/) |
| Installed clients | [CLI application lifecycle](https://bettercli.org/design/cli-application-lifecycle/) |
| Releases | [Versioning CLI applications](https://bettercli.org/design/versioning/) |
| Reuse | [Using CLI as an SDK](https://bettercli.org/design/cli-as-sdk/) |

## Additional primary sources

| Source | Apply it to |
| --- | --- |
| [Command Line Interface Guidelines](https://clig.dev/) | Human and automation workflows, scriptable confirmations, previews, completion, cancellation, terminal restoration |
| [NO_COLOR](https://no-color.org/) | Nonempty-value semantics, explicit overrides, and color versus other styling |
| [Microsoft command-line design guidance](https://learn.microsoft.com/en-us/dotnet/standard/commandline/design-guidance) | Resource groups, action commands, descriptive naming, alias restraint, quiet/interactive behavior |
| [GNU C Library: argument syntax conventions](https://sourceware.org/glibc/manual/latest/html_node/Argument-Syntax.html) | POSIX-style options, `--`, stream operands, and differences introduced by GNU parsing |

Treat the design guides as advice, not universal standards. Several Better CLI sections are incomplete, especially SDK use and portions of configuration, messaging, debugging, and security. Use Microsoft's general interface principles without importing its framework, exact verbosity levels, or .NET-specific aliases.

## Resolve differences deliberately

Prefer a narrowly applicable convention over a broad guide's shorthand: follow NO_COLOR's nonempty-value rule rather than assuming mere presence always disables color. Preserve user-selected overrides while keeping machine output free of formatting.

Balance quiet success against human feedback: a data-producing utility can remain terse; a long-running human workflow may need status and a useful next step on stderr. Neither choice permits extra text inside a machine-readable result. Use native path and interruption mechanisms rather than treating Unix behavior as platform independent.

Use GNU's explanation of POSIX-style syntax as scoped convention, not a requirement to use C, GNU libraries, option permutation, or abbreviation. Avoid automatic abbreviation when future options could change an invocation's meaning.

Distinguish additional synthesis from source claims: the combined workflow, independent input/output capability checks, suggested configuration precedence, structured-output contracts, safe retries, subprocess and credential handling, and the validation matrix. Verify platform mechanisms against the project's runtime documentation.

Preserve context-dependent decisions. Do not turn discussions of telemetry consent, security overrides, quiet success, or update strategies into universal mandates. Choose behavior from user requirements and compatibility commitments.
