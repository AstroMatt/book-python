.. _Software Engineering Conventions:

********************************
Software Engineering Conventions
********************************


PEP 8 - Style Guide for Python Code
===================================

Tabs or spaces?
---------------
* 4 spacje
* IDE zamienia tab na 4 spacje

Line length
-----------
* najbardziej kontrowersyjna klauzula
* 79 znaków kod
* 72 znaki docstrings/comments
* Python standard library is conservative and requires limiting lines to 79 characters (and docstrings/comments to 72)
* soft wrap
* co z monitorami 4k?
* Preferred way of wrapping long lines is by using Python's implied line continuation inside parentheses, brackets and braces.

.. code-block:: python

    class FoodProduct(models.Model):
        vitamins_folic_acid = models.DecimalField(verbose_name=_('Folic Acid'), help_text=_('µg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
        vitamins_a = models.DecimalField(verbose_name=_('Vitamin A'), help_text=_('µg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
        vitamins_b1 = models.DecimalField(verbose_name=_('Vitamin B1'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
        vitamins_b2 = models.DecimalField(verbose_name=_('Vitamin B2'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
        vitamins_b6 = models.DecimalField(verbose_name=_('Vitamin B6'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
        vitamins_b12 = models.DecimalField(verbose_name=_('Vitamin B12'), help_text=_('µg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
        vitamins_c = models.DecimalField(verbose_name=_('Vitamin C'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
        vitamins_d = models.DecimalField(verbose_name=_('Vitamin D'), help_text=_('µg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
        vitamins_e = models.DecimalField(verbose_name=_('Vitamin E'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
        vitamins_pp = models.DecimalField(verbose_name=_('Vitamin PP'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)

        minerals_zinc = models.DecimalField(verbose_name=_('Zinc'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
        minerals_phosphorus = models.DecimalField(verbose_name=_('Phosphorus'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
        minerals_iodine = models.DecimalField(verbose_name=_('Iodine'), help_text=_('µg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
        minerals_magnesium = models.DecimalField(verbose_name=_('Magnesium'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
        minerals_copper = models.DecimalField(verbose_name=_('Copper'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
        minerals_potasium = models.DecimalField(verbose_name=_('Potasium'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
        minerals_selenium = models.DecimalField(verbose_name=_('Selenium'), help_text=_('µg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
        minerals_sodium = models.DecimalField(verbose_name=_('Sodium'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
        minerals_calcium = models.DecimalField(verbose_name=_('Calcium'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)
        minerals_iron = models.DecimalField(verbose_name=_('Iron'), help_text=_('mg/100g'), decimal_places=2, max_digits=5, blank=True, null=True, default=None)


File encoding
-------------
* UTF-8
* always remember to open files for reading and writing with ``encoding='utf-8'``
* All identifiers in the Python standard library MUST use ASCII-only identifiers, and SHOULD use English words wherever feasible (in many cases, abbreviations and technical terms are used which aren't English).
* String literals and comments must also be in ASCII.
* Authors whose names are not based on the Latin alphabet (latin-1, ISO/IEC 8859-1 character set) MUST provide a transliteration of their names in this character set.

Comments
--------
* Comments that contradict the code are worse than no comments.
* Comments should be complete sentences.
* Block comments generally consist of one or more paragraphs built out of complete sentences
* Each sentence ending in a period.
* Python coders from non-English speaking countries: please write your comments in English, unless you are 120% sure that the code will never be read by people who don't speak your language.
* Each line of a block comment starts with a # and a single space (unless it is indented text inside the comment).

Documentation Strings
---------------------
* :pep:`257` -- Docstring Conventions
* Write docstrings for all public modules, functions, classes, and methods.
* Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method does.
* For one liner docstrings, please keep the closing """ on the same line.
* :pep:`257` -- Docstring Conventions: For multiline ``str`` always use three double quote (``"""``) characters

Use better names, rather than comments
--------------------------------------
.. code-block:: python

    def cal_var(data):
        """Calculate variance"""
        return sum((Xi-m) ** 2 for Xi in data) / len(data)

    def calculate_variance(data):
        return sum((Xi-m) ** 2 for Xi in data) / len(data)

.. code-block:: python

    def fabs(a, b):
        return float(abs(a + b))

    def float_absolute_value(a, b):
        return float(abs(a + b))

    def abs(a: int, b: int) -> float:
        return float(abs(a + b))

    def absolute_value(a: int, b: int) -> float:
        return float(abs(a + b))

Commented code?
---------------
* NO!
* Never commit files with commented code

Author name or revision version
-------------------------------
* Do not put author name or revision version to the files
* Version Control System is responsible for that

Naming convention
-----------------

Constants and Variables
^^^^^^^^^^^^^^^^^^^^^^^
* Używanie ``_`` w nazwach (snake_case) - // Python - snake ;)
* ``variable`` or ``variable_name``

    .. code-block:: python

        name = 'José Jiménez'

        firstname = 'José'
        lastname = 'Jiménez'

* ``CONSTANT`` or ``CONSTANT_NAME``

    .. code-block:: python

        PATH = '/etc/hosts'

        FILE_NAME = 'README.txt'

Classes
^^^^^^^
* ``CamelCase``

    .. code-block:: python

        class MyClass:
            pass

Class Attributes
----------------
* Public attributes should have no leading underscores.
* If your public attribute name collides with a reserved keyword, append a single trailing underscore to your attribute name.
* ``cls`` is the preferred spelling for any variable or argument which is known to be a class, especially the first argument to a class method.


Methods/Functions
-----------------
* Używanie ``_`` w nazwach (snake_case) - // Python - snake ;)
* ``method_name()`` or ``function_name()``

    .. code-block:: python

        def add_numbers(a, b):
            return a + b

* Nie robimy camelCase

    .. code-block:: python

        def addNumbers(a, b):
            return a + b

Modules names
-------------
* ``modulename``
* ``module_name``
* Preferable one word

    .. code-block:: python

        import random
        import argparse

Function/Method argument names
------------------------------
* ``self``

    .. code-block:: python

        class Astronaut:
            name = 'José Jiménez'

            def say_hello(self):
                print(f'My name... {self.name}')


* ``cls``

    .. code-block:: python

        class Astronaut:
            pass

        class Cosmonaut:
            pass

        class Starman:
            pass

        def is_spaceman(cls):
            if instance(cls, (Astronaut, Cosmonaut)):
                return True
            else:
                return False


        is_spaceman(Cosmonaut)  # True
        is_spaceman(Astronaut)  # True
        is_spaceman(Starman)    # False

* ``self`` and ``other``

    .. code-block:: python

        class Vector:
            x = 0
            y = 1

            def __add__(self, other):
                return Vector(
                    x=self.x+other.x,
                    y=self.y+other.y
                )

Using ``__`` and ``_`` in names
-------------------------------
* W Pythonie nie ma private/protected/public
* Funkcje o nazwie zaczynającej się od ``_`` przez konwencję są traktowane jako prywatne

    .. code-block:: python

        from random import _ceil

        _ceil()
        # good IDE will display information, that you're accessing protected member

* Funkcje i zmienne o nazwie zaczynającej się od ``__`` i kończących się na ``__`` przez konwencję są traktowane jako systemowe

    .. code-block:: python

        print(__file__)

* ``_`` at the end of name when name collision

    .. code-block:: python

        def print_(text1, text2):
            print(values, sep=';', end='\n')


Single or double quotes?
------------------------
* Python nie rozróżnia czy stosujemy pojedyncze znaki cudzysłowu czy podwójne.
* Ważne jest aby wybrać jedną konwencję i się jej konsekwentnie trzymać.
* Interpreter Pythona domyślnie stosuje pojedyncze znaki cudzysłowu.
* Z tego powodu w tej książce będziemy trzymać się powyższej konwencji.
* Ma to znaczenie przy ``doctest``, który zawsze korzysta z pojedynczych i rzuca errorem jak są podwójne
* :pep:`257` -- Docstring Conventions: For multiline ``str`` always use three double quote (``"""``) characters

.. code-block:: python

    print('It\'s Watney\'s Mars')
    print("It is Watney's Mars")

.. code-block:: python

    print('<a href="http://python.astrotech.io">Python and Machine Learning</a>')

Trailing Commas
---------------
.. code-block:: python
    :caption: Yes

    FILES = ('setup.cfg',)

.. code-block:: python
    :caption: OK, but confusing

    FILES = 'setup.cfg',

Indents
-------
.. code-block:: python
    :caption: Good

    # More indentation included to distinguish this from the rest.
    def server(
            host='example.com', port=443, secure=True,
            username='myusername', password='mypassword'):
        return locals()


    # Aligned with opening delimiter.
    connection = server(host='example.com', port=443, secure=True,
                        username='myusername', password='mypassword')

    # Hanging indents should add a level.
    connection = server(
        host='example.com', port=443, secure=True,
        username='myusername', password='mypassword')

    # The best
    connection = server(
        host='example.com',
        username='myusername',
        password='mypassword',
        port=443,
        secure=True,
    )

.. code-block:: python
    :caption: Bad

    # Further indentation required as indentation is not distinguishable.
    def Connection(
        host='example.com', port=1337,
        username='myusername', password='mypassword'):
        return host, port, username, password


    # Arguments on first line forbidden when not using vertical alignment.
    connection = Connection(host='example.com', port=1337,
        username='myusername', password='mypassword')

Brackets
--------
.. code-block:: python

    vector = [
        1, 2, 3,
        4, 5, 6,
    ]

    result = some_function_that_takes_arguments(
        'a', 'b', 'c',
        'd', 'e', 'f',
    )

    vector = [
        1, 2, 3,
        4, 5, 6]

    result = some_function_that_takes_arguments(
        'a', 'b', 'c',
        'd', 'e', 'f')

.. code-block:: python

    TYPE_CHOICES = [
        ('custom', _('Custom Made')),
        ('brand', _('Brand Product')),
        ('gourmet', _('Gourmet Food')),
        ('restaurant', _('Restaurant'))]

    FORM_CHOICES = [
        ('solid', _('Solid')),
        ('liquid', _('Liquid'))]

    CATEGORY_CHOICES = [
        ('other', _('Other')),
        ('fruits', _('Fruits')),
        ('vegetables', _('Vegetables')),
        ('meat', _('Meat'))]

Modules
-------
* Modules should explicitly declare the names in their public API using the ``__all__`` attribute.
* Setting ``__all__`` to an empty list indicates that the module has no public API.

Line continuation
-----------------
Linie możemy łamać poprzez stawianie znaku ukośnika ``\`` na końcu:

.. code-block:: python

    with open('/path/to/some/file/you/want/to/read') as file1, \
            open('/path/to/some/file/being/written', mode='w') as file2:
        content = file1.read()
        file2.write(content)

.. code-block:: python
    :caption: Easy to match operators with operands

    income = (gross_wages
              + taxable_interest
              + (dividends - qualified_dividends)
              - ira_deduction
              - student_loan_interest)

.. code-block:: python

    class Server:
        def __init__(self, username, password, host='example.com'
                     port=80, secure=False):

            if not instance(username, str) or not instance(password, str) or
                    not instance(host, str) or not instance(secure, bool) or
                    (not instance(port, int) and 0 < port <= 65535):
                raise TypeError(f'One of your parameters is incorrect type')

         def __str__(self):
            if secure:
                protocol = 'https'
            else:
                protocol = 'http'

            return f'{protocol}://{self.username}:{self.password}@{self.host}:{self.port}/'

    server = Server(
        host='example.com',
        username='myusername',
        password='mypassword',
        port=443,
        secure=True,
    )

Blank lines
-----------
* Surround top-level function and class definitions with two blank lines.
* Method definitions inside a class are surrounded by a single blank line.
* Extra blank lines may be used (sparingly) to separate groups of related functions.
* Use blank lines in functions, sparingly, to indicate logical sections.

.. code-block:: python

    class Server:
        def __init__(self, username, password, host='example.com'
                     port=80, secure=False):

            if not instance(username, str):
                raise TypeError(f'Username must be str')

            if not instance(password, str):
                raise TypeError(f'Password must be str')

            if not instance(port, int):
                raise TypeError(f'Port must be int')
            elif: 0 < port <= 65535
                raise ValueError(f'Port must be 0-65535')

        def __str__(self):
            if secure:
                protocol = 'https'
            else:
                protocol = 'http'

            return f'{protocol}://{self.username}:{self.password}@{self.host}:{self.port}/'

Whitespace in function calls
----------------------------
.. code-block:: python

    spam(ham[1], {eggs: 2})        # Good
    spam( ham[ 1 ], { eggs: 2 } )  # Bad

.. code-block:: python

    spam(1)     # Good
    spam (1)    # Bad

.. code-block:: python

    do_one()    # Good
    do_two()    # Good
    do_three()  # Good

    do_one(); do_two(); do_three()                  # Bad

    do_one(); do_two(); do_three(long, argument,    # Bad
                                 list, like, this)  # Bad

Whitespace in slices
--------------------
.. code-block:: python

    ham[1:9]                          # Good
    ham[1:9:3]                        # Good
    ham[:9:3]                         # Good
    ham[1::3]                         # Good
    ham[1:9:]                         # Good

    ham[1: 9]                         # Bad
    ham[1 :9]                         # Bad
    ham[1:9 :3]                       # Bad

.. code-block:: python

    ham[lower:upper]                  # Good
    ham[lower:upper:]                 # Good
    ham[lower::step]                  # Good

    ham[lower : : upper]              # Bad

.. code-block:: python

    ham[lower+offset : upper+offset]  # Good
    ham[: upper_fn(x) : step_fn(x)]   # Good
    ham[:: step_fn(x)]                # Good

    ham[lower + offset:upper + offset]    # Bad

.. code-block:: python

    ham[:upper]             # Good
    ham[ : upper]           # Bad
    ham[ :upper]            # Bad

Whitespace in assignments
-------------------------
.. code-block:: python

    x = 1                   # Good
    y = 2                   # Good
    long_variable = 3       # Good

    x             = 1       # Bad
    y             = 2       # Bad
    long_variable = 3       # Bad

.. code-block:: python

    i = i + 1               # Good
    i=i+1                   # Bad

.. code-block:: python

    submitted += 1          # Good
    submitted +=1           # Bad

Whitespace in math operators
----------------------------
.. code-block:: python

    x = x*2 - 1             # Good
    x = x * 2 - 1           # Bad

.. code-block:: python

    hypot2 = x*x + y*y      # Good
    hypot2 = x * x + y * y  # Bad

.. code-block:: python

    c = (a+b) * (a-b)      # Good
    c = (a + b) * (a - b)  # Bad

Whitespace in accessors
-----------------------
.. code-block:: python

    dct['key'] = lst[index]     # Good
    dct ['key'] = lst[ index ]  # Bad

Whitespace in functions
-----------------------
:Good:
    .. code-block:: python

        def complex(real, imag=0.0):
            return magic(r=real, i=imag)

:Bad:
    .. code-block:: python

        def complex(real, imag = 0.0):
            return magic(r = real, i = imag)

:Controversial:
    .. code-block:: python

        def move(self, left: int = 0, down: int = 0, up: int = 0, right: int = 0) -> None:
            self.set_position_coordinates(
                x=self.position.x + right - left,
                y=self.position.y + down - up
            )

Whitespace in conditionals
--------------------------
:Good:
    .. code-block:: python

        if foo == 'blah':
            do_blah_thing()

:Bad:
    .. code-block:: python

        if foo == 'blah': do_blah_thing()

        if foo == 'blah': one(); two(); three()

        if foo == 'blah': do_blah_thing()
        else: do_non_blah_thing()

Whitespace in exceptions
------------------------
:Good:
    .. code-block:: python

        try:
            do_something()
        except Exception:
            pass

:Bad:
    .. code-block:: python

        try: something()
        finally: cleanup()

Conditionals
------------
:Good:
    .. code-block:: python

        if greeting:
            pass

:Bad:
    .. code-block:: python

        if greeting == True:
            pass

        if greeting is True:
            pass


Negative Conditionals
---------------------
:Good:
    .. code-block:: python

        if name is not None:
            pass

:Bad:
    .. code-block:: python

        # if (! name == null) {}
        if not name is None:
            pass

    .. code-block:: python

        usernames = {'José', 'Max', 'Иван'}

        # if (! usernames.contains('José')) {}
        if not 'José' in usernames:
            print('I do not know you')
        else:
            print('Hello my friend')

Checking if not empty
---------------------
:Good:
    .. code-block:: python

        if sequence:
            pass

        if not sequence:
            pass

:Bad:
    .. code-block:: python

        if len(sequence):
            pass

        if not len(sequence):
            pass

Explicit return
---------------
:Good:
    .. code-block:: python

        def foo(x):
            if x >= 0:
                return math.sqrt(x)
            else:
                return None

:Bad:
    .. code-block:: python

        def foo(x):
            if x >= 0:
                return math.sqrt(x)

Explicit return value
---------------------
:Good:
    .. code-block:: python

        def bar(x):
            if x < 0:
                return None
            return math.sqrt(x)
:Bad:
    .. code-block:: python

        def bar(x):
            if x < 0:
                return
            return math.sqrt(x)

Imports
-------
* Każdy z importów powinien być w osobnej linii
* importy systemowe na górze
* importy bibliotek zewnętrznych poniżej systemowych
* importy własnych modułów poniżej bibliotek zewnętrznych
* jeżeli jest dużo importów, pomiędzy grupami powinna być linia przerwy

:Good:
    .. code-block:: python

        import os
        import sys
        import requests
        import numpy as np

    .. code-block:: python

        from datetime import date
        from datetime import time
        from datetime import datetime
        from datetime import timezone

    .. code-block:: python

        from datetime import date, time, datetime, timezone

    .. code-block:: python

        from datetime import date, time, datetime, timezone
        import os
        import sys
        from random import shuffle
        from subprocess import Popen, PIPE
        import requests
        import numpy as np

:Bad:
    .. code-block:: python

        import sys, os, requests, numpy

    .. code-block:: python

        import sys, os
        import requests, numpy

Whitespace with type annotations
--------------------------------
:Good:
    .. code-block:: python

        def function(first: str):
            pass

        def function(first: str = None):
            pass

        def function() -> None:
            pass

        def function(first: str, second: str = None, limit: int = 1000) -> int:
            pass

:Bad:
    .. code-block:: python

        def function(first: str=None):
            pass

        def function(first:str):
            pass

        def function(first: str)->None:
            pass


Magic number i magic string
---------------------------
* NO!

PEP 8, but...
-------------
* http://docs.python-requests.org/en/master/dev/contributing/#kenneth-reitz-s-code-style


Static Code Analysis
====================
.. note:: Topic is covered in details in chapters: :ref:`cicd-tools` and :ref:`cicd-pipelines`.

``pycodestyle``
---------------
* Previously known as ``pep8``
* Python style guide checker.
* ``pycodestyle`` is a tool to check your Python code against some of the style conventions in ``PEP 8``
* Plugin architecture: Adding new checks is easy
* Parseable output: Jump to error location in your editor
* Small: Just one Python file, requires only stdlib
* Comes with a comprehensive test suite

Installation
^^^^^^^^^^^^
.. code-block:: console

    $ pip install pycodestyle

Usage
^^^^^
.. code-block:: console

    $ pycodestyle FILE.py
    $ pycodestyle DIRECTORY/*.py
    $ pycodestyle DIRECTORY/
    $ pycodestyle --statistics -qq DIRECTORY/
    $ pycodestyle --show-source --show-pep8 FILE.py

Configuration
^^^^^^^^^^^^^
* ``setup.cfg``

.. code-block:: ini

    [pycodestyle]
    max-line-length = 120
    ignore = E402,W391


Assignments
===========

.. todo:: Convert assignments to literalinclude

Cleanup your file
-----------------
* Assignment: Cleanup your file
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min
* Filename: :download:`assignments/cleanup.py`

English:
    .. todo:: English Translation

Polish:
    #. Install ``pycodestyle``
    #. Run ``pycodestyle`` on your last script
    #. Fix all errors
    #. Run ``pycodestyle`` on directory with all of your scripts
    #. Fix all errors
