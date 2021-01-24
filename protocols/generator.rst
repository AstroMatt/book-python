.. _Generators and Comprehensions:

*****************************
Generators and Comprehensions
*****************************


Lazy evaluation
===============
* Code do not execute instantly
* Sometimes code is not executed at all!

Declaring generators
--------------------
* ``range()`` requires ``int`` arguments

.. code-block:: python
    :caption: This will not execute code!

    range(0, 5)
    range(0, 5)
    range(0, 5)

.. code-block:: python
    :caption: This will only create generator expression, but not execute it!

    numbers = range(0, 5)

    print(numbers)
    # range(0, 5)

Getting  values from generator
------------------------------
* Get all values from generator (not very efficient)

    .. code-block:: python

        numbers = range(0, 5)

        list(numbers)
        # [0, 1, 2, 3, 4]

* Generator will calculate next number for every loop iteration, forgetting previous number, and not knowing next one

    .. code-block:: python

        for i in range(0, 5):
            print(i)

        # 0
        # 1
        # 2
        # 3
        # 4

* Will generate only three numbers, and then stop and forget generator

    .. code-block:: python

        for i in range(0, 5):
            print(i)

            if i == 3:
                break

        # 0
        # 1
        # 2


Generator expressions vs. Comprehensions
========================================

Comprehensions
--------------
* Executes instantly

.. code-block:: python

    list(x for x in range(0, 5))        # [0, 1, 2, 3, 4]
    [x for x in range(0, 5)]            # [0, 1, 2, 3, 4]

.. code-block:: python

    set(x for x in range(0, 5))         # {0, 1, 2, 3, 4}
    {x for x in range(0, 5)}            # {0, 1, 2, 3, 4}

.. code-block:: python

    {x: x for x in range(0, 5)}         # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}

.. code-block:: python

    tuple(x for x in range(0, 5))       # (0, 1, 2, 3, 4)
    (x for x in range(0, 5))            # <generator object <genexpr> at 0x1197032a0>

.. code-block:: python

    all(x for x in range(0, 5))         # False
    any(x for x in range(0, 5))         # True
    sum(x for x in range(0, 5))         # 10

Generator Expressions
---------------------
* Lazy evaluation

.. code-block:: python

    (x for x in range(0, 5))
    # <generator object <genexpr> at 0x1197032a0>

What is the difference?
-----------------------
* Execution and assignment

    .. code-block:: python

        numbers = [x for x in range(0, 5)]

        print(numbers)
        # [0, 1, 2, 3, 4]

        print(numbers)
        # [0, 1, 2, 3, 4]

* Create generator object and assign pointer (do not execute)

    .. code-block:: python

        numbers = (x for x in range(0, 5))

        print(numbers)
        # <generator object <genexpr> at 0x111e7acd0>

        print(list(numbers))
        # [0, 1, 2, 3, 4]

        print(list(numbers))
        # []

Which one is better?
--------------------
* Comprehensions - Using values more than one
* Generators - Using value one (for example in the loop iterator)


Conditions
==========
.. code-block:: python

    [x for x in range(0, 5) if x % 2 == 0]
    # [0, 2, 4]

.. code-block:: python

    def is_even(x):
        if x % 2 == 0:
            return True
        else:
            return False

    [x for x in range(0, 5) if is_even(x)]
    # [0, 2, 4]


Returning nested objects
========================
.. code-block:: python
    :caption: Returning nested objects

    def my_function(number):
        return number, number+10

    [my_function(x) for x in range(0, 5)]
    # [
    #   (0, 10),
    #   (1, 11),
    #   (2, 12),
    #   (3, 13),
    #   (4, 14)
    # ]

.. code-block:: python
    :caption: Returning nested objects

    def my_function(number):
        if number % 2 == 0:
            return {'number': number, 'status': 'even'}
        else:
            return {'number': number, 'status': 'odd'}


    [my_function(x) for x in range(0, 5)]
    # [
    #    {'number': 0, 'status': 'even'},
    #    {'number': 1, 'status': 'odd'},
    #    {'number': 2, 'status': 'even'},
    #    {'number': 3, 'status': 'odd'},
    #    {'number': 4, 'status': 'even'},
    # ]

