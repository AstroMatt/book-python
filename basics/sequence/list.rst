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
    * ``[]`` is used more often
    * ``list()`` is more readable
    * Comma after last element of a one element list is optional
    * Brackets are required

.. code-block:: python

    data = list()
    data = []

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
    :caption: Adding two lists

    data = [1, 2]
    data = data + [3, 4]

    print(data)
    # [1, 2, 3, 4]

.. code-block:: python
    :caption: Adding two lists

    data = [1, 2]
    data += [3, 4]

    print(data)
    # [1, 2, 3, 4]

.. code-block:: python
    :caption: Extending lists

    data = [1, 2]
    data.extend([3, 4])

    print(data)
    # [1, 2, 3, 4]

.. code-block:: python
    :caption: Appending single item

    data = [1, 2]
    data.append(3)

    print(data)
    # [1, 2, 3]

.. code-block:: python
    :caption: Appending multiple items

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
    any(data)       # True
    all(data)       # False

.. code-block:: python

    data = [True, False, True]

    min(data)       # False
    max(data)       # True
    sum(data)       # 2
    len(data)       # 3
    any(data)       # True
    all(data)       # False


Assignments
===========

Sequence List Create
--------------------
* Assignment name: Sequence List Create
* Complexity level: easy
* Lines of code to write: 1 lines
* Estimated time of completion: 2 min
* Suggested filename: sequence_list_create.py

English:
    #. Create list ``result`` with elements:

        * ``'a'``
        * ``1``
        * ``2.2``

    #. Compare result with "Tests" section (see below)

Polish:
    #. Stwórz listę ``result`` z elementami:

        * ``'a'``
        * ``1``
        * ``2.2``

    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    .. code-block:: text

        >>> assert type(result) is list
        >>> result
        ['a', 1, 2.2]

Sequence List Many
------------------
* Assignment name: Sequence List Many
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min
* Suggested filename: sequence_list_many.py

English:
    #. Use data from "Given" section (see below)
    #. Create list ``a`` with data from row 1
    #. Create list ``b`` with data from row 2
    #. Create list ``c`` with data from row 3
    #. Do not use values from "Row" column
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Stwórz listę ``a`` z danymi z wiersza 1
    #. Stwórz listę ``b`` z danymi z wiersza 2
    #. Stwórz listę ``c`` z danymi z wiersza 3
    #. Nie używaj wartości z kolumny "Row"
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. csv-table:: Input data
        :header: "Row", "Sepal length", "Sepal width", "Petal length", "Petal width", "Species"
        :stub-columns: 1

        "1", "5.8", "2.7", "5.1", "1.9", "virginica"
        "2", "5.1", "3.5", "1.4", "0.2", "setosa"
        "3", "5.7", "2.8", "4.1", "1.3", "versicolor"

Tests:
    .. code-block:: text

        >>> assert type(a) is list
        >>> assert type(b) is list
        >>> assert type(c) is list
        >>> a
        # [5.8, 2.7, 5.1, 1.9, 'virginica']
        >>> b
        # [5.1, 3.5, 1.4, 0.2, 'setosa']
        >>> c
        # [5.7, 2.8, 4.1, 1.3, 'versicolor']

Sequence List Modify
--------------------
* Assignment name: Sequence List Modify
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 5 min
* Suggested filename: sequence_list_modify.py

English:
    #. Use data from "Given" section (see below)
    #. Insert at the begin of ``a`` last element popped from ``b``
    #. Append to the ``b`` last element popped from ``a``
    #. For getting elements use ``list.pop()``
    #. From list ``c`` using ``del`` delete last element
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Na początek ``a`` wstaw ostatni element wyciągnięty z ``b``
    #. Na koniec ``b`` wstaw ostatni element wyciągnięty z ``a``
    #. Do wyciągnięcia używaj ``list.pop()``
    #. Z listy ``c`` za pomocą ``del`` usuń ostatni element
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        a = [4.7, 3.2, 1.3, 0.2, 'setosa']
        b = [7.0, 3.2, 4.7, 1.4, 'versicolor']
        c = [7.6, 3.0, 6.6, 2.1, 'virginica']

Tests:
    .. code-block:: text

        >>> assert type(a) is list
        >>> assert type(b) is list
        >>> assert type(c) is list
        >>> a
        ['versicolor', 4.7, 3.2, 1.3, 0.2]
        >>> b
        [7.0, 3.2, 4.7, 1.4, 'setosa']
        >>> c
        [7.6, 3.0, 6.6, 2.1]

