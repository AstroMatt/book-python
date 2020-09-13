**************
Good Practices
**************


Rationale
=========
.. figure:: img/goodpractices-programmer-exp
    :align: center
    :scale: 75%

    Code Complexity vs. Programmer Experiance


Range
=====
.. code-block:: python
    :caption: Replace it with ``range()``

    i = 0

    while i < ...:
        i += 1


Enumerate
=========
.. code-block:: python
    :caption: Replace it with ``enumerate()``

    i = 0

    for ...:
        value = DATA[i]
        i += 1

Sum
===
.. code-block:: python
    :caption: Replace it with ``sum()``

    total = 0

    for ...:
        total += ...


Zip
===
.. code-block:: python
    :caption: Replace it with ``zip()``

    header = [...]
    values = [...]

    for ...:
        header[i]
        values[i]


List Comprehension
==================
.. code-block:: python
    :caption: Replace it with list comprehension

    result = list()

    for ...:
        result.append(...)


Dict Comprehension
==================
.. code-block:: python
    :caption: Replace it with dict comprehension

    result = dict()

    for ...:
        result[...] = ...


Set Comprehension
=================
.. code-block:: python
    :caption: Replace it with set comprehension

    result = set()

    for ...:
        result.add(...)

Map
===
.. code-block:: python
    :caption: Replace it with ``map()``

    result = (func(x) for x in DATA)
    result = map(func, DATA)


Filter
======
.. code-block:: python
    :caption: Replace it with ``filter()``

    result = (x for x in DATA if func(x))
    result = filter(func, DATA)


Str
===
.. code-block:: python

    result = str[-3:] == 'osa'
    result = str.endswith('osa')

    result = str[-3:] == 'osa' or str[-2:] == 'ca'
    result = str.endswith(('osa', 'ca'))

.. code-block:: python

    result = str[:1] == 'v'
    result = str.startswith('v')

    result = str[:1] == 'v' or str[:1] == 's'
    result = str.startswith(('v', 's'))

.. code-block:: python
    :caption: Replace with ``str.join()``

    data = ['line1', 'line2', 'line3']

    result = [line + '\n' for line in data]
    result = '\n'.join(data)


Others
======
.. code-block:: python
    :caption: The same for ...

    all(), any(), iter(), next()


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
