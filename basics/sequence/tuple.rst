Sequence Tuple
==============


Rationale
---------
* Immutable - cannot add, modify or remove items


Definition
----------
Defining empty tuple with ``()`` is used more often, but ``tuple()`` is more explicit:

    >>> data = ()
    >>> data = tuple()

Can store elements of any type:

    >>> data = (1, 2, 3)
    >>> data = (1.1, 2.2, 3.3)
    >>> data = (True, False)
    >>> data = ('a', 'b', 'c')
    >>> data = ('a', 1, 2.2, True, None)

Brackets are optional, but it's a good practice to always write them:

    >>> data = (1, 2, 3)
    >>> data = 1, 2, 3

Single element ``tuple`` require comma at the end (**important!**):

    >>> data = (1,)
    >>> type(data)
    <class 'tuple'>

    >>> data = (1)
    >>> type(data)
    <class 'int'>

Comma after last element of multi value tuple is optional:

    >>> data = (1, 2)
    >>> type(data)
    <class 'tuple'>

    >>> data = (1, 2,)
    >>> type(data)
    <class 'tuple'>


Type Casting
------------
Builtin function ``tuple()`` converts argument to ``tuple``

    >>> data = 'abcd'
    >>> tuple(data)
    ('a', 'b', 'c', 'd')

    >>> data = ['a', 'b', 'c', 'd']
    >>> tuple(data)
    ('a', 'b', 'c', 'd')

    >>> data = ('a', 'b', 'c', 'd')
    >>> tuple(data)
    ('a', 'b', 'c', 'd')

    >>> tuple('a', 'b', 'c', 'd')
    Traceback (most recent call last):
    TypeError: tuple expected at most 1 argument, got 4


GetItem
-------
* More information in :ref:`Sequence GetItem` and :ref:`Sequence Slice`

    >>> data = ('a', 'b', 'c', 'd')

    >>> data[0]
    'a'
    >>> data[1]
    'b'
    >>> data[2]
    'c'
    >>> data[3]
    'd'


Tuple or Int, Float, Str
------------------------
    >>> data = 1
    >>> type(data)
    <class 'int'>

    >>> data = 1,
    >>> type(data)
    <class 'tuple'>

    >>> data = 1.
    >>> type(data)
    <class 'float'>

    >>> data = 1.2
    >>> type(data)
    <class 'float'>
    >>> data = 1,2
    >>> type(data)
    <class 'tuple'>
    >>> data = 1.2,
    >>> type(data)
    <class 'tuple'>
    >>> data = 1,2.3
    >>> type(data)
    <class 'tuple'>

    >>> data = 1.
    >>> type(data)
    <class 'float'>
    >>> data = 1,
    >>> type(data)
    <class 'tuple'>
    >>> data = 1.,
    >>> type(data)
    <class 'tuple'>

    >>> data = .2
    >>> type(data)
    <class 'float'>
    >>> data = .2,
    >>> type(data)
    <class 'tuple'>
    >>> data = 1.2
    >>> type(data)
    <class 'float'>

    >>> data = 1
    >>> type(data)
    <class 'int'>
    >>> data = 1.,1.
    >>> type(data)
    <class 'tuple'>
    >>> data = .2,.2
    >>> type(data)
    <class 'tuple'>
    >>> data = 1.,.2
    >>> type(data)
    <class 'tuple'>

    >>> data = 'foo'
    >>> type(data)
    <class 'str'>
    >>> data = ('foo',)
    >>> type(data)
    <class 'tuple'>
    >>> data = 'foo'.
    Traceback (most recent call last):
    SyntaxError: invalid syntax


Tuple or List
-------------
Both:

    * ordered
    * possible to getitem and slice
    * elements can be duplicated
    * elements of any types

Tuple:

    * immutable
    * one contingent block of data in memory

List:

    * mutable
    * implemented in memory as list of pointers to objects
    * objects are scattered in memory

Memory Footprint:

    >>> from sys import getsizeof
    >>>
    >>> a = [1, 2, 3]
    >>> b = (1, 2, 3)
    >>>
    >>> getsizeof(a)
    120
    >>>
    >>> getsizeof(b)
    64

.. figure:: img/memory-tuple.png

    Define tuple

.. figure:: img/memory-list.png

    Define list

.. figure:: img/memory-all.png

    Define str, tuple and list


Assignments
-----------
.. literalinclude:: assignments/sequence_tuple_create.py
    :caption: :download:`Solution <assignments/sequence_tuple_create.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_tuple_select.py
    :caption: :download:`Solution <assignments/sequence_tuple_select.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_tuple_mean.py
    :caption: :download:`Solution <assignments/sequence_tuple_mean.py>`
    :end-before: # Solution
