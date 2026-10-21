# Runtime and lifecycle

## Diagnostics

Offer consistent verbosity and debug controls across commands. Keep diagnostics on stderr and redact credentials, sensitive URLs, and payloads before emission. Include useful version and execution context without dumping the environment.

If writing diagnostic files, use an appropriate application or explicitly selected location. Avoid unexpected files in the working directory. Report the location and apply suitable access controls and retention. Treat remote crash reporting as data collection, not an automatic extension of local debugging.

## Networking

Apply transport configuration consistently to business requests and optional update or analytics requests. Prefer a shared transport policy over independent clients with different behavior.

Define proxy discovery and bypass support, custom certificate authorities, endpoint overrides, authentication, and supported address families. Verify the library's handling of uppercase/lowercase proxy settings and bypass matching. Redact proxy credentials.

Use TLS verification by default. Prefer configured trust over disabling verification. If an insecure mode exists, make it explicit, visible, and scoped. Document contacted services and a useful application/version identifier.

Set bounded connection and operation deadlines. Retry transient failures only within a limit and when repetition is safe. For writes, use idempotency or establish the prior result before replay. Preserve unknown-outcome errors when certainty is unavailable. Support cancellation of outstanding work.

## Performance

Measure startup, help, first useful feedback, and representative completion times on stated hardware and workloads. Choose budgets appropriate to actual use rather than a universal numerical target.

Validate cheap input errors before expensive initialization or network calls. Defer irrelevant work. Bound concurrency and memory for large input. Distinguish throughput from responsiveness and compare equivalent environments when investigating regressions.

## Analytics, when requested

First consider existing service or distribution metrics. Add direct collection only for a defined need. Make collection and its controls visible; preserve the agreed consent model.

Prefer predefined event fields over raw arguments, paths, environment data, error text, or request bodies. Treat metadata as potentially sensitive. Sanitize before sending and on the server; define a removal process for accidental collection. Use a stable first-party ingestion boundary when vendor changes or long-lived clients matter.

Bound collection time and resources. Optional analytics must not change command success, block useful work, or hold the process open indefinitely. Avoid retries when offline or blocked. Interpret results by version and environment, accounting for missing and self-selected reporting populations.

## Security and side effects

Treat inputs as untrusted at their boundaries. Use argument-vector subprocess APIs where available; avoid concatenating untrusted values into shell code. Check path and target scope before destructive operations. Request elevated privileges only where needed.

Document filesystem writes, dependencies, and network access. Prefer verifiable releases and auditable dependencies; provide signatures, provenance, or an SBOM appropriate to distribution. Use native credential facilities when available and explain storage and deletion. Avoid exposing secrets through command history, process arguments, logs, or examples.

## Distribution and installers

Choose channels around the audience's environment and dependencies. State supported OS/architecture combinations, runtime requirements, artifact identity, integrity verification, install location, and executable discovery. Support exact versions when reproducibility matters.

Test fresh install, replacement, removal, and failure recovery for supported channels. Preserve user data unless removal is explicitly requested. Do not require a language toolchain solely because the CLI is implemented in it.

For standalone installers, support version and destination selection, detect existing installations, and check prerequisites before changes. Make the installer inspectable and versionable; offer an alternative to immediate remote-script execution. Make interruption recoverable and document cleanup. Do not assume one script is portable across shells and operating systems.

## Versioning and lifecycle

Define the public contract and release policy. Prefer a version scheme compatible with intended channels; use semantic versioning where appropriate. Include build identity separately when useful; keep version inspection local and fast.

Treat changed flags, defaults, exit meanings, machine-output schemas, and configuration semantics as potential breaking changes. Provide a migration or deprecation path. Keep notices out of result data and make schema evolution explicit.

Expect version pinning, upgrades, downgrades, and parallel installations. Define persistent configuration/credential migration and unknown-future-schema behavior. Avoid silently overwriting data a previous version cannot read; make rollback limitations clear.

Respect the installation owner's update mechanism, including package managers and mirrors. Keep update checks optional, bounded, and separate from requested work. Never replace a pinned executable or introduce a breaking update as an incidental side effect. Add automatic updates only when in scope, with verification and recovery.

## Programmatic reuse, when needed

For subprocess consumers, expose a documented invocation and output contract. For a library API, separate reusable operations from process exit, rendering, and global argument parsing. Do not require language bindings or library distribution for every CLI.
