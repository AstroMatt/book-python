.. _Conditional Statements:

**********************
Conditional Statements
**********************


Positive and Negative Values
============================
.. highlights::
    Negative values:

        * empty ``bool()`` or ``False``
        * empty ``int()`` or ``0``
        * empty ``float()`` or ``0.0``
        * empty ``complex()`` or ``0+0j`` or ``0.0+0.0j``
        * empty ``str()`` or ``''``
        * empty ``tuple()`` or ``()``
        * empty ``list()`` or ``[]``
        * empty ``set()``
        * empty ``frozenset()``
        * empty ``dict()`` or ``{}``
        * ``None``

    Positive values:

        * any other


Conditional Statement
=====================
.. code-block:: text
    :caption: ``if`` generic syntax

    if <condition>:
        <do something>

.. code-block:: python
    :caption: Single line statements

    if True:
        print('First line of the true statement')

    # First line of the true statement

.. code-block:: python
    :caption: Multiline blocks

    if True:
        print('First line of the true statement')
        print('Second line of the true statement')
        print('Third line of the true statement')

    # First line of the true statement
    # Second line of the true statement
    # Third line of the true statement

.. code-block:: python
    :caption: Multiline blocks

    if True:
        print('First line of the true statement')
        print('Second line of the true statement')

        if True:
            print('First line of inner true statement')

    # First line of the true statement
    # Second line of the true statement
    # First line of inner true statement

.. code-block:: python
    :caption: Checking for simple value

    age = 7

    if age == 7:
        print('Go to school')

    # Go to school

.. code-block:: python
    :caption: Checking for simple value.

    country = 'USA'

    if country == 'USA':
        job = 'astronaut'

    print(job)
    # astronaut

.. code-block:: python
    :caption: Checking for simple value

    number = 4

    if number % 2 == 0:
        print('Even')

    # Even

.. code-block:: python
    :caption: Checking if value is in range

    age = 7

    if 0 <= age < 18:
        print('Age is between [0, 18)')

    # Age is between [0, 18)

.. code-block:: python
    :caption: Checking if value is in range

    a = 10
    b = 100

    if 0 <= a <= 50 < b:
        print('Yes')

    # Yes

.. code-block:: python
    :caption: Checking if has value

    name = input('What is your name?: ')
    # What is your name?: Jan Twardowski<ENTER>

    if name:
        print(f'My name is... {name}')

    # My name is Jan Twardowski

.. code-block:: python
    :caption: Checking if has value

    name = input('What is your name?: ')
    # What is your name?: <ENTER>

    if name:
        print(f'My name... {name}')


Unconditional Alternative
=========================
.. highlights::
    * Optional
    * Executed when condition is not met

.. code-block:: text
    :caption: ``else`` generic syntax

    if <condition>:
        <do something>
    else:
        <do something>

.. code-block:: python
    :caption: Single line statements

    if True:
        print('True statement')
    else:
        print('Else statement')

    # True statement

.. code-block:: python
    :caption: Multiline blocks

    if True:
        print('True statement, first line')
        print('True statement, second line')
    else:
        print('Else statement, first line')
        print('Else statement, second line')

    # True statement, first line
    # True statement, second line

.. code-block:: python
    :caption: Nested multiline blocks

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

    # Outer block, true statement, first line
    # Outer block, true statement, second line
    # Inner block, true statement, first line
    # Inner block, true statement, second line

.. code-block:: python

    number = 3

    if number % 2 == 0:
        print('Even')
    else:
        print('Odd')

    # Odd

.. code-block:: python
    :caption: Checking if variable is certain value

    country = 'Russia'

    if country == 'USA':
        job = 'astronaut'
    else:
        job = 'cosmonaut'

    print(job)
    # cosmonaut

.. code-block:: python
    :caption: Checking if variable is certain value

    name = input('What is your name?: ')
    # What is your name?: <ENTER>

    if name:
        print(f'My name is... {name}')
    else:
        print('Did you forget to type your name?')

    # Did you forget to type your name?

