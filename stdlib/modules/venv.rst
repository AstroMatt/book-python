.. _Module venv:

***********
Module venv
***********



Rationale
=========
* Bundled with Python since 3.3
* Isolated Python environment
* Allows to have multiple versions of Python for one project
* For testing on different versions: ``py37``, ``py38``, ``py39``, ``py310a1``
* Test libraries and frameworks before upgrading (create venv, install requirements, run tests, delete if fails)
* Allows to have different versions of libraries and frameworks for each project


Create
======
* ``DIRECTORY`` is the name of venv folder (see "Directory Naming Convention" below)

.. code-block:: console

    $ cd PROJECT
    $ python3.9 -m venv DIRECTORY

.. code-block:: console
    :caption: Example

    $ cd PROJECT
    $ python3.9 -m venv venv-3.9.0


Activate
========
* ``Scripts`` for Windows
* ``bin`` for macOS, Linux, BSD
* Note the direction of slash and backslash (OS dependent)

.. code-block:: console
    :caption: Windows

    $ cd PROJECT
    $ venv-3.9.0\Scripts\activate.bat

.. code-block:: console
    :caption: macOS, Linux, BSD

    $ cd PROJECT
    $ venv-3.9.0/bin/activate


Directory Naming Convention
===========================
* No standard naming convention
* Naming directory like module (``venv``) name is a good idea
* Adding Python version is also a good practice
* Optionally naming per main framework/library version
* Dot at the beginning hides directory on Linux and macOS (but doesn't work on Windows)
* Underscore is Python convention for private/protected, but does not work for OS and Git

.. code-block:: text

    venv/
    .venv/
    _venv/

    virtualenv/
    .virtualenv/
    _virtualenv/

    py
    python
    py-3.9
    python-3.9
    python-3.9.0

    .py
    .python
    .py-3.9
    .python-3.9
    .python-3.9.0

    venv-3.6/
    venv-3.7/
    venv-3.8/
    venv-3.9/
    venv-3.10/

    venv-3.8.0/
    venv-3.8.1/
    venv-3.8.2/
    venv-3.8.3/

    venv-3.9.0/
    venv-3.9.1/
    venv-3.9.2/
    venv-3.9.3/

    venv-3.10-alpha1/
    venv-3.10-alpha2/
    venv-3.10-beta1/
    venv-3.10-beta2/
    venv-3.10-rc1/

    venv-django-2.1
    venv-django-2.2
    venv-django-2.3
    venv-django-3.0
    venv-django-3.1
    venv-django-3.2
    venv-django-4.0a1
    venv-django-4.0a2
    venv-django-4.0b1
    venv-django-4.0b2
    venv-django-4.0rc1
    venv-django-4.0rc2

    venv-py39-dj33
    venv-python39-django33
    venv-python310alpha1-django40a1

.. code-block:: text
    :caption: This convention is from ``virtualenv-wrapper`` module (mostly used in Python 2)

    ~/.virtualenv/PROJECT_NAME/


Good practices
==============
* name as version ``venv-3.9.0``
* place in your project directory and add folder to ``.gitignore`` (important!)
* otherwise place it in ``~/.virtualenv/``, but some meaningful name is required
* Append at the end of ``venv-3.9.0/bin/activate``:

    .. code-block:: bash

        project_name='My Project'

        red='\[\033[00;31m\]'
        green='\[\033[00;32m\]'
        blue='\[\033[00;36m\]'
        white='\[\033[00;39m\]'

        export PS1="\n${blue}${project_name}> ${white}"


Further Reading
===============
* https://github.com/pypa/virtualenv/issues/2007


Assignments
===========

.. todo:: Convert assignments to literalinclude

Virtualenv
----------
* Assignment: Virtualenv
* Filename: :download:`assignments/venv.py`
* Complexity: easy
* Lines of code: 0 lines
* Time: 2 min

English:
    #. Create ``venv``
    #. Add ``venv`` as a Python interpreter in your IDE

Polish:
    #. Stwórz ``venv``
    #. Dodaj ``venv`` jako interpreter Python w Twoim IDE
