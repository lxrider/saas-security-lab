# Minimum Viable Product

RedRocket now needs a first version that is small enough to understand and useful enough to observe.

## Product

The MVP contains four objects:

```mermaid
flowchart TD
    O["Organization"]
    O --> U["Users"]
    O --> C["Contacts"]
    O --> P["Campaigns"]
```

Every user, contact and campaign belongs to one organization.

## Users

Two roles are enough for the first version:

- **Member:** works with contacts and campaigns inside the organization.
- **Admin:** can additionally manage users and roles.

## Scope

The first MVP allows a user to:

- log in
- view and manage contacts
- create and manage draft campaigns
- log out

An admin can also:

- view users
- create users
- change user roles

That is enough for now.

## Not yet

The MVP does not include:

- public registration
- email delivery
- public API
- integrations
- billing
- advanced campaign features

Those can appear later if the product gives us a reason to add them.

## Next

Build the smallest working version, then observe where concrete security problems appear.

Significant architecture decisions made along the way are recorded as Architecture Decision Records.
