******************
Micro-benchmarking
******************

    We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil -- Donald Knuth


Evaluation
==========
* Fresh start of Python process
* Clean memory before start
* Same data
* Same start conditions, CPU load, RAM usage, ``iostat``
* Do not measure how long Python wakes up
* Check what you measure


.. _timeit:

``timeit``
==========

Programmatic use
----------------
.. literalinclude:: src/utils-timeit-simple.py
    :language: python
    :caption: Timeit simple statement

.. literalinclude:: src/utils-timeit-multiple.py
    :language: python
    :caption: Timeit multiple statements with setup code

.. literalinclude:: src/utils-timeit-globals.py
    :language: python
    :caption: Timeit with ``globals()``

Console use
-----------
.. literalinclude:: src/utils-timeit.sh
    :language: console
    :caption: Timeit

.. code-block:: text

    -n N, --number=N
    how many times to execute ‘statement’

    -r N, --repeat=N
    how many times to repeat the timer (default 5)

    -s S, --setup=S
    statement to be executed once initially (default pass)

    -p, --process
    measure process time, not wallclock time, using time.process_time() instead of time.perf_counter(), which is the default

    -u, --unit=U
    specify a time unit for timer output; can select nsec, usec, msec, or sec

    -v, --verbose
    print raw timing results; repeat for more digits precision

    -h, --help
    print a short usage message and exit


.. _Micro-benchmarking use case:

String Concatenation
====================
.. code-block:: python

    from time import time


    class Timeit:
        def __init__(self, name):
            self.name = name

        def __enter__(self):
            self.start = time()
            return self

        def __exit__(self, *arg):
            end = time()
            print(f'Duration of {self.name} is {end-self.start:.2f} second')


    a = 1
    b = 2
    repetitions = int(1e7)


    with Timeit('f-string'):
        for _ in range(repetitions):
            f'{a}{b}'

    with Timeit('string concat'):
        for _ in range(repetitions):
            a + b

    with Timeit('str.format()'):
        for _ in range(repetitions):
            '{0}{1}'.format(a, b)

    with Timeit('str.format()'):
        for _ in range(repetitions):
            '{}{}'.format(a, b)

    with Timeit('str.format()'):
        for _ in range(repetitions):
            '{a}{b}'.format(a=a, b=b)

    with Timeit('%-style'):
        for _ in range(repetitions):
            '%s%s' % (a, b)

    with Timeit('%-style'):
        for _ in range(repetitions):
            '%d%d' % (a, b)

    with Timeit('%-style'):
        for _ in range(repetitions):
            '%f%f' % (a, b)

    # Duration of f-string is 2.70 second
    # Duration of string concat is 0.68 second
    # Duration of str.format() is 3.46 second
    # Duration of str.format() is 3.37 second
    # Duration of str.format() is 4.85 second
    # Duration of %-style is 2.59 second
    # Duration of %-style is 2.59 second
    # Duration of %-style is 3.82 second


Case Studies - Unique Keys
==========================
* Runtime: Jupyter ``%%timeit``