.. code-block:: python

    data = [True, False, True]

    if any(data):
        print('Yes')
    else:
        print('No')

    # Yes

.. code-block:: python

    data = [True, False, True]

    if all(data):
        print('Yes')
    else:
        print('No')

    # No


Conditional Alternative
=======================
.. highlights::
    * Used to check for additional condition if first is not met
    * In other languages is known as ``else if``

.. code-block:: text
    :caption: ``elif`` generic syntax

    if <condition>:
        <do something>
    elif <condition>:
        <do something>
    else:
        <do something>

.. code-block:: python

    language = input('What is your language?: ')
    # What is your language?: Polish<ENTER>

    if language == 'English':
        print('Hello')
    elif language == 'Russian':
        print('Здравствуйте')
    elif language == 'German':
        print('Guten Tag')
    elif language == 'Polish':
        print('Witaj')
    else:
        print("I don't speak this language")

    # Witaj


Shorthand Expressions
=====================
.. code-block:: python

    number = 3
    is_even = (number % 2 == 0 )

    print(is_even)
    # False

.. code-block:: python

    number = 3
    is_digit = (number in range(0,10))

    print(is_digit)
    # True


Conditional Expression
======================
.. code-block:: python

    number = 3

    if number in range(0,10):
        is_digit = True
    else:
        is_digit = False

    print(is_digit)
    # True

.. code-block:: python

    number = 3
    is_digit = True if number in range(0,10) else False

    print(is_digit)
    # True

.. code-block:: python

    ip = '127.0.0.1'
    protocol = 'IPv4' if '.' in ip else 'IPv6'

    print(protocol)
    # IPv4

.. code-block:: python
    :caption: Normal ``if``

    country = 'Russia'

    if country == 'USA':
        job = 'astronaut'
    else:
        job = 'cosmonaut'

    print(job)
    # cosmonaut

.. code-block:: python
    :caption: Inline ``if``

    country = 'Russia'
    job = 'astronaut' if country == 'USA' else 'cosmonaut'

    print(job)
    # astronaut

.. code-block:: python
    :caption: :ref:`Type Str Methods is Numeric`

    age = input('What is your age?: ')
    # What is your age?: 10<ENTER>

    age = float(age) if age.isnumeric() else None
    print(age)
    # 10.0


Switch
======
.. highlights::
    * No ``switch`` statement in Python!
    * ``switch`` in Object Oriented Programming is considered a bad practise
    * `PEP 275 <https://www.python.org/dev/peps/pep-0275/>`_

.. code-block:: python

    switch = {
        'English': 'Hello',
        'Russian': 'Здравствуйте',
        'German': 'Guten Tag',
        'Polish': 'Witaj',
        'default': "I don't speak this language"}


    language = input('What is your language?: ')
    # What is your language?: French<ENTER>

    switch.get(language, switch['default'])
    # "I don't speak this language"

.. code-block:: python

    def switch(key):
        data = {
            'English': 'Hello',
            'Russian': 'Здравствуйте',
            'German': 'Guten Tag',
            'Polish': 'Witaj',
            'default': "I don't speak this language"}
        return data.get(language, data['default'])


    switch('Russian')
    # 'Здравствуйте'

    switch('French')
    # "I don't speak this language"


Assignments
===========

Conditional Statements
----------------------
* Assignment name: Conditional Statements
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/conditional_statements.py`

:English:
    #. Ask user to input age
    #. User will pass only valid ``int``
    #. Print whether user is adult

:Polish:
    #. Poproś użytkownika o wprowadzenie swojego wieku
    #. Użytkownika poda tylko poprawne ``int``
    #. Wypisz czy użytkownik jest pełnoletni

:The whys and wherefores:
    * Reading input
    * Type casting
    * Conditional statements
    * Defining variables
    * Magic Number
