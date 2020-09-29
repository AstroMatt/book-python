.. _Loop Comprehension:

******************
Loop Comprehension
******************


Recap
=====
.. code-block:: python

    result = []

    for x in range(0,5):
        result.append(x)

    print(result)
    # [0, 1, 2, 3, 4]


Syntax
======
.. code-block:: text

    result = [<RETURN> for <VARIABLE> in <ITERABLE>]

.. code-block:: python

    [x for x in range(0,5)]
    # [0, 1, 2, 3, 4]


Convention
==========
.. highlights::
    * Use shorter variable names
    * ``x`` is common name


Comprehensions and Generator Expression
=======================================
.. highlights::
    * Comprehensions executes instantly
    * Generator expression executes lazily

.. code-block:: python

    list(x for x in range(0,5))        # [0, 1, 2, 3, 4]
    [x for x in range(0,5)]            # [0, 1, 2, 3, 4]

    set(x for x in range(0,5))         # {0, 1, 2, 3, 4}
    {x for x in range(0,5)}            # {0, 1, 2, 3, 4}

    dict((x,x) for x in range(0,5))    # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
    {x:x for x in range(0,5)}          # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}

    tuple(x for x in range(0,5))       # (0, 1, 2, 3, 4)
    (x for x in range(0,5))            # <generator object <genexpr> at 0x118c1aed0>


Comprehensions or Generator Expression
======================================
.. code-block:: python
    :caption: Comprehension

    data = [x for x in range(0,10)]

    for x in data:
        print(x)
        if x == 3:
            break

    # 0
    # 1
    # 2
    # 3

    for x in data:
        print(x)
        if x == 6:
            break
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6

    print(list(data))
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(list(data))
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

.. code-block:: python
    :caption: Generator

    data = (x for x in range(0,10))

    for x in data:
        print(x)
        if x == 3:
            break

    # 0
    # 1
    # 2
    # 3

    for x in data:
        print(x)
        if x == 6:
            break

    # 4
    # 5
    # 6

    print(list(data))
    # [7, 8, 9]

    print(list(data))
    # []


List Comprehension
==================
.. code-block:: python
    :caption: ``list`` comprehension approach to applying function to elements

    [x+10 for x in range(0,5)]
    # [10, 11, 12, 13, 14]

    list(x+10 for x in range(0,5))
    # [10, 11, 12, 13, 14]


Set Comprehension
=================
.. code-block:: python
    :caption: ``set`` comprehension approach to applying function to elements

    {x+10 for x in range(0, 5)}
    # {10, 11, 12, 13, 14}

    set(x+10 for x in range(0, 5))
    # {10, 11, 12, 13, 14}


Dict Comprehension
==================
.. code-block:: python
    :caption: ``dict`` comprehension approach to applying function to elements

    {x:x+10 for x in range(0,5)}
    # {0:10, 1:11, 2:12, 3:13, 4:14}

    dict((x,x+10) for x in range(0,5))
    # {0:10, 1:11, 2:12, 3:13, 4:14}

.. code-block:: python
    :caption: ``dict`` comprehension approach to applying function to elements

    {x+10:x for x in range(0,5)}
    # {10:0, 11:1, 12:2, 13:3, 14:4}

    dict((x+10,x) for x in range(0,5))
    # {10:0, 11:1, 12:2, 13:3, 14:4}

.. code-block:: python
    :caption: ``dict`` Comprehension approach to applying function to elements

    {x+10:x+10 for x in range(0,5)}
    # {10:10, 11:11, 12:12, 13:13, 14:14}

    dict((x+10:x+10) for x in range(0,5))
    # {10:10, 11:11, 12:12, 13:13, 14:14}


Tuple Comprehension?!
=====================
.. highlights::
    * Tuple Comprehension vs. Generator Expression
    * More information in :ref:`Generators`

.. code-block:: python
    :caption: Tuple Comprehension

    tuple(x+10 for x in range(0,5))
    # (10, 11, 12, 13, 14)

.. code-block:: python
    :caption: Generator Expression

    (x+10 for x in range(0,5))
    # <generator object <genexpr> at 0x11eaef570>


Conditional Comprehension
=========================
.. code-block:: python
    :caption: Iterative approach to applying function to selected elements

    result = []

    for x in range(0,5):
        if x % 2 == 0:
            result.append(x)

    print(result)
    # [0, 2, 4]

.. code-block:: python
    :caption: ``list`` Comprehensions approach to applying function to selected elements

    [x for x in range(0,5) if x%2==0]
    # [0, 2, 4]

