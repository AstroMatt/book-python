.. _Sequence Type Annotation:

************************
Sequence Type Annotation
************************


Rationale
=========
* Python 3.9 introduced :pep:`585` -- Type Hinting Generics In Standard Collections
* Before Python 3.9 you need ``from typing import List, Set, Tuple, Dict``

.. code-block:: python

    DATA = [
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    ]

    for row in DATA:
        species = row[-1]
        species  # IDE don't know what type is species
                 # and cannot give hints for autocompletion

    for row in DATA:
        species: str = row[-1]
        species  # IDE knows exacly what type is species
                 # and what methods hint for autocompletion

Tuple
=====
.. code-block:: python
    :caption: Generic type annotation

    data: tuple = ()
    data: tuple = tuple()

    data: tuple = 'a', 2, 3.3
    data: tuple = ('a', 2, 3.3)

.. code-block:: python
    :caption: Explicit type annotation since Python 3.9

    data: tuple[int, int, int] = (1, 2, 3)
    data: tuple[str, str, str] = ('setosa', 'virginica', 'versicolor')
    data: tuple[str, int, float] = ('a', 2, 3.3)

    data: tuple[int, ...] = (1, 2, 3)
    data: tuple[str, ...] = ('setosa', 'virginica', 'versicolor')

.. code-block:: python
    :caption: Explicit type annotation before Python 3.9

    from typing import Tuple

    data: Tuple[int, int, int] = (1, 2, 3)
    data: Tuple[str, str, str] = ('setosa', 'virginica', 'versicolor')
    data: Tuple[str, int, float] = ('a', 2, 3.3)

    data: Tuple[int, ...] = (1, 2, 3)
    data: Tuple[str, ...] = ('setosa', 'virginica', 'versicolor')


List
====
.. code-block:: python

    data: list = list()
    data: list = []
    data: list = ['a', 1, 2.2]

    data: list[int] = [1, 2, 3, 4]
    data: list[float] = [5.8, 2.7, 5.1, 1.9]
    data: list[str] = ['a', 'b', 'c', 'd']

.. code-block:: python
    :caption: Before Python 3.9

    from typing import List

    data: list = list()
    data: list = []
    data: list = ['a', 1, 2.2]
    data: List[int] = [1, 2, 3, 4]
    data: List[float] = [5.8, 2.7, 5.1, 1.9]
    data: List[str] = ['a', 'b', 'c', 'd']


Set
===
.. code-block:: python

    data: set = set()
    data: set = {'a', 1, 2.2}

    data: set[int] = {1, 2, 3}
    data: set[float] = {0.0, 1.1, 2.2}
    data: set[str] = {'a', 'b', 'c'}

.. code-block:: python
    :caption: Before Python 3.9

    from typing import Set

    data: set = set()
    data: set = {'a', 1, 2.2}
    data: Set[int] = {1, 2, 3}
    data: Set[float] = {0.0, 1.1, 2.2}
    data: Set[str] = {'a', 'b', 'c'}


Frozenset
=========
.. code-block:: python
    :caption: Generic type annotation

    data: frozenset = set()
    data: frozenset = {'a', 1, 2.2}

    data: frozenset[int] = {1, 2, 3}
    data: frozenset[float] = {0.0, 1.1, 2.2}
    data: frozenset[str] = {'a', 'b', 'c'}

.. code-block:: python
    :caption: Before Python 3.9

    from typing import FrozenSet

    data: frozenset = set()
    data: frozenset = {'a', 1, 2.2}
    data: FrozenSet[int] = {1, 2, 3}
    data: FrozenSet[float] = {0.0, 1.1, 2.2}
    data: FrozenSet[str] = {'a', 'b', 'c'}


List of Tuples
==============
.. code-block:: python

    data: list[tuple] = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    data: list[tuple[float, float, float, float, str]] = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    row = tuple[float, float, float, float, str]
    data: list[row] = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

.. code-block:: python
    :caption: Before Python 3.9

    from typing import List, Tuple

    data: List[tuple] = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    data: List[Tuple[float, float, float, float, str]] = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    Row = Tuple[float, float, float, float, str]
    data: List[Row] = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]


List of Lists
=============
.. code-block:: python

    data: list[list] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    data: list[list[int]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

.. code-block:: python
    :caption: Before Python 3.9

    from typing import List

    data: List[list] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    data: List[List[int]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]


Aliases
=======
.. code-block:: python

    Point = tuple[int, int]
    locations: list[Point] = [
        (0, 1),
        (5, -3),
        (-10, 20)
    ]

    GeographicCoordinate = tuple[float, float]
    locations: list[GeographicCoordinate] = [
        (25.91375, -60.15503),
        (-11.01983, -166.48477),
        (-11.01983, -166.48477)
    ]

    Iris = tuple[float, float, float, float, str]
    data: list[Iris] = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

.. code-block:: python
    :caption: Before Python 3.9

    from typing import List, Tuple


    GeographicCoordinate = Tuple[float, float]
    locations: List[GeographicCoordinate] = [
        (25.91375, -60.15503),
        (-11.01983, -166.48477),
        (-11.01983, -166.48477)
    ]

    Iris = Tuple[float, float, float, float, str]
    data: List[Iris] = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]


Unions
======
.. code-block:: python

    from typing import Union


    data: list[Union[list, tuple, set]] = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
    ]

    data: llist[Union[list[int], tuple[int, ...], set[int]]] = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
    ]

    row = Union[list[int], tuple[int, ...], set[int]]
    data: list[row] = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
    ]

.. code-block:: python
    :caption: Before Python 3.9

    from typing import Union, List, Tuple, Set


    data: List[Union[list, tuple, set]] = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
    ]


    data: List[Union[List[int], Tuple[int, int, int], Set[int]]] = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
    ]


    Row = Union[List[int],
                Tuple[int, int, int],
                Set[int]]

    data: List[Row] = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
    ]


More Information
================
.. note:: More information in :ref:`Type Annotations` and :ref:`CI/CD Type Checking`
