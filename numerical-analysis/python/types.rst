*****
Types
*****


``int``
=======
.. highlights::
    * In Python 3 there is not maximal ``int`` value
    * Python 3 dynamically extends ``int``, when it's too big

.. code-block:: python

    value = 30              # 30
    value = -30             # -30

.. code-block:: python
    :caption: You can use ``_`` for easier read especially with big numbers

    million = 1000000        # 1000000
    million = 1_000_000      # 1000000

Converting to ``int``
---------------------
.. highlights::
    * Also known as "type casting"
    * ``int()`` converts argument to ``int``
    * ``int()`` does not round numbers, it returns integer value

.. code-block:: python

    int(10)                 # 10
    int(10.0)               # 10
    int(10.9)               # 10
    int(13.37)              # 13
    int(-13.37)             # -13
    int('1')                # 1
    int('-1')               # -1
    int('13.37')            # ValueError: invalid literal for int() with base 10: '1.23'
    int('-13.37')           # ValueError: invalid literal for int() with base 10: '-1.23'

Assignments
-----------
* Assignment name: Assignments
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 12 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/types_int.py`

:English:
    #. Calculate how many seconds is five minutes
    #. Calculate how many seconds is one hour
    #. Calculate how many seconds is work day (8 hours)
    #. Calculate how many seconds is work month (22 days per 8 hours)
    #. Calculate how many minutes is work week (40 hours)

:Polish:
    #. Oblicz ile sekund to pięć minut
    #. Oblicz ile sekund to jedna godzina
    #. Oblicz ile sekund to dzień pracy (8 godzin)
    #. Oblicz ile sekund to miesiąc pracy (22 dni po 8 godzin)
    #. Oblicz ile minut to tydzień pracy (40 godzin)

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Mathematical operations

:Hints:
    * 1 h = 60 min
    * 1 min = 60 s


``float``
=========
.. code-block:: python

    value = 13.37           # 13.37
    value = -13.37          # -13.37

.. code-block:: python
    :caption: Notation without leading or trailing zero. Used by ``numpy``

    value = 10.             # 10.0
    value = .44             # 0.44

.. code-block:: python
    :caption: Engineering notation

    million = 1e6           # 1000000.0
    million = 1E6           # 1000000.0
    +1e6                    # 1000000.0
    -1e6                    # -1000000.0
    1e-3                    # 0.001
    1e-4                    # 0.0001
    1e-5                    # 1e-05
    1e-6                    # 1e-06
    1.337 * 1e3             # 1337.0
    1.337 * 1e-3            # 0.001337

Converting to ``float``
-----------------------
.. highlights::
    * Also known as "type casting"
    * ``float()`` converts argument to ``float``

.. code-block:: python

    float(10)               # 10.0
    float(-10)              # -10.0
    float(10.5)             # 10.5
    float(-10.5)            # -10.5
    float(13.37)            # 13.37
    float(-13.37)           # -13.37
    float('+13.37')         # 13.37
    float('-13.37')         # -13.37
    float('13,37')          # ValueError: could not convert string to float: '13,37'
    float('-13,37')         # ValueError: could not convert string to float: '-13,37'

Assignments
-----------
* Assignment name: Assignments
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/types_float.py`

:English:
    #. Use code from "Input" section (see below)
    #. Declare variable for holding value of 1337 meters
    #. Print values in other units
    #. Convert data to types shown in comments at the right side
    #. Instead ``...`` substitute calculated and converted values
    #. Non-functional requirements:

        * Do not use ``input()``

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj zmienną dla przechowywania wartości 1337 metrów
    #. Wypisz wartość w różnych jednostkach
    #. Przekonwertuj dane do typów podanych w komentarzu po prawej stronie
    #. Zamiast ``...`` podstaw wyliczone i przekonwertowane wartości
    #. Wymagania niefunkcjonalne:

        * Nie używaj ``input()``

:Input:
    .. code-block:: python

        print(f'Meters: {...}')                              # int
        print(f'Kilometers: {...}')                          # int
        print(f'Miles: {...}')                               # float
        print(f'Nautical Miles: {...}')                      # float
        print(f'm: {...}, km: {...}, mi: {...}, nm: {...}')  # int, int, float, float

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Print formatting
    * Mathematical operations
    * Separation of business logic and view

:Hints:
    * 1000 m = 1 km
    * 1608 m = 1 mile
    * 1852 m = 1 nautical mile


``str``
=======
.. code-block:: python

    data = ''
    data = 'Jan Twardowski'

.. code-block:: python
    :caption: Multiline ``str``. Always use double quote characters to be consistent with the docstring convention :pep:`257`

    data = """First line
    Second line
    Third line"""
    # 'First line\nSecond line\nThird line'

    data = """
        First line
        Second line
        Third line
    """
    # '\n        First line\n        Second line\n        Third line\n    '

Single or double quote?
-----------------------
.. highlights::
    * ``"`` and ``'`` works the same
    * Choose one and keep consistency in code
    * Python console uses ``'``
    * it matters for ``doctest``, which compares two outputs character by character

