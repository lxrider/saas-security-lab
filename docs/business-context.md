# Business Context

## The problem

Small B2B teams often manage customer information across spreadsheets, shared files and disconnected tools.

This makes it harder to:

* keep customer information in one place
* share it safely between team members
* know who can access or modify it
* prepare customer engagement campaigns consistently

RedRocket Engage 🚀 provides a shared workspace where an organization can manage its users, contacts and campaigns.

## The value

RedRocket creates value by centralizing customer information and making it available to the people who need it.

A customer therefore relies on RedRocket to:

* store customer information
* make it available to authorized users
* preserve the integrity of that information
* keep one organization's data separate from another

The product becomes part of the customer's business operations.

## The trust created by the product

By using RedRocket, a customer gives the service access to business data and business capabilities.

This creates several expectations:

* another customer must not be able to access its data
* unauthorized users must not gain control over privileged functions
* a compromise of one part of the service should not unnecessarily expose everything else

These expectations define the first security scope of the lab.

## Critical security outcomes

For the MVP, RedRocket focuses on three outcomes that should not be possible.

### 1. Unauthorized access to customer data

A user from one organization must not be able to access data belonging to another organization.

### 2. Unauthorized privileged control

An attacker must not be able to obtain or abuse administrative capabilities.

### 3. Broad compromise from a limited foothold

Compromising one part of RedRocket should not unnecessarily provide access to the rest of the application or its data.

These are not intended to represent every possible SaaS threat.

They are the first risks derived from the business value and trust model of RedRocket.

## Security approach

The lab does not start from a framework or a predefined list of controls.

It starts from the business problem, the value delivered by the product and the trust placed in it.

From there, we identify where the design creates paths toward the critical outcomes above.

The process is:

**Understand → Sketch → Identify problems → Build → Observe → Iterate**
