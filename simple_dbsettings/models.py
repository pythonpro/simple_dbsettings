from django.db import models
from django.conf import settings
from django.core.cache import caches

from polymorphic.models import PolymorphicModel

if settings.SIMPLE_DBSETTINGS_CACHE is None:
    CACHE = None
else:
    CACHE = caches[settings.SIMPLE_DBSETTINGS_CACHE]


class BaseSettingsParameter(PolymorphicModel):
    """
    A polymorphic model for creating different types of dynamic settings parameter models
    by "concrete base model inheritance".

    The primary goal of using this approach is to be able to handle and display
    instances of different models like they belong to the same model.
    """
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

    def parameter_value(self):
        return self.value

    parameter_value.short_description = 'value'

    def parameter_type(self):
        return self.type_str

    parameter_type.short_description = 'type'

    def short_description(self):
        if self.description is None:
            return ''
        else:
            if len(self.description) > 48:
                return self.description[:45] + '...'
            else:
                return self.description

    short_description.short_description = 'description'

    def default_value(self):
        if self.name in settings.SIMPLE_DBSETTINGS_PARAMETERS:
            return settings.SIMPLE_DBSETTINGS_PARAMETERS[self.name][0]
        else:
            return None

    class Meta:
        verbose_name = 'dynamic settings parameter'
        verbose_name_plural = 'dynamic settings parameters'


class UpdateCacheMixin:
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if CACHE is not None:
            # Put to the cache.
            CACHE.add("%s%s" % (settings.SIMPLE_DBSETTINGS_CACHE_KEY_PREFIX, self.name), self.value)


class StringSettingsParameter(UpdateCacheMixin, BaseSettingsParameter):
    """
    Dynamic parameter with string value.
    """
    type_str = 'string'
    value = models.CharField(max_length=256, blank=True, null=True)


class IntegerSettingsParameter(UpdateCacheMixin, BaseSettingsParameter):
    """
    Dynamic parameter with integer value.
    """
    type_str = 'integer'
    value = models.IntegerField(blank=True, null=True)


class FloatSettingsParameter(UpdateCacheMixin, BaseSettingsParameter):
    """
    Dynamic parameter with float value.
    """
    type_str = 'float'
    value = models.FloatField(blank=True, null=True)


class BooleanSettingsParameter(UpdateCacheMixin, BaseSettingsParameter):
    """
    Dynamic parameter with boolean value.
    """
    type_str = 'boolean'
    value = models.BooleanField(blank=True, null=True)
