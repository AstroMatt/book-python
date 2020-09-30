***************
Python Language
***************


.. figure:: img/python-logo.png
    :width: 75%
    :align: center

    Python Logo


Rationale
=========
* Turing complete, general purpose language
* Multi platform
* Dynamic typing with automatic memory allocation and GC
* Code readability and simplicity is important
* White space are important
* Everything is an object, but you can write functional code too
* Standard language in Machine Learning and Data Science
* Very good standard system library
* Huge ecosystem of external open source libraries
* Open Source created by non-profit Python Software Foundation


Which Version?
==============
* You should use newest official Python version
* Soruce: https://devguide.python.org/#status-of-python-branches
* Source: https://www.python.org/downloads/

.. csv-table:: Future Versions
    :header: "Version", "PEP", "Status", "Release", "End-of-life", "Release Manager"

    "3.11", "TBA",        "future",       "2022-10-04", "TBA",     "Pablo Galindo Salgado"
    "3.10", "TBA",        "development",  "2021-10-04", "TBA",     "Pablo Galindo Salgado"

.. csv-table:: Currently Supported Versions
    :header: "Version", "PEP", "Status", "Release", "End-of-life", "Release Manager"

    "3.9",  ":pep:`596`", "features",     "2020-10-05", "TBA",     "Łukasz Langa"
    "3.8",  ":pep:`569`", "features",     "2019-10-20", "2024-10",     "Łukasz Langa"
    "3.7",  ":pep:`537`", "bugfix",       "2018-06-27", "2023-06-27",  "Ned Deily"
    "3.6",  ":pep:`494`", "security",     "2016-12-23", "2021-12-23",  "Ned Deily"

.. csv-table:: Unsupported Versions
    :header: "Version", "PEP", "Status", "Release", "End-of-life", "Release Manager"

    "3.5",  ":pep:`478`", "end of life",  "2015-09-13", "2020-09-13",  "Larry Hastings"
    "3.4",  ":pep:`429`", "end of life",  "2014-03-16", "2019-03-16",  "Larry Hastings"
    "3.3",  ":pep:`398`", "end of life",  "2012-09-29", "2017-09-29",  "Georg Brandl"
    "3.2",  ":pep:`392`", "end of life",  "2011-02-20", "2016-02-20",  "Georg Brandl"
    "3.1",  ":pep:`375`", "end of life",  "2009-06-27", "2012-04-09",  "Benjamin Peterson"
    "3.0",  ":pep:`361`", "end of life",  "2008-12-03", "2009-01-13",  "Barry Warsaw"
    "2.7",  ":pep:`373`", "end of life",  "2010-07-03", "2020-04-20",  "Benjamin Peterson"
    "2.6",  ":pep:`361`", "end of life",  "2008-10-01", "2013-10-29",  "Barry Warsaw"


Why not Python 2?
=================
* 2020-04-20 - end of Life for Python 2.7 :pep:`373`
* Python 2 is no longer developed [`1 <https://www.python.org/psf/press-release/pr20191220/>`_, `2 <https://mail.python.org/archives/list/python-dev@python.org/message/N6JIGTTJCJHS47AYSI76SJPCQS25EBWR/>`_]
* Python 2.7 is the last in 2.x branch, and there won't be Python 2.8 :pep:`404`
* Python 2.7.18, the last release of Python 2 [`3 <https://pythoninsider.blogspot.com/2020/04/python-2718-last-release-of-python-2.html>`_]


Changes in Python 3
===================
* All strings are Unicode
* In Python 3 ``print()`` is a function, not a keyword
* Changes in standard library modules naming and location
* New string formatting


Python Release Cycle
====================
.. versionadded:: Python 3.9
    See :pep:`602`

* 12 months (1 year) release cycle
* 18 months (1.5 year) of bugfix updates
* 42 months (3.5 year) of security updates

.. figure:: img/pep602-release-calendar.png
    :width: 85%
    :align: center

    Python 12 months release cycle.


