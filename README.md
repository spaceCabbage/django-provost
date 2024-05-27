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
to install `django-provost` simply run:
```sh
# this does not work yet as provost is not yet available from pipy
pip install django-provost
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
