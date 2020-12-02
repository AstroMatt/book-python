.. _Type Str Methods:

****************
Type Str Methods
****************


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


Rationale
=========
.. highlights::
    * ``str`` is immutable
    * ``str`` methods create a new modified ``str``

.. code-block:: python

    a = 'Python'
    a.replace('P', 'C')

    print(a)  # Python

.. code-block:: python

    a = 'Python'
    b = a.replace('P', 'C')

    print(a)  # Python
    print(b)  # Cython

.. code-block:: python

    a = 'Python'
    a = a.replace('P', 'C')

    print(a)  # Cython


Strip Whitespace
================
.. code-block:: python

    name = '\tJan Twardowski    \n'

    name.strip()        # 'Jan Twardowski'
    name.rstrip()       # '\tJan Twardowski'
    name.lstrip()       # 'Jan Twardowski    \n'

.. code-block:: python

    cmd = input('Type system command to execute: ').strip()
    print(cmd)


Change Case
===========
.. highlights::
    * Unify data format before analysis

.. code-block:: python

    name = 'Angus MacGyver III'

    name.upper()       # 'ANGUS MACGYVER III'
    name.lower()       # 'angus macgyver iii'
    name.title()       # 'Angus Macgyver Iii'
    name.capitalize()  # 'Angus macgyver iii'


Replace
=======
.. code-block:: python

    name = 'Jan Twardowski Iii'

    name.replace('Iii', 'III')
    # 'Jan Twardowski III'

.. code-block:: python
    :caption: This is naive sanitization. Reverse ordering will allow deleting files

    cmd = input('Type system command to execute: ').strip()
    # Type system command to execute: ls && rm -fr /

    cmd = cmd.replace('&&', '#')
    print(cmd)
    # ls # rm -fr /


Starts With
===========
.. code-block:: python

    'Jan Twardowski'.startswith('Jan')  # True

.. code-block:: python

    START = ('vir', 'ver')

    'virginica'.startswith(START)       # True
    'versicolor'.startswith(START)      # True
    'setosa'.startswith(START)          # False

.. code-block:: python
    :caption: Will check if command typed by user startswith disallowed command

    forbidden = ('rm', 'cp', 'mv')

    cmd = input('Type system command to execute: ').strip()
    cmd.startswith(forbidden)


Ends With
=========
.. code-block:: python

    'Jan Twardowski'.endswith(';')      # False

.. code-block:: python

    allowed = ('gov', 'int')

    'nasa.gov'.endswith(allowed)         # True
    'esa.int'.endswith(allowed)          # True
    'roscosmos.ru'.endswith(allowed)     # False

.. code-block:: python
    :caption: Will check if command typed by user startswith disallowed command

    allowed = ('gov', 'int')

    email = input('Type your email: ').strip()
    email.endswith(allowed)


Split by Line
=============
.. code-block:: python

    DATA = """First Line
    Second Line
    Third Line
    """

    DATA.splitlines()
    # [
    #   'First Line',
    #   'Second Line',
    #   'Third Line'
    # ]


Split by Character
==================
.. highlights::
    * No argument - any number of whitespaces

.. code-block:: python

    setosa = '5.1,3.5,1.4,0.2,setosa'

    setosa.split(',')
    # ['5.1', '3.5', '1.4', '0.2', 'setosa']

.. code-block:: python

    text = 'We choose to go to the Moon'

    text.split(' ')
    # ['We', 'choose', 'to', 'go', 'to', 'the', 'Moon']

    text.split()
    # ['We', 'choose', 'to', 'go', 'to', 'the', 'Moon']

.. code-block:: python

    text = '10.13.37.1      nasa.gov esa.int roscosmos.ru'

    text.split(' ')
    # ['10.13.37.1', '', '', '', '', '', 'nasa.gov', 'esa.int', 'roscosmos.ru']

    text.split()
    # ['10.13.37.1', 'nasa.gov', 'esa.int', 'roscosmos.ru']

.. code-block:: python
    :caption: Naive sanitization. For this purpose there is ``shlex.split()``

    cmd = input('Type system command to execute: ').strip()
    # Type system command to execute: ls && rm -fr /

    cmd.split('&&')
    # ['ls', 'rm -fr /']


Join by Character
=================
.. code-block:: python

    text = ['We', 'choose', 'to', 'go', 'to', 'the', 'Moon']

    ' '.join(text)
    # 'We choose to go to the Moon'

