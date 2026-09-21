# Security Problems

This document tracks the security problems that appear as RedRocket evolves.

The goal is not to solve them yet.

For now, I only want to understand what problems are created by the product
and its architecture.

Controls and technologies will come later.

## 1. Tenant isolation

RedRocket serves multiple customer organizations.

A user from one organization must never be able to access data belonging
to another organization.

The moment RedRocket becomes multi-tenant, this problem exists.

## 2. Identity

RedRocket has users.

The application therefore needs to know who is interacting with it.

If that identity cannot be trusted, later access decisions cannot be trusted
either.

## 3. Permissions

Knowing who the user is is not enough.

Different users may be allowed to perform different actions.

RedRocket therefore needs to decide what each user is allowed to do.

## 4. Customer data

Customers trust RedRocket with their data.

That immediately creates three basic problems:

- data must not be exposed to the wrong people
- data must not be modified unexpectedly
- data must remain available when needed

These requirements exist because of the product itself, not because of a
security framework.

## 5. Untrusted input

The browser sends information to the application.

The application cannot assume that everything it receives is valid,
expected or harmless.

The user controls one side of this relationship.

## 6. Application to database trust

The application needs to read and modify data stored in the database.

That creates another trust relationship.

The database must decide whether the application can connect and what it
can do.

If this relationship is abused, customer data may be exposed, modified or
destroyed.

## Current state

These are the security problems visible in the smallest RedRocket
architecture.

They are not solved yet.

As the product grows, new components and relationships will create new
problems.

They will be added here when they actually appear.
