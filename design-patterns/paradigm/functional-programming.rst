**********************
Functional Programming
**********************


Pure function
=============
* Function which returns always the same results based on the same argument.
* ``random.randint()`` - Not pure
* ``pow()`` - Pure


Lambda - Anonymous functions
============================

Example 1
---------
.. code-block:: python

    DATA = [1, 2, 3, 4]


    def is_even(x):
        if x % 2 == 0:
            return True
        else:
            return False


    result = filter(is_even, DATA)
    print(list(result))
    # [2, 4]

.. code-block:: python

    DATA = [1, 2, 3, 4]

    result = filter(lambda x: x % 2 == 0, DATA)
    print(list(result))
    # [2, 4]

Example 2
---------
.. code-block:: python

    DATA = [
        {'user': 'twardowski', 'uid': 1000},
        {'user': 'root', 'uid': 0},
    ]

    def is_system_user(data):
        if data['uid'] < 1000:
            return True
        else:
            return False

    result = []

    for user in DATA:
        if is_system_user(user):
            result.append(user)

    print(result)
    # [{'user': 'root', 'uid': 0}]


.. code-block:: python

    DATA = [
        {'user': 'twardowski', 'uid': 1000},
        {'user': 'root', 'uid': 0},
    ]


    result = filter(lambda x: x['uid'] < 1000, DATA)

    print(list(result))
    # [{'user': 'root', 'uid': 0}]

Monkey patching
---------------
.. code-block:: python

    class Astronaut:
        pass

    jan = Astronaut()
    jan.say_hello = lambda: print('hello')

    jan.say_hello()


Function Passing
================
.. code-block:: python

    print(
        tuple(
            filter(lambda x: x[1]<100,
                   enumerate(
                       filter(lambda x: x%2==0,
                              map(lambda x: pow(x, 2),
                                  map(float,
                                      (x for x in range(0, 34) if x % 3 == 0
    ))))))))



Built-in functions
==================

``map()``
---------
.. code-block:: python

    DATA = [1, 2, 3]

    result = map(float, DATA)

    print(result)
    # <map object at 0x11d2241d0>

    print(list(result))
    # [1.0, 2.0, 3.0]

.. code-block:: python

    DATA = [1, 2, 3]

    def square(x):
        return pow(x, 2)

    result = map(square, DATA)

    print(list(result))
    # [1, 4, 9]

.. code-block:: python

    DATA = [1, 2, 3]

    result = map(lambda x: pow(x, 2), DATA)

    print(list(result))
    # [1, 4, 9]

``zip()``
---------
.. code-block:: python

    keys = ['a', 'b', 'c']
    values = [1, 2, 3]

    result = zip(keys, values)

    print(result)
    # <zip object at 0x11cfea280>

    print(list(result))
    # [('a', 1), ('b', 2), ('c', 3)]

.. code-block:: python

    keys = ['a', 'b', 'c']
    values = [1, 2, 3]

    result = zip(keys, values)

    print(dict(result))
    # {'a': 1, 'b': 2, 'c': 3}

``filter()``
------------
.. code-block:: python

    DATA = [
        {'name': 'Jan Twardowski', 'age': 21},
        {'name': 'Mark Watney', 'age': 25},
        {'name': 'Melissa Lewis', 'age': 18},
    ]

    def is_adult(person):
        if person['age'] >= 21:
            return True
        else:
            return False


    result = filter(is_adult, DATA)
    print(list(result))
    # [
    #   {'name': 'Jan Twardowski', 'age': 21},
    #   {'name': 'Mark Watney', 'age': 25},
    # ]

.. code-block:: python

    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False


    DATA = range(0, 10)

    result = filter(is_even, DATA)

    print(list(result))
    # [0, 2, 4, 6, 8]

.. code-block:: python

    DATA = range(0, 10)

    result = filter(lambda x: x % 2 == 0, DATA)

    print(list(result))
    # [0, 2, 4, 6, 8]


.. code-block:: python

    result = filter(lambda x: x % 2 == 0, range(0, 10))

    print(list(result))
    # [0, 2, 4, 6, 8]

``all()``
---------
Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:

.. code-block:: python

    def all(iterable):
        if not iterable:
            return False

        for element in iterable:
            if not element:
                return False

        return True

``any()``
---------
Return True if any element of the iterable is true. If the iterable is empty, return False. Equivalent to:

.. code-block:: python

    def any(iterable):
        if not iterable:
            return False

        for element in iterable:
            if element:
                return True

        return False


``functools``
=============

.. code-block:: python

    from functools import reduce


    DATA = [1, 2, 3, 4, 5]

    def add(x, y):
        return (x + y)

    result = reduce(add, DATA)

    print(result)
    # 15

.. code-block:: python

    from functools import reduce


    DATA = [1, 2, 3, 4, 5]

    result = reduce(lambda x, y: x + y, DATA)

    print(result)
    # 15

``lru_cache``
-------------
.. code-block:: python

    from functools import lru_cache


    @lru_cache(maxsize=None)
    def fib(num):
        if num < 2:
            return num
        else:
            return fib(num-1) + fib(num-2)


    fib(16)
    # 987

    fib
    # <functools._lru_cache_wrapper object at 0x11cce6730>

    fib.cache_info()
    # CacheInfo(hits=14, misses=17, maxsize=None, currsize=17)

memoize
-------
.. code-block:: python

    def factorial(n):
        if not hasattr(factorial, '__cache__'):
            factorial.__cache__ = {1: 1}

        if not n in factorial.__cache__:
            factorial.__cache__[n] = n * factorial(n - 1)

        return factorial.__cache__[n]


    factorial(5)
    # 120

    factorial.__cache__
    # {1:1, 2:2, 3:6, 4:24, 5:120}

