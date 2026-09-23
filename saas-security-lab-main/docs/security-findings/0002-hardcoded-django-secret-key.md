# SF-0002: Hardcoded Django secret key

## Status

Treated

## Context

The Django project was created with a generated `SECRET_KEY` stored directly in
`config/settings.py`.

Unlike the PostgreSQL password discovered in SF-0001, this secret was introduced
automatically by the Django project template rather than manually during database
configuration.

The implementation therefore introduced a second application secret:

```text
Django
   ↓
SECRET_KEY
   ↓
Cryptographic signing
```

## Security implication

Django uses `SECRET_KEY` as a root secret for cryptographic signing.

If the key is available in source control, anyone with access to the repository
can obtain it.

The impact depends on which Django features rely on signing, but disclosure can
undermine security properties of signed values and tokens as the application
evolves.

The key must therefore be treated as an application secret rather than ordinary
configuration.

This does not justify introducing a dedicated secret-management platform.

The minimal secret-handling mechanism already introduced for SF-0001 is sufficient
for the current local development environment.

## Security objectives affected

**Preserve authorized control**

A compromised signing key could undermine mechanisms used to establish or verify
trusted application state.

**Limit the impact of compromise**

Access to the source code should not automatically provide access to application
secrets.

## Attacker objective

Obtain the application's signing secret and use it to forge or manipulate values
that RedRocket expects Django to authenticate cryptographically.

## Finding

`SECRET_KEY` must not be stored directly in tracked application configuration.

## Treatment

Reuse the minimum local secret-handling mechanism introduced by SF-0001:

- remove the hardcoded `SECRET_KEY` from `config/settings.py`
- read the key from the runtime environment
- store the local value in the gitignored `.env`
- document `DJANGO_SECRET_KEY` in `.env.example` without providing a real key
- keep local `.env` permissions restricted
- rotate the key that was exposed in source code
- fail explicitly if `DJANGO_SECRET_KEY` is not provided

Example application configuration:

```python
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
```

## Evidence

- no Django secret key is present in tracked files
- `.env` remains excluded from Git
- `.env.example` contains only the variable name or a non-secret placeholder
- Django reads `DJANGO_SECRET_KEY` from the runtime environment
- Django fails to start if `DJANGO_SECRET_KEY` is missing
- the previously tracked key is no longer used by the application
- `python manage.py check` succeeds when the runtime secret is provided