.. code-block:: python
    :caption: Using ``list`` comprehension for filtering

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    ]

    [features for *features,label in DATA if label == 'setosa']
    # [[5.1, 3.5, 1.4, 0.2],
    #  [4.7, 3.2, 1.3, 0.2]]

    [X for *X,y in DATA if y=='setosa']
    # [[5.1, 3.5, 1.4, 0.2],
    #  [4.7, 3.2, 1.3, 0.2]]


Apply Function
==============
.. code-block:: python
    :caption: Applying function to each output element

    [float(x) for x in range(0,5)]
    # [0.0, 1.0, 2.0, 3.0, 4.0]

    [float(x) for x in range(0,5) if x%2==0]
    # [0.0, 2.0, 4.0]

.. code-block:: python
    :caption: Applying function to each output element

    [pow(2,x) for x in range(0,5)]
    # [1, 2, 4, 8, 16]

    [pow(2,x) for x in range(0,5) if x%2==0]
    # [1, 4, 16]

.. code-block:: python
    :caption: Using ``list`` comprehension for filtering

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    ]

    [tuple(features) for *features,label in DATA if label == 'setosa']
    # [(5.1, 3.5, 1.4, 0.2),
    #  (4.7, 3.2, 1.3, 0.2)]

    [tuple(X) for *X,y in DATA if y=='setosa']
    # [(5.1, 3.5, 1.4, 0.2),
    #  (4.7, 3.2, 1.3, 0.2)]


Indent
======
.. code-block:: python

    result = [pow(x,2) for x in range(0,5)]

.. code-block:: python

    result = [pow(x,2)
              for x in range(0,5)]

.. code-block:: python

    result = [pow(x,2) for x in range(0,5) if x%2==0]

.. code-block:: python

    result = [pow(x,2)
              for x in range(0,5)
                  if x % 2 == 0]

.. code-block:: python

    result = [pow(x,2)
              for x in range(0,5)
              if x % 2 == 0]


Nested
======
.. code-block:: python

    DATA = {
        6: ['Doctorate', 'Prof-school'],
        5: ['Masters', 'Bachelor', 'Engineer'],
        4: ['HS-grad'],
        3: ['Junior High'],
        2: ['Primary School'],
        1: ['Kindergarten'],
    }

    result = {title: str(i)
              for i, titles in DATA.items()
                 for title in titles}

    print(result)
    # {
    #   'Doctorate': '6',
    #   'Prof-school': '6',
    #   'Masters': '5',
    #   'Bachelor': '5',
    #   'Engineer': '5',
    #   'HS-grad': '4',
    #   'Junior High': '3',
    #   'Primary School': '2',
    #   'Kindergarten': '1'
    # }


Examples
========
.. code-block:: python
    :caption: Increment and decrement

    [x+1 for x in range(0,5)]
    # [1, 2, 3, 4, 5]

    [x-1 for x in range(0,5)]
    # [-1, 0, 1, 2, 3]

.. code-block:: python
    :caption: Sum

    sum(x for x in range(0,5))
    # 10

    sum(x for x in range(0,5) if x%2==0)
    # 6

.. code-block:: python
    :caption: Power

    [pow(2,x) for x in range(0,5)]
    # [1, 2, 4, 8, 16]

    [2**x for x in range(0,5)]
    # [1, 2, 4, 8, 16]

.. code-block:: python
    :caption: Even or Odd

    [x for x in range(0,5)]
    # [0, 1, 2, 3, 4]

    [x%2==0 for x in range(0,5)]
    # [True, False, True, False, True]

.. code-block:: python
    :caption: Even or Odd

    result = {}

    for x in range(0,5):
        is_even = (x % 2 == 0)
        result.update({x: is_even})

    print(result)
    # {0: True, 1: False, 2: True, 3: False, 4: True}


    {x: (x%2==0) for x in range(0,5)}
    # {0: True, 1: False, 2: True, 3: False, 4: True}

