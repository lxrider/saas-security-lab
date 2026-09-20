# Business Context

Before choosing AWS services or security tools, I want to understand what
I am actually trying to protect.

## RedRocket Engage

RedRocket Engage is a fictional European B2B SaaS company.

Its product is a small multi-tenant application used by companies to manage
contacts and prepare simple marketing campaigns.

The company is growing and security has mostly been handled by developers
and infrastructure teams when needed.

There is no dedicated security function yet.

That's where this lab starts.

## Product

Each customer has its own organization.

Inside an organization, users can:

- manage contacts
- create campaigns
- manage users and roles
- use the REST API

For now, campaigns are prepared but not actually sent.

## Users

### Customer users

They work with contacts and campaigns inside their own organization.

### Customer administrators

They can manage users, permissions and organization settings.

### Internal support

Support may occasionally need access to investigate customer issues.

That access should be limited and traceable.

### Engineering

Engineers build and operate the platform.

Some actions may require privileged access to production systems.

## What matters

The platform only works as a business if customers can trust it.

The main concerns are:

- customer data must remain confidential
- customers must remain isolated from each other
- privileged access must be controlled
- the service should remain available
- important actions should be traceable
- security incidents should be detectable and understandable

## Crown jewels

### Customer contacts

Names, email addresses and other customer-owned information.

### Tenant isolation

A customer must never be able to access another customer's data.

### Administrative accounts

Compromising an administrator could have a major impact.

### API credentials and secrets

Tokens, credentials and application secrets must remain protected.

### Production access

Privileged access to production systems must be tightly controlled.

### CI/CD pipeline

Compromising the software delivery process could provide a path into production.

## A few obvious risks

- cross-tenant data exposure
- compromised administrator account
- leaked credentials or API tokens
- vulnerable application dependencies
- malicious changes reaching production
- exposed customer data
- service outage
- security incidents that cannot be properly investigated

This is not the threat model yet.

The threat model will come once the first architecture exists.

## Constraint

RedRocket is a small company.

Security cannot depend on dozens of specialists or a huge SOC.

Controls should be understandable, maintainable and proportionate to the risk.

## First principle

Security starts with understanding the business first:

what matters, what is at stake, the systems that support it, the risks,
the constraints and, above all, the people who rely on them.
