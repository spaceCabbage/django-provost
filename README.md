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

Run these commands to clone, install and setup your local development server

> Note: for those using Mac or Linux you must replace occurences of the `python` commands with `python3`

```sh
# clone the repo
$ git clone https://github.com/spaceCabbage/django-provost.git

# navigate into the project root directory
$ cd django-provost

# create and activate a virtual environment\
# Linux or Mac
$ python3 -m venv venv
$ source venv/bin/activate
# windows
$ python -m venv venv
$ venv\Scripts\activate

# Install dependencies
$ pip install -r requirements.txt

# run migrations
$ python manage.py migrate

# create a superuser account for yourself
$ python manage.py createsuperuser

# Generate fake user, post and comment data
$ python manage.py populate

# And finally
# Run the dev server
$ python manage.py runserver

```

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
