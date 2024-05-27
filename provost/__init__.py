"""
Implementation of per object permissions for Django.
"""

import django

if django.VERSION < 5:
    default_app_config = "provost.apps.ProvostConfig"
