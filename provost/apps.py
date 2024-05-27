from django.apps import AppConfig


class ProvostConfig(AppConfig):
    name = "provost"
    default_auto_field = "django.db.models.AutoField"

    def ready(self):
        pass
