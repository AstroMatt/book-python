.. _Loop Unpacking Assignment:

*************************
Loop Unpacking Assignment
*************************


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


Longer data
===========
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


Unpacking Assignment
====================
.. code-block:: python

    *features, label = (5.8, 2.7, 5.1, 1.9, 'virginica')

    features                # [5.8, 2.7, 5.1, 1.9]
    label                   # 'virginica'

.. code-block:: python

    DATA = [
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    ]

    for *features, label in DATA:
        avg = sum(features) / len(features)
        print(label, avg)

    # virginica 3.875
    # setosa 2.55
    # versicolor 3.475

.. code-block:: python

    DATA = [
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    ]

    for *_, label in DATA:
        print(label)

    # virginica
    # setosa
    # versicolor


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

.. literalinclude:: solution/loop_unpacking_months.py
    :caption: :download:`Solution <solution/loop_unpacking_months.py>`
    :end-before: # Solution

.. literalinclude:: solution/loop_unpacking_endswith.py
    :caption: :download:`Solution <solution/loop_unpacking_endswith.py>`
    :end-before: # Solution
