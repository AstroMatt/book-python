.. _Mapping Dict:

************
Mapping Dict
************


Rationale
=========
.. highlights::
    * ``dict`` are key-value storage
    * key lookup is very efficient ``O(1)``
    * Mutable - can add, remove, and modify items


Type Definition
===============
.. highlights::
    * ``{}`` is used more often
    * ``dict()`` is more readable
    * Comma after last element is optional
    * Since Python 3.7 ``dict`` keeps order of elements
    * Before Python 3.7 ``dict`` order is not ensured!!

.. code-block:: python

    data = {}
    data = dict()

    data = {
        1961: 'First Human Space Flight',
        1969: 'First Step on the Moon'}

    data = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    data = dict(
        commander='Melissa Lewis',
        botanist='Mark Watney',
        chemist='Alex Vogel')

.. code-block:: python
    :caption: Duplicating items are overridden by latter

    data = {
        'commander': 'Melissa Lewis',
        'commander': 'Jan Twardowski',
    }
    # {'commander': 'Jan Twardowski'}


Get Item
========
.. highlights::
    * ``[...]`` throws ``KeyError`` exception if key not found in ``dict``
    * ``.get()`` returns ``None`` if key not found
    * ``.get()`` can have default value, if key not found

.. code-block:: python
    :caption: Getitem Method

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    crew['commander']
    # Melissa Lewis

    crew['pilot']
    # KeyError: 'pilot'

.. code-block:: python
    :caption: Get Method

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    crew.get('commander')
    # Melissa Lewis

    crew.get('pilot')
    # None

    crew.get('pilot', 'not assigned')
    # 'not assigned'

.. code-block:: python
    :caption: Getting keys other than ``str``

    calendarium = {
        1961: 'First Human Space Flight',
        1969: 'First Step on the Moon'}

    calendarium[1961]
    # 'First Human Space Flight'

    calendarium.get(1961)
    # 'First Human Space Flight'

    calendarium['1961']
    # KeyError: '1961'

    calendarium.get('1961')
    # None

    calendarium.get('1961', 'unknown')
    # 'unknown'


Get Keys, Values and Key-Value Pairs
====================================
.. highlights::
    * Key can be any hashable object

.. code-block:: python

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    list(crew.keys())
    # ['commander', 'botanist', 'chemist']

    list(crew.values())
    # ['Melissa Lewis', 'Mark Watney', 'Alex Vogel']

    list(crew.items())
    # [('commander', 'Melissa Lewis'),
    #  ('botanist', 'Mark Watney'),
    #  ('chemist', 'Alex Vogel')]


Set Item
========
.. highlights::
    * Adds if value not exist
    * Updates if value exist

.. code-block:: python
    :caption: Set Item Method

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    crew['pilot'] = 'Rick Martinez'

    print(crew)
    # {'commander': 'Melissa Lewis',
    #  'botanist': 'Mark Watney',
    #  'chemist': 'Alex Vogel',
    #  'pilot': 'Rick Martinez'}

.. code-block:: python
    :caption: Update Method

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    crew.update(pilot='Rick Martinez')
    print(crew)
    # {'commander': 'Melissa Lewis',
    #  'botanist': 'Mark Watney',
    #  'chemist': 'Alex Vogel',
    #  'pilot': 'Rick Martinez'}

    crew.update(mission=['Artemis', 'Ares III'])
    print(crew)
    # {'commander': 'Melissa Lewis',
    #  'botanist': 'Mark Watney',
    #  'chemist': 'Alex Vogel',
    #  'pilot': 'Rick Martinez',
    #  'mission': ['Artemis', 'Ares III']}

.. code-block:: python
    :caption: Update Method

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    new = {
        'pilot': 'Rick Martinez',
        'surgeon': 'Chris Beck',
        'engineer': 'Beth Johanssen'}

    crew.update(new)
    print(crew)
    # {'commander': 'Melissa Lewis',
    #  'botanist': 'Mark Watney',
    #  'chemist': 'Alex Vogel',
    #  'pilot': 'Rick Martinez',
    #  'surgeon': 'Chris Beck',
    #  'engineer': 'Beth Johanssen'}


Delete Item
===========
.. code-block:: python
    :caption: Pop Method

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel',
        'pilot': 'Rick Martinez',
        'surgeon': 'Chris Beck',
        'engineer': 'Beth Johanssen'}

    left_alone_on_mars = crew.pop('botanist')

    print(crew)
    # {'commander': 'Melissa Lewis',
    #  'chemist': 'Alex Vogel',
    #  'pilot': 'Rick Martinez',
    #  'surgeon': 'Chris Beck',
    #  'engineer': 'Beth Johanssen'}

    print(left_alone_on_mars)
    # 'Mark Watney'

