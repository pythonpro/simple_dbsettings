from django.utils.functional import LazyObject

__version__ = '0.0.1'
__doc__ = 'Django Simple DB Settings app'

default_app_config = 'simple_dbsettings.apps.SimpleDbsettingsConfig'


class LazyConfig(LazyObject):
    def _setup(self):
        from .base import Config
        self._wrapped = Config()


config = LazyConfig()
