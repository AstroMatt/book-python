**************
Good Practices
**************


Rationale
=========
.. figure:: img/goodpractices-programmer-exp.png
    :align: center
    :scale: 50%

    Code Complexity vs. Programmer Experience


Range
=====
.. doctest::

    >>> i = 0
    >>> while i < 5:
    ...    i += 1

.. doctest::

    >>> for i in range(5):
    ...    pass


ForEach
=======
.. doctest::

    >>> DATA = ['a', 'b', 'c']
    >>> for i in range(len(DATA)):
    ...    value = DATA[i]

.. doctest::

    >>> DATA = ['a', 'b', 'c']
    >>> for value in DATA:
    ...    pass


Sum
===
.. doctest::

    >>> DATA = [1, 2, 3]
    >>> total = 0
    >>> for i in range(len(DATA)):
    ...    total += DATA[i]

.. doctest::

    >>> DATA = [1, 2, 3]
    >>> sum(DATA)


Enumerate
=========
.. doctest::

    >>> DATA = ['a', 'b', 'c']
    >>> i = 0

    >>> while i < len(DATA):
    ...    value = DATA[i]
    ...    i += 1

.. doctest::

    >>> DATA = ['a', 'b', 'c']

    >>> for i, value in enumerate(DATA):
    ...    pass


Zip
===
.. doctest::

    >>> header = ['a', 'b', 'c']
    >>> values = [1, 2, 3]
    >>> result = {}

    >>> for i in range(len(header)):
    ...    key = header[i]
    ...    val = values[i]
    ...    result[key] = value

.. doctest::

    >>> header = ['a', 'b', 'c']
    >>> values = [1, 2, 3]

    >>> zip(header, values)


List Comprehension
==================
.. doctest::

    >>> DATA = ['a', 'b', 'c']
    >>> result = list()

    >>> for x in DATA:
    ...    result.append(x)

.. doctest::

    >>> DATA = ['a', 'b', 'c']
    >>> result = [x for x in DATA]


Set Comprehension
=================
.. doctest::

    >>> DATA = ['a', 'b', 'c']
    >>> result = set()

    >>> for x in DATA:
    ...    result.add(x)

.. doctest::

    >>> DATA = ['a', 'b', 'c']
    >>> result = {x for x in DATA}


Dict Comprehension
==================
.. doctest::

    >>> DATA = {'a': 1, 'b': 2, 'c': 3}
    >>> result = dict()

    >>> for key, value in DATA.items():
    ...    result[key] = value

.. doctest::

    >>> DATA = {'a': 1, 'b': 2, 'c': 3}
    >>> result = {k:v for k,v in DATA.items()}


Map
===
.. doctest::

    >>> def func(x):
    ...     return float()

    >>> DATA = [1, 2, 3]
    >>> result = (func(x) for x in DATA)

.. doctest::

    >>> def func(x):
    ...     return float()

    >>> DATA = [1, 2, 3]
    >>> result = map(func, DATA)


Filter
======
.. doctest::

    >>> def func(x):
    ...     return x % 2 == 0

    >>> DATA = [1, 2, 3]
    >>> result = (x for x in DATA if func(x))

.. doctest::

    >>> def func(x):
    ...     return x % 2 == 0

    >>> DATA = [1, 2, 3]
    >>> result = filter(func, DATA)


For Else
========
.. doctest::

    >>> DATA = [1, 2, 3]
    >>> FIND = 10
    >>> found = False

    >>> for value in DATA:
    ...     if value == FIND:
    ...         print('Found')
    ...         found = True
    ...         break

    >>> if not found:
    ...     print('Not Found')

.. doctest::

    >>> DATA = [1, 2, 3]
    >>> FIND = 10

    >>> for value in DATA:
    ...     if value == FIND:
    ...         print('Found')
    ...         break
    ... else:
    ...     print('Not Found')


While Else
==========
.. doctest::

    >>> DATA = [1, 2, 3]
    >>> FIND = 10
    >>> found = False

    >>> while i < len(DATA):
    ...     value = DATA[i]
    ...     i += 1
    ...     if value == FIND:
    ...         print('Found')
    ...         found = True
    ...         break

    >>> if not found:
    ...     print('Not Found')