.. code-block:: python

    setosa = ['5.1', '3.5', '1.4', '0.2', 'setosa']

    ','.join(setosa)
    # '5.1,3.5,1.4,0.2,setosa'

.. code-block:: python

    crew = ['Mark Watney', 'Jan Twardowski', 'Melissa Lewis']

    '\n'.join(crew)
    # 'Mark Watney\nJan Twardowski\nMelissa Lewis'

    print('\n'.join(crew))
    # Mark Watney
    # Jan Twardowski
    # Melissa Lewis

.. code-block:: python

    TEXT = ['We choose to go to the Moon!',
            'We choose to go to the Moon in this decade and do the other things,',
            'not because they are easy, but because they are hard;',
            'because that goal will serve to organize and measure the best of our energies and skills,',
            'because that challenge is one that we are willing to accept, one we are unwilling to postpone,',
            'and one we intend to win, and the others, too.']

    print('\n'.join(TEXT))
    # We choose to go to the Moon!
    # We choose to go to the Moon in this decade and do the other things,
    # not because they are easy, but because they are hard;
    # because that goal will serve to organize and measure the best of our energies and skills,
    # because that challenge is one that we are willing to accept, one we are unwilling to postpone,
    # and one we intend to win, and the others, too.


Expand Tabs
===========
.. code-block:: python

    '01\t012\t0123\t01234'.expandtabs()
    # '01      012     0123    01234'

    '01\t012\t0123\t01234'.expandtabs(4)
    #'01  012 0123    01234'


Is Whitespace
=============
.. code-block:: python

    ''.isspace()        # False
    ' '.isspace()       # True
    '\t'.isspace()      # True
    '\n'.isspace()      # True

.. figure:: img/iss.jpg
    :width: 50%
    :align: center

    ISS - International Space Station.
    Credits: NASA/Crew of STS-132 (img: s132e012208).


Is Alphabet Characters
======================
.. code-block:: python

    'hello'.isalpha()   # True
    'hello1'.isalpha()  # False


.. _Type Str Methods is Numeric:

Is Numeric
==========
* https://docs.python.org/library/stdtypes.html#str.isdecimal
* https://docs.python.org/library/stdtypes.html#str.isdigit
* https://docs.python.org/library/stdtypes.html#str.isnumeric
* https://docs.python.org/library/stdtypes.html#str.isalnum

.. code-block:: python

    '1'.isdecimal()     # True
    '+1'.isdecimal()    # False
    '-1'.isdecimal()    # False
    '1.'.isdecimal()    # False
    '1,'.isdecimal()    # False
    '1.0'.isdecimal()   # False
    '1,0'.isdecimal()   # False
    '1_0'.isdecimal()   # False
    '10'.isdecimal()    # True

    '1'.isdigit()       # True
    '+1'.isdigit()      # False
    '-1'.isdigit()      # False
    '1.'.isdigit()      # False
    '1,'.isdigit()      # False
    '1.0'.isdigit()     # False
    '1,0'.isdigit()     # False
    '1_0'.isdigit()     # False
    '10'.isdigit()      # True

    '1'.isnumeric()     # True
    '+1'.isnumeric()    # False
    '-1'.isnumeric()    # False
    '1.'.isnumeric()    # False
    '1.0'.isnumeric()   # False
    '1,0'.isnumeric()   # False
    '1_0'.isnumeric()   # False
    '10'.isnumeric()    # True

    '1'.isalnum()       # True
    '+1'.isalnum()      # False
    '-1'.isalnum()      # False
    '1.'.isalnum()      # False
    '1,'.isalnum()      # False
    '1.0'.isalnum()     # False
    '1,0'.isalnum()     # False
    '1_0'.isalnum()     # False
    '10'.isalnum()      # True


Find Sub-String Position
========================
.. code-block:: python

    text = 'We choose to go to the Moon'

    text.find('M')      # 23
    text.find('Moo')    # 23
    text.find('x')      # -1


Contains
========
.. code-block:: python

    'Monty' in 'Python'  # False
    'Py' in 'Python'     # True
    'py' in 'Python'     # False


Count Occurrences
=================
.. code-block:: python

    text = 'Moon'

    text.count('o')     # 2
    text.count('Moo')   # 1
    text.count('x')     # 0


