.. _Loop Unpacking Sequences:

************************
Loop Unpacking Sequences
************************


Recap
=====
.. code-block:: python

    a, b = 1, 2
    a, b = (1, 2)
    k, v = (1, 2)
    key, value = (1, 2)


List of Pairs
=============
.. code-block:: python

    DATA = [
        ('a', 1),
        ('b', 2),
        ('c', 3),
    ]

    for key, value in DATA:
        print(f'{key} -> {value}')

    # a -> 1
    # b -> 2
    # c -> 3


List of Sequence
================
.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for sepal_length, sepal_width, petal_length, petal_width, species in DATA:
        print(species, '->', sepal_length)

    for sl, sw, pl, pw, s in DATA:
        print(s, '->', sl)

    for *features, label in DATA:
        print(label, '->', sum(features))

    for *X,y in DATA:
        print(y, '->', sum(X))

    # setosa -> [5.1, 3.5, 1.4, 0.2]
    # versicolor -> [5.7, 2.8, 4.1, 1.3]
    # virginica -> [6.3, 2.9, 5.6, 1.8]


Mixed
=====
.. code-block:: python

    DATA = [
        (1, 2),
        ('name', 'Jan Twardowski'),
        ('species', ['setosa', 'versicolor', 'virginica']),
        ((1, 2), ['Johnson Space Center', 'Kennedy Space Center']),
        (['NASA', 'ESA', 'Roscosmos'], 1),
    ]

    for key, value in DATA:
        print(f'{key} -> {value}')

    # 1 -> 2
    # name -> Jan Twardowski
    # species -> ['setosa', 'versicolor', 'virginica']
    # (1, 2) -> ['Johnson Space Center', 'Kennedy Space Center']
    # ['NASA', 'ESA', 'Roscosmos'] -> 1


Enumerate
=========
.. highlights::
    * Pythonic way
    * Preferred over ``i=0`` and ``i+=1`` for every iteration
    * ``enumerate()`` will return ``counter`` and ``value`` for every iteration

.. code-block:: python
    :caption: ``enumerate()`` will return ``counter`` and ``value`` for every iteration

    DATA = ['a', 'b', 'c']

    for i, letter in enumerate(DATA):
        print(i, letter)

    # 0 a
    # 1 b
    # 2 c

.. code-block:: python
    :caption: ``enumerate()`` can start with custom number

    DATA = ['a', 'b', 'c']

    for i, letter in enumerate(DATA, start=5):
        print(i, letter)

    # 5 a
    # 6 b
    # 7 c

.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for i, row in enumerate(DATA):
        print(f'{i} -> {row}')

    # 0 -> (5.1, 3.5, 1.4, 0.2, 'setosa')
    # 1 -> (5.7, 2.8, 4.1, 1.3, 'versicolor')
    # 2 -> (6.3, 2.9, 5.6, 1.8, 'virginica')


Assignments
===========

Loop Unpacking Months
---------------------
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/loop_unpacking_months.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Use ``enumerate()`` to convert ``MONTH`` into dict:

        * Keys: month number
        * Values: month name

    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Użyj ``enumerate()`` do konwersji ``MONTH`` w słownik:

        * klucz: numer miesiąca
        * wartość: nazwa miesiąca

    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        MONTHS = ['January', 'February', 'March', 'April',
                  'May', 'June', 'July', 'August', 'September',
                  'October', 'November', 'December']

:Output:
    .. code-block:: python

        result: dict
        # {1: 'January',
        #  2: 'February',
        #  3: 'March',
        #  4: 'April',
        #  5: 'May',
        #  6: 'June',
        #  7: 'July',
        #  8: 'August',
        #  9: 'September',
        #  10: 'October',
        #  11: 'November',
        #  12: 'December'}

Loop Unpacking Endswith
-----------------------
* Complexity level: medium
* Lines of code to write: 3 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/loop_unpacking_endswith.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Separate header from data
    #. Iterating over data unpack row to ``*features`` and ``label``
    #. Print species names ending with "ca" or "osa"

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Odseparuj nagłówek od danych
    #. Iterując po danych rozpakuj wiersz do ``*features`` oraz ``label``
    #. Wypisz nazwy gatunków kończące się na "ca" lub "osa"

:Input:
    .. code-block:: python

        DATA = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, {'virginica'}),
            (5.1, 3.5, 1.4, 0.2, {'setosa'}),
            (5.7, 2.8, 4.1, 1.3, {'versicolor'}),
            (6.3, 2.9, 5.6, 1.8, {'virginica'}),
            (6.4, 3.2, 4.5, 1.5, {'versicolor'}),
            (4.7, 3.2, 1.3, 0.2, {'setosa'}),
            (7.0, 3.2, 4.7, 1.4, {'versicolor'}),
            (7.6, 3.0, 6.6, 2.1, {'virginica'}),
            (4.6, 3.1, 1.5, 0.2, {'setosa'}),
        ]

:The whys and wherefores:
    * Accessing ``set`` items
    * Iterating over nested structure
    * Unpacking in ``for`` loop

:Hints:
    * ``str.endswith()``
    * ``set.pop()``
    * ``isinstance`` or ``type``
