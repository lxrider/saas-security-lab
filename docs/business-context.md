# Business Context

Before thinking about architecture, cloud services or security controls, I first
need to understand what RedRocket is supposed to do and what actually matters.

## RedRocket Engage 🚀

RedRocket Engage is a fictional European B2B SaaS application. Companies use it
to manage contacts and prepare simple marketing campaigns.

Each customer has its own organization containing:

- users
- contacts
- campaigns

For now, campaigns are only prepared. No real email delivery yet. That's
probably a topic for a future iteration.

## Users

There are two types of users for the first version:

- **Members** work with contacts and campaigns inside their organization.
- **Administrators** can also manage users, roles and organization settings.

That is enough for now.

## What matters

RedRocket only works as a product if customers can trust it. That means:

- customer data stays confidential
- one customer cannot access another customer's data
- important data is not modified unexpectedly
- privileged actions are controlled
- the service remains available

These requirements already exist before choosing any security technology.

## What would an attacker want?

The useful question is not:

> "What can I break?"

It is:

> "What would an attacker want from RedRocket?"

In other words: what are the **attacker's objectives?**

For the current version, they are simple:

- steal customer data
- access another tenant's data
- take control of a user or administrator account
- modify contacts or campaigns
- abuse privileged functionality
- disrupt the service or destroy data

These objectives will evolve with the product. New capabilities will create
new attacker objectives and new security problems.

## Regulatory context

RedRocket operates in Europe, where some customers may be subject to regulations
such as NIS2.

Even if RedRocket itself is not necessarily a regulated entity, customers may
expect their SaaS suppliers to demonstrate appropriate security practices,
particularly around risk management, secure development and supply chain security.

For this lab, NIS2 is not a checklist. It is one more business reason to
understand security early and build it into the product from the beginning.

## Constraint

RedRocket should remain small enough to understand. The goal is not to add
complexity faster than the product itself.

Security controls should stay understandable, maintainable and proportionate
to the problems they are meant to solve.

## First principle

Security starts with understanding the business first: 
- what matters?
- what is at stake?
- what the product does?
- who relies on it?
