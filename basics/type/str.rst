.. _Type Str:

********
Type Str
********


Type Definition
===============
.. highlights::
    * ``str`` is a sequence

.. code-block:: python
    :caption: ``str`` Type Definition

    data = ''
    data = 'Jan Twardowski'

    data = """First line
    Second line
    Third line"""
    # 'First line\nSecond line\nThird line'


Type Casting
============
* ``str()`` converts argument to ``str``
* ``print()`` before printing on the screen runs ``str()`` on its arguments

.. code-block:: python
    :caption: ``str()`` converts argument to ``str``

    str('Moon')                     # 'Moon'
    str(1969)                       # '1969'
    str(1.337)                      # '1.337'


Single and Double Quotes
========================
.. highlights::
    * ``"`` and ``'`` works the same
    * Choose one and keep consistency in code
    * Python console prefers single quote (``'``) character
    * It matters for ``doctest``, which compares two outputs character by character
    * For multiline always use double quote characters to be consistent with the docstring convention :pep:`257`

.. code-block:: python
    :caption: Python console prefers single quote (``'``)

    data = 'My name is José Jiménez'

    print(data)
    # 'My name is José Jiménez'

.. code-block:: python
    :caption: Python console prefers single quote (``'``)

    data = "My name is José Jiménez"

    print(data)
    # 'My name is José Jiménez'

.. code-block:: python
    :caption: It's better to use double quotes, when text has apostrophes. This is the behavior of Python console.

    data = 'My name\'s José Jiménez'

    print(data)
    # "My name's José Jiménez"

.. code-block:: python
    :caption: HTML and XML uses double quotes to enclose attribute values, hence it's better to use single quotes for the string.

    data = '<a href="http://python.astrotech.io">Python and Machine Learning</a>'

    print(data)
    # '<a href="http://python.astrotech.io">Python and Machine Learning</a>'

.. code-block:: python
    :caption: For multiline always use double quote characters to be consistent with the docstring convention :pep:`257`

    data = """My name's "José Jiménez""""
    data = '''My name\'s "José Jiménez"'''


Docstring
=========
.. highlights::
    * For multiline always use double quote characters to be consistent with the docstring convention :pep:`257`
    * More information in :ref:`Function Doctest`

.. code-block:: python
    :caption: If assigned to variable, it serves as multiline ``str`` otherwise it's a docstring.

    """
    We choose to go to the Moon!
    We choose to go to the Moon in this decade and do the other things,
    not because they are easy, but because they are hard;
    because that goal will serve to organize and measure the best of our energies and skills,
    because that challenge is one that we are willing to accept, one we are unwilling to postpone,
    and one we intend to win, and the others, too.
    """


Escape Characters
=================
.. highlights::
    * ``\n`` - New line (ENTER)
    * ``\t`` - Horizontal Tab (TAB)
    * ``\'`` - Single quote ``'`` (escape in single quoted strings)
    * ``\"`` - Double quote ``"`` (escape in double quoted strings)
    * ``\\`` - Backslash ``\`` (to indicate, that this is not escape char)
    * More information in :ref:`Builtin Printing`
    * https://en.wikipedia.org/wiki/List_of_Unicode_characters

.. code-block:: python

    print('\U0001F680')     # 🚀


Format String
=============
.. highlights::
    * String interpolation (variable substitution)
    * Since Python 3.6
    * Used for ``str`` concatenation

.. code-block:: python

    name = 'José Jiménez'

    print(f'My name... {name}')
    # My name... José Jiménez

.. code-block:: python

    firstname = 'José'
    lastname = 'Jiménez'
    result = f'My name... {firstname} {lastname}'

    print(result)
    # My name... José Jiménez


Unicode Literal
===============
.. highlights::
    * In Python 3 ``str`` is Unicode
    * In Python 2 ``str`` is Bytes
    * In Python 3 ``u'...'`` is only for compatibility with Python 2

.. code-block:: python

    u'zażółć gęślą jaźń'


Bytes Literal
=============
.. highlights::
    * Used while reading from low level devices and drivers
    * Used in sockets and HTTP connections
    * ``bytes`` is a sequence of octets (integers between 0 and 255)
    * ``bytes.decode()`` conversion to unicode ``str``
    * ``str.encode()`` conversion to ``bytes``

.. code-block:: python

    'Moon'              # Unicode (in Python 3)
    b'Moon'             # Bytes Literal

.. code-block:: python

    'Moon'.encode()     # b'Moon'
    b'Moon'.decode()    # 'Moon'


Raw String
==========
.. highlights::
    *  Escapes does not matters

.. code-block:: python
    :caption: In Regular Expressions

    r'[a-z0-9]\n'

.. code-block:: python

    print(r'C:\Users\Admin\file.txt')
    # C:\Users\Admin\file.txt

    print('C:\\Users\\Admin\\file.txt')
    # C:\Users\Admin\file.txt

    print('C:\Users\Admin\file.txt')
    # Traceback (most recent call last):
    #     ...
    # SyntaxError: (unicode error) 'unicodeescape'
    #   codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

* Problem: ``\Users``
* after ``\U...`` python expects Unicode codepoint in hex
* ``s`` is invalid hexadecimal character


Reading Input
=============
.. highlights::
    * ``input()`` returns ``str``
    * Good practice: add space at the end of prompt
    * Good practice: always ``.strip()`` text from user input
    * Good practice: always sanitize values from user prompt

.. code-block:: python
    :caption: ``input()`` function argument is prompt text, which "invites" user to enter specific information. Note colon space (": ") at the end. Space is needed to separate user input from prompt.

    name = input('What is your name: ')  # Jan Twardowski<ENTER>

    print(name)     # 'Jan Twardowski'
    type(name)      # <class 'str'>

.. code-block:: python
    :caption: ``input()`` always returns a ``str``. To get numeric value type casting to ``int`` is needed.

    age = input('What is your age: ')  # 42<ENTER>

    print(age)      # '42'
    type(age)       # <class 'str'>

    age = int(age)
    print(age)      # 42
    type(age)       # <class 'int'>

.. code-block:: python
    :caption: Conversion to ``float`` handles decimals, which ``int`` does not support

    age = input('What is your age: ')  # 42.5<ENTER>

    age = int(age)      # ValueError: invalid literal for int() with base 10: '42.5'
    age = float(age)    # 42.5

    print(age)          # 42.5
    type(age)           # <class 'int'>

.. code-block:: python
    :caption: Conversion to ``float`` cannot handle comma (',') as a decimal separator

    age = input('What is your age: ')  # 42,5<ENTER>

    age = int(age)      # ValueError: invalid literal for int() with base 10: '45,5'
    age = float(age)    # ValueError: could not convert string to float: '45,5'


Length
======
.. code-block:: python

    len('hello')
    # 5


Concatenation
=============
.. highlights::
    * Preferred string concatenation is using ``f-string`` formatting

.. code-block:: python

    'a' + 'b'
    # 'ab'

    '1' + '2'
    # '12'

.. code-block:: python

    text1 = 'a'
    text2 = 'b'

    text1 + text2
    # 'ab'

.. code-block:: python

    a = '1'
    b = '2'

    a + b
    '12'

.. code-block:: python

    '-' * 10                # '----------'
    'Beetlejuice' * 3       # 'BeetlejuiceBeetlejuiceBeetlejuice'
    'Mua' + 'Ha' * 2        # 'MuaHaHa'
    'Mua' + ('Ha'*2)        # 'MuaHaHa'
    ('Mua'+'Ha') * 2        # 'MuaHaMuaHa'

.. code-block:: python

    firstname = 'Jan'
    lastname = 'Twardowski'

    firstname + lastname
    # JanTwardowski

    firstname + ' ' + lastname
    # Jan Twardowski

String Immutability
===================
.. code-block:: python
    :caption: How many string are there in a memory?

    firstname = 'Jan'
    lastname = 'Twardowski'

    firstname + ' ' + lastname
    # Jan Twardowski

.. code-block:: python
    :caption: How many string are there in a memory?

    firstname = 'Jan'
    lastname = 'Twardowski'

    f'{firstname} {lastname}'
    # Jan Twardowski

.. code-block:: python
    :caption: How many string are there in a memory?

    firstname = 'Jan'
    lastname = 'Twardowski'
    age = 42

    'Hello ' + firstname + ' ' + lastname + ' ' + str(age) + '!'
    # 'Hello Jan Twardowski 42!'

.. code-block:: python
    :caption: How many string are there in a memory?

    firstname = 'Jan'
    lastname = 'Twardowski'
    age = 42

    f'Hello {firstname} {lastname} {age}!'
    # 'Hello Jan Twardowski 42!'

.. figure:: img/memory-str-1.png
    :align: center
    :scale: 50%

    Define str

.. figure:: img/memory-str-2.png
    :align: center
    :scale: 50%

    Define another str with the same value

.. figure:: img/memory-str-3.png
    :align: center
    :scale: 50%

    Define another str with different value


Assignments
===========

Type String Input
-----------------
* Assignment name: Type String Input
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/type_str_input.py`

:English:
    #. Ask user to input text
    #. Print number of characters

:Polish:
    #. Poproś użytkownika o wprowadzenie tekstu
    #. Wypisz liczbę znaków

Type String Emoticon
--------------------
* Assignment name: Type String Emoticon
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/type_str_emoticon.py`

:English:
    #. Ask user to input name
    #. Print ``hello NAME EMOTICON``, where:

        * NAME is a name read from user
        * EMOTICON is Unicode Codepoint "\U0001F642"

:Polish:
    #. Poproś użytkownika o wprowadzenie imienia
    #. Wypisz ``hello NAME EMOTICON``, gdzie:

        * NAME to imię wczytane od użytkownika
        * EMOTICON to Unicode Codepoint "\U0001F642"

:The whys and wherefores:
    * Variable declaration
    * Print formatting
    * Reading input data from user

Type String Quotes
------------------
* Assignment name: Type String Quotes
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/type_str_quotes.py`

:English:
    #. Ask user to input name
    #. To print use f-string formatting
    #. Note, that second line starts with tab
    #. Value ``NAME`` in double quotes is a name read from user
    #. Mind the different quotes, apostrophes, tabs and newlines
    #. Do not use neither space not enter - use ``\n`` and ``\t``
    #. Do not use string addition (``str + str``)
    #. Compare result with "Output" section (see below)

:Polish:
    #. Poproś użytkownika o wprowadzenie imienia
    #. Do wypisania użyj f-string formatting
    #. Zauważ, że druga linijka zaczyna się od tabulacji
    #. Wartość ``NAME`` w podwójnych cudzysłowach to ciąg od użytkownika
    #. Zwróć uwagę na znaki apostrofów, cudzysłowów, tabulacji i nowych linii
    #. Nie używaj spacji ani klawisza enter - użyj ``\n`` i ``\t``
    #. Nie korzystaj z dodawania stringów (``str + str``)
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        '''My name... "NAME".
            I'm an """astronaut!"""'''

:The whys and wherefores:
    * Variable declaration
    * Print formatting
    * Reading input data from user
