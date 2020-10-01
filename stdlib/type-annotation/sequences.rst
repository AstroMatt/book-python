*********
Sequences
*********


One-dimensional sequences
=========================

List
----
.. code-block:: python

    data: list = ['a', 2, 3.3]

.. code-block:: python

    from typing import List

    data: List[int] = [1, 2, 3]
    data: List[float] = [1.1, 2.2, 3.3]
    data: List[str] = ['a', 'b', 'c']

Set
---
.. code-block:: python

    data: set = {'a', 2, 3.3}

.. code-block:: python

    from typing import Set

    data: Set[int] = {1, 2, 3}
    data: Set[float] = {1.1, 2.2, 3.3}
    data: Set[str] = {'a', 'b', 'c'}

Tuple
-----
.. code-block:: python

    data: tuple = 'a', 2, 3.3
    data: tuple = ('a', 2, 3.3)

    data: tuple[int, int, int] = (1, 2, 3)
    data: tuple[float, float, float] = (1.1, 2.2, 3.3)
    data: tuple[str, str, str] = ('a', 'b', 'c')
    data: tuple[str, int, float] = ('a', 2, 3.3)

.. code-block:: python

    from typing import Sequence


    def fire_employees(e: Sequence[Employee]) -> None:
        print(employee)


Multidimensional sequences
==========================

List of dict
------------
.. code-block:: python

    from typing import List

    list_of_dicts: List[dict] = [
        {'a': 1},
        {2: 'b'},
        {3.3: 'c'}
    ]

.. code-block:: python

    from typing import List, Dict

    list_of_dicts: List[Dict[str, int]] = [
        {'a': 1},
        {'b': 2},
        {'c': 3},
    ]

List of tuples
--------------
.. code-block:: python

    from typing import List

    data: List[tuple] = [
        (1, 2, 3),
        (1.1, 2.2, 3.3),
        ('a', 'b', 'c'),
        ('a', 2, 3.3),
    ]

.. code-block:: python

    from typing import List, Tuple

    data: List[Tuple[int, int, int]] = [
        (1, 2, 3),
        (1, 2, 3),
        (1, 2, 3),
    ]