Remove Prefix or Suffix
=======================
.. versionadded:: Python 3.9
    :pep:`616` String methods to remove prefixes and suffixes

.. code-block:: python

    filename = '1969-apollo11.tmp'

    filename.removeprefix('1969-')
    # 'apollo11.tmp'

    filename.removesuffix('.tmp')
    # '1969-apollo11'

    filename.removeprefix('1969-').removesuffix('.tmp')
    # 'apollo11'


Method Chaining
===============
.. code-block:: python

    a = 'Python'

    a = a.upper()
    a = a.replace('P', 'C')
    a = a.title()

    print(a)
    # Cython

.. code-block:: python

    a = 'Python'
    a = a.upper().replace('P', 'C').title()

    print(a)
    # Cython

.. code-block:: python

    a.upper().replace('P', 'C').title()

    # a -> 'Python'
    # 'Python'.upper() -> 'PYTHON'
    # 'PYTHON'.replace('P', 'C') -> 'CYTHON'
    # 'CYTHON'.title() -> 'Cython'

.. code-block:: python
    :caption: Note, that there cannot be any char, not even space after ``\`` character

    a = 'Python'

    a = a \
        .upper() \
        .replace('P', 'C') \
        .title()

    print(a)

.. code-block:: python

    a = 'Python'

    a = (a
        .upper()
        .replace('P', 'C')
        .title())

    print(a)

.. code-block:: python

    a = 'Python'

    a = a.upper().startswith('P').replace('P', 'C')
    # Traceback (most recent call last):
    # AttributeError: 'bool' object has no attribute 'replace'


Cleaning User Input
===================
.. highlights::
    * 80% of machine learning and data science is cleaning data
    * Is This the Same Address?
    * This is a dump of distinct records of a single address
    * Which one of the below is a true address?

.. code-block:: text
    :caption: Addresses

    'ul. Jana III Sobieskiego'
    'ul Jana III Sobieskiego'
    'ul.Jana III Sobieskiego'
    'ulicaJana III Sobieskiego'
    'Ul. Jana III Sobieskiego'
    'UL. Jana III Sobieskiego'
    'ulica Jana III Sobieskiego'
    'Ulica. Jana III Sobieskiego'

    'os. Jana III Sobieskiego'

    'Jana 3 Sobieskiego'
    'Jana 3ego Sobieskiego'
    'Jana III Sobieskiego'
    'Jana Iii Sobieskiego'
    'Jana IIi Sobieskiego'
    'Jana lll Sobieskiego'  # three small letters 'L'

.. code-block:: text
    :caption: Streets

    'ul'
    'ul.'
    'Ul.'
    'UL.'
    'ulica'
    'Ulica'

    'os'
    'os.'
    'Os.'
    'osiedle'
    'oś'
    'oś.'
    'Oś.'
    'ośedle'

    'pl'
    'pl.'
    'Pl.'
    'plac'

    'al'
    'al.'
    'Al.'
    'aleja'
    'aleia'
    'alei'
    'aleii'
    'aleji'

.. code-block:: text
    :caption: House and Apartment Number

    'Ćwiartki 3/4'
    'Ćwiartki 3 / 4'
    'Ćwiartki 3 m. 4'
    'Ćwiartki 3 m 4'
    'Brighton Beach 1st apt 2'
    'Brighton Beach 1st apt. 2'
    'Myśliwiecka 3/5/7'

    'Jana Twardowskiego 180f/8f'
    'Jana Twardowskiego 180f/8'
    'Jana Twardowskiego 180/8f'

    'Jana Twardowskiego III 3 m. 3'
    'Jana Twardowskiego 13d bud. A piętro II sala 3'

.. code-block:: text
    :caption: Phone Numbers

    +48 (12) 355 5678
    +48 123 555 678

    123 555 678
    123555678
    +48123555678
    +48 12 355 5678
    +48 123-555-678
    +48 123 555 6789
    +1 (123) 555-6789
    +1 (123).555.6789

    +1 800-python
    +1 800-798466

    +48 123 555 678 wew. 1337
    +48 123555678,1
    +48 123555678,1,,2


Assignments
===========

.. literalinclude:: assignments/type_str_normalize.py
    :caption: :download:`Solution <assignments/type_str_normalize.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_str_clean.py
    :caption: :download:`Solution <assignments/type_str_clean.py>`
    :end-before: # Solution
