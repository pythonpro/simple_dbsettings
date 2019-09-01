=============================
Django Simple DB Settings app
=============================

Django Simple DB Settings is a simple Django app for storing dynamic settings parameter values in the DB.

It supports sting, integer, float and boolean parameter values.
Also it optionally supports caching.

Quick start
-----------
0. Install the app::

    pip install git+https://github.com/pythonpro/simple_dbsettings.git
1. Add "simple_dbsettings" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'simple_dbsettings',
    ]

2. Add app-specific settings to the settings.py::

    SIMPLE_DBSETTINGS_PARAMETERS = {
    'param_1': (5, int, ''),  # No description provided.
    'param_2': (56, int, 'Parameter 1 description'),
    'param_3': (5.6, float, 'Parameter 3 description'),
    'param_4': (True, bool, ''),
    'param_5': [None, str, 'Parameter 5 description']  # No default value.
    }
    # Put here Django cache name or None for disabling cache usage.
    SIMPLE_DBSETTINGS_CACHE = 'default'
    SIMPLE_DBSETTINGS_CACHE_KEY_PREFIX = 'simpledbsettings'


3. Run ``python manage.py migrate`` to apply all existing migrations.

4. Start the development server and visit http://127.0.0.1:8000/admin/simple_dbsettings/basesettingsparameter/ for editing dynamic settings parameters.

5. Access dynamic settings parameters in the code::

    from simple_dbsettings import config
    print(config.param_1)

6. Access dynamic settings parameters in the templates:
    * Put ``'simple_dbsettings.context_processors.config'`` to the list of context processors in the settings.py
    * Assess the parameters in the templates like this::

        {{ simple_dbsettings.param_1 }}
