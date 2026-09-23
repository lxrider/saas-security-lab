# Development

This document describes the minimum local development environment required to work on RedRocket.

The objective is to keep the setup simple, reproducible and easy to understand.

## Development environment

RedRocket currently requires:

- Linux
- Python
- Django
- PostgreSQL
- Git

On Windows, WSL2 can be used as the Linux development environment.

The project does not currently require Docker, containers, a reverse proxy or any remote development infrastructure.

## Clone the repository

```bash
git clone https://github.com/lxrider/saas-security-lab.git
cd saas-security-lab
```

GitHub CLI can also be used:

```bash
gh repo clone lxrider/saas-security-lab
cd saas-security-lab
```

## Python environment

Create a local virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Verify Django:

```bash
python -m django --version
```

## PostgreSQL

PostgreSQL must be available locally.

On Debian or Ubuntu:

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo service postgresql start
```

Create the development database and user:

```bash
sudo -u postgres psql
```

Then:

```sql
CREATE USER redrocket;
\password redrocket
CREATE DATABASE redrocket OWNER redrocket;
\q
```

PostgreSQL prompts for the password interactively.

Do not place database passwords directly in shell commands or SQL commands that may be retained in command history.

Test the connection:

```bash
psql -h localhost -U redrocket -d redrocket
```

Enter the password interactively when prompted.

## Application configuration

Local application configuration is provided through environment variables.

Create the local environment file from the provided example:

```bash
cp .env.example .env
chmod 600 .env
```

Generate a local Django secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the generated value into `.env` together with the local PostgreSQL
configuration:

```text
POSTGRES_DB=redrocket
POSTGRES_USER=redrocket
POSTGRES_PASSWORD='replace-with-your-local-password'
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

DJANGO_SECRET_KEY='replace-with-your-generated-secret-key'
```

The `.env` file contains local secrets and must not be committed to the repository.

Because the file is loaded by the shell, secret values should remain quoted so
characters generated in passwords or Django keys are not interpreted by Bash.

Load the variables into the current shell before running Django:

```bash
set -a
source .env
set +a
```

`set -a` automatically exports variables loaded from `.env` so they are available to the Django process.

The tracked `.env.example` file documents the required variables but must never contain real credentials or application secrets.

## Database migrations

Once the Django project is configured, verify the application configuration:

```bash
python manage.py check
```

Apply the existing database migrations:

```bash
python manage.py migrate
```

When the data model changes, create the corresponding migration:

```bash
python manage.py makemigrations
python manage.py migrate
```

New migration files must be committed to the repository.


## Tests

Django creates a temporary PostgreSQL database when running the test suite.

For local development only, the `redrocket` PostgreSQL role therefore needs
permission to create that temporary database:

```bash
sudo -u postgres psql
```

Then:

```sql
ALTER ROLE redrocket CREATEDB;
\q
```

Run the tests with:

```bash
python manage.py test
```

`CREATEDB` is a local development requirement for this setup. It must not be
interpreted as a desired production privilege for the application identity.

## Run RedRocket

Start the Django development server:

```bash
python manage.py runserver
```

The application should then be available at:

```text
http://127.0.0.1:8000/
```

## Current development target

The first working slice is intentionally small:

```text
Organization
    ↓
User
    ↓
Login
    ↓
Contacts
```

The objective is not to build all RedRocket features at once.

The first milestone is to create enough real application behavior to test whether tenant boundaries and authorization are correctly preserved.

## Development principle

Keep the environment and implementation as small as possible.

Before adding a new tool, dependency or infrastructure component, ask:

> What concrete RedRocket problem requires this?

If there is no concrete answer, do not add it.
