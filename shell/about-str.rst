.. _Type Str:

********
Type Str
********


Type Definition
===============
.. highlights::
    * ``str`` is a sequence

.. code-block:: python

    data = ''
    data = 'Jan Twardowski'

.. code-block:: python

    data =  'First line\nSecond line\nThird line'

    data = """First line
    Second line
    Third line"""
    # 'First line\nSecond line\nThird line'


Type Casting
============
* ``str()`` converts argument to ``str``
* ``print()`` before printing on the screen runs ``str()`` on its arguments

.. code-block:: python

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
    * :pep:`257` -- Docstring Conventions: For multiline ``str`` always use three double quote (``"""``) characters


.. code-block:: python
    :caption: Python console prefers single quote (``'``)

    data = 'My name is José Jiménez'
    data
    # 'My name is José Jiménez'

.. code-block:: python
    :caption: Python console prefers single quote (``'``)

    data = "My name is José Jiménez"
    data
    # 'My name is José Jiménez'

.. code-block:: python
    :caption: It's better to use double quotes, when text has apostrophes. This is the behavior of Python console.

    data = 'My name\'s José Jiménez'
    data
    # "My name's José Jiménez"

.. code-block:: python
    :caption: HTML and XML uses double quotes to enclose attribute values, hence it's better to use single quotes for the string.

    data = '<a href="http://python.astrotech.io">Python and Machine Learning</a>'
    data
    # '<a href="http://python.astrotech.io">Python and Machine Learning</a>'

.. code-block:: python
    :caption: :pep:`257` -- Docstring Conventions: For multiline ``str`` always use three double quote (``"""``) characters

    data = """My name's "José Jiménez""""
    data = '''My name\'s "José Jiménez"'''


Docstring
=========
.. highlights::
    * :pep:`257` -- Docstring Conventions: For multiline ``str`` always use three double quote (``"""``) characters
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

.. code-block:: python
    :force:

    a = '\U0001F9D1'  # 🧑
    b = '\U0000200D'  # ''
    c = '\U0001F680'  # 🚀

    a + b + c
    # '🧑\u200d🚀'

    astronaut = a + b + c
    print(astronaut)
    🧑‍🚀


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

    data = 'Moon'

    type(data)
    # <class 'str'>

    data.encode()
    # b'Moon'

.. code-block:: python

    data = b'Moon'

    type(data)
    # <class 'bytes'>

    data.decode()
    # 'Moon'


Raw String
==========
.. highlights::
    * Escapes does not matters

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
    # SyntaxError: (unicode error) 'unicodeescape'
    #   codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

* Problem: ``\Users``
* after ``\U...`` python expects Unicode codepoint in hex i.e. '\\U0001F680' which is 🚀 emoticon
* ``s`` is invalid hexadecimal character
* Only valid characters are ``0123456789abcdefABCDEF``


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

    print(name)     # Jan Twardowski
    type(name)      # <class 'str'>

.. code-block:: python
    :caption: ``input()`` always returns a ``str``. To get numeric value type casting to ``int`` is needed.

    age = input('What is your age: ')  # 42<ENTER>

    print(age)      # 42
    type(age)       # <class 'str'>

    age = int(age)
    print(age)      # 42
    type(age)       # <class 'int'>

.. code-block:: python
    :caption: Conversion to ``float`` handles decimals, which ``int`` does not support

    age = input('What is your age: ')  # 42.5<ENTER>

    age = int(age)
    # Traceback (most recent call last):
    # ValueError: invalid literal for int() with base 10: '42.5'

    age = float(age)
    print(age)          # 42.5
    type(age)           # <class 'float'>

.. code-block:: python
    :caption: Conversion to ``float`` cannot handle comma (',') as a decimal separator

    age = input('What is your age: ')  # 42,5<ENTER>

    age = int(age)
    # Traceback (most recent call last):
    # ValueError: invalid literal for int() with base 10: '45,5'

    age = float(age)
    # Traceback (most recent call last):
    # ValueError: could not convert string to float: '45,5'


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

    a = 'a'
    b = 'b'

    a + b
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
