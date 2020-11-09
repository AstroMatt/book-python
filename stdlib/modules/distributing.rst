*********************
Distributing Packages
*********************

.. _Distributing Packages:

Installing Packages
===================
* ``pip search``
* ``pip install``
* ``pip install -r requirements.txt``


Modularization
==============

``__init__.py``
---------------
* https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/__init__.py
* https://github.com/django/django/blob/master/django/views/generic/__init__.py


``__all__``
-----------
* https://github.com/django/django/blob/master/django/views/generic/__init__.py

.. code-block:: python

    from backend.api_v2.models.click import Click
    from backend.api_v2.models.event import Event
    from backend.api_v2.models.survey import Survey
    from backend.api_v2.models.trial import Trial


    __all__ = ['Click', 'Event', 'Survey', 'Trial']


Creating packages
=================

``distutils``
-------------
* Provides support for building and installing additional modules into a Python.
* The new modules may be either 100%-pure Python, or may be extension modules written in C, or may be collections of Python packages which include modules coded in both Python and C.

``setuptools``
--------------
* Enhanced alternative to distutils that provides:

    #. support for declaring project dependencies
    #. additional mechanisms for configuring which files to include in source releases (including plugins for integration with version control systems)
    #. the ability to declare project “entry points”, which can be used as the basis for application plugin systems
    #. the ability to automatically generate Windows command line executables at installation time rather than needing to prebuild them
    #. consistent behaviour across all supported Python versions

Setuptools is a fully-featured, actively-maintained, and stable library designed to facilitate packaging Python projects, where packaging includes:

    * Python package and module definitions
    * Distribution package metadata
    * Test hooks
    * Project installation
    * Platform-specific details
    * Python 3 support

``wheel`` vs. ``egg``
---------------------
* to build a python wheel package
* ``sdist`` will generate a ``.tar.gz`` file in ``dist/``
* ``bdist_wheel`` will generate a ``.whl`` file in ``dist/``

.. code-block:: console

    $ python setup.py sdist bdist_wheel

.. code-block:: console

    $ python setup.py sdist bdist_wheel --universal

``requirements.txt`` vs ``setup.py``
------------------------------------

``setup.py``
------------

.. code-block:: python

    from setuptools import find_packages
    from setuptools import setup
    from os import path


    assert sys.version_info >= (3, 6), "Python 3.6+ required."


    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


    # Get the long description from the relevant file
    with open(path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as file:
        long_description = file.read()


    # Get the project requirements from requirements.txt file
    with open(path.join(BASE_DIR, 'requirements.txt'), encoding='utf-8') as file:
        requirements = file.read().splitlines()


    setup(
        name='HabitatOS',

        # Versions should comply with PEP440.  For a discussion on single-sourcing
        # the version across setup.py and the project code, see
        # https://packaging.python.org/en/latest/single_source_version.html
        version='0.5.0',

        description='Analog Habitat Operating System',
        long_description=long_description,

        # The project's main homepage.
        url='https://github.com/astromatt/HabitatOS',

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
        packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

        # List run-time dependencies here.  These will be installed by pip when
        # your project is installed. For an analysis of "install_requires" vs pip's
        # requirements files see:
        # https://packaging.python.org/en/latest/requirements.html
        install_requires=requirements,

        # List additional groups of dependencies here (e.g. development
        # dependencies). You can install these using the following syntax,
        # for example:
        # $ pip install -e .[dev,test]
        extras_require={
            'dev': ['check-manifest'],
            'test': ['coverage', 'pep8'],
        },

        # If there are data files included in your packages that need to be
        # installed, specify them here.  If using Python 2.6 or less, then these
        # have to be included in MANIFEST.in as well.
        package_data={
            # 'sample': ['package_data.dat'],
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
                'habitatOS=habitat:manage',
            ],
        },
    )

``setup.cfg``
-------------
* Configuring setup() using setup.cfg files
* A setup.py file containing a setup() function call is still required even if your configuration resides in setup.cfg.

.. code-block:: ini

    [bdist_wheel]
    universal = 1

    [metadata]
    license_file = LICENSE

    [pycodestyle]
    max-line-length = 999
    exclude = */migrations/*
    ignore = E402,W391

.. code-block:: ini

    [metadata]
    name = my_package
    version = attr: src.VERSION
    description = My package description
    long_description = file: README.rst, CHANGELOG.rst, LICENSE.rst
    keywords = one, two
    license = BSD 3-Clause License
    classifiers =
        Framework :: Django
        License :: OSI Approved :: BSD License
        Programming Language :: Python :: 3
        Programming Language :: Python :: 3.5

    [options]
    zip_safe = False
    include_package_data = True
    packages = find:
    scripts =
      bin/first.py
      bin/second.py
    install_requires =
      requests
      importlib; python_version == "2.6"

    [options.package_data]
    * = *.txt, *.rst
    hello = *.msg

    [options.extras_require]
    pdf = ReportLab>=1.2; RXP
    rest = docutils>=0.3; pack ==1.1, ==1.3

    [options.packages.find]
    exclude =
        src.subpackage1
        src.subpackage2

    [options.data_files]
    /etc/my_package =
        site.d/00_default.conf
        host.d/00_default.conf
    data = data/img/logo.png, data/svg/icon.svg

``python setup.py sdist upload``
--------------------------------
* upload is deprecated in favor of using ``twine``

``twine``
---------
.. code-block:: console

    pip install twine
    $ python setup.py sdist bdist_wheel

    # Upload with twine to Test PyPI and verify things look right.
    $ twine upload --repository-url https://test.pypi.org/legacy/ dist/*

    # Upload to PyPI
    $ twine upload dist/*

Signing packages
----------------
.. code-block:: console

    # Remove any old distributions
    $ rm -rf dist/

    # Create new tar.gz and wheel files
    # Only create a universal wheel if py2/py3 compatible and no C extensions
    $ python setup.py bdist_wheel --universal

    # Sign the distributions
    $ gpg --detach-sign -a dist/*

    # Upload to PyPI
    $ twine upload dist/*

Artifactory
-----------
* https://www.jfrog.com/confluence/display/RTF/PyPI+Repositories#PyPIRepositories-PublishingtoArtifactory

.. code-block:: console

    $ docker run --name artifactory -d -p 8081:8081 docker.bintray.io/jfrog/artifactory-oss:latest

.. code-block:: ini
    :caption: ~/.pypirc

    [distutils]
    index-servers =
        local
        pypi

    [pypi]
    repository: https://pypi.org/pypi
    username: myusername
    password: mypassword

    [local]
    repository: http://example.com:8081/artifactory/api/pypi/pypi-local
    username: myusername
    password: mypassword

.. code-block:: console

    $ python setup.py sdist upload -r local
    $ python setup.py bdist_wheel upload -r local
    $ python setup.py sdist bdist_wheel upload -r local

.. code-block:: console
    :caption: Search

    $ pip search myapp --index http://example.com:8081/artifactory/api/pypi/pypi-local/
    myapp                   - My Simple App


Future of packaging and distribution
====================================
* https://www.youtube.com/watch?v=jOiAp3wtx18
* https://www.youtube.com/watch?v=Oc9khbXBes8
