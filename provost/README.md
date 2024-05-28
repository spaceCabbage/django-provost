# Django-Provost

## Quick Start

> This does not yet work, we still need to upload to PYPI

1. Install `django-provost`:

```sh
$ pip install django-provost
```

2. Add `provost` to your `INSTALLED_APPS` settings:

```python
INSTALLED_APPS = [
    ...
    "provost",
]
```

2. Add extra authorization backend to your `AUTHENTICATION_BACKENDS`:

```python
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', # default
    'provost.backends.ObjectPermissionBackend',
]
```

3. Create `provost` tables by running:

```sh
$ python manage.py migrate
```

## Usage

we dont know how to use it yet, If you do, please let us know
