.. _Function Generators:

*******************
Function Generators
*******************


Range
=====
.. highlights::
    * optional ``start``, inclusive, default: ``0``
    * required ``stop``, exclusive,
    * optional ``step``, default: ``1``

.. code-block:: python
    :caption: ``range()`` syntax

    range([start], <stop>, [step])

.. code-block:: python
    :caption: ``range()`` definition

    range(0,3)
    # range(0, 3)

    list(range(0,3))
    # [0, 1, 2]

    tuple(range(0,3))
    # (0, 1, 2)

    set(range(0,3))
    # {0, 1, 2}

    frozenset(range(0,3))
    # frozenset({0, 1, 2})

.. code-block:: python

    list(range(4, 11, 2))
    # [4, 6, 8, 10]

.. code-block:: python

    header = ['a', 'b', 'c']
    data = [1, 2, 3]
    result = {}

    for i in range(len(header)):
        key = header[i]
        value = data[i]
        result[key] = value

    print(result)
    # {'a': 1, 'b': 2, 'c': 3}


Zip
===
.. code-block:: python
    :caption: ``zip()`` syntax

    zip(<sequence>, <sequence>, ...)

.. code-block:: python
    :caption: ``zip()`` definition

    header = ['a', 'b', 'c']
    data = [1, 2, 3]

    zip(header, data)
    # <zip object at 0x11cf54b90>

    list(zip(header, data))
    # [('a', 1), ('b', 2), ('c', 3)]

    tuple(zip(header, data))
    # (('a', 1), ('b', 2), ('c', 3))

    set(zip(header, data))
    # {('b', 2), ('a', 1), ('c', 3)}

    frozenset(zip(header, data))
    # frozenset({('b', 2), ('a', 1), ('c', 3)})

    dict(zip(header, data))
    # {'a': 1, 'b': 2, 'c': 3}

.. code-block:: python
    :caption: ``zip()`` adjust to shortest sequence

    header = ['a', 'b', 'c']
    data = [1, 2, 3, 4, 5, 6]

    result = zip(header, data)

    print(list(result))
    # [('a', 1), ('b', 2), ('c', 3)]

.. code-block:: python
    :caption: ``zip()`` examples

    header = ['a', 'b', 'c']
    data = [1, 2, 3]
    row = [77, 88, 99]

    result = [(h,d,r) for h,d,r in zip(header, data, row)]

    print(result)
    # [('a', 1, 77), ('b', 2, 88), ('c', 3, 99)]


Enumerate
=========
.. code-block:: python
    :caption: ``enumerate()`` syntax

    enumerate(<sequence>)

.. code-block:: python
    :caption: ``enumerate()`` definition

    header = ['a', 'b', 'c']

    list(enumerate(header))
    # [(0, 'a'), (1, 'b'), (2, 'c')]

    dict(enumerate(header))
    # {0: 'a', 1: 'b', 2: 'c'}

    dict((v,k) for k,v in enumerate(data))
    # {'a': 0, 'b': 1, 'c': 2}

    {v:k for k,v in enumerate(data, start=5)}
    # {'a': 5, 'b': 6, 'c': 7}

.. code-block:: python
    :caption: ``enumerate()`` example

    header = ['a', 'b', 'c']
    data = [1, 2, 3]
    result = {}

    for i, _ in enumerate(header):
        key = header[i]
        value = data[i]
        result[key] = value

    print(result)
    # {'a': 1, 'b': 2, 'c': 3}

.. code-block:: python

    header = ['a', 'b', 'c']
    data = [1, 2, 3]
    result = {}

    for i, header in enumerate(header):
        result[header] = data[i]

    print(result)
    # {'a': 1, 'b': 2, 'c': 3}


Map
===
.. code-block:: python
    :caption: ``map()`` syntax

    map(<callable>, <sequence>)

.. code-block:: python
    :caption: ``map()`` definition

    data = [1, 2, 3]

    map(float, data)
    # <map object at 0x11d15a190>

    list(map(float, data))
    # [1.0, 2.0, 3.0]

    tuple(map(float, data))
    # (1.0, 2.0, 3.0)

    set(map(float, data))
    # {1.0, 2.0, 3.0}

    frozenset(map(float, data))
    # frozenset({1.0, 2.0, 3.0})

.. code-block:: python

    DATA = [1.1111, 2.22222, 3.3333]

    result = [round(x) for x in DATA]
    # [1, 2, 3]

    result = map(round, DATA)
    list(result)
    # [1, 2, 3]


.. code-block:: python
    :caption: ``map()`` examples

    def square(x):
        return x ** 2

    data = [1, 2, 3]

    result = map(square, data)
    list(result)
    # [1, 4, 9]


Filter
======
.. code-block:: python
    :caption: ``filter()`` syntax

    filter(<callable>, <sequence>)

