**********
Deployment
**********

Deployment platforms
====================

Apache + mod_wsgi
-----------------

Nginx + uwsgi
-------------
.. code-block:: nginx

    # mysite_nginx.conf

    # the upstream component nginx needs to connect to
    upstream django {
        # server unix:///path/to/your/mysite/mysite.sock; # for a file socket
        server 127.0.0.1:8001; # for a web port socket (we'll use this first)
    }

    # configuration of the server
    server {
        # the port your site will be served on
        listen      8000;
        # the domain name it will serve for
        server_name example.com; # substitute your machine's IP address or FQDN
        charset     utf-8;

        # max upload size
        client_max_body_size 75M;   # adjust to taste

        # Django media
        location /media  {
            alias /path/to/your/mysite/media;  # your Django project's media files - amend as required
        }

        location /static {
            alias /path/to/your/mysite/static; # your Django project's static files - amend as required
        }

        # Finally, send all non-media requests to the Django server.
        location / {
            uwsgi_pass  django;
            include     /path/to/your/mysite/uwsgi_params; # the uwsgi_params file you installed
        }
    }

.. code-block:: ini

    # mysite_uwsgi.ini file
    [uwsgi]

    # Django-related settings
    # the base directory (full path)
    chdir           = /path/to/your/project
    # Django's wsgi file
    module          = project.wsgi
    # the virtualenv (full path)
    home            = /path/to/virtualenv

    # process-related settings
    # master
    master          = true
    # maximum number of worker processes
    processes       = 10
    # the socket (use the full path to be safe
    socket          = /path/to/your/project/mysite.sock
    # ... with appropriate permissions - may be needed
    # chmod-socket    = 664
    # clear environment on exit
    vacuum          = true

Gunicorn
--------

Vagrant + Puppet
----------------

Docker + Gunicorn
-----------------
:entrypoint.sh:
    .. code-block:: sh

        #!/bin/bash

        # Prepare log files and start outputting logs to stdout
        touch ./logs/gunicorn.log
        touch ./logs/gunicorn-access.log
        tail -n 0 -f ./logs/gunicorn*.log &

        export DJANGO_SETTINGS_MODULE=myproject.settings

        exec gunicorn myproject.wsgi:application \
            --name myproject \
            --bind 0.0.0.0:8000 \
            --workers 5 \
            --log-level=info \
            --log-file=./logs/gunicorn.log \
            --access-logfile=./logs/gunicorn-access.log \
        "$@"

:Dockerfile:

    .. code-block:: dockerfile

        # Set the base image to Ubuntu
        FROM ubuntu:lts

        # Update the default application repository sources list
        RUN apt-get update && apt-get install -y \
            python-dev \
            python \
            python-pip \
            python-setuptools \
            build-essential \
            python-dev \
            git

        # Set variables for project name, and where to place files in container.
        ENV PROJECT=myproject
        ENV CONTAINER_HOME=/opt
        ENV CONTAINER_PROJECT=$CONTAINER_HOME/$PROJECT

        # Create application subdirectories
        WORKDIR $CONTAINER_HOME
        RUN mkdir logs

        # Copy application source code to $CONTAINER_PROJECT
        COPY . $CONTAINER_PROJECT

        # Install Python dependencies
        RUN pip install -r $CONTAINER_PROJECT/requirements.txt
        RUN pip install gunicorn

        # Copy and set entrypoint
        WORKDIR $CONTAINER_PROJECT
        COPY ./entrypoint.sh /
        ENTRYPOINT ["/entrypoint.sh"]

.. code-block:: console

    $ docker build -t django_gunicorn:v1 .

.. code-block:: console

    $ docker run --restart=always -p 8000:8000 -i -t django_gunicorn:v1

Heroku
------
:Procfile:
    .. code-block:: text

        release: python manage.py migrate --noinput
        web: gunicorn habitat.wsgi

:runtime.txt:
    .. code-block:: text

        python-3.6.5

Packaging
=========

``setup.py``
------------
.. code-block:: python

    import os
    import sys
    from setuptools import setup, find_packages
    from os import path


    assert sys.version_info >= (3, 6), "Python 3.6+ required."


    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


    with open(path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as file:
        long_description = file.read()


    setup(
        name='habitatOS',

        # Versions should comply with PEP440.  For a discussion on single-sourcing
        # the version across setup.py and the project code, see
        # https://packaging.python.org/en/latest/single_source_version.html
        version='0.9.0',

        description='Analog space habitat operating system.',
        long_description=long_description,

        # The project's main homepage.
        url='https://github.com/astromatt/habitatOS',

        # Author details
        author='Matt Harasymczuk',
        author_email='dev@habitatos.space',

        # Choose your license
        license='MIT',

        # See https://pypi.python.org/pypi?:action=list_classifiers
        classifiers=[
            # How mature is this project? Common values are
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 4 - Beta',

            # Indicate who your project is intended for
            'Intended Audience :: Science/Research',
            'Topic :: Scientific/Engineering',
            'Topic :: System :: Operating System',

            # Pick your license as you wish (should match "license" above)
            'License :: OSI Approved :: MIT License',

            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            'Programming Language :: Python :: 3.6',
        ],

        # What does your project relate to?
        keywords='space exploration analog analogue habitat operating system',

        # You can just specify the packages manually here if your project is
        # simple. Or you can use find_packages().
        packages=find_packages(exclude=['docs', 'experiments', 'tmp']),
        include_package_data=True,


        # List run-time dependencies here.  These will be installed by pip when
        # your project is installed. For an analysis of "install_requires" vs pip's
        # requirements files see:
        # https://packaging.python.org/en/latest/requirements.html
        install_requires=[],

        # List additional groups of dependencies here (e.g. development
        # dependencies). You can install these using the following syntax,
        # for example:
        # $ pip install -e .[dev,test]
        extras_require={
            'dev': ['check-manifest'],
            'test': ['coverage', 'pep8'],
        },

        # Although 'package_data' is the preferred approach, in some case you may
        # need to place data files outside of your packages. See:
        # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
        # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
        # data_files=[('my_data', ['data/data_file.txt'])],

        # To provide executable scripts, use entry points in preference to the
        # "scripts" keyword. Entry points provide cross-platform support and allow
        # pip to create the appropriate form of executable for the target platform.
        entry_points={
            'console_scripts': [
                'habitatOS = habitat:manage',
            ],
        },
    )

``Manifest.in``
---------------
.. code-block:: text

    include requirements.txt
    include README.md
    include LICENSE
    recursive-include HabitatOS *

    global-exclude __pycache__
    global-exclude *.pyc
    global-exclude *.pyo


Staticfiles serving
===================
