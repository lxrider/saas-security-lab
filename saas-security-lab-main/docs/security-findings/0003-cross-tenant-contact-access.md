# SF-0003: Cross-tenant contact access

## Status

Treated

## Observation

The first contact detail flow has been implemented and tested.

Alice belongs to Organization A.

Contact B belongs to Organization B.

While authenticated as Alice, requesting the direct URL for Contact B returns
the contact successfully.

Tenant ownership is therefore not enforced on the contact detail lookup.

## Vulnerability

The contact detail view retrieves a contact by its identifier only.

Authentication succeeds, but authorization does not verify that the requested
contact belongs to the authenticated user's organization.

This allows an authenticated user to access contact data belonging to another
tenant.

## Security objective violated

**Preserve customer boundaries**

## Attacker objective achieved

Access data belonging to another customer organization.

## Impact

Cross-tenant disclosure of customer data.

## Treatment

The contact detail lookup is now scoped to both:

- the requested contact identifier
- the authenticated user's organization

The application no longer retrieves tenant-owned contacts by identifier alone.

The lookup now preserves the expected tenant boundary.

## Evidence

Before treatment:

```text
Alice (Organization A)
→ Contact B (Organization B)
→ HTTP 200
```

After treatment:

```text
Alice (Organization A)
→ Contact B (Organization B)
→ HTTP 404
```

An automated Django test now verifies that an authenticated user cannot access
a contact belonging to another organization.

Test result:

```text
Ran 1 test
OK
```