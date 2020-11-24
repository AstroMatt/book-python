.. _Loop Dict:

**************
Loop over Dict
**************


Rationale
=========
.. highlights::
    * Since Python 3.7 ``dict`` keeps order
    * Before Python 3.7 ``dict`` order is not ensured!!


Iterate
=======
.. highlights::
    * By default ``dict`` iterates over keys
    * Suggested variable name: ``key``

.. code-block:: python

    DATA = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    for obj in DATA:
        print(obj)

    # 'Sepal length'
    # 'Sepal width'
    # 'Petal length'
    # 'Petal width'
    # 'Species'


Iterate Keys
============
.. highlights::
    * Suggested variable name: ``key``

.. code-block:: python

    DATA = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    list(DATA.keys())
    # ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']

    for obj in DATA.keys():
        print(obj)

    # 'Sepal length'
    # 'Sepal width'
    # 'Petal length'
    # 'Petal width'
    # 'Species'


Iterate Values
==============
.. highlights::
    * Suggested variable name: ``value``

.. code-block:: python

    DATA = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    list(DATA.values())
    # [5.1, 3.5, 1.4, 0.2, 'setosa']

    for obj in DATA.values():
        print(obj)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'


Iterate Key-Value Pairs
=======================
.. highlights::
    * Suggested variable name: ``key``, ``value``

.. code-block:: python
    :caption: Getting pair: ``key``, ``value`` from ``dict`` items

    DATA = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    list(DATA.items())
    # [('Sepal length', 5.1),
    #  ('Sepal width', 3.5),
    #  ('Petal length', 1.4),
    #  ('Petal width', 0.2),
    #  ('Species', 'setosa')]

    for key, value in DATA.items():
        print(key, '->', value)

    # Sepal length -> 5.1
    # Sepal width -> 3.5
    # Petal length -> 1.4
    # Petal width -> 0.2
    # Species -> setosa