.. code-block:: python
    :caption: Filtering

    DATA = [
        {'is_astronaut': True,  'name': 'Jan Twardowski'},
        {'is_astronaut': True,  'name': 'Mark Watney'},
        {'is_astronaut': False, 'name': 'José Jiménez'},
        {'is_astronaut': True,  'name': 'Melissa Lewis'},
        {'is_astronaut': False, 'name': 'Alex Vogel'},
    ]

    astronauts = [person
                  for person in DATA
                  if person['is_astronaut']]

    print(astronauts)
    # [{'is_astronaut': True, 'name': 'Jan Twardowski'},
    #  {'is_astronaut': True, 'name': 'Mark Watney'},
    #  {'is_astronaut': True, 'name': 'Melissa Lewis'}]


    astronauts = [person['name']
                  for person in DATA
                  if person['is_astronaut']]

    print(astronauts)
    # ['Jan Twardowski', 'Mark Watney', 'Melissa Lewis']


    astronauts = [{'firstname': person['name'].split()[0],
                   'lastname': person['name'].split()[1]}
                   for person in DATA
                   if person['is_astronaut']]

    print(astronauts)
    # [{'firstname': 'Jan', 'lastname': 'Twardowski'},
    #  {'firstname': 'Mark', 'lastname': 'Watney'},
    #  {'firstname': 'Melissa', 'lastname': 'Lewis'}]

.. code-block:: python
    :caption: Using ``list`` comprehension for filtering with more complex expression

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    ]


    def is_setosa(species):
        if species == 'setosa':
            return True
        else:
            return False


    [tuple(X) for *X,y in DATA if is_setosa(y)]
    # [(5.1, 3.5, 1.4, 0.2),
    #  (4.7, 3.2, 1.3, 0.2)]

.. code-block:: python
    :caption: Quick parsing lines

    DATA = [
        '5.8,2.7,5.1,1.9,virginica',
        '5.1,3.5,1.4,0.2,setosa',
        '5.7,2.8,4.1,1.3,versicolor',
    ]

    result = []

    for row in DATA:
        row = row.split(',')
        result.append(row)

    print(result)
    # [['5.8', '2.7', '5.1', '1.9', 'virginica'],
    #  ['5.1', '3.5', '1.4', '0.2', 'setosa'],
    #  ['5.7', '2.8', '4.1', '1.3', 'versicolor']]


    [row.split(',') for row in DATA]
    # [['5.8', '2.7', '5.1', '1.9', 'virginica'],
    #  ['5.1', '3.5', '1.4', '0.2', 'setosa'],
    #  ['5.7', '2.8', '4.1', '1.3', 'versicolor']]

.. code-block:: python
    :caption: Reversing ``dict`` keys with values

    DATA = {'a': 1, 'b': 2}

    list(DATA.items())
    # [
    #    ('a', 1),
    #    ('b', 2),
    # ]

    [(k,v) for k,v in DATA.items()]
    # [
    #    ('a', 1),
    #    ('b', 2),
    # ]

    [(v,k) for k,v in DATA.items()]
    # [
    #    (1, 'a'),
    #    (2, 'b'),
    # ]

    {v:k for k,v in DATA.items()}
    # {1:'a', 2:'b'}

.. code-block:: python
    :caption: Value collision while reversing ``dict``

    DATA = {'a': 1, 'b': 2, 'c': 2}

    {v:k for k,v in DATA.items()}
    # {1:'a', 2:'c'}


All and Any
===========
.. code-block:: python

    all(x for x in range(0,5))         # False
    any(x for x in range(0,5))         # True

.. code-block:: python

    DATA = [
        {'is_astronaut': True,  'name': 'Jan Twardowski'},
        {'is_astronaut': True,  'name': 'Mark Watney'},
        {'is_astronaut': False, 'name': 'José Jiménez'},
        {'is_astronaut': True,  'name': 'Melissa Lewis'},
        {'is_astronaut': False, 'name': 'Alex Vogel'},
    ]

    if all(person['is_astronaut'] for person in DATA):
        print('Everyone is astronaut')
    else:
        print('Not everyone is astronaut')

.. code-block:: python

    DATA = [
        {'is_astronaut': True,  'name': 'Jan Twardowski'},
        {'is_astronaut': True,  'name': 'Mark Watney'},
        {'is_astronaut': False, 'name': 'José Jiménez'},
        {'is_astronaut': True,  'name': 'Melissa Lewis'},
        {'is_astronaut': False, 'name': 'Alex Vogel'},
    ]

    if any(person['is_astronaut'] for person in DATA):
        print('At least one person is astronaut')
    else:
        print('There are no astronauts')

.. code-block:: python

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    ]

    all(observation > 1.0
        for *features, label in DATA[1:]
        for observation in features
        if isinstance(observation, float))
    # False


    all(x > 1.0
        for *X,y in DATA[1:]
        for x in X
        if isinstance(x, float))
    # False


