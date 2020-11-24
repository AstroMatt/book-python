.. _Sequence List:

*************
Sequence List
*************


Rationale
=========
.. highlights::
    * Can store elements of any types
    * Mutable - can add, remove, and modify items


Type Definition
===============
.. highlights::
    * Defining empty list with ``[]`` is used more often, but ``list()`` is more readable
    * Comma after last element of a one element list is optional
    * Brackets are required

.. code-block:: python

    data = list()
    data = []

.. code-block:: python

    data = [1]
    data = [1, 2, 3]
    data = [1.1, 2.2, 3.3]
    data = [True, False]
    data = ['a', 'b', 'c']
    data = ['a', 1, 2.2, True, None]

.. code-block:: python

    list(1, 2, 3, 4)
    # Traceback (most recent call last):
    #     ...
    # TypeError: list expected at most 1 argument, got 4

    list([1, 2, 3, 4])
    # [1, 2, 3, 4]


Type Casting
============
.. highlights::
    * ``list()`` converts argument to ``list``

.. code-block:: python

    data = 'abcd'
    list(data)
    # ['a', 'b', 'c', 'd']

.. code-block:: python

    data = ['a', 'b', 'c', 'd']
    list(data)
    # ['a', 'b', 'c', 'd']

.. code-block:: python

    data = ('a', 'b', 'c', 'd')
    list(data)
    # ['a', 'b', 'c', 'd']

.. code-block:: python

    data = {'a', 'b', 'c', 'd'}
    list(data)
    # ['a', 'b', 'c', 'd']

.. code-block:: python

    data = frozenset({'a', 'b', 'c', 'd'})
    list(data)
    # ['a', 'b', 'c', 'd']


GetItem
=======
.. highlights::
    * More information in :ref:`Sequence GetItem` and :ref:`Sequence Slice`

.. code-block:: python

    data = ['a', 'b', 'c', 'd']

    data[0]         # 'a'
    data[1]         # 'b'
    data[2]         # 'c'
    data[3]         # 'd'


Set Item
========
.. code-block:: python

    data = ['a', 'b', 'c', 'd']
    data[0] = 'x'

    print(data)
    # ['x', 'b', 'c', 'd']

.. code-block:: python

    data = ['a', 'b', 'c', 'd']
    data[4] = 'x'
    # Traceback (most recent call last):
    #     ...
    # IndexError: list assignment index out of range


Del Item
========
.. code-block:: python

    data = ['a', 'b', 'c', 'd']
    del data[3]

    print(data)
    # ['a', 'b', 'c']

.. code-block:: python

    data = ['a', 'b', 'c', 'd']
    value = data.pop()

    print(data)
    # ['a', 'b', 'c']

    print(value)
    # 'd'


Append
======
.. highlights::
    * ``list + list``
    * ``list += list``
    * ``list.extend()``
    * ``list.append()``

.. code-block:: python

    data = [1, 2]
    data = data + [3, 4]

    print(data)
    # [1, 2, 3, 4]

.. code-block:: python

    data = [1, 2]
    data += [3, 4]

    print(data)
    # [1, 2, 3, 4]

.. code-block:: python

    data = [1, 2]
    data.extend([3, 4])

    print(data)
    # [1, 2, 3, 4]

.. code-block:: python

    data = [1, 2]
    data.append(3)

    print(data)
    # [1, 2, 3]

.. code-block:: python

    data = [1, 2]
    data.append([3, 4])

    print(data)
    # [1, 2, [3, 4]]


Insert
======
.. highlights::
    * Insert at specific position

.. code-block:: python

    data = ['a', 'b', 'c', 'd']
    data.insert(0, 'x')

    print(data)
    # ['x', 'a', 'b', 'c', 'd']

.. code-block:: python

    data = ['a', 'b', 'c', 'd']
    data.insert(1, 'x')

    print(data)
    # ['a', 'x', 'b', 'c', 'd']


Sort
====
.. epigraph::
    Timsort is a hybrid sorting algorithm, derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data. It was invented by Tim Peters in 2002 for use in the Python programming language. The algorithm finds subsets of the data that are already ordered, and uses the subsets to sort the data more efficiently. This is done by merging an identified subset, called a run, with existing runs until certain criteria are fulfilled. Timsort has been Python's standard sorting algorithm since version 2.3. It is now also used to sort arrays in Java SE 7, and on the Android platform.

.. highlights::
    * ``sorted()`` - Returns sorted list, do not modify the original
    * ``list.sort()`` - Changes object permanently, returns None

.. code-block:: python

    a = [3, 1, 2]
    b = sorted(a)

    print(a)
    # [3, 1, 2]

    print(b)
    # [1, 2, 3]

.. code-block:: python

    a = [3, 1, 2]
    b = a.sort()

    print(a)
    # [1, 2, 3]

    print(b)
    # None


Method Chaining
===============
.. code-block:: python

    data = [3, 1, 2]
    data.sort()
    data.append(4)

    print(data)
    # [1, 2, 3, 4]

.. code-block:: python

    data = [3, 1, 2]

    data.sort().append(4)
    # Traceback (most recent call last):
    #     ...
    # AttributeError: 'NoneType' object has no attribute 'append'


Built-in Functions
==================
.. highlights::
    * ``min()`` - Minimal value
    * ``max()`` - Maximal value
    * ``sum()`` - Sum of elements
    * ``len()`` - Length of a list
    * ``all()`` - All values are ``True``
    * ``any()`` - Any values is ``True``

.. code-block:: python

    data = [2, 0, 1]

    min(data)       # 0
    max(data)       # 2
    sum(data)       # 3
    len(data)       # 3

.. code-block:: python

    data = [True, False, True]

    any(data)       # True
    all(data)       # False


Assignments
===========

.. literalinclude:: solution/sequence_list_create.py
    :caption: :download:`Solution <solution/sequence_list_create.py>`
    :end-before: # Solution

.. literalinclude:: solution/sequence_list_many.py
    :caption: :download:`Solution <solution/sequence_list_many.py>`
    :end-before: # Solution

.. literalinclude:: solution/sequence_list_modify.py
    :caption: :download:`Solution <solution/sequence_list_modify.py>`
    :end-before: # Solution
