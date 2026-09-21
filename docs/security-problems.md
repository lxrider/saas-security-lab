# Security Problems

This document tracks the security problems that appear as RedRocket evolves.

The goal is not to solve them immediately.

For now, I only want to understand:

- where the problem comes from
- what part of the product creates it
- what could happen if the assumption fails

Controls and technologies will come later.

The list will grow with the product.

## SP-001: Cross-tenant data exposure

### Appears when

RedRocket becomes a multi-tenant application.

Multiple customer organizations share the same platform.

### Problem

A user from Organization A could potentially access data belonging to
Organization B.

### Why it matters

Tenant isolation is one of the fundamental security properties of the product.

A failure here could expose customer data across organizations.

---

## SP-002: User impersonation

### Appears when

RedRocket introduces users.

### Problem

The application needs a reliable way to determine who is interacting with it.

If identity cannot be trusted, someone could act as another user.

### Why it matters

Most later access decisions depend on knowing who the user actually is.

---

## SP-003: Unauthorized actions

### Appears when

Different users have different responsibilities.

### Problem

Knowing who a user is does not tell RedRocket what that user is allowed to do.

A user could potentially perform actions outside their expected privileges.

### Why it matters

Administrative or sensitive actions should not be available to every user.

---

## SP-004: Customer data exposure

### Appears when

RedRocket stores customer contacts.

### Problem

Customer-owned information could be accessed by someone who should not see it.

### Why it matters

Customers trust RedRocket with names, email addresses and other information.

Confidentiality is therefore a direct business requirement.

---

## SP-005: Unauthorized or incorrect data modification

### Appears when

Users can create or modify contacts and campaigns.

### Problem

Customer data could be changed intentionally or accidentally in a way that
RedRocket should not accept.

### Why it matters

Customers need to be able to trust the correctness of the data stored in
the platform.

---

## SP-006: Data loss or service unavailability

### Appears when

Customers depend on RedRocket to store and access their data.

### Problem

Data or application functionality could become unavailable.

### Why it matters

A service that customers cannot use no longer provides its expected business
function.

---

## SP-007: Untrusted client input

### Appears when

A browser starts sending information to the RedRocket application.

### Problem

The application cannot assume that requests received from the browser are
valid, expected or harmless.

A user controls the client side of this trust boundary.

### Why it matters

Unexpected or malicious input may influence application behaviour or data.

---

## SP-008: Application to database trust

### Appears when

The RedRocket application connects to the database.

### Problem

The database must decide whether the application is allowed to connect and
what it is allowed to do.

The application also needs some way to prove its identity to the database.

### Why it matters

Compromise or misuse of this relationship could expose or modify all data
accessible to the application.

---

## SP-009: Excessive database privileges

### Appears when

The application receives permissions on the database.

### Problem

The application may have more database access than it actually needs.

### Why it matters

If the application is compromised, unnecessary privileges could increase the
impact.

---

## SP-010: Database exposure

### Appears when

A database becomes part of the technical architecture.

### Problem

The database could potentially become reachable by systems or users that
should never communicate with it directly.

### Why it matters

Direct access could bypass application-level security decisions.

---

## Current state

These problems have been identified.

They have not been solved yet.

That is intentional.

The next design and implementation steps will probably introduce new security
problems, which will be added here before deciding how to address them.
