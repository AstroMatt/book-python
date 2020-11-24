.. _Sequence GetItem:

****************
Sequence GetItem
****************


Rationale
=========
.. highlights::
    * Works with ordered sequences: ``str``, ``list``, ``tuple``
    * Index must ``int`` (positive, negative or zero)
    * Positive Index starts with ``0``
    * Negative index starts with ``-1``

.. code-block:: python

    data = 'abcd'

    data[0]
    # 'a'

    data[1]
    # 'b'

    data[-1]
    # 'd'

    data[1.1]
    # Traceback (most recent call last):
    #     ...
    # TypeError: list indices must be integers or slices, not float


Positive Index
==============
* Starts with ``0``
* Index must be less than length of an object
* Ascending

.. code-block:: python

    data = ['a', 'b', 'c', 'd']

    data[0]     # 'a'
    data[1]     # 'b'
    data[2]     # 'c'
    data[3]     # 'd'

    data[4]
    # Traceback (most recent call last):
    #     ...
    # IndexError: string index out of range


Negative Index
==============
* ``0`` is equal to ``-0``
* Starts with ``-1``
* Descending
* Negative index starts from the end and go right to left

.. code-block:: python

    data = ['a', 'b', 'c', 'd']

    data[-0]     # 'a'
    data[-1]     # 'd'
    data[-2]     # 'c'
    data[-3]     # 'b'
    data[-4]     # 'a'

    data[-5]
    # Traceback (most recent call last):
    #     ...
    # IndexError: string index out of range


Ordered Sequence
================
.. code-block:: python
    :caption: GetItem from ``str``

    data = 'abcd'

    data[0]             # 'a'
    data[1]             # 'b'
    data[2]             # 'c'
    data[-0]            # 'a'
    data[-1]            # 'd'
    data[-2]            # 'c'

.. code-block:: python
    :caption: GetItem from ``list``

    data = ['a', 'b', 'c', 'd']

    data[0]             # 'a'
    data[1]             # 'b'
    data[2]             # 'c'
    data[-0]            # 'a'
    data[-1]            # 'd'
    data[-2]            # 'c'

.. code-block:: python
    :caption: GetItem from ``tuple``

    data = ('a', 'b', 'c', 'd')

    data[0]             # 'a'
    data[1]             # 'b'
    data[2]             # 'c'
    data[-0]            # 'a'
    data[-1]            # 'd'
    data[-2]            # 'c'


Unordered Sequence
==================
.. code-block:: python
    :caption: GetItem from ``set`` is impossible. ``set`` is unordered data structure.

    data = {'a', 'b', 'c', 'd'}

    data[0]             # TypeError: 'set' object is not subscriptable
    data[1]             # TypeError: 'set' object is not subscriptable
    data[2]             # TypeError: 'set' object is not subscriptable
    data[-0]            # TypeError: 'set' object is not subscriptable
    data[-1]            # TypeError: 'set' object is not subscriptable
    data[-2]            # TypeError: 'set' object is not subscriptable

.. code-block:: python
    :caption: GetItem from ``frozenset`` is impossible. ``frozenset`` is unordered data structure.

    data = frozenset({'a', 'b', 'c', 'd'})

    data[0]             # TypeError: 'frozenset' object is not subscriptable
    data[1]             # TypeError: 'frozenset' object is not subscriptable
    data[2]             # TypeError: 'frozenset' object is not subscriptable
    data[-0]            # TypeError: 'frozenset' object is not subscriptable
    data[-1]            # TypeError: 'frozenset' object is not subscriptable
    data[-2]            # TypeError: 'frozenset' object is not subscriptable


Nested Sequence
===============
.. code-block:: python
    :caption: Get elements from ``list`` of ``list``

    data = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    data[0][0]  # 1
    data[0][1]  # 2
    data[0][2]  # 3
    data[1][0]  # 4
    data[1][1]  # 5
    data[1][2]  # 6
    data[2][0]  # 7
    data[2][1]  # 8
    data[2][2]  # 9

.. code-block:: python
    :caption: Get elements from ``list`` of ``tuple``

    data = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    data[0]     # (4.7, 3.2, 1.3, 0.2, 'setosa')
    data[0][0]  # 4.7
    data[0][4]  # 'setosa'
    data[1]     # (7.0, 3.2, 4.7, 1.4, 'versicolor')
    data[1][0]  # 7.0
    data[1][4]  # 'versicolor'
    data[2]     # (7.6, 3.0, 6.6, 2.1, 'virginica')
    data[2][0]  # 7.6
    data[2][4]  # 'virginica'

.. code-block:: python
    :caption: Get elements from list of sequences

    data = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
    ]

    data[0]     # [1, 2, 3]
    data[0][0]  # 1
    data[0][1]  # 2
    data[0][2]  # 3
    data[1]     # (4, 5, 6)
    data[1][0]  # 4
    data[1][1]  # 5
    data[1][2]  # 6
    data[2]     # {7, 8, 9}
    data[2][0]
    # Traceback (most recent call last):
    #     ...
    # TypeError: 'set' object is not subscriptable


Assignments
===========

.. literalinclude:: solution/sequence_getitem_select.py
    :caption: :download:`Solution <solution/sequence_getitem_select.py>`
    :end-before: # Solution
