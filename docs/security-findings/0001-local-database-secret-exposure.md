# SF-0001: Local database secret exposure

## Status

Treated

## Context

Django requires a PostgreSQL credential to connect to the RedRocket database.

During initial setup, the password was temporarily placed directly in
application configuration and entered as a literal value in command-line and
SQL commands.

Depending on the client configuration, such values may remain in shell or
database-client command history.

## Security implication

The implementation introduced a database credential that can provide direct
access to application data outside normal application authorization controls.

RedRocket therefore requires a minimal secret-handling mechanism.

This does not justify introducing a dedicated secret-management platform yet.

## Security objectives affected

**Preserve customer boundaries**

A leaked database credential could allow direct access to customer data outside
the application's tenant-isolation and authorization controls.

**Limit the impact of compromise**

Compromise of an application or development secret should not automatically
provide unnecessary access to the underlying data store.

## Attacker objective

Obtain database credentials to access RedRocket data directly.

## Finding

The database password must not be stored in source code or passed as a literal
value in commands that may be retained in command history.

## Treatment

Introduce the minimum secret-handling mechanism required for local development:

- read the database password from the runtime environment
- store local values in a gitignored `.env`
- restrict local file permissions
- provide a non-secret `.env.example`
- avoid placing secret values directly in shell or SQL commands
- set PostgreSQL passwords interactively using `\password`
- rotate any credential that has been exposed

## Evidence

- no database password is present in tracked files
- `.env` is ignored by Git
- `.env` permissions are restricted locally
- PostgreSQL passwords are set interactively rather than embedded in SQL commands
- no real database password appears in documented shell commands
- Django fails if `POSTGRES_PASSWORD` is not provided
- the application connects successfully when the variable is loaded
