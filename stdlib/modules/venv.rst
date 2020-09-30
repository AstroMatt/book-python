.. _Module venv:

***********
Module venv
***********



``venv`` Module
===============
* What is ``venv``
* Isolated Python installation for project
* Allows to have multiple versions of Python for one project (i.e. for testing)
* Allows to test libraries and frameworks before upgrading
* Allows to have different versions of libraries and frameworks for each project


Create ``venv``
===============
* ``DIRECTORY`` is the name of venv folder (see "Directory Naming Convention" below)

.. code-block:: console

    $ cd PROJECT
    $ python3.7 -m venv DIRECTORY

Directory Naming Convention
---------------------------
* No standard naming convention
* Naming directory like module (``venv``) name is a good idea
* Adding Python version is also a good practice
* Optionally naming per main framework/library version
* Dot at the beginning hides directory on Linux and macOS (but doesn't work on Windows)

.. code-block:: text
    :caption: Explicitly states which Python version is installed
    :emphasize-lines: 14

    .venv/
    venv/
    virtualenv/

    venv-3.6/
    venv-3.7/
    venv-3.8/

    venv-3.7.0/
    venv-3.7.1/
    venv-3.7.2/
    venv-3.7.3/
    venv-3.7.4/
    venv-3.7.5/

    venv-3.8.0/
    venv-3.8.1/

    venv-3.9-alpha1/
    venv-3.9-alpha2/
    venv-3.9-beta1/
    venv-3.9-beta2/
    venv-3.9-rc1/

    venv-django-2.1
    venv-django-2.2
    venv-django-3.0beta1
    venv-django-3.0beta2

    venv-py37-dj22
    venv-python37-django22
    venv-python38beta-django30beta

.. code-block:: text
    :caption: This convention is from ``virtualenv-wrapper`` module (mostly used in Python 2)

    ~/.virtualenv/PROJECT_NAME/

Example
-------
.. code-block:: console

    $ cd PROJECT
    $ python3.7 -m venv venv-3.7.4


Activate Virtualenv
===================

Windows
-------
.. code-block:: console

    $ cd PROJECT
    $ venv-3.7.4\Scripts\activate.bat

macOS, Linux, BSD
-----------------
.. code-block:: console

    $ cd PROJECT
    $ venv-3.7.4/bin/activate


Good practices
==============
* name as version ``venv-3.7.4``
* place in your project directory
* add folder to ``.gitignore`` (important!)
* Add to ``venv-3.7.4/bin/activate``:

    .. code-block:: bash

        project_name='My Project'

        red='\[\033[00;31m\]'
        green='\[\033[00;32m\]'
        blue='\[\033[00;36m\]'
        white='\[\033[00;39m\]'

        export PS1="\n${blue}${project_name}> ${white}"


Assignments
===========

Virtualenv
----------
* Assignment name: Virtualenv
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 0 lines
* Estimated time of completion: 2 min
* Solution: :download:`solution/venv.py`

:English:
    #. Create ``venv``
    #. Add ``venv`` as a Python interpreter in your IDE

:Polish:
    #. Stwórz ``venv``
    #. Dodaj ``venv`` jako interpreter Python w Twoim IDE
