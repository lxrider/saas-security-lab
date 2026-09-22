# Security Concerns

This document tracks the security concerns that emerge from RedRocket's business model and architecture.

A security concern is not necessarily a vulnerability or a confirmed problem. It identifies an area where the design could create a path towards one of RedRocket's three critical security outcomes.

Concrete security problems will be documented when they appear during implementation and observation.

## 1. Customer and tenant boundaries

RedRocket serves multiple customer organizations and centralizes their contacts and campaigns in the same service.

This creates a clear security concern: one organization's data must remain separated from another organization's data.

This concern is directly related to the first critical outcome:

**Unauthorized access to customer data.**

At this stage, the concern exists because of the multi-tenant design. The concrete implementation problems will only be documented when the application is built and observed.

## 2. Identity and privileged capabilities

RedRocket has users with different responsibilities.

Members work with contacts and campaigns. Administrators can also manage users, roles and organization settings.

This creates a second security concern: the application must be able to distinguish who is acting and which privileged capabilities that identity is allowed to use.

This concern is directly related to the second critical outcome:

**Unauthorized privileged control.**

The exact problems will depend on how identity, sessions and authorization are implemented.

## 3. Application and data trust

The RedRocket application needs to read and modify customer data stored in its database.

This creates a trust relationship between the application and the data it can reach.

If the application or one of its components is compromised, the impact should not automatically extend to everything stored or managed by the service.

This concern is directly related to the third critical outcome:

**Broad compromise from a limited foothold.**

The actual blast radius will depend on the implementation choices made during the build.

## Current state

These are the first security concerns visible from the smallest RedRocket architecture.

They are not a complete threat model and they are not a catalogue of controls.

New concerns should only be added when the product or architecture creates a clear reason for them to exist. Concrete security problems will be recorded when they are observed during implementation.
