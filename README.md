# SaaS Security Lab

A hands-on project to understand how security fits into a modern SaaS environment.

**RedRocket Engage** is a small fictional multi-tenant B2B SaaS application. I start from a blank page, build the smallest useful product, observe the security problems that appear, and improve it step by step.

If you just want to know what can be broken today, run a penetration test. Here, the goal is to understand why security problems appear in the first place and how security can be built into the product from the beginning.

> **This is Security by Design.**

## The product

RedRocket Engage stays intentionally small. A customer organization can:

- manage users
- manage contacts
- create campaigns

No real email delivery yet. That's probably a topic for a future iteration.

The application is just complex enough to expose real SaaS security problems without spending weeks building the product itself.

## Approach

The idea is simple: start from the foundations and avoid jumping directly to security tools, frameworks or advanced cloud architecture.

First, understand:

- what we are building
- who will use it
- what data it will handle
- what the smallest architecture looks like
- what each component has to trust
- what security problems already appear

External requirements may also shape the product. Customers subject to regulations such as **NIS2**, for example, may expect security requirements from their SaaS providers.

The first security problems are visible before writing code. Building the product will create new questions, and those questions will drive the next security decisions.

I'd rather understand the first 50 cm properly than jump straight to 1.5 m without understanding what is underneath.

```mermaid
flowchart LR
    A["Understand"] --> B["Sketch"]
    B --> C["Identify problems"]
    C --> D["Build"]
    D --> E["Observe"]
    E --> F["Iterate"]
    F --> B
```

## What I want to explore

As RedRocket grows, different security topics should appear naturally:

- **Product:** multi-tenancy, authentication, authorization, RBAC, API security
- **Platform:** cloud security, IAM, secrets, vulnerabilities, CI/CD
- **Operations:** logging, detection, incident response

This is not a checklist. A topic should appear because the product or architecture creates a real problem that needs to be understood.

## Current status

The business context, architecture foundations and first MVP are now defined. The next step is to make the first architecture decisions and start building RedRocket.

Project documentation:

- [Business Context](docs/business-context.md)
- [Architecture Foundations](docs/architecture-foundations.md)
- [Minimum Viable Product](docs/mvp.md)
- [Security Problems](docs/security-problems.md)
- [Roadmap](ROADMAP.md)
- [Architecture Decisions](docs/adr/)

## Build. Break. Understand. Rebuild better.
