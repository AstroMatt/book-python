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
* Assignment name: Mapping Generate Pairs
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 1 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/mapping_generate_pairs.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create ``result: dict``
    #. Convert ``DATA`` to ``dict`` and assign to ``result``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz ``result: dict``
    #. Przekonwertuj ``DATA`` do ``dict`` i przypisz do ``result``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = [
            ('Sepal length', 5.8),
            ('Sepal width', 2.7),
            ('Petal length', 5.1),
            ('Petal width', 1.9),
            ('Species', 'virginica')
        ]

:Output:
    .. code-block:: python

        result: dict
        # {'Sepal length': 5.8,
        #  'Sepal width': 2.7,
        #  'Petal length': 5.1,
        #  'Petal width': 1.9,
        #  'Species': 'virginica'}

Mapping Generate Enumerate
--------------------------
* Assignment name: Mapping Generate Enumerate
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/mapping_generate_enumerate.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create ``result: dict``
    #. Using ``enumerate()`` convert data to ``dict`` and assign to ``result``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz ``result: dict``
    #. Używając ``enumerate()`` przekonwertuj dane do ``dict`` i przypisz do ``result``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = ['setosa', 'versicolor', 'virginica']

:Output:
    .. code-block:: python

        result: dict
        # {0: 'setosa',
        #  1: 'versicolor',
        #  2: 'virginica'}

Mapping Generate Zip
--------------------
* Assignment name: Mapping Generate Zip
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/mapping_generate_zip.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create ``result: dict``
    #. Using ``zip()`` convert data to ``dict`` and assign to ``result``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz ``result: dict``
    #. Używając ``zip()`` przekonwertuj dane do ``dict`` i przypisz do ``result``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        KEYS =  ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
        VALUES = [5.8, 2.7, 5.1, 1.9, 'virginica']

:Output:
    .. code-block:: python

        result: dict
        # {'Sepal length': 5.8,
        #  'Sepal width': 2.7,
        #  'Petal length': 5.1,
        #  'Petal width': 1.9,
        #  'Species': 'virginica'}
