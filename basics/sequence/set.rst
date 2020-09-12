.. _Sequence Set:

************
Sequence Set
************


Rationale
=========
.. highlights::
    * Only unique values
    * Mutable - can add, remove, and modify items
    * Can store elements of any **hashable** types


Type Definition
===============
.. highlights::
    * Set is unordered data structure (each time order differs)
    * Do not record element position
    * Do not record order of insertion
    * Do not support getitem
    * Do not support slice
    * Defining only with ``set()`` - no short syntax
    * Comma after last element of a one element set is optional
    * Brackets are required

.. code-block:: python
    :caption: ``set`` type definition

    data = set()

    data = {1}
    data = {1, 2, 3}
    data = {1.1, 2.2, 3.3}
    data = {True, False}
    data = {'a', 'b', 'c'}
    data = {'a', 1, 2.2, True, None}

.. code-block:: python
    :caption: ``set`` stores only unique values.

    {1, 2, 1}                       # {1, 2}
    {1, 2, 'a'}                     # {1, 2, 'a'}
    {1, 2, (3, 4)}                  # {1, 2, (3, 4)}
    {1, 2, [3, 4]}                  # TypeError: unhashable type: 'list'
    {1, 2, {3, 4}}                  # TypeError: unhashable type: 'set'
    {1, 2, frozenset({3, 4})}       # {1, 2, frozenset({3, 4})}

.. code-block:: python
    :caption: ``set`` compares by values, not types

    {1}                             # {1}
    {1.0}                           # {1.0}
    {1, 1.0}                        # {1}
    {1.0, 1}                        # {1.0}


Type Casting
============
.. highlights::
    * ``set()`` converts argument to ``set``

.. code-block:: python

    data = [1, 2, 3]
    set(data)
    # {1, 2, 3}

.. code-block:: python

    data = (1, 2, 3)
    set(data)
    # {1, 2, 3}

.. code-block:: python

    data = {1, 2, 3}
    set(data)
    # {1, 2, 3}

.. code-block:: python

    data = frozenset({1, 2, 3})
    set(data)
    # {1, 2, 3}


Deduplicate
===========
.. highlights::
    * Works with ``tuple``, ``list``, ``str``

.. code-block:: python

    data = [1,2,3,1,1,2,4]

    set(data)
    # {1, 2, 3, 4}

.. code-block:: python
    :caption: Converting ``set`` deduplicate items

    data = [
        'Twardowski',
        'Twardowski',
        'Watney',
        'Twardowski'
    ]

    set(data)
    # {'Twardowski', 'Watney'}


Add
===
.. code-block:: python

    data = {1, 2}

    data.add(3)
    # {1, 2, 3}

    data.add(3)
    # {1, 2, 3}

    data.add(4)
    # {1, 2, 3, 4}

.. code-block:: python

    data = {1, 2}
    data.add([3, 4])
    # TypeError: unhashable type: 'list'

.. code-block:: python

    data = {1, 2}
    data.add((3, 4))
    # {1, 2, (3, 4)}

.. code-block:: python

    data = {1, 2}
    data.add({3, 4})
    # TypeError: unhashable type: 'set'

.. code-block:: python

    data = {1, 2}
    data.add(frozenset({3,4}))
    # {frozenset({3, 4}), 1, 2}


Update
======
.. code-block:: python

    data = {1, 2}
    # {1, 2}

    data.update({3, 4})
    # {1, 2, 3, 4}

    data.update([5, 6])
    # {1, 2, 3, 4, 5, 6}

    data.update((7, 8))
    # {1, 2, 3, 4, 5, 6, 7, 8}


Pop
===
.. highlights::
    * Gets and remove items

.. code-block:: python

    data = {1, 2, 3}

    value = data.pop()

    print(data)
    # {1, 2}

    print(value)
    # 3


Membership
==========

Is Disjoint?
------------
.. highlights::
    * ``True`` - if there are no common elements in ``data`` and ``x``
    * ``False`` - if any ``x`` element are in data

.. code-block:: python

    data = {1,2}

    data.isdisjoint({1,2})     # False
    data.isdisjoint({1,3})     # False
    data.isdisjoint({3,4})     # True

Is Subset?
----------
.. highlights::
    * ``True`` - if ``x`` has all elements from ``data``
    * ``False`` - if ``x`` don't have element from ``data``

.. code-block:: python

    data = {1,2}

    data.issubset({1})          # False
    data.issubset({1,2})        # True
    data.issubset({1,2,3})      # True
    data.issubset({1,3,4})      # False

.. code-block:: python

    {1,2} < {3,4}               # False
    {1,2} < {1,2}               # False
    {1,2} < {1,2,3}             # True
    {1,2,3} < {1,2}             # False

.. code-block:: python

    {1,2} <= {3,4}              # False
    {1,2} <= {1,2}              # True
    {1,2} <= {1,2,3}            # True
    {1,2,3} <= {1,2}            # False

Is Superset?
------------
.. highlights::
    * ``True`` - if ``data`` has all elements from ``x``
    * ``False`` - if ``data`` don't have element from ``x``

.. code-block:: python

    data = {1,2}

    data.issuperset({1})        # True
    data.issuperset({1,2})      # True
    data.issuperset({1,2,3})    # False
    data.issuperset({1,3})      # False
    data.issuperset({2,1})      # True

