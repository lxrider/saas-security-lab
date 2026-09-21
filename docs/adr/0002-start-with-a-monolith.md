# ADR-0002: Start with a monolith

## Status

Accepted

## Context

The first RedRocket MVP is intentionally small.

It contains:

- organizations
- users
- contacts
- campaigns

The goal is to understand the product and the security problems created by
its architecture without introducing unnecessary complexity.

A microservices architecture would immediately create additional components
and communication between them.

## Decision

The first RedRocket MVP will be built as a monolithic application.

The application logic will run as one deployable unit and use one database.

## Why not microservices?

RedRocket does not need them yet.

Microservices would immediately introduce new questions around:

- service-to-service communication
- service identity
- authentication and authorization between services
- network exposure
- secrets
- additional trust boundaries

Those are real security problems, but there is no reason to create them before
the product needs them.

## Consequences

The first architecture stays small and understandable.

We can focus on the security problems already created by the product.

If RedRocket eventually needs several services, that decision will be reviewed
and the new security problems will be documented.
