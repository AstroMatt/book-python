"""
* Assignment: Decorator Function Disable
* Filename: decorator_func_disable.py
* Complexity: easy
* Lines of code: 1 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Modify decorator `disable`
    3. Decorator raises an exception `PermissionError` and does not execute function
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Zmodyfikuj dekorator `disable`
    3. Dekorator podnosi wyjątek `PermissionError` i nie wywołuje funkcji
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isfunction
    >>> assert isfunction(disable)
    >>> assert isfunction(disable(lambda: None))

    >>> @disable
    ... def echo(text):
    ...     print(text)

    >>> echo('hello')
    Traceback (most recent call last):
    PermissionError: Function is disabled
"""


# Given
def disable(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


# Solution
def disable(func):
    def wrapper(*args, **kwargs):
        raise PermissionError('Function is disabled')
    return wrapper

