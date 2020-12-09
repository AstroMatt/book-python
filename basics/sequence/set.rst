Sequence Set
============


Rationale
---------
* Only unique values
* Mutable - can add, remove, and modify items
* Can store elements of any **hashable** types
* Set is unordered data structure and do not record element position or insertion
* Do not support getitem and slice

Hashable (Immutable):

    * ``int``
    * ``float``
    * ``bool``
    * ``NoneType``
    * ``str``
    * ``tuple``
    * ``frozenset``

Non-hashable (Mutable):

    * ``list``
    * ``set``
    * ``dict``

"Hashable types are also immutable" is true for builtin types, but it's not a universal truth. More info: :ref:`OOP Hash` and :ref:`OOP Object Identity`.


Definition
----------
Defining only with ``set()`` - no short syntax:

    >>> data = set()

Comma after last element of a one element set is optional.
Brackets are required

    >>> data = {1}
    >>> data = {1, 2, 3}
    >>> data = {1.1, 2.2, 3.3}
    >>> data = {True, False}
    >>> data = {'a', 'b', 'c'}
    >>> data = {'a', 1, 2.2, True, None}

Stores only unique values:

    >>> {1, 2, 1}
    {1, 2}

Compares by values, not types:

    >>> {1}
    {1}
    >>> {1.0}
    {1.0}
    >>> {1, 1.0}
    {1}
    >>> {1.0, 1}
    {1.0}

Can store elements of any **hashable** types:

    >>> data = {1, 2, 'a'}
    >>> data = {1, 2, (3, 4)}
    >>>
    >>> data = {1, 2, [3, 4]}
    Traceback (most recent call last):
    TypeError: unhashable type: 'list'
    >>>
    >>> data = {1, 2, {3, 4}}
    Traceback (most recent call last):
    TypeError: unhashable type: 'set'


Type Casting
------------
* ``set()`` converts argument to ``set``

    >>> data = 'abcd'
    >>> set(data) == {'a', 'b', 'c', 'd'}
    True

    >>> data = ['a', 'b', 'c', 'd']
    >>> set(data) == {'a', 'b', 'c', 'd'}
    True

    >>> data = ('a', 'b', 'c', 'd')
    >>> set(data) == {'a', 'b', 'c', 'd'}
    True

    >>> data = {'a', 'b', 'c', 'd'}
    >>> set(data) == {'a', 'b', 'c', 'd'}
    True

    >>> data = frozenset({'a', 'b', 'c', 'd'})
    >>> set(data) == {'a', 'b', 'c', 'd'}
    True


Deduplicate
-----------
Works with ``str``, ``list``, ``tuple``, ``frozenset``

    >>> data = [1, 2, 3, 1, 1, 2, 4]
    >>> set(data)
    {1, 2, 3, 4}

Converting ``set`` deduplicate items:

    >>> data = ['Twardowski',
    ...        'Twardowski',
    ...        'Watney',
    ...        'Twardowski']
    ...
    >>> set(data) == {'Twardowski', 'Watney'}
    True


Add
---
    >>> data = {1, 2}
    >>>
    >>> data.add(3)
    >>> data == {1, 2, 3}
    True
    >>>
    >>> data.add(3)
    >>> data == {1, 2, 3}
    True
    >>>
    >>> data.add(4)
    >>> data == {1, 2, 3, 4}
    True

    >>> data = {1, 2}
    >>> data.add([3, 4])
    Traceback (most recent call last):
    TypeError: unhashable type: 'list'

    >>> data = {1, 2}
    >>> data.add((3, 4))
    >>> data == {1, 2, (3, 4)}
    True

    >>> data = {1, 2}
    >>> data.add({3, 4})
    Traceback (most recent call last):
    TypeError: unhashable type: 'set'

    >>> data = {1, 2}
    >>> data.add(frozenset({3,4}))
    >>> data
    {frozenset({3, 4}), 1, 2}


Update
------
    >>> data = {1, 2}

    >>> data.update({3, 4})
    >>> data == {1, 2, 3, 4}
    True

    >>> data.update([5, 6])
    >>> data == {1, 2, 3, 4, 5, 6}
    True

    >>> data.update((7, 8))
    >>> data == {1, 2, 3, 4, 5, 6, 7, 8}
    True


Pop
---
Gets and remove items

.. code-block:: python

    >>> data = {1, 2, 3}
    >>> value = data.pop()
    >>>
    >>> data == {1, 2}
    True
    >>>
    >>> print(value)
    3


Membership
----------
Is Disjoint?:

    * ``True`` - if there are no common elements in ``data`` and ``x``
    * ``False`` - if any ``x`` element are in data

    >>> data = {1,2}
    >>>
    >>> data.isdisjoint({1,2})
    False
    >>> data.isdisjoint({1,3})
    False
    >>> data.isdisjoint({3,4})
    True

