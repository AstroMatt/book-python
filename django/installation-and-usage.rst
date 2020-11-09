************************
Installation and Running
************************

Instalacja
==========
.. code-block:: console

    $ pip install django

Starting new project
====================
.. code-block:: console

    $ django-admin startproject addressbook

    $ python manage.py migrate

    $ python manage.py createsuperuser
    Username (leave blank to use 'admin'): mark.watney
    Email address: mark.watney@nasa.gov
    Password:
    Password (again):
    Superuser created successfully.

    $ python manage.py runserver
    Performing system checks...

    System check identified no issues (0 silenced).
    July 21, 1969 - 02:56:15
    Django version 2.1.0, using settings 'addressbook.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

Sprawdź w przeglądarce strony:

* ``http://127.0.0.1:8000/``
* ``http://localhost:8000/admin/``

IDE Run configuration
=====================

Run configuration
-----------------

Debug configuration
-------------------
