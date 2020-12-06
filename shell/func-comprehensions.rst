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

    result = [x for x in range(0,5)]

    print(result)
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

    # List Comprehension
    list(x for x in range(0,5))        # [0, 1, 2, 3, 4]
    [x for x in range(0,5)]            # [0, 1, 2, 3, 4]

    # Set Comprehension
    set(x for x in range(0,5))         # {0, 1, 2, 3, 4}
    {x for x in range(0,5)}            # {0, 1, 2, 3, 4}

    # Dict Comprehension
    dict((x,x) for x in range(0,5))    # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
    {x:x for x in range(0,5)}          # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}

    # Tuple Comprehension
    tuple(x for x in range(0,5))       # (0, 1, 2, 3, 4)

    # Generator Expression
    (x for x in range(0,5))            # <generator object <genexpr> at 0x118c1aed0>


Comprehensions or Generator Expression
======================================
.. code-block:: python

    data = [x for x in range(0,10)]
    print(data)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    data = (x for x in range(0,10))
    print(data)
    # <generator object <genexpr> at 0x10ef1d040>

.. code-block:: python
    :caption: Comprehension

    data = [x for x in range(0,10)]

    for x in data:
        print(x, end=' ')
        if x == 3:
            break
    # 0 1 2 3

    for x in data:
        print(x, end=' ')
        if x == 6:
            break
    # 0 1 2 3 4 5 6

    print(list(data))
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(list(data))
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

.. code-block:: python
    :caption: Generator

    data = (x for x in range(0,10))

    for x in data:
        print(x, end=' ')
        if x == 3:
            break
    # 0 1 2 3

    for x in data:
        print(x, end=' ')
        if x == 6:
            break
    # 4 5 6

    print(list(data))
    # [7, 8, 9]

    print(list(data))
    # []


List Comprehension
==================
.. code-block:: python

    [x+1 for x in range(0,5)]
    # [1, 2, 3, 4, 5]

    [x-1 for x in range(0,5)]
    # [-1, 0, 1, 2, 3]

    [x**2 for x in range(0,5)]
    # [0, 1, 4, 9, 16]

    [2**x for x in range(0,5)]
    # [1, 2, 4, 8, 16]

.. code-block:: python

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


Filter
======
.. code-block:: python

    result = []

    for x in range(0,5):
        if x % 2 == 0:
            result.append(x)

    print(result)
    # [0, 2, 4]

.. code-block:: python

    [x for x in range(0,5) if x%2==0]
    # [0, 2, 4]

.. code-block:: python

    DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor')]

    [features for *features,label in DATA if label == 'setosa']
    # [[5.1, 3.5, 1.4, 0.2],
    #  [4.7, 3.2, 1.3, 0.2]]

    [X for *X,y in DATA if y=='setosa']
    # [[5.1, 3.5, 1.4, 0.2],
    #  [4.7, 3.2, 1.3, 0.2]]


Map
===
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

    DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor')]

    [tuple(features) for *features,label in DATA if label == 'setosa']
    # [(5.1, 3.5, 1.4, 0.2),
    #  (4.7, 3.2, 1.3, 0.2)]

    [tuple(X) for *X,y in DATA if y=='setosa']
    # [(5.1, 3.5, 1.4, 0.2),
    #  (4.7, 3.2, 1.3, 0.2)]


Indent and Whitespaces
======================
.. code-block:: python

    result = [pow(x,2) for x in range(0,5)]

.. code-block:: python

    result = [pow(x,2)
              for x in range(0,5)]

.. code-block:: python

    result = [pow(x, 2) for x in range(0, 5) if x % 2 == 0]

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

    [pow(x,2) for x in range(0,5)]
    # [0, 1, 4, 9, 16]

    [x**2 for x in range(0,5)]
    # [0, 1, 4, 9, 16]

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

    DATA = [{'is_astronaut': True,  'name': 'Jan Twardowski'},
            {'is_astronaut': True,  'name': 'Mark Watney'},
            {'is_astronaut': False, 'name': 'José Jiménez'},
            {'is_astronaut': True,  'name': 'Melissa Lewis'},
            {'is_astronaut': False, 'name': 'Alex Vogel'}]

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

    DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor')]


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

    DATA = ['5.8,2.7,5.1,1.9,virginica',
            '5.1,3.5,1.4,0.2,setosa',
            '5.7,2.8,4.1,1.3,versicolor']

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

    DATA = [{'is_astronaut': True,  'name': 'Jan Twardowski'},
            {'is_astronaut': True,  'name': 'Mark Watney'},
            {'is_astronaut': False, 'name': 'José Jiménez'},
            {'is_astronaut': True,  'name': 'Melissa Lewis'},
            {'is_astronaut': False, 'name': 'Alex Vogel'}]

    if all(person['is_astronaut'] for person in DATA):
        print('Everyone is astronaut')
    else:
        print('Not everyone is astronaut')

.. code-block:: python

    DATA = [{'is_astronaut': True,  'name': 'Jan Twardowski'},
            {'is_astronaut': True,  'name': 'Mark Watney'},
            {'is_astronaut': False, 'name': 'José Jiménez'},
            {'is_astronaut': True,  'name': 'Melissa Lewis'},
            {'is_astronaut': False, 'name': 'Alex Vogel'}]

    if any(person['is_astronaut'] for person in DATA):
        print('At least one person is astronaut')
    else:
        print('There are no astronauts')

.. code-block:: python

    DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor')]

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


Assignments
===========

.. literalinclude:: assignments/loop_comprehension_create.py
    :caption: :download:`Solution <assignments/loop_comprehension_create.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_comprehension_months.py
    :caption: :download:`Solution <assignments/loop_comprehension_months.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_comprehension_translate.py
    :caption: :download:`Solution <assignments/loop_comprehension_translate.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_comprehension_split.py
    :caption: :download:`Solution <assignments/loop_comprehension_split.py>`
    :end-before: # Solution
