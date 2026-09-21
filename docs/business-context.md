# Business Context

Before choosing AWS services or security tools, I want to understand what
I am actually trying to protect.

## RedRocket Engage 🚀

RedRocket Engage is a fictional European B2B SaaS application.

Companies use it to manage contacts and prepare simple marketing campaigns.

The product stays intentionally small.

That's where this lab starts.

## Product

Each customer has its own organization.

Inside an organization, users can:

- manage contacts
- create campaigns
- manage users and roles

For now, campaigns are prepared but not actually sent.

No real email delivery yet. That's probably a topic for a future lab.

## Users

### Customer users

They work with contacts and campaigns inside their own organization.

### Customer administrators

They can also manage users, permissions and organization settings.

At this point, that is enough to create different levels of access inside
the same customer organization.

## What matters

The platform only works as a business if customers can trust it.

The first expectations are simple:

- customer data must remain confidential
- customers must remain isolated from each other
- important data must not be modified unexpectedly
- privileged actions must be controlled
- the service should remain available

These requirements already exist before choosing any security technology.

## Crown jewels

### Customer data

Contacts and other information customers trust RedRocket with.

Names, email addresses and other customer-owned information have value
because customers expect RedRocket to protect them.

### Tenant isolation

A customer must never be able to access another customer's data.

This is one of the most important properties of a multi-tenant application.

### Administrative accounts

Administrators can perform actions that normal users cannot.

Compromising one of these accounts could therefore have a larger impact.

### Service availability

Customers need to be able to access and use the service.

A platform that cannot be used no longer provides its business function.

## Think like the attacker first

The interesting question is not:

> "What can I break?"

It is:

> "What would an attacker want from RedRocket, and what could they use to get there?"

Before listing vulnerabilities, I want to understand what an attacker would
actually try to achieve.

An attacker does not care that a system has "a vulnerability" in the abstract.

They care about the effect they can create by compromising it.

So for the current version of RedRocket, I start with very simple attacker
objectives.

### Steal customer data

An attacker may want to:

- access customer contacts
- access another tenant's data
- extract personal information

### Take control of an account

An attacker may want to:

- compromise a customer user
- compromise a customer administrator
- use their permissions to access or modify data

### Abuse the product

An attacker may want to:

- impersonate a legitimate user
- create or modify campaigns
- manipulate customer data
- abuse privileged functionality

### Disrupt the service

An attacker may want to:

- make the service unavailable
- destroy or corrupt customer data
- prevent legitimate users from working

These objectives are intentionally basic.

As RedRocket gains new capabilities, new attacker objectives and attack paths
will appear.

They will be added when the product gives us a reason to add them.

## Constraint

RedRocket should remain small enough to understand.

Security cannot depend on adding complexity faster than the product itself.

Controls should stay human, understandable, maintainable and proportionate
to the risk.

## First principle

Security starts with understanding the business first:

what matters, what is at stake, the systems that support it, the risks,
the constraints and, above all, the people who rely on them.
