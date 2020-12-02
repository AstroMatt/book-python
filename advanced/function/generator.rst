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

``enumerate()``
---------------
* ``enumerate(iterable)``

.. code-block:: python

    data = ['a', 'b', 'c']
    result = enumerate(data)

    next(result)
    # (0, 'a')

    next(result)
    # (1, 'b')

    next(result)
    # (2, 'c')

    next(result)
    # Traceback (most recent call last):
    # StopIteration

.. code-block:: python

    data = ['a', 'b', 'c']
    result = enumerate(data)

    list(result)
    # [(0, 'a'), (1, 'b'), (2, 'c')]

.. code-block:: python

    data = ['a', 'b', 'c']
    result = enumerate(data)

    dict(result)
    # {0: 'a', 1: 'b', 2: 'c'}

.. code-block:: python

    crew = ['Mark Watney', 'Melissa Lewis', 'Alex Vogel']

    for i, astro in enumerate(crew):
        print(i, astro, sep=' -> ')

    # 0 -> Mark Watney
    # 1 -> Melissa Lewis
    # 2 -> Alex Vogel

.. code-block:: python

    crew = ['Mark Watney', 'Melissa Lewis', 'Alex Vogel']

    dict(enumerate(crew))
    # {0: 'Mark Watney', 1: 'Melissa Lewis', 2: 'Alex Vogel'}

``zip()``
---------
* ``zip(*iterable)``

.. code-block:: python

    header = ['a', 'b', 'c']
    data = [1, 2, 3]
    result = zip(header, data)

    next(result)
    # ('a', 1)

    next(result)
    # ('b', 2)

    next(result)
    # ('c', 3)

    next(result)
    # Traceback (most recent call last):
    # StopIteration

.. code-block:: python

    header = ['a', 'b', 'c']
    data = [1, 2, 3]
    row = [True, False, None]
    result = zip(header, data, row)

    next(result)
    # ('a', 1, True)

    next(result)
    # ('b', 2, False)

    next(result)
    # ('c', 3, None)

    next(result)
    # Traceback (most recent call last):
    # StopIteration

.. code-block:: python

    header = ['a', 'b', 'c']
    data = [1, 2, 3]
    result = zip(header, data)

    list(result)
    # [('a', 1), ('b', 2), ('c', 3)]

.. code-block:: python

    header = ['a', 'b', 'c']
    data = [1, 2, 3]
    result = zip(header, data)

    dict(result)
    # {'a': 1, 'b': 2, 'c': 3}

.. code-block:: python

    roles = ['botanist', 'commander', 'chemist']
    crew = ['Mark Watney', 'Melissa Lewis', 'Alex Vogel']

    for role, astro in zip(roles, crew):
        print(role, astro, sep=' -> ')

    # botanist -> Mark Watney
    # commander -> Melissa Lewis
    # chemist -> Alex Vogel

.. code-block:: python

    roles = ['botanist', 'commander', 'chemist']
    crew = ['Mark Watney', 'Melissa Lewis', 'Alex Vogel']

    dict(zip(roles, crew))
    # {'botanist': 'Mark Watney',
    #  'commander': 'Melissa Lewis',
    #  'chemist': 'Alex Vogel'}

``map()``
---------
* ``map(callable, *iterable)``

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

``filter()``
------------
* ``filter(callable, *iterable)``

.. code-block:: python

    def even(x):
        return x % 2 == 0


    numbers = [1, 2, 3, 4, 5, 6]
    result = filter(even, numbers)

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


    numbers = [1, 2, 3, 4, 5, 6]
    result = filter(even, numbers)

    list(result)
    # [2, 4, 6]

.. code-block:: python

    numbers = [1, 2, 3, 4, 5, 6]
    result = filter(lambda x: x % 2 == 0, numbers)

    list(result)
    # [2, 4, 6]

.. code-block:: python
    :caption: ``filter()`` example

    PEOPLE = [{'age': 21, 'name': 'Jan Twardowski'},
              {'age': 25, 'name': 'Mark Watney'},
              {'age': 18, 'name': 'Melissa Lewis'}]


    def adult(person):
        return person['age'] >= 21:


    result = filter(adult, PEOPLE)

    list(result)
    # [{'age': 21, 'name': 'Jan Twardowski'},
    #  {'age': 25, 'name': 'Mark Watney'}]



Loops Under the Hood
====================
.. code-block:: python

    data = (x for x in range(0,3))

    for a in data:
        print(a)

    # is analogous to:
    try:
        i = iter(data)

        a = next(i)
        print(a)

        a = next(i)
        print(a)

        a = next(i)
        print(a)

        a = next(i)
        print(a)

        a = next(i)
        print(a)
    except StopIteration:
        pass


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


Memory Footprint
================
* ``sys.getsizeof(object)`` returns the size of an object in bytes
* ``sys.getsizeof(object)`` calls the object's ``__sizeof__`` method
* ``sys.getsizeof(object)`` adds an additional garbage collector overhead if the object is managed by the garbage collector

.. code-block:: python

    from sys import getsizeof


    a1 = (x for x in range(0,10))
    a2 = (x for x in range(0,10))
    b = (x for x in range(0,100))
    c = (x for x in range(0,1000))

    getsizeof(a1)
    # 112

    getsizeof(a2)
    # 112

    getsizeof(b)
    # 112

    getsizeof(c)
    # 112

.. code-block:: python

    from sys import getsizeof


    a1 = [x for x in range(0,10)]
    a2 = [x for x in range(0,10)]
    b = [x for x in range(0,100)]
    c = [x for x in range(0,1000)]

    getsizeof(a1)
    # 184

    getsizeof(a2)
    # 184

    getsizeof(b)
    # 920

    getsizeof(c)
    # 8856


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
