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
    * :pep:`8` -- Style Guide for Python Code: Use ``\n`` for newline

.. doctest::

    >>> print('Hello!\nHow are you?')
    Hello!
    How are you?


Line Length
===========
* Most controversial rule
* :pep:`8` -- Style Guide for Python Code: 79 for line with code
* :pep:`8` -- Style Guide for Python Code: 72 for line with comment
* ``black``: 90-ish
* ``django``: 120 for code, 300 for models


Comments
========
.. highlights::
    * :pep:`8` -- Style Guide for Python Code: for line comments: Hash (``#``), space and then comment
    * :pep:`8` -- Style Guide for Python Code: for inline comments: code, two spaces, hash (``#``), space and then comment
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


Docstring and Doctests
======================
.. highlights::
    * Docstring is a first multiline comment in: File/Module, Class, Method/Function
    * Used for ``doctest``. More information in :ref:`Function Doctest`
    * :pep:`257` -- Docstring Conventions: For multiline ``str`` always use three double quote (``"""``) characters

.. code-block:: python

    """
    This is my first Python script

    >>> result
    12
    """

    result = 10 + 2



Indentation
===========
.. highlights::
    * Python uses indentation instead of braces
    * Code indented on the same level belongs to block
    * :pep:`8` -- Style Guide for Python Code: 4 spaces indentation, `no tabs <https://youtu.be/SsoOG6ZeyUI>`_
    * Python throws ``IndentationError`` exception on problem

.. code-block:: python

    if True:
        print('True statement, first line')
    else:
        print('Else statement, first line')

.. code-block:: python

    if True:
        print('True statement, first line')
        print('True statement, second line')
        print('True statement, third line')
    else:
        print('Else statement, first line')
        print('Else statement, second line')
        print('Else statement, third line')

.. code-block:: python

    if True:
        print('Outer block, true statement, first line')
        if True:
            print('Inner block, true statement, first line')
        else:
            print('Inner block, else statement, fist line')
    else:
        print('Outer block, else statement, first line')


.. code-block:: python

    if True:
        print('Outer block, true statement, first line')
        print('Outer block, true statement, second line')
        print('Outer block, true statement, third line')

        if True:
            print('Inner block, true statement, first line')
            print('Inner block, true statement, second line')
            print('Inner block, true statement, third line')
        else:
            print('Inner block, else statement, fist line')
            print('Inner block, else statement, second line')
            print('Inner block, else statement, third line')

    else:
        print('Outer block, else statement, first line')
        print('Outer block, else statement, second line')
        print('Outer block, else statement, third line')


Good practices
==============
* :pep:`8` -- Style Guide for Python Code
* :pep:`20` -- The Zen of Python

.. doctest::

    >>> import this
    The Zen of Python, by Tim Peters
    <BLANKLINE>
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

.. literalinclude:: assignments/about_print.py
    :caption: :download:`assignments/about_print.py`
    :end-before: # Solution

.. literalinclude:: assignments/about_syntax.py
    :caption: :download:`assignments/about_syntax.py`
    :end-before: # Solution