.. code-block:: python
    :caption: Popitem Method

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    last = crew.popitem()

    print(crew)
    # {'commander': 'Melissa Lewis',
    #  'botanist': 'Mark Watney'}

    print(last)
    # ('chemist', 'Alex Vogel')

.. code-block:: python
    :caption: Del Keyword

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    del crew['chemist']

    print(crew)
    # {'commander': 'Melissa Lewis',
    #  'botanist': 'Mark Watney'}


Get Item and Slice
==================
.. highlights::
    * Get item with index on ``dict`` is not possible
    * Slicing on ``dict`` is not possible

.. code-block:: python

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    crew[0]             # KeyError: 0
    crew[1]             # KeyError: 1
    crew[2]             # KeyError: 2

    crew[-0]            # KeyError: 0
    crew[-1]            # KeyError: -1
    crew[-2]            # KeyError: -2

    crew[1:2]           # TypeError: unhashable type: 'slice'
    crew[:2]            # TypeError: unhashable type: 'slice'
    crew[::2]           # TypeError: unhashable type: 'slice'

.. code-block:: python

    crew = {
        0: 'Melissa Lewis',
        1: 'Mark Watney',
        2: 'Alex Vogel'}

    crew[0]             # 'Melissa Lewis'
    crew[1]             # 'Mark Watney'
    crew[2]             # 'Alex Vogel'

    crew[-0]            # 'Melissa Lewis'
    crew[-1]            # KeyError: -1
    crew[-2]            # KeyError: -2

    crew[1:2]           # TypeError: unhashable type: 'slice'
    crew[:2]            # TypeError: unhashable type: 'slice'
    crew[::2]           # TypeError: unhashable type: 'slice'


Dict or Set
===========
.. highlights::
    * Both ``set`` and ``dict`` keys must be hashable
    * Both ``set`` and ``dict`` uses the same ``{`` and ``}`` braces
    * Despite similar syntax, they are different types

.. code-block:: python

    {1, 2}            # set
    {1: 2}            # dict

    {1, 2, 3, 4}      # set
    {1: 2, 3: 4}      # dict

.. code-block:: python
    :caption: Empty ``dict`` and empty ``set``

    data = {1: 1}       # {1:1}
    data.pop(1)         # {}

    data = {1}          # {1}
    data.pop()          # set()

.. code-block:: python
    :caption: Differences

    data = {1: 1}
    isinstance(data, set)          # False
    isinstance(data, dict)         # True

    data = {1}
    isinstance(data, set)          # True
    isinstance(data, dict)         # False

    data = {}
    isinstance(data, (set, dict))  # True
    isinstance(data, set)          # False
    isinstance(data, dict)         # True


Length
======
.. code-block:: python

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}


    len(crew)
    # 3

    len(crew.keys())
    # 3

    len(crew.values())
    # 3

    len(crew.items())
    # 3


Examples
========
.. code-block:: python

    git = {
        'ce16a8ce': 'commit/1',
        'cae6b510': 'commit/2',
        '895444a6': 'commit/3',
        'aef731b5': 'commit/4',
        '4a92bc79': 'branch/master',
        'b3bbd85a': 'tag/v1.0',
    }


Future
======
.. versionadded:: Python 3.9
    :pep:`584` merge (``|``) and update (``|=``) operators have been added to the built-in dict class.

.. code-block:: python

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    new = {
        'pilot': 'Rick Martinez',
        'surgeon': 'Chris Beck',
        'engineer': 'Beth Johanssen'}

    everyone = crew | new

    print(crew)
    # {'commander': 'Melissa Lewis',
    #  'botanist': 'Mark Watney',
    #  'chemist': 'Alex Vogel'}

    print(new)
    # {'pilot': 'Rick Martinez',
    #  'surgeon': 'Chris Beck',
    #  'engineer': 'Beth Johanssen'}

    print(everyone)
    # {'commander': 'Melissa Lewis',
    #  'botanist': 'Mark Watney',
    #  'chemist': 'Alex Vogel',
    #  'pilot': 'Rick Martinez',
    #  'surgeon': 'Chris Beck',
    #  'engineer': 'Beth Johanssen'}

