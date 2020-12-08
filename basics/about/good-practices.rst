**************
Good Practices
**************


Rationale
=========
.. figure:: img/goodpractices-programmer-exp.png

    Code Complexity vs. Programmer Experience


Range
=====
>>> i = 0
>>>
>>> while i < 5:
...    i += 1

>>> for i in range(5):
...    pass


ForEach
=======
>>> DATA = ['a', 'b', 'c']
>>>
>>> for i in range(len(DATA)):
...    value = DATA[i]

>>> DATA = ['a', 'b', 'c']
>>> for value in DATA:
...    pass


Sum
===
>>> DATA = [1, 2, 3]
>>> total = 0
>>>
>>> for i in range(len(DATA)):
...    total += DATA[i]

>>> DATA = [1, 2, 3]
>>> sum(DATA)
6


Enumerate
=========
>>> DATA = ['a', 'b', 'c']
>>> i = 0
>>>
>>> while i < len(DATA):
...    value = DATA[i]
...    i += 1

>>> DATA = ['a', 'b', 'c']
>>>
>>> for i, value in enumerate(DATA):
...    pass


Zip
===
>>> header = ['a', 'b', 'c']
>>> values = [1, 2, 3]
>>> result = {}
>>>
>>> for i in range(len(header)):
...    key = header[i]
...    val = values[i]
...    result[key] = value

>>> header = ['a', 'b', 'c']
>>> values = [1, 2, 3]
>>>
>>> result = zip(header, values)
>>> dict(result)
{'a': 1, 'b': 2, 'c': 3}


List Comprehension
==================
>>> DATA = ['a', 'b', 'c']
>>> result = list()
>>>
>>> for x in DATA:
...    result.append(x)
...
>>> result
['a', 'b', 'c']

>>> DATA = ['a', 'b', 'c']
>>> result = [x for x in DATA]
>>> result
['a', 'b', 'c']


Set Comprehension
=================
>>> DATA = ['a', 'b', 'c']
>>> result = set()
>>>
>>> for x in DATA:
...    result.add(x)

>>> DATA = ['a', 'b', 'c']
>>> result = {x for x in DATA}


Dict Comprehension
==================
>>> DATA = {'a': 1, 'b': 2, 'c': 3}
>>> result = dict()
>>>
>>> for key, value in DATA.items():
...    result[key] = value

>>> DATA = {'a': 1, 'b': 2, 'c': 3}
>>> result = {k:v for k,v in DATA.items()}


Map
===
>>> def func(x):
...     return float()
...
>>> DATA = [1, 2, 3]
>>> result = (func(x) for x in DATA)

>>> def func(x):
...     return float()
...
>>> DATA = [1, 2, 3]
>>> result = map(func, DATA)


Filter
======
>>> def func(x):
...     return x % 2 == 0
...
>>> DATA = [1, 2, 3]
>>> result = (x for x in DATA if func(x))

>>> def func(x):
...     return x % 2 == 0
...
>>> DATA = [1, 2, 3]
>>> result = filter(func, DATA)


For Else
========
>>> DATA = [1, 2, 3]
>>> FIND = 10
>>> found = False
>>>
>>> for value in DATA:
...     if value == FIND:
...         print('Found')
...         found = True
...         break
...
>>> if not found:
...     print('Not Found')
Not Found

>>> DATA = [1, 2, 3]
>>> FIND = 10
>>>
>>> for value in DATA:
...     if value == FIND:
...         print('Found')
...         break
... else:
...     print('Not Found')
Not Found


While Else
==========

>>> DATA = [1, 2, 3]
>>> FIND = 10
>>> found = False
>>>
>>> while i < len(DATA):
...     value = DATA[i]
...     i += 1
...     if value == FIND:
...         print('Found')
...         found = True
...         break
...
>>> if not found:
...     print('Not Found')
Not Found

>>> DATA = [1, 2, 3]
>>> FIND = 10
>>>
>>> while i < len(DATA):
...     value = DATA[i]
...     i += 1
...     if value == FIND:
...         print('Found')
...         break
... else:
...     print('Not Found')
Not Found


Str Startswith
==============
>>> data = 'virginica'
>>> data[:1] == 'v'
True
>>> data[:1] == 'v' or data[:1] == 's'
True

>>> data = 'virginica'
>>> data.startswith('v')
True
>>> data.startswith(('v', 's'))
True


Str Endswith
============
>>> data = 'virginica'
>>> data[-3:] == 'osa'
False
>>> data[-3:] == 'osa' or data[-2:] == 'ca'
True

>>> data = 'setosa'
>>> data.endswith('osa')
True
>>> data.endswith(('osa', 'ca'))
True


Str Join Newline
================
>>> data = ['line1', 'line2', 'line3']
>>> result = [line+'\n' for line in data]

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
* ``reduce(function, iterable[, initializer])``

>>> from functools import *


Itertools
=========
* https://docs.python.org/3/library/itertools.html
* :ref:`Itertools`
* ``count(start=0, step=1)``
* ``cycle(iterable)``
* ``repeat(object[, times])``
* ``accumulate(iterable[, func, *, initial=None])``
* ``chain(*iterables)``
* ``compress(data, selectors)``
* ``islice(iterable, start, stop[, step])``
* ``starmap(function, iterable)``
* ``product(*iterables, repeat=1)``
* ``permutations(iterable, r=None)``
* ``combinations(iterable, r)``
* ``combinations_with_replacement(iterable, r)``
* ``groupby(iterable, key=None)``

>>> from itertools import *


The Zen of Python
=================
* :pep:`20` -- The Zen of Python

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
