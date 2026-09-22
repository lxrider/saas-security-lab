# Architecture Foundations

## Starting from nothing

RedRocket starts with one simple idea:

> a customer uses a service and trusts it with data.

Before choosing a framework, a cloud provider or a security product, I want to
understand what this simple relationship already implies. At this point there is
no AWS architecture, no container platform, no CI/CD pipeline and no security
tooling.

There is only a business need and a system that has to satisfy it.

## The first relationship

The smallest possible view of RedRocket is:

```mermaid
flowchart LR
    C["Customer"] --> R["RedRocket"]
    R --> D["Customer data"]
