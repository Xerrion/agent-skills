# Worked examples

These are fictional, self-contained inputs and sample decision summaries. Their
facts are supplied by the examples, not independently verified claims about a
real project. Do not transfer their requirements, numbers, or technology choices
to a different task.

## 1. Derive background processing before selecting infrastructure

### Input

"We need background report generation. Should we add a broker? We average
30 jobs per minute, with a measured mean processing time of 0.2 seconds per job.
We already operate a durable transactional database whose supported work-claim
mechanism has been verified. A job acknowledged as accepted must survive a worker
process restart. Reports can be regenerated safely. Bursts are not measured."

### Sample decision summary

**Decision:** Start by testing database-backed durable jobs and a worker. A new
broker is not yet justified by the supplied requirements. This is a provisional
choice because burst behavior and contention are unknown.

**Basis:** The supplied average work is:

```text
30 jobs/minute * 0.2 seconds/job = 6 seconds of work/minute
Average utilization for one serial worker = 6 / 60 = 10%
```

This estimates average processing demand. It does not establish peak capacity,
queueing delay, database overhead, or a latency guarantee.

**Mechanism:** Acknowledged acceptance must outlive the worker, so persist the job
before acknowledging it. The already supported work-claim mechanism can assign
jobs to workers. Claims need recovery after worker failure; completion and retry
state must be durable. Safe report regeneration, explicitly supplied here, makes
retrying interrupted work acceptable.

**Challenge:** A broker is a credible alternative when measured bursts, delivery
features, or interference with application traffic justify its operational cost.
It should not be rejected merely because it is an extra component.

**Verification:** The utilization arithmetic is derived from supplied figures.
Crash recovery, claim contention, and burst performance have not been tested.
Test interruption after persistence and after claiming; verify accepted jobs
remain recoverable. Revisit the choice if measured demand or required delivery
features exceed the tested database-backed design.

### Why this meets the method

The requirement produces the need for durable state and recoverable work claims.
It does not directly produce a product choice. Missing measurements remain
unknown, and safe retries are not assumed for other kinds of jobs.

## 2. Check a performance bound before recommending a rewrite

### Input

"Can rewriting this endpoint in Rust cut latency in half? A representative trace
shows 40 ms total: 32 ms waiting for storage and 8 ms computation. These are
non-overlapping wall-clock portions. Assume the rewrite only changes computation.
Do not modify the code."

### Sample decision summary

**Decision:** A compute-only rewrite cannot achieve the stated 20 ms target under
the supplied timing model. Analyze the storage path before selecting a remedy.

**Basis and mechanism:** Even eliminating all computation leaves 32 ms:

```text
New latency = 32 ms + 8 ms / compute_speedup
Best possible latency as compute_speedup grows = 32 ms
Maximum overall speedup = 40 / 32 = 1.25x
```

The requested 2x speedup therefore needs reduced or overlapped storage wait, a
changed requirement, or evidence that the timing model is wrong. The calculation
does not establish whether a particular language or implementation reduces
storage work.

**Challenge:** An algorithmic change in either language might reduce the number
of storage operations. Caching might also help, but its suitability depends on
freshness and invalidation requirements that have not been provided. Neither is
yet a verified fix.

**Verification:** The bound is calculated from supplied measurements. No benchmark
or code change was performed. Inspect storage operations and measure a candidate
against the same workload before claiming an improvement. Revisit the conclusion
if measurements show overlapping work, a different bottleneck, or a change that
also reduces storage wait.

### Why this meets the method

The limiting mechanism is established before choosing a language. The conclusion
is about the stated model, not a universal claim against rewrites or Rust.

## 3. Keep necessary complexity instead of optimizing component count

### Input

"Can we remove our event log and just call consumers directly? Three consumers
must recover independently and replay seven days of accepted events without
relying on the producer to regenerate them. Our approved platform already
operates a durable log that provides this retention and independent positions.
Direct calls do not currently persist events anywhere else."

### Sample decision summary

**Decision:** Keep a durable replay mechanism. Removing the existing log in favor
of direct calls alone would violate the supplied recovery and replay constraints.
Keeping the supported log is the default unless a replacement proves a concrete
benefit.

**Basis and mechanism:** Independent replay requires retained event data and an
independent progress position for each consumer. Direct calls alone provide
neither in this stated design. A replacement would still need to implement or
reuse those capabilities.

**Challenge:** A different durable store with per-consumer progress could meet
the same requirements, but fewer named products would not by itself establish
lower maintenance or migration risk. Compare total burden before replacing the
already supported capability.

**Verification:** This is a requirements-based conclusion using supplied platform
capabilities. No recovery test was run. Verify retention configuration and replay
from a saved consumer position before claiming the deployment satisfies the
requirements. Revisit the design if independent replay is no longer required or
a measured alternative meets the same constraints at lower total cost.

### Why this meets the method

The outcome is not predetermined to be a monolith, a database, or fewer services.
A conventional abstraction survives because its behavior is necessary here.
