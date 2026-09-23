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

Test the connection:

```bash
psql -h localhost -U redrocket -d redrocket
```

## Application configuration

Local database configuration should be provided through environment variables.

Example:

```bash
export POSTGRES_DB=redrocket
export POSTGRES_USER=redrocket
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
```

Local credentials must not be committed to the repository.

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