.. code-block:: python

    data = "Jan Twardowski"
    data = 'Jan Twardowski'
    data = """Jan Twardowski"""
    data = '''Jan Twardowski'''
    data = """My name's "José Jiménez""""
    data = '''My name's "José Jiménez"'''

.. code-block:: python
    :caption: When to use single or double quotes?

    data = 'It\'s Twardowski\'s Moon.'
    data = "It's Twardowski's Moon."
    data = '<a href="http://python.astrotech.io">Python and Machine Learning</a>'

Type casting to ``str``
-----------------------
.. code-block:: python

    str('hello')        # 'hello'
    str(1969)           # '1969'
    str(13.37)          # '13.37'

.. code-block:: python
    :caption: Print converts argument to ``str`` before printing

    print('hello')      # str('hello') -> 'hello'
    # hello

    print(10)           # str(10) -> '10'
    # 10

Escape characters
-----------------
.. highlights::
    * ``\r\n`` - is used on windows
    * ``\n`` - is used everywhere else

.. csv-table:: Escape characters
    :header: "Sequence", "Description"
    :widths: 15, 85

    "``\n``", "New line  (LF - Linefeed)"
    "``\r``", "Carriage Return (CR)"
    "``\t``", "Horizontal Tab (TAB)"
    "``\'``", "Single quote ``'``"
    "``\""``", "Double quote ``""``"
    "``\\``", "Backslash ``\``"
    "``\a``", "Bell (BEL)"
    "``\b``", "Backspace (BS)"
    "``\f``", "New page (FF - Form Feed)"
    "``\v``", "Vertical Tab (VT)"
    "``\uF680``", "Character with 16-bit (2 bytes) hex value ``F680``"
    "``\U0001F680``", "Character with 32-bit (4 bytes) hex value ``0001F680``"
    "``\o755``", "ASCII character with octal value ``755``"
    "``\x1F680``", "ASCII character with hex value ``1F680``"

.. code-block:: python

    print('\U0001F680')     # 🚀

Characters before strings
-------------------------
.. highlights::
    * ``f'string'`` - Format string
    * ``u'string'`` - Unicode literals
    * ``b'string'`` - Bytes literals
    * ``r'string'`` - Raw string

.. code-block:: python
    :caption: Format string (string interpolation)

    firstname = 'Jan'
    lastname = 'Twardowski'

    print(f'My name is {lastname}')
    # My name is Twardowski

    name = f'{firstname} {lastname}'
    print(name)
    # Jan Twardowski

.. code-block:: python
    :caption: Unicode literals. In Python 3 ``u'...'`` is only for compatibility with Python 2

    u'zażółć gęślą jaźń'

.. code-block:: python
    :caption: Bytes literals. Used in sockets and HTTP connections. Use ``bytes.decode()`` or ``str.encode()`` for conversion.

    b'this is bytes literals'

.. code-block:: python
    :caption: Raw String. Escapes does not matters

    pattern = r'[a-z0-9]\n'

    print(r'C:\Users\Admin\file.txt')
    # C:\Users\Admin\file.txt

    print('C:\Users\Admin\file.txt')
    # SyntaxError: (unicode error) 'unicodeescape'
    #   codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

Reading user input
------------------
.. highlights::
    * ``input()`` returns ``str``
    * Good practice: add space at the end of prompt

.. code-block:: python

    name = input('Type your name: ')
    # User inputs: Jan Twardowski

    print(name)     # 'Jan Twardowski'
    type(name)      # <class 'str'>

.. code-block:: python

    age = input('Type your age: ')
    # User inputs: 42

    print(age)      # '42'
    type(age)       # <class 'str'>

Methods
-------
.. code-block:: python
    :caption: Length of a ``str``

    len('Jan')      # 3
    len('')         # 0

