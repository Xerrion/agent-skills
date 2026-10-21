# Behavioral validation

Select applicable cases for the change. Use existing project tools, temporary data, and fake services where practical. Capture stdout, stderr, status, elapsed time, and side effects separately. Set deadlines so a prompt or network hang fails the check.

| Area | Exercise | Verify |
| --- | --- | --- |
| Discovery | Root/subcommand help; version; unavailable credentials/service | Useful local output; successful explicit help; no setup or mutation |
| Parsing | Unknown option, missing value, conflicting options, flag-like operand, global-option placement | Targeted failure before side effects; no automatic typo execution |
| Results | Success, empty/large result, partial failure | Declared format and exit meaning; completeness distinguishable |
| Streams | Capture stdout and stderr independently | Clean result bytes; diagnostics in the intended channel |
| Terminal | Terminal, redirected output, narrow display; NO_COLOR unset/empty/nonempty; explicit color override | Correct precedence; readable output; no unintended control sequences or animation |
| Interaction | Closed stdin; piped data with terminal output; terminal input with redirected output; unattended mode | No accidental data consumption, implicit consent, or hanging prompt |
| Configuration | Conflicting sources; false/empty/unset; malformed/future schemas | Declared precedence, validation, provenance, compatibility |
| Failures | Permission denial, interruption during work/cleanup, full destination, early-closing output consumer | Truthful status, bounded cleanup, restored terminal, recoverable state, defined broken-pipe behavior |
| Network | Offline, timeout, proxy/bypass, custom CA, failed authentication | Bounded execution, consistent transport, useful redacted errors |
| Mutations | Dry-run, unattended confirmation, timeout after submission, partial batch, repeated invocation | Preview makes no changes; no implicit consent, unsafe replay, or false completion |
| Diagnostics | Sensitive sentinels in flags, config, URLs, fake responses | No secrets in normal/debug output, files, or events |
| Performance | Cold start, help, invalid input, representative workload | Stated budgets and comparable measurement conditions |
| Optional services | Analytics/update endpoint blocked or slow | Requested work and exit semantics remain correct |
| Lifecycle | Install, pinned version, upgrade, downgrade, removal | Artifact identity, ownership, migration, recovery, data retention |

Exercise platform and shell combinations the project claims to support. Include paths with spaces and non-ASCII characters where relevant. Distinguish tested native behavior from mocks and assumptions.

For an existing CLI, compare affected invocations with its previous contract, including examples and known scripts. Verify semantics rather than snapshotting incidental spacing unless spacing is promised. Identify unrun checks; a proposal is not evidence of working implementation.

In reviews, rank verified failures by impact on task completion, data, automation, and compatibility. Attach reproductions and observed output. Keep optional conventions separate from contract failures.