Assignment Expressions
======================
.. versionadded:: Python 3.8
    :pep:`572` Assignment Expressions (walrus operator)

.. code-block:: python

    DATA = [
        {'is_astronaut': True,  'name': 'JaN TwarDOwski'},
        {'is_astronaut': True,  'name': 'Mark Jim WaTNey'},
        {'is_astronaut': False, 'name': 'José Maria Jiménez'},
        {'is_astronaut': True,  'name': 'Melissa Lewis'},
        {'is_astronaut': False, 'name': 'Alex Vogel'},
    ]

    astronauts = [{'firstname': name[0], 'lastname': name[-1]}
                  for person in DATA
                  if person['is_astronaut']
                  and (name := person['name'].title().split())]

    print(astronauts)
    # [{'firstname': 'Jan', 'lastname': 'Twardowski'},
    #  {'firstname': 'Mark', 'lastname': 'Watney'},
    #  {'firstname': 'Melissa', 'lastname': 'Lewis'}]

.. code-block:: python

    DATA = [
        {'is_astronaut': True,  'name': 'JaN TwarDOwski'},
        {'is_astronaut': True,  'name': 'Mark Jim WaTNey'},
        {'is_astronaut': False, 'name': 'José Maria Jiménez'},
        {'is_astronaut': True,  'name': 'Melissa Lewis'},
        {'is_astronaut': False, 'name': 'Alex Vogel'},
    ]

    astronauts = [{'firstname': fname, 'lastname': lname}
                  for person in DATA
                  if person['is_astronaut']
                  and (name := person['name'].title().split())
                  and (fname := name[0])
                  and (lname := name[-1])]

    print(astronauts)
    # [{'firstname': 'Jan', 'lastname': 'Twardowski'},
    #  {'firstname': 'Mark', 'lastname': 'Watney'},
    #  {'firstname': 'Melissa', 'lastname': 'Lewis'}]

.. code-block:: python

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    ]

    result = [cls(*features)
              for *features, species in DATA[1:]
              if (clsname := species.capitalize())
              and (cls := globals()[clsname])]


Assignments
===========

Loop Comprehension Create
-------------------------
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/loop_comprehension_create.py`

:English:
    #. Use list comprehension
    #. Generate ``result: list[int]`` of even numbers from 5 to 20
    #. Print ``result``

:Polish:
    #. Użyj rozwinięcia listowego
    #. Wygeneruj ``result: list[int]`` parzystych liczb z przedziału 5 do 20
    #. Wypisz ``result``

Loop Comprehension Translate
----------------------------
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/loop_comprehension_translate.py`

:English:
    #. Use data from "Input" section (see below)
    #. Define ``result: list``
    #. Use list comprehension to iterate over ``DATA``
    #. If letter is in ``PL`` then use conversion value as letter
    #. Add letter to ``result``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj ``result: list``
    #. Użyj rozwinięcia listowego do iteracji po ``DATA``
    #. Jeżeli litera jest w ``PL`` to użyj przekonwertowanej wartości jako litera
    #. Dodaj literę do ``result``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
              'ł': 'l', 'ń': 'n', 'ó': 'o',
              'ś': 's', 'ż': 'z', 'ź': 'z'}

        DATA = 'zażółć gęślą jaźń'

:Output:
    .. code-block:: python

        result: str
        # 'zazolc gesla jazn'

Loop Comprehension Months
-------------------------
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/loop_comprehension_months.py`

:English:
    #. Use data from "Input" section (see below)
    #. Use dict comprehension
    #. Convert ``MONTH`` into dict:

        * Keys: month number
        * Values: month name

    #. Month number must be two letter string (zero padded)
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Użyj rozwinięcia słownikowego
    #. Przekonwertuj ``MONTH`` w słownik:

        * klucz: numer miesiąca
        * wartość: nazwa miesiąca

    #. Numer miesiąca ma być dwyznakowym stringiem (wypełnij zerem)
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        MONTHS = ['January', 'February', 'March', 'April',
                  'May', 'June', 'July', 'August', 'September',
                  'October', 'November', 'December']

:Output:
    .. code-block:: python

        result: dict
        # {'01': 'January',
        #  '02': 'February',
        #  '03': 'March',
        #  '04': 'April',
        #  '05': 'May',
        #  '06': 'June',
        #  '07': 'July',
        #  '08': 'August',
        #  '09': 'September',
        #  '10': 'October',
        #  '11': 'November',
        #  '12': 'December'}

Loop Comprehension Split
------------------------
* Complexity level: medium
* Lines of code to write: 8 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/loop_comprehension_split.py`

