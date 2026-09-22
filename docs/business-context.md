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

## The trust created by the product

By using RedRocket, customers entrust the service with their data and with the ability to act on that data.

They expect RedRocket to keep their organization separated from other customers, keep privileged functions under authorized control and avoid turning a limited security problem into a compromise of the whole service.

This trust defines the first security scope of the lab.

## Three critical security outcomes

RedRocket is intentionally scoped around **three critical security outcomes**.

They represent the situations we primarily want to prevent during the first iterations.

### 1. Unauthorized access to customer data

**Attacker goal:** access data belonging to another organization.

A user from one organization must not be able to access data belonging to another organization.

---

### 2. Unauthorized privileged control

**Attacker goal:** obtain or abuse administrative capabilities.

Privileged functions must remain under the control of authorized users.

---

### 3. Broad compromise from a limited foothold

**Attacker goal:** turn a limited compromise into wider access.

Compromising one part of RedRocket should not unnecessarily provide access to the rest of the application or its data.

---

These three outcomes do not represent every possible SaaS threat. They deliberately limit the scope so that each risk can be traced from the business need to the design, implementation and evidence that it has been treated.

## From business to security

The lab follows a simple line of reasoning:

```text
Business problem
    ↓
Product value
    ↓
Customer trust
    ↓
Critical security outcome
    ↓
Where does the design make it possible?
    ↓
How should the design or implementation change?
    ↓
Can we demonstrate that the treatment works?
```

The objective is not to start with a security framework or a catalogue of controls.

Security questions are introduced when the product or its architecture creates a reason for them to exist.

## Constraint

RedRocket should remain small enough to understand.

The objective is not to reproduce a production SaaS platform. It is to build enough of the product to make meaningful security problems visible, treat them and demonstrate the result.

The working approach remains:

**Understand → Sketch → Identify problems → Build → Observe → Iterate**