Scripts
=======
* Python files use ``.py`` as an extension
* Compiled files are in ``__pycache__`` directory
* Python also uses other extensions

.. csv-table:: Python file types and extensions
    :header-rows: 1
    :widths: 15, 85

    "Extension", "Description"
    "``.pyc``", "Compiled source code (bytecode)"
    "``.pyd``", "Compiled Windows DLL file"
    "``.pyw``", "Compiled Windows file. Executable with ``pythonw.exe``"
    "``.pyx``", "cPythona source for C/C++ conversion"
    "``.pyz``", "`zipapp <https://docs.python.org/3/library/zipapp.html>`_ compressed archive. Since Python 3.5"

.. code-block:: python
    :caption: Minimal script

    print('Ehlo World!')


Python Console (REPL)
=====================
* Read–Eval–Print Loop
* Quickly test and evaluate code
* Lines starts with ``>>>``
* Line continuation starts with ``...``
* Result is printed below
* Open REPL with ``python3`` command in terminal

.. code-block:: console

    $ python3
    3.8.2 (default, Mar 11 2020, 00:29:50)
    [Clang 11.0.0 (clang-1100.0.33.17)]
    Type "help", "copyright", "credits" or "license" for more information.

    >>> print('Ehlo World!')
    Ehlo World!

.. note:: In documentation and books you may find ``>>>`` and ``...`` at the beginning of code listing lines

    .. code-block:: python

        >>> if True:
        ...     print('yes')
        ... else:
        ...     print('no')
        yes


Jupyter
=======
* Open Source web application REPL
* Very popular in Machine Learning and Data Science world
* Create and share documents that contain live code, equations, visualizations and narrative text
* Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, etc


Python Developer Survey
=======================
* Annual survey
* https://www.jetbrains.com/lp/python-developers-survey-2019


Assignments
===========

About Version
-------------
* Complexity level: easy
* Lines of code to write: 0 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/about_version.py`

:English:
    #. Create file wih name ``about_version.py``
    #. Use code from "Input" section (see below)
    #. Run code in your IDE (right click on code -> "Run File in Python Console")
    #. What Python version is installed?
    #. Newest official Python is recommended
    #. Compare result with "Output" section (see below)

:Polish:
    #. Stwórz skrypt o nazwie ``about_version.py``
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Uruchom kod swoim IDE (prawy klawisz myszy na kodzie -> "Run File in Python Console")
    #. Jaka wersja Python jest zainstalowana?
    #. Zalecana jest najnowsza oficjalna wersja Python
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        import sys
        print(sys.version[:5])

:Output:
    .. code-block:: text

        3.8.5

:The whys and wherefores:
    * Czy Python działa
    * Jaka jest wersja Python
    * Korzystanie z print
    * Umiejętność uruchamiania skryptów
    * Szukanie rozwiązań zadań z książki

About Environment
-----------------
* Complexity level: easy
* Lines of code to write: 0 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/about_environment.py`

:English:
    .. todo:: English Translation

:Polish:
    #. Stwórz plik o nazwie ``about_env.py``
    #. Plik ma mieć zawartość:

        .. code-block:: python

            import sys
            import os

            print(f'Python Executable: {sys.executable}')
            print(f'Python Version: {sys.version}')
            print(f'Virtualenv: {os.getenv("VIRTUAL_ENV")}')

    #. Uruchom go w swoim IDE (menu ``Run -> Run... -> nazwa Twojego skryptu``)
    #. Gdzie Python jest zainstalowany?
    #. Czy korzystasz z "Virtualenv"?
    #. Upewnij się, że w linijce z "Virtualenv" nie masz ``None``

:The whys and wherefores:
    * Czy Python działa
    * Jaka jest wersja Python
    * Czy korzystasz z Virtualenv
    * Korzystanie z print
    * Umiejętność uruchamiania skryptów
    * Szukanie rozwiązań zadań z książki
