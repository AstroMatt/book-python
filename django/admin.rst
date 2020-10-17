***********
Admin panel
***********

Customizing
===========
.. code-block:: python

    from django.contrib import admin
    from django.utils.translation import gettext_lazy as _

    admin.site.site_header = _('HabitatOS')
    admin.site.index_title = _('Dashboard')
    admin.site.site_title = _('HabitatOS')

Permissions
===========

Users
-----

Groups
------

Content Types
-------------


Model Admin
===========
* ``admin.ModelAdmin``

Model registering
-----------------
* ``@admin.register(...)``

Admin fields
------------
* readonly_fields
* search (``^``, ``=``, ``@``)
* ordering
* list_filter

Writing own ``list_filter``
---------------------------
.. literalinclude:: src/django-admin-filter.py
    :language: python
    :caption: Writing own ``list_filter``


Model Inlines
=============

StackedInline
-------------

TabularInline
-------------

Extending Admin
===============

Media Class
-----------
.. code-block:: python

    class Media:
        js = [
            'communication/js/email-reply-button.js',
            'communication/js/email-hide-save.js',
        ]
        css = {'all': [
            'communication/css/hide-id-field.css',
            'communication/css/resize-fields.css',
        ]}

ModelAdmin Example
==================
.. literalinclude:: src/django-admin-example.py
    :language: python
    :caption: ModelAdmin Example

``django-import-export``
========================
.. code-block:: console

    $ pip install django-import-export

.. code-block:: python

    # settings.py
    INSTALLED_APPS += ['import_export']

.. code-block:: python

    # <app>/admin.py
    from import_export.admin import ImportExportModelAdmin

    @admin.register(Command)
    class CommandAdmin(ImportExportModelAdmin):
        pass


Grapelli
========

Installation
------------
.. code-block:: console

    $ pip install django-grapelli

* dodanie do INSTALLED_APPS

.. code-block:: python

    INSTALLED_APPS = [
        'grappelli.dashboard',
        'grappelli',
    ]

* dodanie do urls

.. code-block:: python

    from django.conf.urls import url
    from django.conf.urls import include
    from django.contrib import admin


    urlpatterns += [
        url(r'^grappelli/', include('grappelli.urls'), name='grappelli'),
        url(r'^', admin.site.urls, name='admin'),
    ]

Settings
--------
.. code-block:: python

    GRAPPELLI_SWITCH_USER = True
    GRAPPELLI_ADMIN_TITLE = _('HabitatOS')
    GRAPPELLI_INDEX_DASHBOARD = 'habitat.dashboard.aatc.AdminDashboard'
    GRAPPELLI_AUTOCOMPLETE_SEARCH_FIELDS = {
        'auth': {
            'user': ['username__icontains']
        }
    }

.. code-block:: python

    from django.utils.translation import gettext_lazy as _
    from grappelli.dashboard import Dashboard
    from grappelli.dashboard import modules


    class AdminDashboard(Dashboard):

        def init_with_context(self, context):

            # Column 1
            self.children.append(modules.ModelList(
                title=_('Questionnaires - Visible only to you'),
                column=1,
                collapsible=False,
                models=[
                    'habitat.reporting.models.mood.Mood',
                    'habitat.reporting.models.sociodynamics.SociodynamicReport',
                    'habitat.reporting.models.sleep.Sleep']))

            self.children.append(modules.ModelList(
                title=_('Health - Visible only to you'),
                column=1,
                collapsible=False,
                models=[
                    'habitat.health.models.blood_pressure.BloodPressure',
                    'habitat.health.models.urine.Urine',
                    'habitat.health.models.temperature.Temperature',
                    'habitat.health.models.weight.Weight']))

            # Column 2
            self.children.append(modules.ModelList(
                title=_('Communication'),
                column=2,
                collapsible=False,
                models=[
                    'habitat.communication.models.email.Email']))

            self.children.append(modules.ModelList(
                title=_('Reporting - Visible to anyone'),
                column=2,
                collapsible=False,
                models=[
                    'habitat.reporting.models.daily.Daily',
                    'habitat.reporting.models.repair.Repair',
                    'habitat.reporting.models.incident.Incident',
                    'habitat.reporting.models.waste.Waste',
                    'habitat.communication.models.diary.DiaryEntry',
                    'habitat.extravehicular.models.activity.Activity']))

            self.children.append(modules.ModelList(
                title=_('Water - Visible to anyone'),
                column=2,
                collapsible=False,
                models=[
                    'habitat.water.models.technical.TechnicalWater',
                    'habitat.water.models.drinking.DrinkingWater',
                    'habitat.water.models.green.GreenWater']))

            # Column 3
            if context['user'].has_perm('admin.add_user'):
                self.children.append(modules.ModelList(
                    title=_('Administration'),
                    column=3,
                    collapsible=True,
                    models=['django.contrib.*'],
                    css_classes=['grp-closed']))

            self.children.append(modules.LinkList(
                title=_('Shortcuts'),
                collapsible=False,
                column=3,
                children=[
                    {'title': _('Schedule'), 'url': '/api/v1/dashboard/schedule/'},
                    {'title': _('Martian Clock Converter'), 'url': '/api/v1/timezone/martian-standard-time/converter/'},
                    {'title': _('Subjective Time Perception'), 'url': 'http://time.astrotech.io'},
                ]))

            self.children.append(modules.ModelList(
                title=_('Sensors'),
                column=3,
                collapsible=False,
                models=[
                    'habitat.sensors.models.zwave_sensor.ZWaveSensor']))

Template overwrite
------------------
.. code-block:: python

    change_list_template = 'admin/change_list_import_export.html'
    change_list_filter_template = 'admin/filter_listing.html'

Autocomplete
------------

TinyMCE
-------

FileUploader
------------

``list_editable``
-----------------

``date_hierarchy``
------------------
