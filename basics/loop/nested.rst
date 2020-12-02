.. _Loop Nested Sequences:

*********************
Loop Nested Sequences
*********************


Convention
==========
* ``row`` - best for nested loops with sequence inside
* Conventions for rows and columns:

    * ``row`` - row (all elements)
    * ``column`` - current column element from ``row`` sequence
    * ``i`` - row number
    * ``j`` - column number
    * ``x`` - row number
    * ``y`` - column number
    * ``outer`` - for outer loop element
    * ``inner`` - for inner loop element

* Note that ``i`` may interfere with ``i`` used as loop counter


List of Pairs
=============
.. code-block:: python

    DATA = [
        ('commander', 'Melissa Lewis'),
        ('botanist', 'Mark Watney'),
        ('chemist', 'Alex Vogel'),
    ]

    for pair in DATA:
        role = pair[0]
        name = pair[1]
        print(f'{role} -> {name}')

    # commander -> Melissa Lewis
    # botanist -> Mark Watney
    # chemist -> Alex Vogel


List of Sequence
================
.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for row in DATA:
        sepal_length = row[0]
        sepal_width = row[1]
        petal_length = row[2]
        petal_width = row[3]
        species = row[4]
        features = sepal_length + sepal_width + petal_length + petal_width
        print(f'{species} -> {total}')

    # setosa -> 10.2
    # versicolor -> 13.9
    # virginica -> 16.599999999999998

.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for row in DATA:
        features = row[0:4]
        label = row[4]
        print(f'{label} -> {sum(features)}')

    # setosa -> 10.2
    # versicolor -> 13.9
    # virginica -> 16.599999999999998


Matrix
======
.. highlights::
    * Suggested variable name: ``row``

.. code-block:: python

    DATA = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    for row in DATA:
        a = row[0]
        b = row[1]
        c = row[2]
        print(f'{a=} {b=} {c=}')

    # a=1 b=2 c=3
    # a=4 b=5 c=6
    # a=7 b=8 c=9

.. code-block:: python

    DATA = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    for row in DATA:
        print()

        for value in row:
            print(f'{value}', end=' ')

    # 1 2 3
    # 4 5 6
    # 7 8 9


Mixed
=====
.. code-block:: python
    :caption: Iterating over ``list`` with scalar and vector values - simple loop

    DATA = [('Jan', 'Twardowski'), 'Watney', 42, 13.37, {True, None, False}]

    for obj in DATA:
        print(obj)

    # ('Jan', 'Twardowski')
    # Watney
    # 42
    # 13.37
    # {False, True, None}

.. code-block:: python
    :caption: Iterating over ``list`` with scalar and vector values - nested loop

    DATA = [('Jan', 'Twardowski'), 'Watney', 42, 13.37, {True, None, False}]

    for obj in DATA:
        for element in obj:
            print(element)

    # Jan
    # Twardowski
    # W
    # a
    # t
    # n
    # e
    # y
    # Traceback (most recent call last):
    # TypeError: 'int' object is not iterable

.. code-block:: python
    :caption: Iterating over ``list`` with scalar and vector values - smart loop

    DATA = [('Jan', 'Twardowski'), 'Watney', 42, 13.37, {True, None, False}]


    for obj in DATA:
        if type(obj) in (list, tuple, set, frozenset):
            for element in obj:
                print(element)
        else:
            print(obj)

    # Jan
    # Twardowski
    # Watney
    # 42
    # 13.37
    # False
    # True
    # None


Assignments
===========

.. literalinclude:: assignments/loop_nested_mean.py
    :caption: :download:`Solution <assignments/loop_nested_mean.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_nested_unique_keys.py
    :caption: :download:`Solution <assignments/loop_nested_unique_keys.py>`
    :end-before: # Solution