Nested Comprehensions
---------------------
.. code-block:: python

   DATA = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Mark', 'last_name': 'Watney'},
        {'first_name': 'Иван'},
        {'first_name': 'Jan', 'last_name': 'Twardowski', 'born': 1961},
        {'first_name': 'Melissa', 'last_name': 'Lewis', 'first_step': 1969},
    ]

    fieldnames = set()
    fieldnames.update(key for record in DATA for key in record.keys())

.. code-block:: python

   DATA = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Mark', 'last_name': 'Watney'},
        {'first_name': 'Иван'},
        {'first_name': 'Jan', 'last_name': 'Twardowski', 'born': 1961},
        {'first_name': 'Melissa', 'last_name': 'Lewis', 'first_step': 1969},
    ]

    fieldnames = set()
    fieldnames.update(key
        for record in DATA
            for key in record.keys()
    )


``yield`` Operator
==================
.. code-block:: python

    # ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),
        (5.4, 3.9, 1.7, 0.4, 'setosa'),
        (4.6, 3.4, 1.4, 0.3, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (5.7, 2.8, 4.5, 1.3, 'versicolor'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 3.3, 6.0, 2.5, 'virginica'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (4.9, 2.5, 4.5, 1.7, 'virginica'),
    ]

.. code-block:: python

    def get_species(species):
        output = []

        for record in DATA:
            if record[4] == species:
                output.append(record)

        return output


    data = get_species('setosa')

    print(data)
    # [(5.1, 3.5, 1.4, 0.2, 'setosa'),
    #  (4.9, 3.0, 1.4, 0.2, 'setosa'),
    #  (5.4, 3.9, 1.7, 0.4, 'setosa'),
    #  (4.6, 3.4, 1.4, 0.3, 'setosa')]

    for row in data:
        print(row)
    # (5.1, 3.5, 1.4, 0.2, 'setosa')
    # (4.9, 3.0, 1.4, 0.2, 'setosa')
    # (5.4, 3.9, 1.7, 0.4, 'setosa')
    # (4.6, 3.4, 1.4, 0.3, 'setosa')

.. code-block:: python

    def get_species(species):
        for record in DATA:
            if record[4] == species:
                yield record

    data = get_species('setosa')

    print(data)
    # <generator object get_species at 0x11af257c8>

    for row in data:
        print(row)
    # (5.1, 3.5, 1.4, 0.2, 'setosa')
    # (4.9, 3.0, 1.4, 0.2, 'setosa')
    # (5.4, 3.9, 1.7, 0.4, 'setosa')
    # (4.6, 3.4, 1.4, 0.3, 'setosa')


Example
=======

Filtering ``list`` items
------------------------
.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),
        (5.4, 3.9, 1.7, 0.4, 'setosa'),
        (4.6, 3.4, 1.4, 0.3, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (5.7, 2.8, 4.5, 1.3, 'versicolor'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 3.3, 6.0, 2.5, 'virginica'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (4.9, 2.5, 4.5, 1.7, 'virginica'),
    ]

    setosa = [row for row in DATA if row[4] == 'setosa']
    print(setosa)

Filtering ``dict`` items
------------------------
.. code-block:: python

    DATA = [
        {'first_name': 'Иван', 'last_name': 'Иванович', 'agency': 'Roscosmos'},
        {'first_name': 'Jose', 'last_name': 'Jimenez', 'agency': 'NASA'},
        {'first_name': 'Melissa', 'last_name': 'Lewis', 'agency': 'NASA'},
        {'first_name': 'Alex', 'last_name': 'Vogel', 'agency': 'ESA'},
        {'first_name': 'Mark', 'last_name': 'Watney', 'agency': 'NASA'},
    ]

    nasa_astronauts = [(x['first_name'], x['last_name'])
                            for x in DATA if x['agency'] == 'NASA']
    # [
    #   ('Jose', 'Jimenez'),
    #   ('Melissa', 'Lewis'),
    #   ('Mark', 'Watney')
    # ]

Reversing ``dict`` keys with values
-----------------------------------
.. code-block:: python

    data = {'first_name': 'Jan', 'last_name': 'Twardowski'}

    {v: k for k, v in data.items()}
    # {'Jan': 'first_name', 'Twardowski': 'last_name'}


Readability counts
==================
.. literalinclude:: src/generator-clean-code.py
    :name: listing-generator-clean-code
    :language: python
    :caption: Clean Code in generator

.. code-block:: python

    DATA = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Mark', 'last_name': 'Watney'},
        {'first_name': 'Иван'},
        {'first_name': 'Jan', 'last_name': 'Twardowski', 'born': 1961},
        {'first_name': 'Melissa', 'last_name': 'Lewis', 'first_step': 1969},
    ]

    [asd(value)

                for d in DATA
            for key, value in d.items()
        if key == 'username'

    ]