.. doctest::

    >>> DATA = [1, 2, 3]
    >>> FIND = 10

    >>> while i < len(DATA):
    ...     value = DATA[i]
    ...     i += 1
    ...     if value == FIND:
    ...         print('Found')
    ...         break
    ... else:
    ...     print('Not Found')


Str Startswith
==============
.. doctest::

    >>> data = 'virginica'

    >>> result = data[:1] == 'v'
    True
    >>> result = data[:1] == 'v' or data[:1] == 's'
    True

.. doctest::

    >>> data = 'virginica'
    >>> result = data.startswith('v')
    True
    >>> result = data.startswith(('v', 's'))
    True


Str Endswith
============
.. doctest::

    >>> data = 'virginica'

    >>> result = data[-3:] == 'osa'
    False
    >>> result = data[-3:] == 'osa' or data[-2:] == 'ca'
    True

.. doctest::

    >>> data = 'setosa'

    >>> result = str.endswith('osa')
    True
    >>> result = str.endswith(('osa', 'ca'))
    True


Str Join Newline
================
.. doctest::

    >>> data = ['line1', 'line2', 'line3']
    >>> result = [line+'\n' for line in data]

.. doctest::

    >>> data = ['line1', 'line2', 'line3']
    >>> result = '\n'.join(data)


Others
======
* ``all()``
* ``any()``
* ``iter()``
* ``next()``


Functools
=========
* https://docs.python.org/3/library/functools.html

.. doctest:: TODO

    >>> from functools import *
    >>> # reduce(function, iterable[, initializer])


Itertools
=========
* https://docs.python.org/3/library/itertools.html
* :ref:`Itertools`

.. doctest:: TODO

    >>> from itertools import *

    >>> # count(start=0, step=1)
    >>> # cycle(iterable)
    >>> # repeat(object[, times])
    >>> # accumulate(iterable[, func, *, initial=None])
    >>> # chain(*iterables)
    >>> # compress(data, selectors)
    >>> # islice(iterable, start, stop[, step])
    >>> # starmap(function, iterable)
    >>> # product(*iterables, repeat=1)
    >>> # permutations(iterable, r=None)
    >>> # combinations(iterable, r)
    >>> # combinations_with_replacement(iterable, r)
    >>> # groupby(iterable, key=None)


The Zen of Python
=================
* :pep:`20` -- The Zen of Python

.. doctest::

    >>> import this
    The Zen of Python, by Tim Peters
    <BLANKLINE>
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

Polish:

    * Piękne jest lepsze niż brzydkie.
    * **Wyrażone wprost jest lepsze niż domniemane.**
    * **Proste jest lepsze niż złożone.**
    * Złożone jest lepsze niż skomplikowane.
    * Płaskie jest lepsze niż wielopoziomowe.
    * Rzadkie jest lepsze niż gęste.
    * **Czytelność się liczy.**
    * **Sytuacje wyjątkowe nie są na tyle wyjątkowe, aby łamać reguły.**
    * Choć praktyczność przeważa nad konsekwencją.
    * Błędy zawsze powinny być sygnalizowane.
    * Chyba że zostaną celowo ukryte.
    * W razie niejasności powstrzymaj pokusę zgadywania.
    * Powinien być jeden -- i najlepiej tylko jeden -- oczywisty sposób na zrobienie danej rzeczy.
    * Choć ten sposób może nie być oczywisty jeśli nie jest się Holendrem.
    * Teraz jest lepsze niż nigdy.
    * Chociaż nigdy jest często lepsze niż natychmiast.
    * **Jeśli rozwiązanie jest trudno wyjaśnić, to jest ono złym pomysłem.**
    * Jeśli rozwiązanie jest łatwo wyjaśnić, to może ono być dobrym pomysłem.
    * Przestrzenie nazw to jeden z niesamowicie genialnych pomysłów -- miejmy ich więcej!


Style Guide for Python Code
===========================
* :pep:`8` -- Style Guide for Python Code
* ``black``:

    * https://black.readthedocs.io/
    * https://github.com/psf/black
    * `Łukasz Langa - Life Is Better Painted Black, or: How to Stop Worrying and Embrace Auto-Formatting. PyCon 2019 <https://www.youtube.com/watch?v=esZLCuWs_2Y>`_