.. code-block:: python

    data = [True, False, True]

    filter(bool, data)
    # <filter object at 0x11d182990>

    result = filter(bool, data)
    list(result)
    # [True, True]

.. code-block:: python
    :caption: ``filter()`` example

    def is_even(x):
        if x % 2 == 0:
            return True
        else:
            return False

    data = [1, 2, 3, 4, 5, 6]

    result = filter(is_even, data)
    list(result)
    # [2, 4, 6]

.. code-block:: python

    def is_even(x):
        return x % 2 == 0

    data = [1, 2, 3, 4, 5, 6]

    result = filter(is_even, data)
    list(result)
    # [2, 4, 6]


Functools
=========
* https://docs.python.org/3/library/functools.html

.. code-block:: python

    from functools import *

    reduce(callable, iterable[, initializer])


Itertools
=========
* https://docs.python.org/3/library/itertools.html
* :ref:`Itertools`

.. code-block:: python

    from itertools import *

    count(start=0, step=1)
    cycle(iterable)
    repeat(object[, times])
    accumulate(iterable[, func, *, initial=None])
    chain(*iterables)
    compress(data, selectors)
    islice(iterable, start, stop[, step])
    starmap(function, iterable)
    product(*iterables, repeat=1)
    permutations(iterable, r=None)
    combinations(iterable, r)
    combinations_with_replacement(iterable, r)
    groupby(iterable, key=None)


Examples
========
.. code-block:: python

    data = [1, 2, 3, 4]

    def increment(x):
        return x + 1

    result = map(increment, data)
    list(result)
    # [2, 3, 4, 5]

.. code-block:: python

    PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
          'ł': 'l', 'ń': 'n', 'ó': 'o',
          'ś': 's', 'ż': 'z', 'ź': 'z'}

    text = 'zażółć gęślą jaźń'

    def translate(letter):
        return PL.get(letter, letter)

    result = map(translate, text)
    ''.join(result)
    # 'zazolc gesla jazn'

.. code-block:: python
    :caption: ``filter()`` example

    def adult(person):
        return person['age'] >= 21:

    people = [
        {'age': 21, 'name': 'Jan Twardowski'},
        {'age': 25, 'name': 'Mark Watney'},
        {'age': 18, 'name': 'Melissa Lewis'}]

    result = filter(adult, people)
    list(result)
    # [{'age': 21, 'name': 'Jan Twardowski'},
    #  {'age': 25, 'name': 'Mark Watney'}]

.. code-block:: python
    :caption: ``filter()`` example

    def astronaut(person):
        return person['is_astronaut']

    people = [
        {'is_astronaut': False, 'name': 'Jan Twardowski'},
        {'is_astronaut': True, 'name': 'Mark Watney'},
        {'is_astronaut': True, 'name': 'Melissa Lewis'}]

    result = filter(astronaut, people)
    list(result)
    # [{'is_astronaut': True, 'name': 'Mark Watney'},
    #  {'is_astronaut': True, 'name': 'Melissa Lewis'}]

.. code-block:: python

    astronauts = ['Mark Watney', 'Melissa Lewis']

    people = ['Jan Twardowski', 'Mark Watney',
              'Melissa Lewis', 'Jimenez']

    def is_astronaut(person):
        return person in astronauts

    result = filter(is_astronaut, people)
    list(result)
    # ['Mark Watney', 'Melissa Lewis']

.. code-block:: python

    import sys
    print(sum(map(int, sys.stdin)))

.. code-block:: console

    $ cat ~/.profile |grep addnum
    alias addnum='python -c"import sys; print(sum(map(int, sys.stdin)))"'


Assignments
===========

Function Generator Chain
------------------------
* Assignment: Function Generator Chain
* Filename: function_generators_chain.py
* Complexity: easy
* Lines of code to write: 10 lines
* Estimated time: 13 min

English:
    #. Use generator expression to create ``numbers``
    #. In generator use ``range()`` to get numbers from 1 to 33 (inclusive) divisible by 3
    #. Use ``filter()`` to get odd numbers from ``numbers``
    #. Use ``map()`` to cube all numbers in ``numbers``
    #. Create ``result: float`` with arithmetic mean of ``numbers``
    #. Do not use ``lambda`` expressions
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj wyrażenia generatorowego do stworzenia ``numbers``
    #. W generatorze użyj ``range()`` aby otrzymać liczby od 1 do 33 (włącznie) podzielne przez 3
    #. Użyj ``filter()`` aby otrzymać liczby nieparzyste z ``numbers``
    #. Użyj ``map()`` aby podnieść wszystkie liczby w ``numbers`` do sześcianu
    #. Stwórz ``result: float`` ze średnią arytmetyczną z ``numbers``
    #. Nie używaj wyrażeń lambda
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * type cast to ``list()`` before calculating mean to expand generator
    * ``mean = sum(...) / len(...)``

Tests:
    >>> type(result) is float
    True
    >>> result
    11502.0

