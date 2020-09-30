.. _Sequence Tuple:

**************
Sequence Tuple
**************


Rationale
=========
.. highlights::
    * Can store elements of any types
    * Immutable - cannot add, modify or remove items


Type Definition
===============
.. highlights::
    * ``()`` is used more often
    * ``tuple()`` is more readable
    * Single element ``tuple`` require comma at the end (**important!**)
    * Brackets are optional
    * Comma after last element of one element tuple is optional

.. code-block:: python

    data = ()
    data = tuple()

    data = (1,)
    data = (1, 2, 3)
    data = (1.1, 2.2, 3.3)
    data = (True, False)
    data = ('a', 'b', 'c')
    data = ('a', 1, 2.2, True, None)

    data = 1,
    data = 1, 2, 3
    data = 1.1, 2.2, 3.3
    data = True, False
    data = 'a', 'b', 'c'
    data = 'a', 1, 2.2, True, None


Type Casting
============
.. highlights::
    * ``tuple()`` converts argument to ``tuple``

.. code-block:: python

    data = 'abcd'
    tuple(data)
    # ('a', 'b', 'c', 'd')

.. code-block:: python

    data = ['a', 'b', 'c', 'd']
    tuple(data)
    # ('a', 'b', 'c', 'd')

.. code-block:: python

    data = ('a', 'b', 'c', 'd')
    tuple(data)
    # ('a', 'b', 'c', 'd')

.. code-block:: python

    data = {1, 2, 3}
    tuple(data)
    # ('a', 'b', 'c', 'd')

.. code-block:: python

    data = frozenset({'a', 'b', 'c', 'd'})
    tuple(data)
    # ('a', 'b', 'c', 'd')


Get Item
========
.. highlights::
    * More information in :ref:`Sequence Get Item` and :ref:`Sequence Slice`

.. code-block:: python

    data = ('a', 'b', 'c', 'd')

    data[0]         # 'a'
    data[1]         # 'b'
    data[2]         # 'c'
    data[3]         # 'd'


Tuple or Int, Float, Str
=========================
.. code-block:: python

    data = 1
    type(data)
    # <class 'int'>

    data = 1,
    type(data)
    # <class 'tuple'>

    data = 1.
    type(data)
    # <class 'float'>

.. code-block:: python

    type(1.2)        # <class 'float'>
    type(1,2)        # <class 'tuple'>

.. code-block:: python

    type(1.2,)       # <class 'tuple'>
    type(1,2.3)      # <class 'tuple'>

    type(1.)         # <class 'float'>
    type(1,)         # <class 'tuple'>
    type(1.,)        # <class 'tuple'>
    type(.2)         # <class 'float'>
    type(.2,)        # <class 'tuple'>
    type(1.2)        # <class 'float'>
    type(1)          # <class 'int'>

    type(1.,1.)      # <class 'tuple'>
    type(.2,.2)      # <class 'tuple'>
    type(1.,.2)      # <class 'tuple'>

    type('foo')      # <class 'str'>
    type('foo',)     # <class 'tuple'>
    type('foo'.)     # SyntaxError: invalid syntax


Tuple or List
=============
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

.. figure:: img/memory-tuple.png
    :align: center
    :scale: 50%

    Define tuple

.. figure:: img/memory-list.png
    :align: center
    :scale: 50%

    Define list

.. figure:: img/memory-all.png
    :align: center
    :scale: 50%

    Define str, tuple and list


Assignments
===========

Sequence Tuple Create
---------------------
* Assignment name: Sequence Tuple Create
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/sequence_tuple_create.py`
* Last update: 2020-10-01

:English:
    #. Create tuple ``result`` with elements:

        * ``'a'``
        * ``1``
        * ``2.2``

    #. Print ``result``
    #. Print number of elements in ``result``

:Polish:
    #. Stwórz tuple ``result`` z elementami:

        * ``'a'``
        * ``1``
        * ``2.2``

    #. Wypisz ``result``
    #. Wypisz liczbę elementów ``result``

Sequence Tuple Many
-------------------
* Assignment name: Sequence Tuple Many
* Complexity level: medium
* Lines of code to write: 13 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/sequence_tuple_many.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Create a ``tuple`` representing all Species
    #. Calculate mean for each numerical values column
    #. To convert table use multiline select with ``alt`` key in your IDE

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz ``tuple`` z nazwami gatunków
    #. Wylicz średnią arytmetyczną dla każdej z kolumn numerycznych
    #. Do przekonwertowania tabelki wykorzystaj zaznaczanie wielu linijek za pomocą klawisza ``alt`` w Twoim IDE

:Input:
    .. code-block:: text

        "Sepal length", "Sepal width", "Petal length", "Petal width", "Species"
        "5.8", "2.7", "5.1", "1.9", "virginica"
        "5.1", "3.5", "1.4", "0.2", "setosa"
        "5.7", "2.8", "4.1", "1.3", "versicolor"
        "6.3", "2.9", "5.6", "1.8", "virginica"
        "6.4", "3.2", "4.5", "1.5", "versicolor"
        "4.7", "3.2", "1.3", "0.2", "setosa"
        "7.0", "3.2", "4.7", "1.4", "versicolor"
        "7.6", "3.0", "6.6", "2.1", "virginica"
        "4.9", "3.0", "1.4", "0.2", "setosa"
        "4.9", "2.5", "4.5", "1.7", "virginica"
        "7.1", "3.0", "5.9", "2.1", "virginica"

:The whys and wherefores:
    * Defining ``tuple``
    * Learning IDE features

:Hints:
    * ``mean = sum(...) / len(...)``
