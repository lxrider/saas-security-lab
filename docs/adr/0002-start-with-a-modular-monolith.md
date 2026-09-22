# ADR-0002: Start with a modular monolith

## Status

Accepted

## Context

The first RedRocket MVP is intentionally small.

It contains:

- organizations
- users
- contacts
- campaigns

The objective is to understand the product, preserve the first security objectives and observe where concrete vulnerabilities appear without introducing distributed complexity too early.

A microservices architecture would immediately create additional deployable units, network communication and trust relationships before the product gives us a reason to need them.

At the same time, RedRocket is intended to evolve. New capabilities may appear as customer needs and market expectations grow.

The first architecture should therefore remain simple without turning the application into a tightly coupled monolith that is difficult to evolve.

## Decision

The first RedRocket version will be built as a **modular monolith**.

It will:

- run as one deployable application
- use one database
- keep clear internal boundaries between the main business capabilities
- avoid distributed infrastructure until a concrete product or operational need appears

The initial modules are expected to reflect the current product:

- identity and users
- contacts
- campaigns

These are code boundaries, not network boundaries.

## Why not microservices?

RedRocket does not need them yet.

Introducing microservices now would immediately create additional concerns around:

- service-to-service communication
- service identity
- authentication and authorization between services
- network exposure
- secrets
- deployment coordination
- observability
- additional trust boundaries

Those concerns are real, but there is no reason to create them before the product or its operation requires them.

A growing number of features alone is not sufficient reason to introduce microservices.

## Why keep internal module boundaries?

The application should remain simple to deploy while making its business boundaries visible.

This gives us a way to:

- keep responsibilities understandable
- limit unnecessary coupling
- make access to data and privileged capabilities easier to reason about
- observe which capabilities actually evolve independently
- prepare for a future extraction without designing distributed services in advance

The objective is not to predict future microservices.

It is to avoid making future evolution unnecessarily difficult.

## When will this decision be revisited?

The modular monolith will be reconsidered when a concrete constraint appears, for example when:

- a capability needs to scale independently
- workloads become significantly different
- deployment cycles need to be separated
- failures need stronger isolation
- teams need independent ownership
- a security boundary would benefit from stronger isolation

If one of these constraints becomes real, the relevant capability may be extracted and the decision will be documented in a new ADR.

## Consequences

The first architecture stays small and understandable.

RedRocket has one deployable application and one database, but its main business capabilities remain separated in the code.

This lets the lab focus on the current security objectives and on concrete vulnerabilities that appear during implementation.

If RedRocket later evolves towards distributed services, the new communication paths, trust relationships and operational constraints will become part of the architecture and security work at that time.
