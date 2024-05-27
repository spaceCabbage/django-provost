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
