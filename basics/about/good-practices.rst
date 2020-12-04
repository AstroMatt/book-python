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
    >>> while i < 10:
    ...    i += 1

.. doctest::

    >>> for i in range(10):
    ...    pass


ForEach
=======
.. doctest::

    >>> for i in range(len(DATA)):
    ...    value = DATA[i]

.. doctest::

    >>> for value in DATA:
    ...    pass


Sum
===
.. doctest::

    >>> total = 0
    >>> for i in range(len(DATA)):
    ...    total += DATA[i]

.. doctest::

    sum(DATA)


Enumerate
=========
.. code-block:: python

    i = 0

    while i < len(DATA):
        value = DATA[i]
        i += 1

.. code-block:: python

    for i, value in enumerate(DATA):
        ...


Zip
===
.. code-block:: python

    header = [...]
    values = [...]
    result = {}

    for i in range(len(header)):
        key = header[i]
        val = values[i]
        result[key] = value

.. code-block:: python

    header = [...]
    values = [...]

    zip(header, values)


List Comprehension
==================
.. code-block:: python

    result = list()

    for x in DATA:
        result.append(x)

.. code-block:: python

    result = [x for x in DATA]


Set Comprehension
=================
.. code-block:: python

    result = set()

    for x in DATA:
        result.add(x)

.. code-block:: python

    result = {x for x in DATA}


Dict Comprehension
==================
.. code-block:: python

    result = dict()

    for key, value in DATA.items():
        result[key] = value

.. code-block:: python

    result = {k:v for k,v in DATA.items()}


Map
===
.. code-block:: python

    result = (func(x) for x in DATA)

.. code-block:: python

    result = map(func, DATA)


Filter
======
.. code-block:: python

    result = (x for x in DATA if func(x))

.. code-block:: python

    result = filter(func, DATA)


For Else
========
.. code-block:: python

    found = False

    for ...:
        if ...:
            found = True
            break

    if not found:
        ....

.. code-block:: python

    for ...:
        if ...:
            found = True
            break
    else:
        ....


While Else
==========
.. code-block:: python

    found = False

    while ...:
        if ...:
            found = True
            break

    if not found:
        ....

.. code-block:: python

    while ...:
        if ...:
            found = True
            break
    else:
        ....


Str Endswith
============
.. code-block:: python

    result = str[-3:] == 'osa'
    result = str[-3:] == 'osa' or str[-2:] == 'ca'

.. code-block:: python

    result = str.endswith('osa')
    result = str.endswith(('osa', 'ca'))


Str Startswith
==============
.. code-block:: python

    result = str[:1] == 'v'
    result = str[:1] == 'v' or str[:1] == 's'

.. code-block:: python

    result = str.startswith('v')
    result = str.startswith(('v', 's'))


Str Join Newline
================
.. code-block:: python
    :caption: Replace with ``str.join()``

    data = ['line1', 'line2', 'line3']

    result = [line + '\n' for line in data]
    result = '\n'.join(data)


Others
======
* ``all()``
* ``any()``
* ``iter()``
* ``next()``


Functools
=========
* https://docs.python.org/3/library/functools.html

.. code-block:: python

    from functools import *

    reduce(function, iterable[, initializer])


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


The Zen of Python
=================
* :pep:`20` -- The Zen of Python

.. code-block:: python

    import this

English
-------
* Beautiful is better than ugly.
* **Explicit is better than implicit.**
* **Simple is better than complex.**
* Complex is better than complicated.
* Flat is better than nested.
* Sparse is better than dense.
* **Readability counts.**
* **Special cases aren't special enough to break the rules.**
* Although practicality beats purity.
* Errors should never pass silently.
* Unless explicitly silenced.
* In the face of ambiguity, refuse the temptation to guess.
* There should be one-- and preferably only one --obvious way to do it.
* Although that way may not be obvious at first unless you're Dutch.
* Now is better than never.
* Although never is often better than *right* now.
* **If the implementation is hard to explain, it's a bad idea.**
* If the implementation is easy to explain, it may be a good idea.
* Namespaces are one honking great idea -- let's do more of those!

Polish
------
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
