# django-provost

The eventual succesor to Django-Gaurdian, WIP

#### Disclaimer

> This project is a very fresh WIP and not yet ready for production,
> so unready, in fact, that there is not yet any code!
>
> This entire Readme is bs

### Documentation

Documentation is non-existent

### Requirements

we have no idea yet

## Installation

### Dev Installation

1. clone repo
2. create a venv

```sh
# inside `django-provost/` run

$ > py -m venv venv # windows
$ > python3 -m venv venv # linux/mac

$ > pip install -r requirements.txt

```

### App installation

to install `django-provost` simply run:

```sh
# this does not work yet as provost is not yet available from pipy
$ > pip install django-provost
```

## Configuration

We need to hook `django-provost` into our project.

1. Put `provost` into your `INSTALLED_APPS` at settings module:

```
INSTALLED_APPS = (
 ...
 'provost',
)
```

2. Add extra authorization backend to your `settings.py`:

```
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
    'provost.backends.ObjectPermissionBackend',
)
```

3. Create `provost` database tables by running:

```
python manage.py migrate
```

### Usage

just dont use this yet

# Gameplan for django-provost

[djang-guardian docs](https://django-guardian.readthedocs.io/en/stable/overview.html)

## Features

- support for DRF and django-ninja
- support pydantic

- object level permisisons
- model level permissions
- view level permissions

- implement a simple interface for checking "is x allowed to access y"
- permissions will cascade from most specific to least (object > model > view)

## API

- Adding permissions
- checking permissions
- removing permissions

### Guardian features to include

- AnonymousUser support
- Decorators
- Django’s admin integration

### Config

- basic setup
- PROVOST_RAISE_403
- PROVOST_RENDER_403
- PROVOST_TEMPLATE_403
- ANONYMOUS_USER_NAME
- PROVOST_GET_INIT_ANONYMOUS_USER
- PROVOST_GET_CONTENT_TYPE
- PROVOST_AUTO_PREFETCH
- PROVOST_USER_OBJ_PERMS_MODEL
- PROVOST_GROUP_OBJ_PERMS_MODEL