.. code-block:: python
    :caption: Setup code used for all examples

    DATA = [{'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
            {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
            {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
            {'Sepal length': 5.0, 'Petal width': 0.2, 'Species': 'setosa'},
            {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
            {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'}]

.. code-block:: python
    :caption: Append if object not in the list

    %%timeit -r 10 -n 1000000

    result = list()

    for row in DATA:
        for key in row.keys():
            if key not in result:
                result.append(key)

    # 2.16 µs ± 26.5 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

.. code-block:: python
    :caption: Append to list and deduplicate at the end

    %%timeit -r 10 -n 1000000

    result = list()

    for row in DATA:
        for key in row.keys():
            result.append(key)

    set(result)

    # 2.5 µs ± 32.9 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

.. code-block:: python
    :caption: Add to set

    %%timeit -r 10 -n 1000000

    result = set()

    for row in DATA:
        for key in row.keys():
            result.add(key)

    # 2.12 µs ± 32.4 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

.. code-block:: python
    :caption: Update set

    %%timeit -r 10 -n 1000000

    result = set()

    for row in DATA:
        result.update(row.keys())

    # 1.57 µs ± 26.7 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

.. code-block:: python
    :caption: Set Comprehension

    %%timeit -r 10 -n 1000000

    result = set(key
        for record in DATA
            for key in record.keys())

    # 2.06 µs ± 79.7 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

.. code-block:: python
    :caption: Add to Set Comprehension. Code appends generator object not values, this is why it is so fast!

    %%timeit -r 10 -n 1000000

    result = set()

    result.add(key
        for record in DATA
           for key in record.keys())

    # 447 ns ± 9.52 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

.. code-block:: python
    :caption: Update Set Comprehension

    %%timeit -r 10 -n 1000000

    result = set()
    result.update(tuple(x.keys()) for x in DATA)

    # 2.06 µs ± 45.9 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

.. code-block:: python

    %%timeit -r 10 -n 1000000

    result = set()

    for row in DATA:
        result.update(tuple(row))

    # 2.09 µs ± 16.1 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

.. code-block:: python

    %%timeit -r 10 -n 1000000

    result = set()

    for row in DATA:
        result.update(list(row))

    # 2.33 µs ± 30.2 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

.. code-block:: python

    %%timeit -r 10 -n 1000000

    result = set()

    for row in DATA:
        result.update(set(row))

    # 1.71 µs ± 54 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)


Case Study - Factorial
======================
.. code-block:: python
    :caption: Recap information about factorial (``n!``)

    """
    5! = 5 * 4!
    4! = 4 * 3!
    3! = 3 * 2!
    2! = 2 * 1!
    1! = 1 * 0!
    0! = 1
    """

    factorial(5)                                    # = 120
        return 5 * factorial(4)                     # 5 * 24 = 120
            return 4 * factorial(3)                 # 4 * 6 = 24
                return 3 * factorial(2)             # 3 * 2 = 6
                    return 2 * factorial(1)         # 2 * 1 = 2
                        return 1 * factorial(0)     # 1 * 1 = 1
                            return 1                # 1

.. code-block:: python
    :caption: Cache with global scope

    _cache = {}

    def cache(func):
        def wrapper(n):
            if n not in _cache:
                _cache[n] = func(n)
            return _cache[n]
        return wrapper


    @cache
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)


    factorial(500)
    factorial(400)
    factorial(450)

.. code-block:: python
    :caption: Cache with local scope

    def cache(func):
        _cache = {}
        def wrapper(n):
            if n not in _cache:
                _cache[n] = func(n)
            return _cache[n]
        return wrapper


    @cache
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)


    factorial(500)
    factorial(400)
    factorial(450)

.. code-block:: python
    :caption: Cache with embedded scope

    def cache(func):
        def wrapper(n):
            if n not in wrapper._cache:
                wrapper._cache[n] = func(n)
            return wrapper._cache[n]
        if not hasattr(wrapper, '_cache'):
            setattr(wrapper, '_cache', {})
        return wrapper


    @cache
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)


    factorial(500)
    factorial(400)
    factorial(450)

.. code-block:: python
    :caption: Without cache

    %%timeit

    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)


    factorial(500)
    factorial(400)
    factorial(450)

    # 283 µs ± 6.63 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

.. code-block:: python
    :caption: Cache contains

    %%timeit

    _cache = {}

    def factorial(n: int) -> int:
        if n in _cache:
            return _cache[n]

        if n == 0:
            return 1
        else:
            result = _cache[n] = n * factorial(n-1)
            return result


    factorial(500)
    factorial(400)
    factorial(450)

    # 153 µs ± 2.49 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

.. code-block:: python
    :caption: Cache get

    %%timeit

    _cache = {}

    def factorial(n: int) -> int:
        result = _cache.get(n)

        if result:
            return result

        if n == 0:
            return 1
        else:
            result = _cache[n] = n * factorial(n-1)
            return result


    factorial(500)
    factorial(400)
    factorial(450)

    # 181 µs ± 10.3 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

.. code-block:: python
    :caption: Cache contains with exceptions

    %%timeit

    _cache = {}

    def factorial(n: int) -> int:
        if n == 0:
            return 1

        try:
            return _cache[n]
        except KeyError:
            _cache[n] = result = n * factorial(n-1)
            return result


    factorial(500)
    factorial(400)
    factorial(450)

    # 618 µs ± 6.6 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

.. code-block:: python
    :caption: Adding cache layer

    %%timeit

    _cache = {}

    def fac(n: int) -> int:

        def factorial(n: int) -> int:
            if n == 0:
                return 1
            return n * factorial(n-1)

        if not n in _cache:
            _cache[n] = factorial(n)

        return _cache[n]


    fac(500)
    fac(400)
    fac(450)

    # 283 µs ± 6.44 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

.. code-block:: python
    :caption: Get from cache

    %%timeit

    _cache = {}

    def factorial(n: int) -> int:
        if n == 0:
            return 1

        if n in _cache:
            return _cache[n]

        result = _cache[n] = n * factorial(n-1)
        return result


    factorial(500)
    factorial(400)
    factorial(450)

    # 153 µs ± 9.64 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

.. code-block:: python

    _cache = {}


    def factorial(n):
        if n == 0:
            return 1

        if (result := _cache.get(n)):
            return result

        result = n * factorial(n-1)
        _cache[n] = result
        return result


References
==========
* https://www.youtube.com/watch?v=RT88FrHttRI