.. code-block:: python

    DATA = [
        {'first_name': 'Иван', 'last_name': 'Иванович', 'agency': 'Roscosmos'},
        {'first_name': 'Jose', 'last_name': 'Jimenez', 'agency': 'NASA'},
        {'first_name': 'Melissa', 'last_name': 'Lewis', 'agency': 'NASA'},
        {'first_name': 'Alex', 'last_name': 'Vogel', 'agency': 'ESA'},
        {'first_name': 'Mark', 'last_name': 'Watney', 'agency': 'NASA'},
    ]

    nasa_astronauts = [(astronaut['first_name'], astronaut['last_name']) for astronaut in DATA if astronaut['agency'] == 'NASA']
    # [
    #   ('Jose', 'Jimenez'),
    #   ('Melissa', 'Lewis'),
    #   ('Mark', 'Watney')
    # ]


Assignments in Polish
=====================

Generators vs. Comprehensions - iris
------------------------------------
* Complexity level: easy
* Lines of code to write: 40 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/generator_iris.py`
* Input data: https://raw.githubusercontent.com/AstroMatt/book-python/master/database/data/iris.csv

#. Skopiuj dane do pliku "iris.csv"
#. Zaczytaj dane pomijając nagłówek
#. Napisz funkcję która zwraca wszystkie pomiary dla danego gatunku
#. Gatunek będzie podawany jako ``str`` do funkcji
#. Zaimplementuj rozwiązanie wykorzystując zwykłą funkcję
#. Zaimplementuj rozwiązanie wykorzystując generator i słówko kluczowe ``yield``
#. Porównaj wyniki jednego i drugiego rozwiązania przez użycie ``sys.getsizeof()``

:The whys and wherefores:
    * Wykorzystanie generatorów
    * Odbieranie danych z lazy evaluation
    * Porównanie wielkości struktur danych
    * Parsowanie pliku
    * Filtrowanie treści w locie

Generators vs. Comprehensions - passwd
--------------------------------------
* Complexity level: easy
* Lines of code to write: 40 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/generator_passwd.py`

#. Napisz program, który wczyta plik :numref:`listing-file-etc-passwd-2`
#. Przefiltruj linie, tak aby nie zawierały komentarzy (zaczynające się od ``#``) oraz pustych linii
#. Przefiltruj linie, aby wyciągnąć konta systemowe - użytkowników, którzy mają UID (trzecie pole) mniejsze niż 1000
#. Zwróć listę loginów użytkowników systemowych
#. Zaimplementuj rozwiązanie wykorzystując zwykłą funkcję
#. Zaimplementuj rozwiązanie wykorzystując generator i słówko kluczowe ``yield``
#. Porównaj wyniki jednego i drugiego rozwiązania przez użycie ``sys.getsizeof()``
#. Dlaczego różnice są tak niewielkie?
#. Co się stanie, gdy ilość danych się zwiększy?

:The whys and wherefores:
    * Wykorzystanie generatorów
    * Odbieranie danych z lazy evaluation
    * Porównanie wielkości struktur danych
    * Parsowanie pliku
    * Filtrowanie treści w locie

.. code-block:: text
    :name: listing-file-etc-passwd-2
    :caption: ``/etc/passwd`` sample file

    ##
    # User Database
    #   - User name
    #   - Encrypted password
    #   - User ID number (UID)
    #   - User's group ID number (GID)
    #   - Full name of the user (GECOS)
    #   - User home directory
    #   - Login shell
    ##

    root:x:0:0:root:/root:/bin/bash
    bin:x:1:1:bin:/bin:/sbin/nologin
    daemon:x:2:2:daemon:/sbin:/sbin/nologin
    adm:x:3:4:adm:/var/adm:/sbin/nologin
    shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
    halt:x:7:0:halt:/sbin:/sbin/halt
    nobody:x:99:99:Nobody:/:/sbin/nologin
    sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
    peck:x:1000:1000:Max Peck:/home/peck:/bin/bash
    jimenez:x:1001:1001:José Jiménez:/home/jimenez:/bin/bash
    ivanovic:x:1002:1002:Ivan Иванович:/home/ivanovic:/bin/bash
