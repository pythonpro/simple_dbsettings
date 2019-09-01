import sys

from django.apps import AppConfig


class SimpleDbsettingsConfig(AppConfig):
    name = 'simple_dbsettings'
    verbose_name = 'Dynamic settings'

    def ready(self):
        if 'migrate' not in sys.argv and 'makemigrations' not in sys.argv:  # A hack, to improve.
            from .base import sync_parameters
            sync_parameters()
