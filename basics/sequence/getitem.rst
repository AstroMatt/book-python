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

Sequence GetItem Select
------------------------
* Assignment name: Sequence GetItem Select
* Last update: 2020-11-17
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/sequence_getitem_select.py`

:English:
    #. Use data from "Input" section (see below)
    #. Write header (row with index 0) to ``header: tuple`` variable
    #. Create ``result: list``
    #. Select row at index 2, convert it to ``list`` and add to ``result``
    #. Select row at index 4, convert it to ``tuple`` and add to ``result``
    #. Select row at index -2, convert it to ``set`` and add to ``result``
    #. Select row at index -4, convert it to ``frozenset`` and add to ``result``
    #. Append to ``result``: empty ``list``, empty ``tuple``, empty ``set`` and empty ``frozenset``
    #. Use only indexes and do not use ``for``, ``while`` or ``slice()``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zapisz nagłówek (wiersz o indeksie 0) do zmiennej ``header: tuple``
    #. Stwórz ``result: list``
    #. Wybierz wiersz o indeksie 2, przekonwertuj go do ``list`` i dodaj do ``result``
    #. Wybierz wiersz o indeksie 4, przekonwertuj go do ``tuple`` i dodaj do ``result``
    #. Wybierz wiersz o indeksie -4, przekonwertuj go do ``set`` i dodaj do ``result``
    #. Wybierz wiersz o indeksie -2, przekonwertuj go do ``frozenset`` i dodaj do ``result``
    #. Dodaj na koniec ``result``: pustą ``list``, pustą ``tuple``, pusty ``set``, pusty ``frozenset``
    #. Korzystaj tylko z indeksów i nie używaj ``for``, ``while`` lub ``slice()``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
        ]

:Output:
    .. code-block:: text

        >>> assert type(header) is tuple
        >>> assert type(result) is list
        >>> header
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species')
        >>> result  # doctest: +NORMALIZE_WHITESPACE
        [[5.1, 3.5, 1.4, 0.2, 'setosa'],
         (6.3, 2.9, 5.6, 1.8, 'virginica'),
         {1.3, 2.8, 4.1, 5.7, 'versicolor'},
         frozenset({1.5, 3.2, 4.5, 6.4, 'versicolor'}),
         [],
         (),
         set(),
         frozenset()]

:The whys and wherefores:
    * Using nested data structures
    * Using indexes
    * Type casting

:Hints:
    * ``from pprint import pprint``
    * ``pprint(result)``