Assignments
-----------
* Assignment name: Assignments
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/types_str.py`

:English:
    * Ask user to input text
    * Print number of characters

:Polish:
    * Poproś użytkownika o wprowadzenie tekstu
    * Wypisz liczbę znaków


``bool``
========
.. code-block:: python

    data = True                 # True
    data = False                # False

Converting to ``bool``
----------------------
.. code-block:: python
    :caption: Negative values

    bool(False)                 # False
    bool(None)                  # False
    bool(0)                     # False
    bool(0.0)                   # False
    bool(0+0j)                  # False
    bool(0.0+0.0j)              # False
    bool(str())                 # False
    bool(tuple())               # False
    bool(dict())                # False
    bool(set())                 # False
    bool('')                    # False
    bool(())                    # False
    bool([])                    # False
    bool({})                    # False

.. code-block:: python
    :caption: Positive values

    bool(1)                     # True
    bool(1.0)                   # True
    bool('Jan Twardowski')      # True


Boolean logic
=============

Using ``and``
-------------
.. code-block:: python

    True and True               # True
    True and False              # False
    False and True              # False
    False and False             # False

.. code-block:: python

    1 and 1                     # True
    1 and 0                     # False
    0 and 1                     # False
    0 and 0                     # False

.. code-block:: python

    'Jan' and 'Jan'             # True
    'Jan' and ''                # False
    '' and 'Jan'                # False
    '' and ''                   # False

.. code-block:: python

    'Jan' and 1                 # True
    'Jan' and 0                 # False
    0.0 and 'Jan'               # False
    1 and False                 # False

Using ``or``
------------
.. code-block:: python

    True or True                # True
    True or False               # True
    False or True               # True
    False or False              # False

.. code-block:: python

    1 or 1                      # True
    1 or 0                      # True
    0 or 1                      # True
    0 or 0                      # False

.. code-block:: python

    'José' or 'Иван'            # True
    'José' or ''                # True
    '' or 'José'                # True
    '' or ''                    # False

.. code-block:: python

    1 or 'Иван'                 # True
    True or ''                  # True
    0 or True                   # True
    0.0 or False                # False

Using both: ``or`` and ``and``
------------------------------
.. code-block:: python

    True and True or False      # True
    True and False or False     # False
    False and False or True     # True


Logic operators
===============
.. csv-table:: Logic operators
    :header-rows: 1
    :widths: 15, 25, 60

    "Operand", "Example", "Description"
    "``x < y``", "``x < 18``", "value of ``x`` is less than ``y``"
    "``x <= y``", "``x <= 18``", "value of ``x`` is less or equal ``y``"
    "``x > y``", "``x > 18``", "value of ``x`` is greater than ``y``"
    "``x >= y``", "``x >= 18``", "value of ``x`` is greater or equal than ``y``"
    "``x == y``", "``x == 18``", "value of ``x`` is equal to ``y``"
    "``x != y``", "``x != 18``", "value of ``x`` is not equal to ``y``"


Assignments
===========

To ``bool`` or not to ``bool``
------------------------------
* Assignment name: To ``bool`` or not to ``bool``
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/types_bool.py`

:English:
    #. Use data from "Input" section (see below)
    #. Which variables are ``True``?
    #. Which variables are ``False``?

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Które zmienne są ``True``?
    #. Które zmienne są ``False``?

:Input:
    .. code-block:: python

        a = bool(False)
        b = bool(True)

        c = bool('a')
        d = bool('.')
        e = bool('0')
        f = bool('0.0')
        g = bool('')
        h = bool(' ')

        i = bool(0)
        j = bool(0.0)
        k = bool(-0)
        l = bool(-0.0)

        m = bool(int('0'))
        n = bool(float('-0'))

        o = bool(-0.0+0.0j)
        p = bool('-0.0+0.0j')

:The whys and wherefores:
    * Defining variables
    * Type casting
    * Logic types


Operators
=========

Numerical Operators
-------------------
.. code-block:: python
    :caption: Addition

    value = 10 + 2
    print(value)
    # 12

    value = 10
    value += 2
    print(value)
    # 12

.. code-block:: python
    :caption: Subtraction

    value = 10 - 2
    print(value)
    # 8

    value = 10
    value -= 2
    print(value)
    # 8

.. code-block:: python
    :caption: Multiplication

    value = 10 * 2
    print(value)
    # 20

    value = 10
    value *= 2
    print(value)
    # 20

.. code-block:: python
    :caption: Number to the ``n-th`` power

    10 ** 2         # 100
    3 ** 4          # 81
    -1 ** 2         # 1
    2 ** -1         # 0.5
    1.337 ** 3      # 2.389979753
    4 ** 0.5        # 2.0
    2 ** 0.5        # 1.4142135623730951

.. code-block:: python
    :caption: Division

    value = 10 / 2
    print(value)
    # 5

    value = 10
    value /= 2
    print(value)
    # 5

.. code-block:: python
    :caption: Quotient of division

    10 // 2         # 5
    10 // 3         # 3
    4 // 2          # 2
    5 // 2          # 2

.. code-block:: python
    :caption: Modulo. Reminder of division.

    10 % 2          # 0
    10 % 3          # 1
    4 % 2           # 0
    5 % 2           # 1

Numeric Functions
-----------------
.. code-block:: python
    :caption: Rounding numbers

    pi = 3.14159265359

    round(pi)               # 3
    round(pi, 2)            # 3.14
    round(pi, 4)            # 3.1416

    print(f'{pi:.2f}')      # 3.14
    print(f'{pi:.4f}')      # 3.1416

.. code-block:: python
    :caption: Minimal value

    min(3, 1, 5)    # 1

.. code-block:: python
    :caption: Maximal value

    max(3, 1, 5)    # 5

.. code-block:: python
    :caption: Absolute value

    abs(1)          # 1
    abs(-1)         # 1
    abs(13.37)      # 13.37
    abs(-13.37)     # 13.37

.. code-block:: python
    :caption: Number to the ``n-th`` power

    pow(10, 2)      # 100
    pow(3, 4)       # 81
    pow(-1, 2)      # 1
    pow(2, -1)      # 0.5
    pow(1.337, 3)   # 2.389979753
    pow(4, 0.5)     # 2.0
    pow(2, 0.5)     # 1.4142135623730951
