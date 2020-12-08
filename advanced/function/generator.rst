.. _Generators:

**********
Generators
**********


Recap
=====
* Comprehensions executes instantly
* Generators are lazy evaluated

.. code-block:: python

    list(x for x in range(0,5))        # [0, 1, 2, 3, 4]
    [x for x in range(0,5)]            # [0, 1, 2, 3, 4]

    set(x for x in range(0,5))         # {0, 1, 2, 3, 4}
    {x for x in range(0,5)}            # {0, 1, 2, 3, 4}

    dict((x,x) for x in range(0,5))    # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
    {x:x for x in range(0,5)}          # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}

    tuple(x for x in range(0,5))       # (0, 1, 2, 3, 4)
    (x for x in range(0,5))            # <generator object <genexpr> at 0x118c1aed0>

    all(x for x in range(0,5))         # False
    any(x for x in range(0,5))         # True
    sum(x for x in range(0,5))         # 10


Rationale
=========
* Create generator object and assign pointer (do not execute)
* Comprehensions will be in the memory until end of a program
* Generators are cleared once they are executed
* Comprehensions - Using values more than one
* Generators - Using values once (for example in the loop iterator)

.. code-block:: python

    data = [x for x in range(0, 5)]

    list(data)
    # [0, 1, 2, 3, 4]

    list(data)
    # [0, 1, 2, 3, 4]

    print(data)
    # [0, 1, 2, 3, 4]

.. code-block:: python

    data = (x for x in range(0, 5))

    list(data)
    # [0, 1, 2, 3, 4]

    list(data)
    # []

    print(data)
    # <generator object <genexpr> at 0x11cb45950>


Instant Evaluation
==================
.. highlights::
    * If you need values evaluated instantly, there is no point in using generators

.. code-block:: python

    data = (x for x in range(0,5))

    list(data)
    # [0, 1, 2, 3, 4]


Lazy Evaluation
===============
.. highlights::
    * Code do not execute instantly
    * Sometimes code is not executed at all!

.. code-block:: python

    data = (x for x in range(0,3))

    next(data)
    # 0

    next(data)
    # 1

    next(data)
    # 2

    next(data)
    # Traceback (most recent call last):
    # StopIteration

.. code-block:: python
    :caption: None of those lines will generate any numbers (util executed)!

    a = (x for x in range(0,5))
    b = (x for x in range(0,5))
    c = (x for x in range(0,5))


Iterative Evaluation
====================
.. highlights::
    * Generator will calculate next number for every loop iteration
    * Generator forgets previous number
    * Generator doesn't know the next number

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


Generator Function
==================
.. code-block:: python

    DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa')]


    def get_values(species):
        result = []
        for row in DATA:
            if row[4] == species:
                result.append(row)
        return result


    data = get_values('setosa')

    print(data)
    # [(5.1, 3.5, 1.4, 0.2, 'setosa'), (4.7, 3.2, 1.3, 0.2, 'setosa')]

    for row in data:
        print(row)
    # (5.1, 3.5, 1.4, 0.2, 'setosa')
    # (4.7, 3.2, 1.3, 0.2, 'setosa')

.. code-block:: python

    DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa')]


    def get_values(species):
        for row in DATA:
            if row[4] == species:
                yield row


    data = get_values('setosa')

    print(data)
    # <generator object get_values at 0x103632820>

    for row in data:
        print(row)
    # (5.1, 3.5, 1.4, 0.2, 'setosa')
    # (4.7, 3.2, 1.3, 0.2, 'setosa')


Built-in generators
===================

Enumerate
---------
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
---
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
---
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
------
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
---------
* https://docs.python.org/3/library/functools.html

.. code-block:: python

    from functools import *

    reduce(callable, iterable[, initializer])

Itertools
---------
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


Memory Footprint
================
* ``sys.getsizeof(obj)`` returns the size of an ``obj`` in bytes
* ``sys.getsizeof(obj)`` calls ``obj.__sizeof__()`` method
* ``sys.getsizeof(obj)`` adds an additional garbage collector overhead if the ``obj`` is managed by the garbage collector

.. code-block:: python

    from sys import getsizeof


    gen1 = (x for x in range(0,10))
    gen10 = (x for x in range(0,10))
    gen100 = (x for x in range(0,100))
    gen1000 = (x for x in range(0,1000))

    com1 = [x for x in range(0,1)]
    com10 = [x for x in range(0,10)]
    com100 = [x for x in range(0,100)]
    com1000 = [x for x in range(0,1000)]

    getsizeof(gen1)
    # 112

    getsizeof(gen10)
    # 112

    getsizeof(gen100)
    # 112

    getsizeof(gen1000)
    # 112

    getsizeof(com1)
    # 88

    getsizeof(com10)
    # 184

    getsizeof(com100)
    # 920

    getsizeof(com1000)
    # 8856


Inspection
==========
.. code-block:: python

    from inspect import isgenerator

    a = [x for x in range(0,5)]
    b = (x for x in range(0,5))

    isgenerator(a)
    # False

    isgenerator(b)
    # True

.. code-block:: python

    from inspect import isgenerator

    data = range(0, 10)

    isgenerator(data)
    # False


Introspection
=============
.. code-block:: python

    data = (x for x in range(0,10))

    next(data)
    # 0

    data.gi_code
    # <code object <genexpr> at 0x11fc4dc90, file "<input>", line 1>

    data.gi_running
    # False

    data.gi_yieldfrom

    data.gi_frame
    # <frame at 0x7f93a1723200, file '<input>', line 1, code <genexpr>>

    data.gi_frame.f_locals
    # {'.0': <range_iterator object at 0x11fc4c840>, 'x': 0}

    data.gi_frame.f_code
    # <code object <genexpr> at 0x11fc4dc90, file "<input>", line 1>

    data.gi_frame.f_lineno
    # 1

    data.gi_frame.f_lasti
    # 8


Assignments
===========

.. literalinclude:: assignments/function_generators_chain.py
    :caption: :download:`Solution <assignments/function_generators_chain.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_generator_iris.py
    :caption: :download:`Solution <assignments/function_generator_iris.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_generator_passwd.py
    :caption: :download:`Solution <assignments/function_generator_passwd.py>`
    :end-before: # Solution
