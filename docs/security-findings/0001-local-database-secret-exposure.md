## Context

Django requires a PostgreSQL credential to connect to the RedRocket database.

During initial setup, the password was temporarily placed directly in
application configuration and entered as a literal value in command-line and
SQL commands.

Depending on the client configuration, such values may remain in shell or
database-client command history.

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