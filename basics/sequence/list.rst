Sequence List
=============


Rationale
---------
* Mutable - can add, remove, and modify items


Definition
----------
Defining empty list with ``[]`` is used more often, but ``list()`` is more explicit:

    >>> data = list()
    >>> data = []

Can store elements of any types:

    >>> data = [1, 2, 3]
    >>> data = [1.1, 2.2, 3.3]
    >>> data = [True, False]
    >>> data = ['a', 'b', 'c']
    >>> data = ['a', 1, 2.2, True, None]

Brackets are required

    >>> data = [1, 2, 3]

Comma after last element of a one element list is optional

    >>> data = [1,]
    >>> type(data)
    <class 'list'>

    >>> data = [1]
    >>> type(data)
    <class 'list'>


Type Casting
------------
Builtin function ``list()`` converts argument to ``list``

    >>> data = 'abcd'
    >>> list(data)
    ['a', 'b', 'c', 'd']

    >>> data = ['a', 'b', 'c', 'd']
    >>> list(data)
    ['a', 'b', 'c', 'd']

    >>> data = ('a', 'b', 'c', 'd')
    >>> list(data)
    ['a', 'b', 'c', 'd']

    >>> list(1, 2, 3, 4)
    Traceback (most recent call last):
    TypeError: list expected at most 1 argument, got 4


GetItem
-------
* More information in :ref:`Sequence GetItem` and :ref:`Sequence Slice`

    >>>data = ['a', 'b', 'c', 'd']
    >>>
    >>>data[0]
    'a'
    >>>data[1]
    'b'
    >>>data[2]
    'c'
    >>>data[3]
    'd'


Set Item
--------
    >>> data = ['a', 'b', 'c', 'd']
    >>> data[0] = 'x'
    >>>
    >>> print(data)
    ['x', 'b', 'c', 'd']

    >>> data = ['a', 'b', 'c', 'd']
    >>> data[4] = 'x'
    Traceback (most recent call last):
    IndexError: list assignment index out of range


Del Item
--------
    >>> data = ['a', 'b', 'c', 'd']
    >>> del data[3]
    >>>
    >>> print(data)
    ['a', 'b', 'c']

    >>> data = ['a', 'b', 'c', 'd']
    >>> value = data.pop()
    >>>
    print(data)
    ['a', 'b', 'c']
    >>>
    print(value)
    'd'


Append
------
* ``list + list``
* ``list += list``
* ``list.extend()``
* ``list.append()``

    >>> data = [1, 2]
    >>> data = data + [3, 4]
    >>>
    >>> print(data)
    [1, 2, 3, 4]

    >>> data = [1, 2]
    >>> data += [3, 4]
    >>>
    >>> print(data)
    [1, 2, 3, 4]

    >>> data = [1, 2]
    >>> data.extend([3, 4])
    >>>
    >>> print(data)
    [1, 2, 3, 4]

    >>> data = [1, 2]
    >>> data.append(3)
    >>>
    >>> print(data)
    [1, 2, 3]

    >>> data = [1, 2]
    >>> data.append([3, 4])
    >>>
    >>> print(data)
    [1, 2, [3, 4]]


Insert
------
* Insert at specific position

    >>> data = ['a', 'b', 'c', 'd']
    >>> data.insert(0, 'x')
    >>>
    >>> print(data)
    ['x', 'a', 'b', 'c', 'd']

    >>> data = ['a', 'b', 'c', 'd']
    >>> data.insert(1, 'x')
    >>>
    >>> print(data)
    ['a', 'x', 'b', 'c', 'd']


Sort vs Sorted
--------------
Timsort is a hybrid stable sorting algorithm, derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data. It was implemented by Tim Peters in 2002 for use in the Python programming language. The algorithm finds subsequences of the data that are already ordered (runs) and uses them to sort the remainder more efficiently. This is done by merging runs until certain criteria are fulfilled. Timsort has been Python's standard sorting algorithm since version 2.3. It is also used to sort arrays of non-primitive type in Java SE 7, on the Android platform, in GNU Octave, on V8, Swift, and Rust. [timsort]_

* ``sorted()`` - Returns sorted list, do not modify the original
* ``list.sort()`` - Changes object permanently, returns None

    >>> a = [3, 1, 2]
    >>> b = sorted(a)
    >>>
    >>> print(a)
    [3, 1, 2]
    >>>
    >>> print(b)
    [1, 2, 3]

    >>> a = [3, 1, 2]
    >>> b = a.sort()
    >>>
    >>> print(a)
    [1, 2, 3]
    >>>
    >>> print(b)
    None


Method Chaining
---------------
    >>> data = [3, 1, 2]
    >>> data.sort()
    >>> data.append(4)
    >>>
    >>> print(data)
    [1, 2, 3, 4]

    >>> data = [3, 1, 2]
    >>>
    >>> data.sort().append(4)
    Traceback (most recent call last):
    AttributeError: 'NoneType' object has no attribute 'append'


Built-in Functions
------------------
* ``min()`` - Minimal value
* ``max()`` - Maximal value
* ``sum()`` - Sum of elements
* ``len()`` - Length of a list
* ``all()`` - All values are ``True``
* ``any()`` - Any values is ``True``

    >>> data = [2, 0, 1]
    >>>
    >>> min(data)
    0
    >>> max(data)
    2
    >>> sum(data)
    3
    >>> len(data)
    3

    >>> data = [True, False, True]
    >>>
    >>> any(data)
    True
    >>> all(data)
    False


References
----------
.. [timsort] https://en.wikipedia.org/wiki/Timsort


Assignments
-----------
.. literalinclude:: assignments/sequence_list_create.py
    :caption: :download:`Solution <assignments/sequence_list_create.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_list_many.py
    :caption: :download:`Solution <assignments/sequence_list_many.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_list_modify.py
    :caption: :download:`Solution <assignments/sequence_list_modify.py>`
    :end-before: # Solution
