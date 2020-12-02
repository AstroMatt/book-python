.. _Decorator Stdlib Functools:

**************************
Decorator Stdlib Functools
**************************


Wraps
=====
* ``from functools import wraps``
* ``@wraps(func)``

.. code-block:: python
    :emphasize-lines: 15,18

    def mydecorator(func):
        def wrapper(*args, **kwargs):
            """wrapper docstring"""
            return func(*args, **kwargs)
        return wrapper


    @mydecorator
    def myfunction(x):
        """myfunction docstring"""
        print(x)


    print(myfunction.__name__)
    # wrapper

    print(myfunction.__doc__)
    # wrapper docstring

.. code-block:: python
    :emphasize-lines: 1,5,19,22

    from functools import wraps


    def mydecorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """wrapper docstring"""
            return func(*args, **kwargs)
        return wrapper


    @mydecorator
    def myfunction(x):
        """myfunction docstring"""
        print(x)


    print(myfunction.__name__)
    # myfunction

    print(myfunction.__doc__)
    # myfunction docstring


Cached Property
===============
* ``from functools import cached_property``
* ``@cached_property(func)``

.. code-block:: python

    import statistics
    from functools import cached_property


    class Iris:
        def __init__(self, *args):
            self._measurements = args

        @cached_property
        def mean(self):
            return statistics.mean(self._measurements)

        @cached_property
        def stdev(self):
            return statistics.stdev(self._measurements)


    flower = Iris(5.1, 3.5, 1.4, 0.2)
    flower.stdev()
    flower.mean()


LRU (least recently used) cache
===============================
* ``from functools import lru_cache``
* ``@lru_cache(maxsize=None)``

.. code-block:: python

    from functools import lru_cache


    @lru_cache(maxsize=None)
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)


    [fib(n) for n in range(16)]
    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

    fib.cache_info()
    # CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)


Assignments
===========

.. literalinclude:: assignments/decorator_functools_func.py
    :caption: :download:`Solution <assignments/decorator_functools_func.py>`
    :end-before: # Solution

.. literalinclude:: assignments/decorator_functools_args.py
    :caption: :download:`Solution <assignments/decorator_functools_args.py>`
    :end-before: # Solution

.. literalinclude:: assignments/decorator_functools_cls.py
    :caption: :download:`Solution <assignments/decorator_functools_cls.py>`
    :end-before: # Solution
