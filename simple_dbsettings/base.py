from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, ObjectDoesNotExist
from django.core.cache import caches

from .models import BaseSettingsParameter, StringSettingsParameter, IntegerSettingsParameter, FloatSettingsParameter
from .models import BooleanSettingsParameter

SUPPORTED_TYPES_MODELS_MAPPING = {
    str: StringSettingsParameter,
    int: IntegerSettingsParameter,
    float: FloatSettingsParameter,
    bool: BooleanSettingsParameter
}


def sync_parameters():
    """
    Sync SIMPLE_DBSETTINGS_PARAMETERS with dynamic parameters in the DB.
    """
    if hasattr(settings, 'SIMPLE_DBSETTINGS_PARAMETERS'):
        for name, value in settings.SIMPLE_DBSETTINGS_PARAMETERS.items():
            # Dynamic parameters sanity check.
            if type(value) in (list, tuple):
                try:
                    default_value, type_, description = value
                except ValueError:
                    raise ImproperlyConfigured(
                        f"Dynamic parameter '{name}': parameter value attributes list should consist of 3 elements.")
            else:
                raise ImproperlyConfigured(
                    f"Dynamic parameter '{name}': parameter value attributes should be provided as list or tuple.")
            # Check parameter value attributes consistency.
            if type_ not in SUPPORTED_TYPES_MODELS_MAPPING:
                raise ImproperlyConfigured(
                    f"Dynamic parameter '{name}': Unsupported parameter value type used.")
            if default_value is not None:
                try:
                    default_value = type_(default_value)
                except ValueError:
                    raise ImproperlyConfigured(
                        f"Dynamic parameter '{name}': Wrong default value for the type.")
            # Check description.
            if not isinstance(description, str):
                raise ImproperlyConfigured(
                    f"Dynamic parameter '{name}': Description should be a string.")

            try:
                base_parameter_instance = BaseSettingsParameter.objects.get(name=name)
            except ObjectDoesNotExist:
                # Create a new parameter instance.
                SUPPORTED_TYPES_MODELS_MAPPING[type_].objects.create(name=name, description=description)
            else:
                # Sync existing parameter instance.
                # Make sure type was not changed.
                if base_parameter_instance.get_real_instance_class() != SUPPORTED_TYPES_MODELS_MAPPING[type_]:
                    raise ImproperlyConfigured(
                        f"Dynamic parameter '{name}': parameter type change is not allowed.")
                # Update description.
                if base_parameter_instance.description != description:
                    base_parameter_instance.description = description
                    base_parameter_instance.save(update_fields=['description'])


class Config:
    def add_prefix(self, key):
        return "%s%s" % (settings.SIMPLE_DBSETTINGS_CACHE_KEY_PREFIX, key)

    def __init__(self):
        if settings.SIMPLE_DBSETTINGS_CACHE is None:
            self._cache = None
        else:
            self._cache = caches[settings.SIMPLE_DBSETTINGS_CACHE]

    def __getattr__(self, key):
        if self._cache is not None:
            # Take from the cache.
            cache_key = self.add_prefix(key)
            value = self._cache.get(cache_key)
            if value is not None:
                return value
        # Take from the DB.
        try:
            base_parameter_instance = BaseSettingsParameter.objects.get(name=key)
        except ObjectDoesNotExist:
            pass
        else:
            parameter_instance = base_parameter_instance.get_real_instance()
            if parameter_instance.value is not None:
                if self._cache is not None:
                    # Put to the cache.
                    cache_key = self.add_prefix(key)
                    self._cache.add(cache_key, parameter_instance.value)
                return parameter_instance.value
        # Take default value from settings.
        if key in settings.SIMPLE_DBSETTINGS_PARAMETERS and \
                settings.SIMPLE_DBSETTINGS_PARAMETERS[key][0] is not None:  # Default value.
            return settings.SIMPLE_DBSETTINGS_PARAMETERS[key][0]
        raise AttributeError(key)

    def __dir__(self):
        return list(set(list(settings.SIMPLE_DBSETTINGS_PARAMETERS.keys()) + list(
            BaseSettingsParameter.objects.values_list('name', flat=True))))
