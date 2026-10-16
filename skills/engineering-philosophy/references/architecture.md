# Architecture Philosophy

Make responsibilities, dependencies, state, and failure boundaries explicit.

Choose structure for the actual system and its constraints. Do not impose a preferred architecture on every project.

Apply these principles to the requested change. Existing design debt does not authorize an unsolicited redesign.

## 1. Follow the Grain

Find the established home for the concept before introducing a new pattern.

Reuse conventions that serve the required behaviour. Do not copy a defect merely because it already exists.

When no suitable pattern exists, introduce the smallest coherent structure and make its responsibility clear.

Choose names that describe the responsibility. A folder name alone does not establish a boundary.

Document a structural decision when its rationale or consequences would otherwise be difficult to recover.

## 2. Strict Layer Direction

Identify the project's intended dependency direction and preserve it.

Business policy should not acquire incidental dependencies on presentation, transport, or storage mechanisms.

Use explicit interfaces or adapters when they protect a real boundary. Do not add them only to imitate a diagram.

Avoid dependency cycles that obscure initialization, ownership, testing, or change impact.

Place shared contracts according to their meaning and ownership. Do not create a miscellaneous shared module merely to silence an import problem.

Layered architecture is one structure, not a universal requirement. Apply the same dependency discipline to modules, plugins, services, and event-driven systems.

## 3. Justifiable Indirection

An abstraction must provide a present benefit.

Valid benefits include policy enforcement, complexity isolation, compatibility, substitution, lifecycle control, and a stable integration boundary.

A forwarding layer can be justified by one of these responsibilities. Forwarding alone is not proof that the layer is unnecessary.

Do not create speculative extension points for hypothetical requirements.

Do not remove a layer before checking its callers, contracts, and intended protection.

Prefer the simplest structure that preserves the required boundary and makes the relevant behaviour understandable.

## 4. Design APIs for the Caller

Design interfaces around the caller's task, not incidental implementation details.

Expose stable domain values where independence from storage, transport, or a vendor is an actual requirement.

Technology-specific adapters may expose technology-specific types. Do not manufacture independence that the component does not promise.

Make transaction ownership explicit.

When several operations must succeed together, preserve the caller's ability to control their shared transaction. A helper must not commit work that belongs to its caller's unit of work.

Describe compatibility, inputs, outputs, side effects, and failure behaviour at public boundaries.

Do not promise implementation interchangeability beyond the contract the system actually supports.

## 5. Atomic Predictability

Separate calculation from external effects where doing so improves clarity and testability.

Make state changes, I/O, time, randomness, and resource ownership visible through the component's contract or dependencies.

Avoid hidden writes and unowned background work.

Define the behaviour of partial failure, cancellation, timeouts, and retries where relevant.

A database transaction does not automatically make external messages or remote calls atomic. Choose an explicit consistency and recovery strategy when operations cross boundaries.

Retries require a policy for duplicate effects. Cleanup requires an owner.

Do not add architectural layers merely to achieve theoretical purity in code whose effects are already clear and controlled.

## 6. Honest Contracts

**One Authoritative Source:** Identify the authoritative owner of each fact and how it may change.

Derived values, caches, materialized views, and replicas are allowed when their purpose is justified.

Define their update, invalidation, freshness, and recovery rules. Do not present them as independent authorities for the same fact.

Model meaningful states explicitly. Avoid parallel flags or fields that can contradict one another without a governing invariant.

Make failure and consistency guarantees part of the interface.

Do not claim immediate consistency, exactly-once effects, or automatic recovery without a mechanism that establishes the claim.

## Application

For a structural change, be able to explain:

- Which responsibility moved or became explicit.
- Which dependencies changed.
- Who owns state and effects.
- What happens on failure.
- Why the additional structure is necessary.

Record material trade-offs. Do not require an architecture document for routine local decisions.