.. code-block:: python

    def memoize(function):
        from functools import wraps

        memo = {}

        @wraps(function)
        def wrapper(*args):
            if args in memo:
                return memo[args]
            else:
                rv = function(*args)
                memo[args] = rv
                return rv
        return wrapper


    @memoize
    def fibonacci(n):
        if n < 2: return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    fibonacci(25)

partial
-------
* Create alias function and its arguments
* Useful when you need to pass function with arguments to for example ``map`` or ``filter``

.. code-block:: python

    from functools import partial


    basetwo = partial(int, base=2)
    basetwo.__doc__ = 'Convert base 2 string to an int.'
    basetwo('10010')
    # 18

partialmethod
-------------
.. code-block:: python

    class Cell(object):
        def __init__(self):
            self._alive = False

        @property
        def alive(self):
            return self._alive

        def set_state(self, state):
            self._alive = bool(state)

        set_alive = partialmethod(set_state, True)
        set_dead = partialmethod(set_state, False)


    c = Cell()

    c.alive
    # False

    c.set_alive()
    c.alive
    # True

reduce
------
Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). The left argument, x, is the accumulated value and the right argument, y, is the update value from the iterable. If the optional initializer is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty. If initializer is not given and iterable contains only one item, the first item is returned.

Roughly equivalent to:

.. code-block:: python

    def reduce(function, iterable, initializer=None):
        it = iter(iterable)
        if initializer is None:
            value = next(it)
        else:
            value = initializer
        for element in it:
            value = function(value, element)
        return value

singledispatch
--------------
.. versionadded:: Python 3.4

* Overload a method
* Python will choose function to run based on argument type

.. code-block:: python

    from functools import singledispatch


    @singledispatch
    def celsius_to_kelvin(arg):
        raise NotImplementedError('Argument must be int or list')

    @celsius_to_kelvin.register
    def _(degree: int):
        return degree + 273.15

    @celsius_to_kelvin.register
    def _(degrees: list):
        return [d+273.15 for d in degrees]


    celsius_to_kelvin(1)
    # 274.15

    celsius_to_kelvin([1,2])
    # [274.15, 275.15]

    celsius_to_kelvin((1,2))
    # NotImplementedError: Argument must be int or list

singledispatchmethod
--------------------
.. versionadded:: Python 3.8

* Overload a method
* Python will choose method to run based on argument type

.. code-block:: python

    from functools import singledispatchmethod


    class Converter:

        @singledispatchmethod
        def celsius_to_kelvin(arg):
            raise NotImplementedError('Argument must be int or list')

        @celsius_to_kelvin.register
        def _(self, degree: int):
            return degree + 273.15

        @celsius_to_kelvin.register
        def _(self, degrees: list):
            return [d+273.15 for d in degrees]


    conv = Converter()

    conv.celsius_to_kelvin(1)
    # 274.15

    conv.celsius_to_kelvin([1,2])
    # [274.15, 275.15]

    conv.celsius_to_kelvin((1,2))
    # NotImplementedError: Argument must be int or list



Callback
========
.. code-block:: python

    def http(obj):
        response = requests.request(
            method=obj.method,
            data=obj.data,
            path=obj.path)

        if response == 200:
            return obj.on_success(response)
        else:
            return obj.on_error(response)


    class Request:
        method = 'GET'
        path = '/index'
        data = None

        def on_success(self, response):
            print('Success!')

        def on_error(self, response):
            print('Error')

    http(
        Request()
    )


Assignments
===========

``map()``, ``filter()`` and ``lambda``
--------------------------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/functional_map_filter_lambda.py`

:Polish:
    #. Używając generatora zbuduj listę zawierającą wszystkie liczby podzielne przez 3 z zakresu od 1 do 33:
    #. Używając funkcji ``filter()`` usuń z niej wszystkie liczby parzyste
    #. Używając wyrażenia ``lambda`` i funkcji ``map()`` podnieś wszystkie elementy tak otrzymanej listy do sześcianu
    #. Odpowiednio używając funkcji ``sum()``  i ``len()`` oblicz średnią arytmetyczną z elementów tak otrzymanej listy.

Balanced Brackets
-----------------
* Complexity level: medium
* Lines of code to write: 10 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/functional_brackets.py`

:English:
    #. Create function which checks if brackets are balanced
    #. Brackets are balanced, when each opening bracket has closing pair
    #. Use recursion
    #. Types of brackets:

        * round: ``(`` i ``)``
        * square: ``[`` i ``]``
        * curly ``{`` i ``}``
        * angle ``<`` i ``>``

:Polish:
    #. Stwórz funkcję, która sprawdzi czy nawiasy są zbalansowane
    #. Nawiasy są zbalansowane, gdy każdy otwierany nawias ma zamykającą parę
    #. Użyj rekurencji
    #. Typy nawiasów:

        * okrągłe: ``(`` i ``)``
        * kwadratowe: ``[`` i ``]``
        * klamrowe ``{`` i ``}``
        * trójkątne ``<`` i ``>``

.. code-block:: python

    def is_bracket_balanced(text: str) -> bool:
        """
        >>> is_bracket_balanced('{}')
        True
        >>> is_bracket_balanced('()')
        True
        >>> is_bracket_balanced('[]')
        True
        >>> is_bracket_balanced('<>')
        True
        >>> is_bracket_balanced('')
        True
        >>> is_bracket_balanced('(')
        False
        >>> is_bracket_balanced('}')
        False
        >>> is_bracket_balanced('(]')
        False
        >>> is_bracket_balanced('([)')
        False
        >>> is_bracket_balanced('[()')
        False
        >>> is_bracket_balanced('{()[]}')
        True
        >>> is_bracket_balanced('() [] () ([]()[])')
        True
        >>> is_bracket_balanced("( (] ([)]")
        False
        """
        pass

