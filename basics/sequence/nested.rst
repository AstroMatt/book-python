.. _Sequence Nested:

***************
Sequence Nested
***************


List of Tuples
==============
.. code-block:: python
    :caption: Get elements from ``list`` of ``tuple``

    data = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    data[2]
    # (7.6, 3.0, 6.6, 2.1, 'virginica')

    data[2][1]
    # 3.0

.. code-block:: python
    :caption: Append elements using ``list.append()``

    data = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    row = (4.9, 2.5, 4.5, 1.7, 'virginica')
    data.append(row)
    # [(4.7, 3.2, 1.3, 0.2, 'setosa'),
    #  (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    #  (7.6, 3.0, 6.6, 2.1, 'virginica'),
    #  (4.9, 2.5, 4.5, 1.7, 'virginica')]

.. code-block:: python
    :caption: Append elements using ``list.extend()``

    data = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    row = (4.9, 2.5, 4.5, 1.7, 'virginica')
    data.extend(row)
    # [(4.7, 3.2, 1.3, 0.2, 'setosa'),
    #  (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    #  (7.6, 3.0, 6.6, 2.1, 'virginica'),
    #  4.9,
    #  2.5,
    #  4.5,
    #  1.7,
    #  'virginica']

.. code-block:: python
    :caption: ``list`` of ``tuple`` length

    data = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    len(data)
    # 3

    len(data[2])
    # 5


List of Lists
=============
.. highlights::
    * Multidimensional lists

.. code-block:: python
    :caption: Lists ``a``, ``b``, ``c``, ``d`` contains the same values, but readability differs depending on whitespaces.

    a = [[1,2,3],[4,5,6],[7,8,9]]

    b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    c = [[1,2,3], [4,5,6], [7,8,9]]

    d = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    e = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

.. code-block:: python
    :caption: Get elements from ``list`` of ``list``

    data = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    data[0][0]
    # 1

    data[0][2]
    # 3

    data[2][1]
    # 8

.. code-block:: python
    :caption: ``list`` of ``list`` length

    data = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    len(data)
    # 3

    len(data[2])
    # 3


Many Types
==========
.. code-block:: python
    :caption: Get elements from union

    data = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
    ]

    data[1]
    # (4, 5, 6)

    data[1][2]
    # 6

    data[2]
    # {7, 8, 9}

    data[2][1]
    # Traceback (most recent call last):
    #     ...
    # TypeError: 'set' object is not subscriptable

.. code-block:: python
    :caption: Union length

    data = [
        [1, 2],
        (3, 4, 5, 6),
        {7, 8, 9, 10, 11},
    ]

    len(data)
    # 3

    len(data[0])
    # 2

    len(data[1])
    # 4

    len(data[2])
    # 5


Assignments
===========

.. literalinclude:: solution/sequence_nested_create.py
    :caption: :download:`Solution <solution/sequence_nested_create.py>`
    :end-before: # Solution
