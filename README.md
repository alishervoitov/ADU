## Django boilerplate

## How to set up project

## How to run project locally bash script (Linux, Mac)

### install requirements

```bash
python3 -m venv env 
source env/bin/activate
pip install -r requirements/production.text
```

### create .env file

```bash
cp .env.example .env
```

### create database

```bash
sudo -u postgres psql
CREATE DATABASE adu_db;
CREATE USER adu_user WITH PASSWORD 'aduPass!123';
ALTER ROLE adu_user SET client_encoding TO 'utf8';
ALTER ROLE adu_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE adu_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE adu_db TO adu_user;
\q
```

### set up .env file with your database credentials

```bash
nano .env
```

### run migrations

```bash
python manage.py migrate
```

### run server

```bash
python manage.py runserver
```

## Pre-commit  must be installed for all projects

```bash
pip install pre-commit
pre-commit install
```


###  For Locale  
#### Barcha tillarga tarjima fayllarini yaratish

- `python manage.py makemessages -l uz`
- `python manage.py makemessages -l cyrl`
- `python manage.py makemessages -l ru`
- `python manage.py makemessages -l en`

#### Yaratilgan tarjima fayllarini kompilatsiya qilish
- `python manage.py compilemessages`

