*******
Linters
*******


``pycodestyle``
===============
* previously known as ``pep8``

:About:
    Python style guide checker. ``pycodestyle`` is a tool to check your Python code
    against some of the style conventions in PEP 8.

    * Plugin architecture: Adding new checks is easy.
    * Parsable output: Jump to error location in your editor.
    * Small: Just one Python file, requires only stdlib. You can use just the
    * pep8.py file for this purpose.
    * Comes with a comprehensive test suite.

:Installation:
    .. code-block:: console

        $ pip install pycodestyle

:Usage:
    .. code-block:: console

        $ pycodestyle FILE.py
        $ pycodestyle DIRECTORY/
        $ pycodestyle --statistics -qq DIRECTORY/
        $ pycodestyle --show-source --show-pep8 FILE.py

    .. code-block:: console

        $ python -m pycodestyle FILE.py

:Config:
    ``setup.cfg``

    .. code-block:: ini

        [pycodestyle]
        max-line-length = 939
        ignore = E402,W391
        exclude = */migrations/*


``flake8``
==========
Simply speaking flake8 is "the wrapper which verifies ``pycodestyle``, ``pyflakes`` and circular complexity". For other functions, it can control the warnings for specific line (impossible by a simple pyflakes)by # flake8: noqa or it can customize warnings happening by configuration file such as ``pycodestyle``.

.. literalinclude:: src/flake8.ini
    :language: ini
    :caption: Flake8 config in ``setup.cfg``


``pylint``
==========
Pylint is a Python source code analyzer which looks for programming errors, helps enforcing a coding standard and sniffs for some code smells (as defined in Martin Fowler’s Refactoring book). Pylint has many rules enabled by default, way too much to silence them all on a minimally sized program. It’s highly configurable and handle pragmas to control it from within your code. Additionally, it is possible to write plugins to add your own checks.

Coding Standard:

* checking line-code's length,
* checking if variable names are well-formed according to your coding standard
* checking if imported modules are used

Error detection:

* checking if declared interfaces are truly implemented
* checking if modules are imported and much more (see the complete check list)

``Pylint`` is shipped with ``Pyreverse`` which creates UML diagrams for python code.

:Install:
    .. code-block:: console

        $ pip install pylint

:Usage:
    .. code-block:: console

        $ pylint DIRECTORY/
        $ pylint FILE.py

:More information:
    * https://pypi.python.org/pypi/pylint/

:Config:
    .. literalinclude:: src/pylintrc.ini
        :language: ini
        :caption: PyLama


``pyflakes``
============
A simple program which checks Python source files for errors. Pyflakes analyzes programs and detects various errors. It works by parsing the source file, not importing it, so it is safe to use on modules with side effects. It’s also much faster.

:Install:
    .. code-block:: console

        $ pip install pyflakes

:Usage:
    .. code-block:: console

        $ pyflakes DIRECTORY/
        $ python -m pyflakes DIRECTORY/

:More information:
    * https://pypi.python.org/pypi/pyflakes

``pylama``
==========
