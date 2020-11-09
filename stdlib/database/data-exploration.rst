********************
Database Exploration
********************


Apache Superset
===============
* https://superset.incubator.apache.org/
* https://www.youtube.com/watch?v=W_Sp4jo1ACg

Install
-------
#. Install superset

    .. code-block:: console

        $ pip install superset

#. Create an admin user

    .. code-block:: console

        $ fabmanager create-admin --app superset

#. Initialize the database

    .. code-block:: sh

        superset db upgrade

#. Load some data to play with

    .. code-block:: console

        $ superset load_examples

#. Create default roles and permissions

    .. code-block:: console

        $ superset init

#. To start a development web server on port 8088, use -p to bind to another port

    .. code-block:: console

        $ superset runserver -d

Configuration
-------------
* ``superset_config.py``

.. code-block:: python

    ROW_LIMIT = 5000
    SUPERSET_WEBSERVER_PORT = 8088

    # Change this for your setup
    SECRET_KEY = '\2\1myscretkey\1\2\e\y\y\h'

    # Superset configuration database only
    # Datasources are managed in the web UI
    SQLALCHEMY_DATABASE_URI = 'sqlite:////path/to/superset.db'

    # Flask CSRF protection
    WTF_CSRF_ENABLED = True
    WTF_CSRF_EXEMPT_LIST = []
    WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

    # Set this API key to enable Mapbox visualizations
    MAPBOX_API_KEY = ''

Production setup
----------------
.. code-block:: console

    $ gunicorn \
        -w 10 \
        -k gevent \
        --timeout 120 \
        -b  0.0.0.0:6666 \
        --limit-request-line 0 \
        --limit-request-field_size 0 \
        --statsd-host localhost:8125 \
        superset:app

Features
--------

Dashboard
^^^^^^^^^
.. figure:: img/superset-01.png
    :align: center
    :width: 75%

    Dashboard

Data exploration
^^^^^^^^^^^^^^^^
.. figure:: img/superset-02.png
    :align: center
    :width: 75%

    Data exploration

SQL IDE
^^^^^^^
.. figure:: img/superset-03.png
    :align: center
    :width: 75%

    SQL IDE

GIS and spatial data
^^^^^^^^^^^^^^^^^^^^
.. figure:: img/superset-04.png
    :align: center
    :width: 75%

    GIS and spatial data
