# Business Context

Security starts with understanding the business first: what problem the product solves, what creates value for the customer and what the customer needs to trust.

## The business problem

Small B2B teams often manage customer information across spreadsheets, shared files and disconnected tools.

This makes it harder to keep customer information in one place, share it between team members and prepare customer engagement campaigns consistently.

RedRocket Engage 🚀 provides a common workspace where an organization can manage its users, contacts and campaigns.

For the first version, campaigns are prepared inside RedRocket but no real email delivery takes place.

## The business value

RedRocket creates value by centralizing customer information and making it available to the people who need it inside the organization.

Each customer has its own organization containing:

- users
- contacts
- campaigns

Two user roles are sufficient for the first version:

- **Members** work with contacts and campaigns.
- **Administrators** can also manage users, roles and organization settings.

The product therefore becomes a shared point of access to customer data and business operations.

## The dependency created by that value

The more useful RedRocket becomes, the more the customer depends on it to preserve the conditions that make the service valuable.

Centralizing information is useful only if the right organization can access it.

Delegating business capabilities is useful only if privileged actions remain under authorized control.

Concentrating data and operations in one service is useful only if a limited security failure does not unnecessarily expose everything else.

These conditions exist before the first technical choice.

They are business-derived security objectives.

See [Security Objectives](security-objectives.md).

## Constraint

RedRocket should remain small enough to understand.

The objective is not to reproduce a production SaaS platform. It is to build enough of the product to make meaningful security problems visible, treat them and demonstrate the result.
