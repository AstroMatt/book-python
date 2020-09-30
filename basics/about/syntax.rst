.. _Python Syntax:

*************
Python Syntax
*************


Variables
=========
.. highlights::
    * Names are case sensitive
    * Lowercase letters for variable names
    * Underscore ``_`` is used for multi-word names
    * ``NameError`` when using not declared variable
    * ``AttributeError`` when cannot assign to variables

.. code-block:: python
    :caption: Variable declaration

    name = 'Mark Watney'

    first_name = 'Mark'
    last_name = 'Watney'

    firstname = 'Mark'
    lastname = 'Watney'

.. code-block:: python
    :caption: Variables vs. constants - Names are case sensitive

    name = 'Mark Watney'        # lower cased names are reserved for variables
    Name = 'Jan Twardowski'     # Capitalized names are reserved for classes


Constants
=========
.. highlights::
    * Names are case sensitive
    * Underscore ``_`` is used for multi-word names
    * Uppercase letters for "constant" names
    * Python do not distinguish between variables and constants
    * Python allows you to change "constants" but it's a bad practice (good IDE will tell you)

.. code-block:: python
    :caption: "Constant" declaration

    FILE = '/etc/passwd'
    FILE_NAME = '/etc/shadow'
    FILENAME = '/etc/group'

.. code-block:: python
    :caption: Python allows you to change "constants" but it's a bad practice (good IDE will tell you)

    NAME = 'Mark Watney'
    NAME = 'Jan Twardowski'


Variables vs. Constants
=======================
.. code-block:: python
    :caption: Variables vs. constants - Names are case sensitive

    name = 'Mark Watney'        # variable
    NAME = 'Jan Twardowski'     # constant
    Name = 'José Jiménez'       # class

.. code-block:: python
    :caption: Variables vs. constants - Definition of second, minute or hour does not change based on location or country (those values should be constants). Definition of workday, workweek and workmonth differs based on location - each country can have different work times (those values should be variables).

    SECOND = 1
    MINUTE = 60 * SECOND
    HOUR = 60 * MINUTE

    workday = 8 * HOUR
    workweek = 5 * workday
    workmonth = 4 * workweek

.. code-block:: python
    :caption: For physical units it is ok to use proper cased names. It is better to be compliant with well known standard, than to enforce something which will mislead everyone.

    Pa = 1
    hPa = 100 * Pa
    kPa = 1000 * Pa
    MPa = 1000 * kPa


Printing Values
===============
.. highlights::
    * Prints on the screen
    * f-string formatting for variable substitution
    * More information in :ref:`Builtin Printing`

.. code-block:: python

    print('My name... José Jiménez')
    # My name... José Jiménez

.. code-block:: python

    name = 'José Jiménez'

    print(name)
    # José Jiménez

    print('My name... {name}')
    # My name... {name}

    print(f'My name... {name}')
    # My name... José Jiménez


End of Lines
============
.. highlights::
    * No semicolon (``;``) at the end of lines
    * :pep:`8`: Use ``\n`` for newline

.. doctest::

    >>> print('Hello!\nHow are you?')
    Hello!
    How are you?


Line Length
===========
* Most controversial rule
* :pep:`8`: 79 for line with code
* :pep:`8`: 72 for line with comment
* ``black``: 90-ish
* ``django``: 120 for code, 300 for models


Comments
========
.. highlights::
    * :pep:`8` for line comments: Hash (``#``), space and then comment
    * :pep:`8` for inline comments: code, two spaces, hash (``#``), space and then comment
    * Commented out code:

        * Never!
        * Use Version Control System instead - e.g.: ``git blame``
        * IDE has Local history (modifications) and you can compare file

.. code-block:: python
    :caption: Line comments

    # Mark thinks he is...
    print('Mark Watney: Space Pirate')

.. code-block:: python
    :caption: Inline comments

    print('Mark Watney: Space Pirate')  # This is who Mark Watney is


Indentation
===========
.. highlights::
    * Python uses indentation instead of braces
    * Code indented on the same level belongs to block
    * :pep:`8`: 4 spaces indentation, `no tabs <https://youtu.be/SsoOG6ZeyUI>`_
    * Python throws ``IndentationError`` exception on problem

.. code-block:: python

    if True:
        print('True statement, first line')
        print('True statement, second line')
    else:
        print('Else statement, first line')
        print('Else statement, second line')

.. code-block:: python

    if True:
        print('Outer block, true statement, first line')
        print('Outer block, true statement, second line')

        if True:
            print('Inner block, true statement, first line')
            print('Inner block, true statement, second line')
        else:
            print('Inner block, else statement, fist line')
            print('Inner block, else statement, second line')

    else:
        print('Outer block, else statement, first line')
        print('Outer block, else statement, second line')


Good practices
==============
* :pep:`8`
* :pep:`20`

.. doctest::

    >>> import this
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!


Assignments
===========

About Print
------------
* Assignment name: About Print
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 1 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/about_print.py`

:English:
    #. Print "Hello World" on the screen
    #. "Hello" must be in a first line
    #. "Wold" must be in a second line
    #. Use only one ``print()`` function call

:Polish:
    #. Wypisz "Hello World" na ekranie
    #. "Hello" ma być w pierwszej linii
    #. "World" ma być w drugiej linii
    #. Użyj tylko jednego wywołania funkcji ``print()``

:The whys and wherefores:
    * Wyświetlanie na ekranie

About Syntax
------------
* Assignment name: About Syntax
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/about_syntax.py`

:English:
    #. Write a multiline comment with program description (todo from this assignments)
    #. Declare variable ``name`` and set its value to your name
    #. Add inline comment to variable declaration with text: "This is my name"
    #. Print "Hello World NAME", where NAME is your name (variable ``name``)
    #. Use f-string

:Polish:
    #. Napisz wieloliniowy komentarz z opisem programu (punkty do wykonania z tego zadania)
    #. Zadeklaruj zmienną ``name`` i ustaw jej wartość na Twoje imię
    #. Dodaj komentarz "inline" do zmiennej o treści: "This is my name"
    #. Wypisz "Hello World NAME", gdzie NAME to Twoje imię (zmienna ``name``)
    #. Zastosuj f-string

:The whys and wherefores:
    * Tworzenie skryptów Python
    * Deklaracja zmiennych
    * Komentowanie kodu
    * Wyświetlanie wartości zmiennych

