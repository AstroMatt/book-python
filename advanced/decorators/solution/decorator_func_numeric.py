"""
* Assignment: Decorator Function Numeric
* Filename: decorator_func_numeric.py
* Complexity: easy
* Lines of code to write: 8 lines
* Estimated time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Create decorator function `numeric`
    3. Decorator checks types arguments `a` and `b`
    4. If type `a` or `b` are not `int` or `float` raise exception `TypeError`
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz dekorator funkcję `numeric`
    3. Dekorator sprawdza typy argumentów `a` oraz `b`
    4. Jeżeli typ `a` lub `b` nie jest `int` lub `float` to podnieś wyjątek `TypeError`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isfunction
    >>> assert isfunction(numeric)
    >>> assert isfunction(numeric(lambda: None))

    >>> @numeric
    ... def add(a, b):
    ...     return a + b

    >>> add(1, 1)
    2
    >>> add(1.5, 2.5)
    4.0
    >>> add(-1, 1.5)
    0.5
    >>> add('one', 1)
    Traceback (most recent call last):
        ...
    TypeError: Argument "a" must be int or float
    >>> add(1, 'two')
    Traceback (most recent call last):
        ...
    TypeError: Argument "b" must be int or float
"""


# Solution
def numeric(func):
    def wrapper(a, b):
        if type(a) not in (int, float):
            raise TypeError('Argument "a" must be int or float')
        if type(b) not in (int, float):
            raise TypeError('Argument "b" must be int or float')
        return func(a, b)
    return wrapper
