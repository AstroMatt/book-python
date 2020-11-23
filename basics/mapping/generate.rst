****************
Mapping Generate
****************


Pair
====
.. code-block:: python

    pair = [
        ('commander', 'Melissa Lewis'),
    ]

    dict(pair)
    # {'commander': 'Melissa Lewis'}


List of Pairs
=============
.. code-block:: python

    pairs = [
        ('commander', 'Melissa Lewis'),
        ('botanist', 'Mark Watney'),
        ('chemist', 'Alex Vogel'),
    ]

    dict(pairs)
    # {
    #   'commander': 'Melissa Lewis',
    #   'botanist': 'Mark Watney',
    #   'chemist': 'Alex Vogel',
    # }


Enumerate
=========
.. code-block:: python

    crew = ['Melissa Lewis', 'Mark Watney', 'Alex Vogel']

    astronaut = enumerate(crew)

    next(astronaut)
    # (0, 'Melissa Lewis')

    next(astronaut)
    # (1, 'Mark Watney')

    next(astronaut)
    # (2, 'Alex Vogel')

    next(astronaut)
    # Traceback (most recent call last):
    #     ...
    # StopIteration

.. code-block:: python

    crew = ['Melissa Lewis', 'Mark Watney', 'Alex Vogel']

    list(enumerate(crew))
    # [(0, 'Melissa Lewis'),
    #  (1, 'Mark Watney'),
    #  (2, 'Alex Vogel')]

    dict(enumerate(crew))
    # {0: 'Melissa Lewis',
    #  1: 'Mark Watney',
    #  2: 'Alex Vogel'}


Zip
===
.. highlights::
    * ``zip`` is a generator
    * ``zip`` will create a list of pairs (like ``dict.items()``)

.. code-block:: python

    roles = ['commander', 'botanist', 'chemist']
    crew = ['Melissa Lewis', 'Mark Watney', 'Alex Vogel']

    astronaut = zip(roles, crew)

    next(astronaut)
    # ('commander', 'Melissa Lewis')

    next(astronaut)
    # ('botanist', 'Mark Watney')

    next(astronaut)
    # ('chemist', 'Alex Vogel')

    next(astronaut)
    # Traceback (most recent call last):
    #     ...
    # StopIteration

.. code-block:: python

    roles = ['commander', 'botanist', 'chemist']
    crew = ['Melissa Lewis', 'Mark Watney', 'Alex Vogel']

    list(zip(roles, crew))
    # [('commander', 'Melissa Lewis'),
    #  ('botanist', 'Mark Watney'),
    #  ('chemist', 'Alex Vogel')]

    dict(zip(roles, crew))
    # {'commander': 'Melissa Lewis',
    #  'botanist': 'Mark Watney',
    #  'chemist': 'Alex Vogel'}

.. code-block:: python

    roles = ['commander', 'botanist', 'chemist']
    crew = [('Melissa', 'Lewis'), ('Mark', 'Watney'), ('Alex', 'Vogel')]

    astronauts = zip(roles, crew)
    astronauts
    # <zip object at 0x120c487c0>

    next(astronauts)
    # ('commander', ('Melissa', 'Lewis'))

    next(astronauts)
    # ('botanist', ('Mark', 'Watney'))

    next(astronauts)
    # ('chemist', ('Alex', 'Vogel'))

    next(astronauts)
    # Traceback (most recent call last):
    #     ...
    # StopIteration

.. code-block:: python

    roles = ['commander', 'botanist', 'chemist']
    crew = [('Melissa', 'Lewis'), ('Mark', 'Watney'), ('Alex', 'Vogel')]

    list(zip(roles, crew))
    # [('commander', ('Melissa', 'Lewis')),
    #  ('botanist', ('Mark', 'Watney')),
    #  ('chemist', ('Alex', 'Vogel'))]

    dict(zip(roles, crew))
    # {'commander': ('Melissa', 'Lewis'),
    #  'botanist': ('Mark', 'Watney'),
    #  'chemist': ('Alex', 'Vogel')}


Assignments
===========

Mapping Generate Pairs
----------------------
* Assignment: Mapping Generate Pairs
* Filename: mapping_generate_pairs.py
* Complexity: easy
* Lines of code to write: 1 lines
* Estimated time of completion: 3 min

English:
    #. Use data from "Given" section (see below)
    #. Create ``result: dict``
    #. Convert ``DATA`` to ``dict`` and assign to ``result``
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Stwórz ``result: dict``
    #. Przekonwertuj ``DATA`` do ``dict`` i przypisz do ``result``
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        DATA = [
            ('Sepal length', 5.8),
            ('Sepal width', 2.7),
            ('Petal length', 5.1),
            ('Petal width', 1.9),
            ('Species', 'virginica')
        ]

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'Sepal length': 5.8,
     'Sepal width': 2.7,
     'Petal length': 5.1,
     'Petal width': 1.9,
     'Species': 'virginica'}

Mapping Generate Enumerate
--------------------------
* Assignment: Mapping Generate Enumerate
* Filename: mapping_generate_enumerate.py
* Complexity: easy
* Lines of code to write: 1 lines
* Estimated time of completion: 3 min

English:
    #. Use data from "Given" section (see below)
    #. Create ``result: dict``
    #. Using ``enumerate()`` convert data to ``dict`` and assign to ``result``
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Stwórz ``result: dict``
    #. Używając ``enumerate()`` przekonwertuj dane do ``dict`` i przypisz do ``result``
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        DATA = ['setosa', 'versicolor', 'virginica']

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {0: 'setosa',
     1: 'versicolor',
     2: 'virginica'}

Mapping Generate Zip
--------------------
* Assignment: Mapping Generate Zip
* Filename: mapping_generate_zip.py
* Complexity: easy
* Lines of code to write: 1 lines
* Estimated time of completion: 3 min

English:
    #. Use data from "Given" section (see below)
    #. Create ``result: dict``
    #. Using ``zip()`` convert data to ``dict`` and assign to ``result``
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Stwórz ``result: dict``
    #. Używając ``zip()`` przekonwertuj dane do ``dict`` i przypisz do ``result``
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        KEYS =  ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
        VALUES = [5.8, 2.7, 5.1, 1.9, 'virginica']

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'Sepal length': 5.8,
     'Sepal width': 2.7,
     'Petal length': 5.1,
     'Petal width': 1.9,
     'Species': 'virginica'}
