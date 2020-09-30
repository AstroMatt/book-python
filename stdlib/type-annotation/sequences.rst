*********
Sequences
*********


One-dimensional sequences
=========================

List
----
.. code-block:: python

    my_list: list = ['a', 2, 3.3]

.. code-block:: python

    from typing import List

    my_list: List[int] = [1, 2, 3]
    my_list: List[float] = [1.1, 2.2, 3.3]
    my_list: List[str] = ['a', 'b', 'c']

Set
---
.. code-block:: python

    my_set: set = {'a', 2, 3.3}

.. code-block:: python

    from typing import Set

    my_set: Set[int] = {1, 2, 3}
    my_set: Set[float] = {1.1, 2.2, 3.3}
    my_set: Set[str] = {'a', 'b', 'c'}

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

    my_data: List[tuple] = [
        (1, 2, 3),
        (1.1, 2.2, 3.3),
        ('a', 'b', 'c'),
        ('a', 2, 3.3),
    ]

.. code-block:: python

    from typing import List, Tuple

    my_data: List[Tuple[int, int, int]] = [
        (1, 2, 3),
        (1, 2, 3),
        (1, 2, 3),
    ]