List of Dicts
=============
.. code-block:: python
    :caption: Unpacking ``list`` of ``dict``

    DATA = [
        {'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
        {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
        {'Sepal length': 6.3, 'Sepal width': 2.9, 'Petal length': 5.6, 'Petal width': 1.8, 'Species': 'virginica'},
    ]

    for row in DATA:
        sepal_length = row['Sepal length']
        species = row['Species']
        print(f'{species} -> {sepal_length}')

    # setosa -> 5.1
    # versicolor -> 5.7
    # virginica -> 6.3


Generate with Range
===================
.. highlights::
    * ``range()``
    * Pythonic way is to use ``zip()``
    * Don't use ``len(range(...))`` - it evaluates generator

.. code-block:: python
    :caption: Create ``dict`` from two ``list``

    header = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
    data = [5.1, 3.5, 1.4, 0.2, 'setosa']
    result = {}

    for i in range(len(header)):
        key = header[i]
        value = data[i]
        result[key] = value

    print(result)
    # {'Sepal length': 5.1,
    #  'Sepal width': 3.5,
    #  'Petal length': 1.4,
    #  'Petal width': 0.2,
    #  'Species': 'setosa'}

Generate with Enumerate
=======================
.. highlights::
    * ``enumerate()``
    * ``_`` regular variable name (not a special syntax)
    * ``_`` by convention is used when variable will not be referenced

.. code-block:: python
    :caption: Create ``dict`` from two ``list``

    header = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
    data = [5.1, 3.5, 1.4, 0.2, 'setosa']
    result = {}

    for i, key in enumerate(header):
        result[key] = data[i]

    print(result)
    # {'Sepal length': 5.1,
    #  'Sepal width': 3.5,
    #  'Petal length': 1.4,
    #  'Petal width': 0.2,
    #  'Species': 'setosa'}


Generate with Zip
=================
.. highlights::
    * ``zip()``
    * The most Pythonic way

.. code-block:: python

    header = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
    data = [5.1, 3.5, 1.4, 0.2, 'setosa']
    result = {}

    for key, value in zip(header, data):
        result[key] = value

    print(result)
    # {'Sepal length': 5.1,
    #  'Sepal width': 3.5,
    #  'Petal length': 1.4,
    #  'Petal width': 0.2,
    #  'Species': 'setosa'}

.. code-block:: python

    header = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
    data = [5.1, 3.5, 1.4, 0.2, 'setosa']

    result = dict(zip(header, data))

    print(result)
    # {'Sepal length': 5.1,
    #  'Sepal width': 3.5,
    #  'Petal length': 1.4,
    #  'Petal width': 0.2,
    #  'Species': 'setosa'}


Assignments
===========

Loop Dict To Dict
-----------------
* Assignment: Loop Dict To Dict
* Filename: loop_dict_to_dict.py
* Complexity: easy
* Lines of code to write: 4 lines
* Estimated time: 8 min

English:
    #. Use data from "Given" section (see below)
    #. Convert to ``result: dict[str, str]``
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Przekonwertuj do ``result: dict[str, str]``
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        DATA = {
            6: ['Doctorate', 'Prof-school'],
            5: ['Masters', 'Bachelor', 'Engineer'],
            4: ['HS-grad'],
            3: ['Junior High'],
            2: ['Primary School'],
            1: ['Kindergarten'],
        }

Tests:
    >>> assert type(result) is dict
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'Doctorate': '6',
     'Prof-school': '6',
     'Masters': '5',
     'Bachelor': '5',
     'Engineer': '5',
     'HS-grad': '4',
     'Junior High': '3',
     'Primary School': '2',
     'Kindergarten': '1'}

Loop Dict To List
-----------------
* Assignment: Loop Dict To List
* Filename: loop_dict_to_list.py
* Complexity: medium
* Lines of code to write: 6 lines
* Estimated time: 8 min

English:
    #. Use data from "Given" section (see below)
    #. Print ``list[dict]``:

        * key - name from the header
        * value - measurement or species

    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Wypisz ``list[dict]``:

        * klucz: nazwa z nagłówka
        * wartość: wyniki pomiarów lub gatunek

    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
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

Tests:
    >>> assert type(result) is list
    >>> assert all(type(x) is dict for x in result)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'Sepal length': 5.8, 'Sepal width': 2.7, 'Petal length': 5.1, 'Petal width': 1.9, 'Species': 'virginica'},
     {'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
     {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
     {'Sepal length': 6.3, 'Sepal width': 2.9, 'Petal length': 5.6, 'Petal width': 1.8, 'Species': 'virginica'},
     {'Sepal length': 6.4, 'Sepal width': 3.2, 'Petal length': 4.5, 'Petal width': 1.5, 'Species': 'versicolor'},
     {'Sepal length': 4.7, 'Sepal width': 3.2, 'Petal length': 1.3, 'Petal width': 0.2, 'Species': 'setosa'}]

Loop Dict Label Encoder
-----------------------
* Assignment: Loop Dict Label Encoder
* Filename: loop_dict_label_encoder.py
* Complexity: hard
* Lines of code to write: 13 lines
* Estimated time: 13 min

English:
    #. Use data from "Given" section (see below)
    #. Define:

        * ``features: list[tuple]`` - measurements
        * ``labels: list[int]`` - species
        * ``label_encoder: dict[int, str]`` - dictionary with encoded (as numbers) species names

    #. Separate header from data
    #. To encode and decode ``labels`` (species) we need ``label_encoder: dict[int, str]``:

        * key - id (incremented integer value)
        * value - species name

    #. ``label_encoder`` must be generated from ``DATA``
    #. For each row add appropriate data to ``features``, ``labels`` and ``label_encoder``
    #. Print ``features``, ``labels`` and ``label_encoder``
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Zdefiniuj:

        * ``features: list[tuple]`` - pomiary
        * ``labels: list[int]`` - gatunki
        * ``label_encoder: dict[int, str]`` - słownik zakodowanych (jako cyfry) nazw gatunków

    #. Odseparuj nagłówek od danych
    #. Aby móc zakodować i odkodować ``labels`` (gatunki) potrzebny jest ``label_encoder: dict[int, str]``:

        * key - identyfikator (kolejna liczba rzeczywista)
        * value - nazwa gatunku

    #. ``label_encoder`` musi być wygenerowany z ``DATA``
    #. Dla każdego wiersza dodawaj odpowiednie dane do ``feature``, ``labels`` i ``label_encoder``
    #. Wypisz ``feature``, ``labels`` i ``label_encoder``
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * Create reversed lookup dict

Given:
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

Tests:
    >>> assert type(features) is list
    >>> assert type(labels) is list
    >>> assert type(label_encoder) is dict

    >>> assert all(type(x) is tuple for x in features)
    >>> assert all(type(x) is int for x in labels)
    >>> assert all(type(x) is int for x in label_encoder.keys())
    >>> assert all(type(x) is str for x in label_encoder.values())

    >>> features  # doctest: +NORMALIZE_WHITESPACE
    [(5.8, 2.7, 5.1, 1.9),
     (5.1, 3.5, 1.4, 0.2),
     (5.7, 2.8, 4.1, 1.3),
     (6.3, 2.9, 5.6, 1.8),
     (6.4, 3.2, 4.5, 1.5),
     (4.7, 3.2, 1.3, 0.2)]

    >>> labels
    [0, 1, 2, 0, 2, 1]

    >>> label_encoder  # doctest: +NORMALIZE_WHITESPACE
    {0: 'virginica',
     1: 'setosa',
     2: 'versicolor'}

