.. _Sequence GetItem:

****************
Sequence GetItem
****************


Rationale
=========
.. highlights::
    * Index must ``int`` (positive, negative or zero)
    * Index must be less than length of an object
    * Negative index starts from the end and go right to left


Positive Index
==============
* Starts with ``0``
* Ascending

.. code-block:: python

    data = ['a', 'b', 'c', 'd']

    data[0]             # 'a'
    data[1]             # 'b'
    data[2]             # 'c'

.. code-block:: python

    data = ['a', 'b', 'c', 'd']

    data[100]
    # Traceback (most recent call last):
    #     ...
    # IndexError: string index out of range


Negative Index
==============
* ``0`` is equal to ``-0``
* Starts with ``-1``
* Descending

.. code-block:: python

    data = ['a', 'b', 'c', 'd']

    data[-0]            # 'a'
    data[-1]            # 'd'
    data[-2]            # 'c'

.. code-block:: python

    data = ['a', 'b', 'c', 'd']

    data[-100]
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


Assignments
===========

.. literalinclude:: solution/sequence_getitem_select.py
    :caption: :download:`Solution <solution/sequence_getitem_select.py>`
    :end-before: # Solution
