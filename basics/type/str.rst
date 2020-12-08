Type Str
========


Definition
----------
* ``str`` is a sequence

    >>> data = ''
    >>> data = 'Jan Twardowski'
    >>> data =  'First line\nSecond line\nThird line'
    >>>
    >>> data = """First line
    ... Second line
    ... Third line"""


Type Casting
------------
Builtin function  ``str()`` converts argument to ``str``

    >>> str('Moon')
    'Moon'
    >>> str(1969)
    '1969'
    >>> str(1.337)
    '1.337'

Builtin function ``print()`` before printing on the screen runs ``str()`` on its arguments

    >>> print(1969)
    1969

Single and Double Quotes
------------------------
* ``"`` and ``'`` works the same
* Choose one and keep consistency in code
* Python console prefers single quote (``'``) character
* It matters for ``doctest``, which compares two outputs character by character
* :pep:`257` -- Docstring Conventions: For multiline ``str`` always use three double quote (``"""``) characters


Python console prefers single quote (``'``):

    >>> data = 'My name is José Jiménez'
    >>> data
    'My name is José Jiménez'

Python console prefers single quote (``'``):

    >>> data = "My name is José Jiménez"
    >>> data
    'My name is José Jiménez'

It's better to use double quotes, when text has apostrophes. This is the behavior of Python console:

    >>> data = 'My name\'s José Jiménez'
    >>> data
    "My name's José Jiménez"

HTML and XML uses double quotes to enclose attribute values, hence it's better to use single quotes for the string:

    >>> data = '<a href="http://python.astrotech.io">Python and Machine Learning</a>'
    >>> data
    '<a href="http://python.astrotech.io">Python and Machine Learning</a>'

:pep:`257` -- Docstring Conventions: For multiline ``str`` always use three double quote (``"""``) characters

    >>> data = """My name's \"José Jiménez\""""
    >>> data = '''My name\'s "José Jiménez"'''


Docstring
---------
* :pep:`257` -- Docstring Conventions: For multiline ``str`` always use three double quote (``"""``) characters
* More information in :ref:`Function Doctest`

If assigned to variable, it serves as multiline ``str`` otherwise it's a docstring.

    >>> TEXT = """
    ... We choose to go to the Moon!
    ... We choose to go to the Moon in this decade and do the other things,
    ... not because they are easy, but because they are hard;
    ... because that goal will serve to organize and measure the best of our energies and skills,
    ... because that challenge is one that we are willing to accept, one we are unwilling to postpone,
    ... and one we intend to win, and the others, too.
    ... """


Escape Characters
-----------------
* ``\n`` - New line (ENTER)
* ``\t`` - Horizontal Tab (TAB)
* ``\'`` - Single quote ``'`` (escape in single quoted strings)
* ``\"`` - Double quote ``"`` (escape in double quoted strings)
* ``\\`` - Backslash ``\`` (to indicate, that this is not escape char)
* More information in :ref:`Builtin Printing`
* https://en.wikipedia.org/wiki/List_of_Unicode_characters

    >>> print('\U0001F680')
    🚀

    >>> a = '\U0001F9D1'  # 🧑
    >>> b = '\U0000200D'  # ''
    >>> c = '\U0001F680'  # 🚀

    >>> astronaut = a + b + c
    >>> print(astronaut)
    🧑‍🚀


Format String
-------------
* String interpolation (variable substitution)
* Since Python 3.6
* Used for ``str`` concatenation

    >>> name = 'José Jiménez'
    >>> print(f'My name... {name}')
    My name... José Jiménez

    >>> firstname = 'José'
    >>> lastname = 'Jiménez'
    >>> result = f'My name... {firstname} {lastname}'
    >>> print(result)
    My name... José Jiménez


Unicode Literal
---------------
* In Python 3 ``str`` is Unicode
* In Python 2 ``str`` is Bytes
* In Python 3 ``u'...'`` is only for compatibility with Python 2

    >>> u'zażółć gęślą jaźń'
    'zażółć gęślą jaźń'


Bytes Literal
-------------
* Used while reading from low level devices and drivers
* Used in sockets and HTTP connections
* ``bytes`` is a sequence of octets (integers between 0 and 255)
* ``bytes.decode()`` conversion to unicode ``str``
* ``str.encode()`` conversion to ``bytes``

    >>> data = 'Moon'   # Unicode Literal
    >>> data = u'Moon'  # Unicode Literal
    >>> data = b'Moon'  # Bytes Literal

    >>> data = 'Moon'
    >>>
    >>> type(data)
    <class 'str'>
    >>> data.encode()
    b'Moon'

    >>>data = b'Moon'
    >>>
    >>> type(data)
    <class 'bytes'>
    >>> data.decode()
    'Moon'


Raw String
----------
* Escapes does not matters

In Regular Expressions:

    >>> r'[a-z0-9]\n'
    '[a-z0-9]\\n'

    >>> print(r'C:\Users\Admin\file.txt')
    C:\Users\Admin\file.txt
    >>>
    >>> print('C:\\Users\\Admin\\file.txt')
    C:\Users\Admin\file.txt
    >>>
    >>> print('C:\Users\Admin\file.txt')
    Traceback (most recent call last):
    SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

* Problem: ``\Users``
* after ``\U...`` python expects Unicode codepoint in hex i.e. '\\U0001F680' which is 🚀 emoticon
* ``s`` is invalid hexadecimal character
* Only valid characters are ``0123456789abcdefABCDEF``


Concatenation
-------------
* Preferred string concatenation is using ``f-string`` formatting

    >>> 'a' + 'b'
    'ab'
    >>> '1' + '2'
    '12'

    >>> a = 'a'
    >>> b = 'b'
    >>>
    >>> a + b
    'ab'

    >>> a = '1'
    >>> b = '2'
    >>>
    >>> a + b
    '12'

    >>> '*' * 10
    '**********'
    >>> 'Beetlejuice' * 3
    'BeetlejuiceBeetlejuiceBeetlejuice'
    >>> 'Mua' + 'Ha' * 2
    'MuaHaHa'
    >>> 'Mua' + ('Ha'*2)
    'MuaHaHa'
    >>> ('Mua'+'Ha') * 2
    'MuaHaMuaHa'

    >>> firstname = 'Jan'
    >>> lastname = 'Twardowski'
    >>>
    >>> firstname + lastname
    'JanTwardowski'
    >>>
    >>> firstname + ' ' + lastname
    'Jan Twardowski'


Length
------
    >>> len('hello')
    5


Reading Input
-------------
* ``input()`` returns ``str``
* Good practice: add space at the end of prompt
* Good practice: always ``.strip()`` text from user input
* Good practice: always sanitize values from user prompt

``input()`` function argument is prompt text, which "invites" user to enter specific information. Note colon space (": ") at the end. Space is needed to separate user input from prompt.

Note, that the line ``input = lambda x: 'Mark Watney'`` is only for testing purposes (it is called "Stub"), and you should not do that in your programs! This assumes, that user will input str ``Mark Watney``

    >>> # Assume user will input 'Mark Watney' and then hit ENTER key
    >>> input = lambda x: 'Mark Watney'  # Don't do this in your code
    >>>
    >>> name = input('What is your name: ')
    >>>
    >>> print(name)
    Mark Watney
    >>> type(name)
    <class 'str'>

``input()`` always returns a ``str``. To get numeric value type casting to ``int`` is needed.

    >>> # Assume user will input '42' and then hit ENTER key
    >>> input = lambda x: '42'  # Don't do this in your code
    >>>
    >>> age = input('What is your age: ')
    >>>
    >>> print(age)
    42
    >>> type(age)
    <class 'str'>
    >>>
    >>> age = int(age)
    >>> print(age)
    42
    >>> type(age)
    <class 'int'>

Conversion to ``float`` handles decimals, which ``int`` does not support:

    >>> # Assume user will input '42.5' and then hit ENTER key
    >>> input = lambda x: '42.5'  # Don't do this in your code
    >>>
    >>> age = input('What is your age: ')
    >>>
    >>> age = int(age)
    Traceback (most recent call last):
    ValueError: invalid literal for int() with base 10: '42.5'
    >>>
    >>> age = float(age)
    >>> print(age)
    42.5
    >>> type(age)
    <class 'float'>

Conversion to ``float`` cannot handle comma (',') as a decimal separator:

    >>> # Assume user will input '42,5' and then hit ENTER key
    >>> input = lambda x: '42,5'  # Don't do this in your code
    >>>
    >>> age = input('What is your age: ')
    >>>
    >>> age = int(age)
    Traceback (most recent call last):
    ValueError: invalid literal for int() with base 10: '45,5'
    >>>
    >>> age = float(age)
    Traceback (most recent call last):
    ValueError: could not convert string to float: '45,5'


Assignments
-----------
.. literalinclude:: assignments/type_str_input.py
    :caption: :download:`Solution <assignments/type_str_input.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_str_emoticon.py
    :caption: :download:`Solution <assignments/type_str_emoticon.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_str_quotes.py
    :caption: :download:`Solution <assignments/type_str_quotes.py>`
    :end-before: # Solution