:English:
    #. Use data from "Input" section (see below)
    #. Separate header from data
    #. Calculate pivot point: length of data times given percent (60%/40%, see below)
    #. Using List Comprehension split data to:

        * ``features: list[tuple]`` - list of measurements (each measurement row is a tuple)
        * ``labels: list[str]`` - list of species names

    #. Split those data structures with proportion:

        * ``features_train: list[tuple]`` - features to train - 60%
        * ``features_test: list[tuple]`` - features to test - 40%
        * ``labels_train: list[str]`` - labels to train - 60%
        * ``labels_test: list[str]`` - labels to test - 40%

    #. Compare results with "Output" section below

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Odseparuj nagłówek od danych
    #. Wylicz punkt podziału: długość danych razy zadany procent (60%/40%, patrz poniżej)
    #. Używając List Comprehension podziel dane na:

        * ``features: list[tuple]`` - lista pomiarów (każdy wiersz z pomiarami ma być tuple)
        * ``labels: list[str]`` - lista nazw gatunków

    #. Podziel te struktury danych w proporcji:

        * ``features_train: list[tuple]`` - features do uczenia - 60%
        * ``features_test: list[tuple]`` - features do testów - 40%
        * ``labels_train: list[str]`` - labels do uczenia - 60%
        * ``labels_test: list[str]`` - labels do testów - 40%

    #. Porównaj wynik z sekcją "Output" poniżej

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
            (7.0, 3.2, 4.7, 1.4, 'versicolor'),
            (7.6, 3.0, 6.6, 2.1, 'virginica'),
            (4.9, 3.0, 1.4, 0.2, 'setosa'),
            (4.9, 2.5, 4.5, 1.7, 'virginica'),
            (7.1, 3.0, 5.9, 2.1, 'virginica'),
            (4.6, 3.4, 1.4, 0.3, 'setosa'),
            (5.4, 3.9, 1.7, 0.4, 'setosa'),
            (5.7, 2.8, 4.5, 1.3, 'versicolor'),
            (5.0, 3.6, 1.4, 0.3, 'setosa'),
            (5.5, 2.3, 4.0, 1.3, 'versicolor'),
            (6.5, 3.0, 5.8, 2.2, 'virginica'),
            (6.5, 2.8, 4.6, 1.5, 'versicolor'),
            (6.3, 3.3, 6.0, 2.5, 'virginica'),
            (6.9, 3.1, 4.9, 1.5, 'versicolor'),
            (4.6, 3.1, 1.5, 0.2, 'setosa'),
        ]

:Output:
    .. code-block:: python

        features_train: list[tuple[float, ...]]
        # [(5.8, 2.7, 5.1, 1.9), (5.1, 3.5, 1.4, 0.2), (5.7, 2.8, 4.1, 1.3),
        #  (6.3, 2.9, 5.6, 1.8), (6.4, 3.2, 4.5, 1.5), (4.7, 3.2, 1.3, 0.2),
        #  (7.0, 3.2, 4.7, 1.4), (7.6, 3.0, 6.6, 2.1), (4.9, 3.0, 1.4, 0.2),
        #  (4.9, 2.5, 4.5, 1.7), (7.1, 3.0, 5.9, 2.1), (4.6, 3.4, 1.4, 0.3)]

        features_test: list[tuple[float, ...]]
        # [(5.4, 3.9, 1.7, 0.4), (5.7, 2.8, 4.5, 1.3), (5.0, 3.6, 1.4, 0.3),
        #  (5.5, 2.3, 4.0, 1.3), (6.5, 3.0, 5.8, 2.2), (6.5, 2.8, 4.6, 1.5),
        #  (6.3, 3.3, 6.0, 2.5), (6.9, 3.1, 4.9, 1.5), (4.6, 3.1, 1.5, 0.2)]

        labels_train: list[str]
        # ['virginica', 'setosa', 'versicolor', 'virginica', 'versicolor',
        #  'setosa', 'versicolor', 'virginica', 'setosa', 'virginica',
        #  'virginica', 'setosa']

        labels_test: list[str]
        # ['setosa', 'versicolor', 'setosa', 'versicolor', 'virginica',
        #  'versicolor', 'virginica', 'versicolor', 'setosa']

:The whys and wherefores:
    * Iterating over nested data structures
    * Using slices
    * Type casting
    * List comprehension
    * Magic Number
