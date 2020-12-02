.. _Sequence Frozenset:

******************
Sequence Frozenset
******************


Rationale
=========
.. highlights::
    * Only unique values
    * Immutable - cannot add, modify or remove items
    * Can store elements of any **hashable** types
    * Has all ``set`` methods such as ``.intersect()``, ``.subset()`` ``.union()``, etc.
    * One solid block in memory
    * Frozenset is unordered data structure and do not record element position
    * Do not support getitem and slice


Type Definition
===============
.. highlights::
    * Defining only with ``frozenset()`` - no short syntax
    * Comma after last element of a one element frozenset is optional
    * Brackets are required

.. code-block:: python

    data = frozenset()

.. code-block:: python

    data = frozenset({1})
    data = frozenset({1, 2, 3})
    data = frozenset({1.1, 2.2, 3.3})
    data = frozenset({True, False})
    data = frozenset({'a', 'b', 'c'})
    data = frozenset({'a', 1, 2.2, True, None})


Type Casting
============
.. highlights::
    * ``frozenset()`` converts argument to ``frozenset``

.. code-block:: python

    data = 'abcd'
    frozenset(data)
    # frozenset({'a', 'b', 'c', 'd'})

.. code-block:: python

    data = ['a', 'b', 'c', 'd']
    frozenset(data)
    # frozenset({'a', 'b', 'c', 'd'})

.. code-block:: python

    data = ('a', 'b', 'c', 'd')
    frozenset(data)
    # frozenset({'a', 'b', 'c', 'd'})

.. code-block:: python

    data = {'a', 'b', 'c', 'd'}
    frozenset(data)
    # frozenset({'a', 'b', 'c', 'd'})

.. code-block:: python

    data = frozenset({'a', 'b', 'c', 'd'})
    frozenset(data)
    # frozenset({'a', 'b', 'c', 'd'})

.. code-block:: python

    data = [1, 2, 3, [4, 5]]
    frozenset(data)
    # Traceback (most recent call last):
    # TypeError: unhashable type: 'list'

.. code-block:: python

    data = [1, 2, 3, (4, 5)]
    frozenset(data)
    # frozenset({(4, 5), 1, 2, 3})


Frozenset or Set
================
Both:

    * unordered
    * impossible to getitem and slice
    * unique elements
    * only **hashable** elements

Frozenset:

    * immutable
    * one contingent block of data in memory

Set:

    * mutable
    * implemented in memory as list of pointers to objects
    * objects are scattered in memory


Assignments
===========


.. literalinclude:: assignments/sequence_frozenset_create.py
    :caption: :download:`Solution <assignments/sequence_frozenset_create.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_frozenset_newline.py
    :caption: :download:`Solution <assignments/sequence_frozenset_newline.py>`
    :end-before: # Solution
