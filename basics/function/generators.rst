.. _Function Generators:

*******************
Function Generators
*******************


Range
=====
* It is not a generator
* optional ``start``, inclusive, default: ``0``
* required ``stop``, exclusive,
* optional ``step``, default: ``1``

.. code-block:: python
    :caption: ``range()`` syntax

    range([start], <stop>, [step])

.. code-block:: python

    range(0,3)
    # range(0, 3)

    list(range(0,3))
    # [0, 1, 2]

    tuple(range(0,3))
    # (0, 1, 2)

    set(range(0,3))
    # {0, 1, 2}

.. code-block:: python

    list(range(4,11,2))
    # [4, 6, 8, 10]


Enumerate
=========
* ``enumerate(*iterables)``

.. code-block:: python

    months = ['January', 'February', 'March']
    result = enumerate(months)

    next(result)
    # (0, 'January')

    next(result)
    # (1, 'February')

    next(result)
    # (2, 'March')

    next(result)
    # Traceback (most recent call last):
    # StopIteration

.. code-block:: python

    months = ['January', 'February', 'March']
    result = enumerate(months)

    list(result)
    # [(0, 'January'), (1, 'February'), (2, 'March')]

.. code-block:: python

    months = ['January', 'February', 'March']
    result = enumerate(months)

    dict(result)
    # {0: 'January', 1: 'February', 2: 'March'}

.. code-block:: python

    months = ['January', 'February', 'March']
    result = enumerate(months, start=1)

    dict(result)
    # {1: 'January', 2: 'February', 3: 'March'}

.. code-block:: python

    months = ['January', 'February', 'March']
    result = {f'{i:02}':month for i,month in enumerate(months, start=1)}

    print(result)
    # {'01': 'January', '02': 'February', '03': 'March'}

.. code-block:: python

    months = ['January', 'February', 'March']

    for i, month in enumerate(months, start=1):
        print(f'{i} -> {month}')

    # 1 -> January
    # 2 -> February
    # 3 -> March


Zip
===
* ``zip(*iterables)``

.. code-block:: python

    firstnames = ['Mark', 'Melissa', 'Alex']
    lastnames = ['Watney', 'Lewis', 'Vogel']
    result = zip(firstnames, lastnames)

    next(result)
    # ('Mark', 'Watney')

    next(result)
    # ('Melissa', 'Lewis')

    next(result)
    # ('Alex', 'Vogel')

    next(result)
    # Traceback (most recent call last):
    # StopIteration

.. code-block:: python

    firstnames = ['Mark', 'Melissa', 'Alex']
    lastnames = ['Watney', 'Lewis', 'Vogel']
    result = zip(firstnames, lastnames)

    list(result)
    # [('Mark', 'Watney'), ('Melissa', 'Lewis'), ('Alex', 'Vogel')]

.. code-block:: python

    firstnames = ['Mark', 'Melissa', 'Alex']
    lastnames = ['Watney', 'Lewis', 'Vogel']
    result = zip(firstnames, lastnames)

    dict(result)
    # {'Mark': 'Watney', 'Melissa': 'Lewis', 'Alex': 'Vogel'}

.. code-block:: python

    roles = ['botanist', 'commander', 'chemist']
    names = ['Mark Watney', 'Melissa Lewis', 'Alex Vogel']

    dict(zip(roles, names))
    # {'botanist': 'Mark Watney',
    #  'commander': 'Melissa Lewis',
    #  'chemist': 'Alex Vogel'}

.. code-block:: python
    :caption: ``zip()`` adjusts to the shortest

    firstnames = ['Mark', 'Melissa']
    lastnames = ['Watney', 'Lewis', 'Vogel']
    result = zip(firstnames, lastnames)

    list(result)
    # [('Mark', 'Watney'), ('Melissa', 'Lewis')]

.. code-block:: python

    roles = ['botanist', 'commander', 'chemist']
    firstnames = ['Mark', 'Melissa', 'Alex']
    lastnames = ['Watney', 'Lewis', 'Vogel']
    result = zip(roles, firstnames, lastnames)

    next(result)
    # ('botanist', 'Mark', 'Watney')

    next(result)
    # ('commander', 'Melissa', 'Lewis')

    next(result)
    # ('chemist', 'Alex', 'Vogel')

    next(result)
    # Traceback (most recent call last):
    # StopIteration

.. code-block:: python

    roles = ['botanist', 'commander', 'chemist']
    names = ['Mark Watney', 'Melissa Lewis', 'Alex Vogel']

    for role, name in zip(roles, names):
        print(f'{role} -> {name}')

    # botanist -> Mark Watney
    # commander -> Melissa Lewis
    # chemist -> Alex Vogel


Map
===
* ``map(callable, *iterables)``

.. code-block:: python

    data = [1, 2, 3]
    result = map(float, data)

    next(result)
    # 1.0

    next(result)
    # 2.0

    next(result)
    # 3.0

    next(result)
    # Traceback (most recent call last):
    # StopIteration

.. code-block:: python

    data = [1, 2, 3]
    result = map(float, data)

    list(result)
    # [1.0, 2.0, 3.0]

.. code-block:: python

    data = [1, 2, 3]
    result = map(float, data)

    tuple(map(float, data))
    # (1.0, 2.0, 3.0)

.. code-block:: python

    data = [1, 2, 3]
    result = map(float, data)

    set(map(float, data))
    # {1.0, 2.0, 3.0}

.. code-block:: python

    DATA = [1, 2, 3]

    result = (float(x) for x in DATA)
    list(result)
    # [1.0, 2.0, 3.0]

    result = map(round, DATA)
    list(result)
    # [1.0, 2.0, 3.0]

.. code-block:: python

    def square(x):
        return x ** 2

    data = [1, 2, 3]

    result = map(square, data)
    list(result)
    # [1, 4, 9]


Filter
======
* ``filter(callable, *iterables)``

.. code-block:: python

    def even(x):
        return x % 2 == 0


    data = [1, 2, 3, 4, 5, 6]
    result = filter(even, data)

    next(result)
    # 2

    next(result)
    # 4

    next(result)
    # 6

    next(result)
    # Traceback (most recent call last):
    # StopIteration

.. code-block:: python

    def even(x):
        return x % 2 == 0


    data = [1, 2, 3, 4, 5, 6]
    result = filter(even, data)

    list(result)
    # [2, 4, 6]

.. code-block:: python

    PEOPLE = [{'age': 21, 'name': 'Jan Twardowski'},
              {'age': 25, 'name': 'Mark Watney'},
              {'age': 18, 'name': 'Melissa Lewis'}]


    def adult(person):
        return person['age'] >= 21:


    result = filter(adult, PEOPLE)

    list(result)
    # [{'age': 21, 'name': 'Jan Twardowski'},
    #  {'age': 25, 'name': 'Mark Watney'}]


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

.. literalinclude:: assignments/function_generators_chain.py
    :caption: :download:`Solution <assignments/function_generators_chain.py>`
    :end-before: # Solution
