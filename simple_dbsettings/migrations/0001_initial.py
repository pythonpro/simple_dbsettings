from django.db import migrations, models
import django.db.models.deletion
import simple_dbsettings.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseSettingsParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_simple_dbsettings.basesettingsparameter_set+', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'dynamic settings parameter',
                'verbose_name_plural': 'dynamic settings parameters',
            },
        ),
        migrations.CreateModel(
            name='BooleanSettingsParameter',
            fields=[
                ('basesettingsparameter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='simple_dbsettings.BaseSettingsParameter')),
                ('value', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=(simple_dbsettings.models.UpdateCacheMixin, 'simple_dbsettings.basesettingsparameter'),
        ),
        migrations.CreateModel(
            name='FloatSettingsParameter',
            fields=[
                ('basesettingsparameter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='simple_dbsettings.BaseSettingsParameter')),
                ('value', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=(simple_dbsettings.models.UpdateCacheMixin, 'simple_dbsettings.basesettingsparameter'),
        ),
        migrations.CreateModel(
            name='IntegerSettingsParameter',
            fields=[
                ('basesettingsparameter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='simple_dbsettings.BaseSettingsParameter')),
                ('value', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=(simple_dbsettings.models.UpdateCacheMixin, 'simple_dbsettings.basesettingsparameter'),
        ),
        migrations.CreateModel(
            name='StringSettingsParameter',
            fields=[
                ('basesettingsparameter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='simple_dbsettings.BaseSettingsParameter')),
                ('value', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=(simple_dbsettings.models.UpdateCacheMixin, 'simple_dbsettings.basesettingsparameter'),
        ),
    ]
