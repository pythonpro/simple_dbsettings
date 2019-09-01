from django.contrib import admin

from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter

from .models import BaseSettingsParameter, StringSettingsParameter, IntegerSettingsParameter, FloatSettingsParameter
from .models import BooleanSettingsParameter


@admin.register(StringSettingsParameter)
class StringSettingsParameterAdmin(PolymorphicChildModelAdmin):
    readonly_fields = ['default_value']


@admin.register(IntegerSettingsParameter)
class IntegerSettingsParameterAdmin(PolymorphicChildModelAdmin):
    readonly_fields = ['default_value']


@admin.register(FloatSettingsParameter)
class FloatSettingsParameterAdmin(PolymorphicChildModelAdmin):
    readonly_fields = ['default_value']


@admin.register(BooleanSettingsParameter)
class BooleanSettingsParameterAdmin(PolymorphicChildModelAdmin):
    readonly_fields = ['default_value']


@admin.register(BaseSettingsParameter)
class BaseSettingsParameterAdmin(PolymorphicParentModelAdmin):
    polymorphic_list = True
    list_display = ['name', 'short_description', 'parameter_value', 'default_value', 'parameter_type']
    child_models = [StringSettingsParameter, IntegerSettingsParameter, FloatSettingsParameter, BooleanSettingsParameter]
    list_filter = [PolymorphicChildModelFilter]
