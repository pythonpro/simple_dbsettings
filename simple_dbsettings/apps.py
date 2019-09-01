from django.apps import AppConfig


class SimpleDbsettingsConfig(AppConfig):
    name = 'simple_dbsettings'
    verbose_name = 'Dynamic settings'

    def ready(self):
        from .base import sync_parameters
        sync_parameters()
