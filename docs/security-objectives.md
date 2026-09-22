# Security Objectives

RedRocket's first security objectives are derived from the value the product is meant to create.

They describe what must remain true for that value to be preserved.

They are not vulnerabilities, implementation problems or security controls.

## 1. Preserve customer boundaries

RedRocket centralizes customer information and makes it available to members of an organization.

For that value to remain trustworthy, one organization's data must remain separated from another organization's data.

**Security objective**

> Customer data remains accessible to the right organization and isolated from other organizations.

**Critical failure outcome**

> Unauthorized access to customer data.

## 2. Preserve authorized control

RedRocket allows users to work with contacts and campaigns, while administrators can also manage users, roles and organization settings.

For those capabilities to remain trustworthy, privileged actions must stay under authorized control.

**Security objective**

> Privileged capabilities remain available only to identities that are allowed to use them.

**Critical failure outcome**

> Unauthorized privileged control.

## 3. Limit the impact of compromise

RedRocket concentrates customer data and business operations in one service.

That concentration creates value, but it can also concentrate impact.

A limited compromise should therefore not automatically provide unnecessary access to the rest of the application or its data.

**Security objective**

> The impact of a compromise remains proportionate to the component or capability that was compromised.

**Critical failure outcome**

> Broad compromise from a limited foothold.

## How these objectives are used

These objectives guide the rest of the lab.

Architecture and implementation choices are examined when they can affect one of them.

The sequence is:

```text
Business value
    ↓
Security objective
    ↓
Architecture or implementation
    ↓
Concrete security problem
    ↓
Treatment
    ↓
Evidence
```

The lab does not attempt to model every possible SaaS threat.

The scope stays deliberately limited to these three objectives until the product creates a clear reason to extend it.
