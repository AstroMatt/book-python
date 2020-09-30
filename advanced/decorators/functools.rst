**************************
Standard Library Functools
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

Decorator Functools Func
------------------------
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/decorator_functools_func.py`
* Last update: 2020-10-01

:English:
    #. Use code from "Input" section (see below)
    #. Use ``functools.wraps`` in correct place
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Użyj ``functools.wraps`` w odpowiednim miejscu
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

.. code-block:: python

    def mydecorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper


    @mydecorator
    def hello():
        """Hello Docstring"""

:Output:
    .. code-block:: text

        >>> hello.__name__
        'hello'
        >>> hello.__doc__
        'Hello Docstring'

Decorator Functools Args
------------------------
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/decorator_functools_args.py`
* Last update: 2020-10-01

:English:
    #. Use code from "Input" section (see below)
    #. Use ``functools.wraps`` in correct place
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Użyj ``functools.wraps`` w odpowiednim miejscu
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

.. code-block:: python

    def mydecorator(happy=True):
        def decorator(func):
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator


    @mydecorator(happy=False)
    def hello():
        """Hello Docstring"""

:Output:
    .. code-block:: text

        >>> hello.__name__
        'hello'
        >>> hello.__doc__
        'Hello Docstring'

Decorator Functools Cls
-----------------------
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/decorator_functools_cls.py`
* Last update: 2020-10-01

:English:
    #. Use code from "Input" section (see below)
    #. Modify code to restore docstring and name from decorated class
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Zmodyfikuj kod aby przywrócić doctring oraz nazwę z dekorowanej klasy
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        def mydecorator(cls):
            class Wrapper(cls):
                pass
            return Wrapper


        @mydecorator
        class Hello:
            """Hello Docstring"""

:Output:
    .. code-block:: text

        >>> hello = Hello()
        >>> hello.__name__
        'Hello'
        >>> hello.__doc__
        'Hello Docstring'
