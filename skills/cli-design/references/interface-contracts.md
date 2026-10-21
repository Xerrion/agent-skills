# Interface contracts

## Command grammar and input

Choose consistent vocabulary around user tasks. Use comparable operations and options across subcommands. Prefer explicit flags for optional settings and positionals for a few essential operands. Reserve short options for frequent use; provide descriptive long forms.

For larger command trees, group related resources and use verbs for leaf actions. Choose a consistent order such as `tool artifact list`. Prefer readable lowercase names and hyphenated long options for a new interface; preserve existing conventions. Define global-option placement, repeated values, and boolean negation explicitly. Do not adopt an ecosystem's short-option meanings outside that ecosystem without checking expectations.

Reject unknown options and invalid combinations with targeted guidance. Suggest corrections without executing them. Support an end-of-options delimiter when operands could resemble flags. Define repeated options, empty input, omitted values, and stdin consumption. Do not consume stdin unexpectedly or use an input data stream for confirmation prompts.

For a new hyphen-option interface, define `--` as the end of option parsing and document how wrappers forward remaining arguments. Do not assume a parser accepts intermixed operands/options, short-option clusters, or long-option abbreviations. Avoid automatic abbreviations for a stable new interface: adding an option can make a previously accepted prefix ambiguous.

For destructive commands, define target scope, preview behavior where useful, and explicit authorization. Keep confirmation bypass separate from input completeness. Never interpret unavailable interaction as consent.

Offer `--dry-run` for consequential operations when an accurate preview is feasible; do not mutate as part of preview. Match confirmation strength to the consequence and keep it scriptable. For file-oriented commands, consider `-` for stdin/stdout and completion for discoverable command names and values.

## Help and discovery

Make explicit help available without credentials, service access, setup, or side effects; print it to stdout and exit successfully. Support command-specific help and established help spellings, usually `--help` and `-h`. Treat version inspection similarly.

Explain purpose, syntax, a realistic first example, commands, significant defaults, required setup, and where to learn more. Keep generated option reference aligned with authored examples. For invalid invocation, print the specific error and relevant usage guidance to stderr, then fail.

Choose no-argument behavior deliberately: run an unambiguous primary action or show an introduction. Avoid forcing a pager; use one only in an appropriate terminal context with a bypass.

## Output and messaging

Keep result data on stdout. Send errors, warnings, progress, and diagnostics to stderr. Avoid redundant success chatter when status suffices.

For automation, define a stable structured or deliberately simple text format. Specify empty results, ordering, record boundaries, and partial results. Keep banners and diagnostics out of that stream. Define whether failure can leave partial stdout data rather than silently presenting it as complete.

Base color and cursor control on the destination stream's capabilities. A nonempty `NO_COLOR` disables default ANSI color, including values such as `0` or `false`; an empty value does not activate the convention. Explicit per-tool configuration or invocation options may override it. Keep this separate from plain-output mode: NO_COLOR concerns color, not all styling. Never let color controls contaminate machine-readable data. Keep plain output readable and meaning independent of color. Avoid assumptions about themes, width, or Unicode support. Suppress animated progress in files, pipes, and machine-readable output.

Report what failed, relevant context, and an actionable next step. After a timed-out mutation, distinguish an unknown remote outcome from confirmed failure. Save technical traces for debug mode.

## Exit and interaction semantics

Use zero for the command's defined successful outcome and nonzero when it fails that contract. Start with simple success/failure; add categories only when callers need different handling. Document empty results, partial completion, cancellation, and domain-specific negative results. Keep meanings stable; do not map arbitrary protocol statuses directly to process exit codes.

Provide a way to complete automation without prompts. When required input is absent and interaction is unavailable or disabled, fail promptly with the missing input and its noninteractive alternative. Check prompt availability separately from presentation. Do not launch a pager, browser, or editor unexpectedly in unattended execution.

Make cancellation available during waits and bound cleanup time. Restore terminal state before exit, including password echo and cursor visibility. Map interrupt handling to native mechanisms rather than assuming Unix signals exist everywhere. Never hide an active prompt behind quiet output.

## Configuration

Document sources, scope, precedence, and merge versus replacement. Preserve existing precedence. For a new CLI, consider explicit flags over environment settings, project configuration, user configuration, and defaults; adjust deliberately for the product. Explain empty, unset, and false values.

Namespace environment settings. Parse booleans and numeric units explicitly; reject invalid values before side effects. Show redacted effective configuration with provenance when troubleshooting needs it.

Choose an evolvable data format and version persistent schemas when needed. Avoid executable configuration unless execution is an intentional trust boundary. Resolve storage locations through native conventions rather than hard-coded OS paths.
