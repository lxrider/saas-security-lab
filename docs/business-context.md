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

## Think like the attacker first

The interesting question is not:

"What can I break?"

It is:

"What would an attacker want from RedRocket, and what could they use to get there?"

Before listing vulnerabilities, I want to understand what an attacker would actually
try to achieve.

An attacker does not care that a system has "a vulnerability" in the abstract.
They care about the effect they can create by compromising it.

The same logic exists outside cybersecurity: the value of a target comes from the
impact of taking control of it, disrupting it or using it against something else.

So for RedRocket, I start with attacker objectives.

### Steal customer data

Possible objectives:

- access contact databases
- access another tenant's data
- extract personal information
- steal API credentials or tokens

### Take control of privileged access

Possible objectives:

- compromise a customer administrator
- compromise an internal support account
- obtain production access
- steal cloud or application credentials

### Abuse the platform

Possible objectives:

- use the platform to send malicious content
- impersonate a customer
- abuse APIs
- create fraudulent accounts or campaigns

### Disrupt the business

Possible objectives:

- make the service unavailable
- destroy or corrupt customer data
- block legitimate users
- increase operational costs

### Compromise the software supply chain

Possible objectives:

- inject malicious code
- compromise CI/CD
- tamper with dependencies
- reach production through the build process

### Stay invisible

Possible objectives:

- avoid detection
- remove or alter evidence
- maintain persistence
- make incident reconstruction difficult

These objectives will later become inputs for the threat model.

## Constraint

RedRocket is a small company.

Security cannot depend on dozens of specialists or a huge SOC.

Controls should be understandable, maintainable and proportionate to the risk.

## First principle

Security starts with understanding the business first:

what matters, what is at stake, the systems that support it, the risks,
the constraints and, above all, the people who rely on them.