.. code-block:: python

    {1,2} > {1,2}               # False
    {1,2} > {1,2,3}             # False
    {1,2,3} > {1,2}             # True

.. code-block:: python

    {1,2} >= {1,2}              # True
    {1,2} >= {1,2,3}            # False
    {1,2,3} >= {1,2}            # True


Basic Operations
================

Union
-----
.. highlights::
    * returns sum of elements from ``data`` and ``x``

.. code-block:: python

    data = {1,2}

    data.union({1,2})           # {1, 2}
    data.union({1,2,3})         # {1, 2, 3}
    data.union({1,2,4})         # {1, 2, 4}
    data.union({1,3}, {2,4})    # {1, 2, 3, 4}

.. code-block:: python

    {1,2} | {1,2}               # {1, 2}
    {1,2,3} | {1,2}             # {1, 2, 3}
    {1,2,3} | {1,2,4}           # {1, 2, 3, 4}
    {1,2} | {1,3} | {2,4}       # {1, 2, 3, 4}

Difference
----------
.. highlights::
    * returns elements from ``data`` which are not in ``x``

.. code-block:: python

    data = {1,2}

    data.difference({1,2})          # set()
    data.difference({1,2,3})        # set()
    data.difference({1,4})          # {2}
    data.difference({1,3}, {2,4})   # set()
    data.difference({3,4})          # {1, 2}

.. code-block:: python

    {1,2} - {2,3}                   # {1}
    {1,2} - {2,3} - {3}             # {1}
    {1,2} - {1,2,3}                 # set()

Symmetric Difference
--------------------
.. highlights::
    * returns elements from ``data`` and ``x``, but without common

.. code-block:: python

    data = {1,2}

    data.symmetric_difference({1,2})           # set()
    data.symmetric_difference({1,2,3})         # {3}
    data.symmetric_difference({1,4})           # {2, 4}
    data.symmetric_difference({1,3}, {2,4})    # TypeError: symmetric_difference() takes exactly one argument (2 given)
    data.symmetric_difference({3,4})           # {1, 2, 3, 4}

.. code-block:: python

    {1,2} ^ {1,2}               # set()
    {1,2} ^ {2,3}               # {1, 3}
    {1,2} ^ {1,3}               # {2, 3}

Intersection
------------
.. highlights::
    * common element from in ``data`` and ``x``

.. code-block:: python

    data = {1,2}

    data.intersection({1,2})           # {1, 2}
    data.intersection({1,2,3})         # {1, 2}
    data.intersection({1,4})           # {1}
    data.intersection({1,3}, {2,4})    # set()
    data.intersection({1,3}, {1,4})    # {1}
    data.intersection({3,4})           # set()


.. code-block:: python

    {1,2} & {2,3}                       # {2}
    {1,2} & {2,3} & {2,4}               # {2}
    {1,2} & {2,3} & {3}                 # set()


Cardinality
===========
.. code-block:: python

    data = {1, 2, 3}

    len(data)
    # 3


Assignments
===========

Sequence Set Create
-------------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/sequence_set_create.py`

:English:
    #. Create set ``result`` with elements:

        * ``'a'``
        * ``1``
        * ``2.2``

    #. Print ``result``
    #. Print number of elements in ``result``

:Polish:
    #. Stwórz zbiór ``result`` z elementami:

        * ``'a'``
        * ``1``
        * ``2.2``

    #. Wypisz ``result``
    #. Wypisz liczbę elementów ``result``

Sequence Set Many
-----------------
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/sequence_set_many.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create set ``result`` representing first row
    #. Values from second row add to ``set`` using ``.add()``
    #. From third row create ``set`` and add it to ``result`` using ``.update()``
    #. From fourth row create ``tuple`` and add it to ``result`` using ``.update()``
    #. From fifth row create ``list`` and add it to ``result`` using ``.update()``
    #. Print ``result``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz zbiór ``result`` reprezentujący pierwszy wiersz
    #. Wartości z drugiego wiersza dodawaj do ``result`` używając ``.add()``
    #. Na podstawie trzeciego wiersza stwórz ``set`` i dodaj go do ``result`` używając ``.update()``
    #. Na podstawie czwartego wiersza stwórz ``tuple`` i dodaj go do ``result`` używając ``.update()``
    #. Na podstawie piątego wiersza stwórz ``list`` i dodaj go do ``result`` używając ``.update()``
    #. Wypis ``result``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. csv-table:: Input data
        :header: "Row", "Sepal length", "Sepal width", "Petal length", "Petal width"
        :stub-columns: 1

        "1", "5.8", "2.7", "5.1", "1.9"
        "2", "5.1", "3.5", "1.4", "0.2"
        "3", "5.7", "2.8", "4.1", "1.3"
        "4", "6.3", "2.9", "5.6", "1.8"
        "5", "6.4", "3.2", "4.5", "1.5"

:Output:
    .. code-block:: python

        result: set
        # {0.2, 1.9, 2.7, 3.5, 1.4, 5.8, 5.1, 1.3, 2.8, 4.1, 5.7, 6.3, 5.6, 6.4, 1.5, 4.5, 3.2, 1.8, 2.9}

:The whys and wherefores:
    * Defining ``set``
    * Basic ``set`` methods