Is Subset?:

    * ``True`` - if ``x`` has all elements from ``data``
    * ``False`` - if ``x`` don't have element from ``data``

    >>> data = {1,2}
    >>>
    >>> data.issubset({1})
    False
    >>> data.issubset({1,2})
    True
    >>> data.issubset({1,2,3})
    True
    >>> data.issubset({1,3,4})
    False

    >>> {1,2} < {3,4}
    False
    >>> {1,2} < {1,2}
    False
    >>> {1,2} < {1,2,3}
    True
    >>> {1,2,3} < {1,2}
    False

    >>> {1,2} <= {3,4}
    False
    >>> {1,2} <= {1,2}
    True
    >>> {1,2} <= {1,2,3}
    True
    >>> {1,2,3} <= {1,2}
    False

Is Superset?:
* ``True`` - if ``data`` has all elements from ``x``
* ``False`` - if ``data`` don't have element from ``x``

    >>> data = {1,2}
    >>>
    >>> data.issuperset({1})
    True
    >>> data.issuperset({1,2})
    True
    >>> data.issuperset({1,2,3})
    False
    >>> data.issuperset({1,3})
    False
    >>> data.issuperset({2,1})
    True

    >>> {1,2} > {1,2}
    False
    >>> {1,2} > {1,2,3}
    False
    >>> {1,2,3} > {1,2}
    True

    >>> {1,2} >= {1,2}
    True
    >>> {1,2} >= {1,2,3}
    False
    >>> {1,2,3} >= {1,2}
    True


Basic Operations
----------------
Union:

    * returns sum of elements from ``data`` and ``x``

    >>> data = {1,2}
    >>>
    >>> data.union({1,2})
    {1, 2}
    >>> data.union({1,2,3})
    {1, 2, 3}
    >>> data.union({1,2,4})
    {1, 2, 4}
    >>> data.union({1,3}, {2,4})
    {1, 2, 3, 4}

    >>> {1,2} | {1,2}
    {1, 2}
    >>> {1,2,3} | {1,2}
    {1, 2, 3}
    >>> {1,2,3} | {1,2,4}
    {1, 2, 3, 4}
    >>> {1,2} | {1,3} | {2,4}
    {1, 2, 3, 4}

Difference:

    * returns elements from ``data`` which are not in ``x``

    >>> data = {1,2}
    >>>
    >>> data.difference({1,2})
    set()
    >>> data.difference({1,2,3})
    set()
    >>> data.difference({1,4})
    {2}
    >>> data.difference({1,3}, {2,4})
    set()
    >>> data.difference({3,4})
    {1, 2}

    >>> {1,2} - {2,3}
    {1}
    >>> {1,2} - {2,3} - {3}
    {1}
    >>> {1,2} - {1,2,3}
    set()

Symmetric Difference:

    * returns elements from ``data`` and ``x``, but without common

    >>> data = {1,2}
    >>>
    >>> data.symmetric_difference({1,2})
    set()
    >>> data.symmetric_difference({1,2,3})
    {3}
    >>> data.symmetric_difference({1,4})
    {2, 4}
    >>> data.symmetric_difference({1,3}, {2,4})
    Traceback (most recent call last):
    TypeError: symmetric_difference() takes exactly one argument (2 given)
    >>> data.symmetric_difference({3,4})
    {1, 2, 3, 4}

    >>> {1,2} ^ {1,2}
    set()
    >>> {1,2} ^ {2,3}
    {1, 3}
    >>> {1,2} ^ {1,3}
    {2, 3}

Intersection:

    * common element from in ``data`` and ``x``

    >>> data = {1,2}
    >>>
    >>> data.intersection({1,2})
    {1, 2}
    >>> data.intersection({1,2,3})
    {1, 2}
    >>> data.intersection({1,4})
    {1}
    >>> data.intersection({1,3}, {2,4})
    set()
    >>> data.intersection({1,3}, {1,4})
    {1}
    >>> data.intersection({3,4})
    set()

    >>> {1,2} & {2,3}
    {2}
    >>> {1,2} & {2,3} & {2,4}
    {2}
    >>> {1,2} & {2,3} & {3}
    set()


Cardinality
-----------
    >>> data = {1, 2, 3}
    >>> len(data)
    3


Assignments
-----------
.. literalinclude:: assignments/sequence_set_create.py
    :caption: :download:`Solution <assignments/sequence_set_create.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_set_many.py
    :caption: :download:`Solution <assignments/sequence_set_many.py>`
    :end-before: # Solution