.. code-block:: python

    crew = {
        'commander': 'Melissa Lewis',
        'botanist': 'Mark Watney',
        'chemist': 'Alex Vogel'}

    new = {
        'pilot': 'Rick Martinez',
        'surgeon': 'Chris Beck',
        'engineer': 'Beth Johanssen'}

    crew |= new

    print(crew)
    # {'commander': 'Melissa Lewis',
    #  'botanist': 'Mark Watney',
    #  'chemist': 'Alex Vogel',
    #  'pilot': 'Rick Martinez',
    #  'surgeon': 'Chris Beck',
    #  'engineer': 'Beth Johanssen'}

    print(new)
    # {'pilot': 'Rick Martinez',
    #  'surgeon': 'Chris Beck',
    #  'engineer': 'Beth Johanssen'}


Assignments
===========

Mapping Dict Define
-------------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/mapping_dict_define.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create ``result: dict`` representing input data

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz ``result: dict`` reprezentujący dane wejściowe

:Input:
    .. code-block:: text

        First Name: Jan
        Last Name: Twardowski
        Missions: Apollo, Artemis

Mapping Dict Items
------------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/mapping_dict_items.py`

:English:
    #. Use data from "Input" section (see below)
    #. Print list of ``DATA`` keys
    #. Print list of ``DATA`` values
    #. Print list of ``DATA`` key-value pairs
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wypisz listę kluczy z ``DATA``
    #. Wypisz listę wartości z ``DATA``
    #. Wypisz listę pary klucz-wartość z ``DATA``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = {
            'Sepal length': 5.8,
            'Sepal width': 2.7,
            'Petal length': 5.1,
            'Petal width': 1.9,
        }

:Output:
    .. code-block:: python

        keys: list
        # ['Sepal length', 'Sepal width', 'Petal length', 'Petal width']

        values: list
        # [5.8, 2.7, 5.1, 1.9]

        items: List[tuple]
        # [('Sepal length', 5.8),
        #  ('Sepal width', 2.7),
        #  ('Petal length', 5.1),
        #  ('Petal width', 1.9)]

Mapping Dict Substitute
-----------------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/mappting_dict_substitute.py`

:English:
    #. Use data from "Input" section (see below)
    #. Ask user to input single letter
    #. Convert to lowercase
    #. If letter is in ``PL_ASCII`` then use conversion value as letter
    #. Print letter

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Poproś użytkownika o wprowadzenie jednej litery
    #. Przekonwertuj literę na małą
    #. Jeżeli litera jest w ``PL_ASCII`` to użyj przekonwertowanej wartości jako litera
    #. Wypisz literę

:Input:
    .. code-block:: python

        PL_ASCII = {'ą': 'a', 'ć': 'c', 'ę': 'e',
                    'ł': 'l', 'ń': 'n', 'ó': 'o',
                    'ś': 's', 'ż': 'z', 'ź': 'z'}

Mapping Dict Get
----------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/mapping_dict_get.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create translator of pilot's alphabet
    #. Each letter has it's phonetic counterpart
    #. To convert table use multiline select with ``alt`` key in your IDE (if shortcut key is not working in your IDE, use only first four letters)
    #. Ask user to input letter
    #. User will always put only one capitalized letter or number
    #. Print phonetic letter pronunciation
    #. If user type character not existing in alphabet, print: "Pilots don't say that"
    #. Do not use ``if``, ``try``, and ``except``

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz tłumacza alfabetu pilotów
    #. Pojedynczym literom przyporządkuj ich fonetyczne odpowiedniki
    #. Do przekonwertowania tabelki wykorzystaj zaznaczanie wielu linijek za pomocą klawisza ``alt`` w Twoim IDE (jeżeli skrót klawiszowy nie działa w Twoim IDE, użyj tylko cztery pierwsze litery)
    #. Poproś użytkownika o wprowadzenie litery
    #. Użytkownik zawsze poda tylko jedną dużą literę lub cyfrę
    #. Wypisz fonetyczną wymowę litery
    #. Jeżeli wpisał znak, który nie występuje w alfabecie, wypisz: "Pilots don't say that"
    #. Nie używaj ``if``, ``try`` ani ``except``

:Input:
    .. code-block:: text

        Letter, Pronounce
        A, Alfa
        B, Bravo
        C, Charlie
        D, Delta
        E, Echo
        F, Foxtrot
        G, Golf
        H, Hotel
        I, India
        J, Juliet
        K, Kilo
        L, Lima
        M, Mike
        N, November
        O, Oscar
        P, Papa
        Q, Quebec
        R, Romeo
        S, Sierra
        T, Tango
        U, Uniform
        V, Victor
        W, Whisky
        X, X-Ray
        Y, Yankee
        Z, Zulu

:The whys and wherefores:
    * Defining ``dict`` with values
    * Type casting
