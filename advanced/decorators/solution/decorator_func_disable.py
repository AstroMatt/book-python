"""
* Assignment: Decorator Function Disable
* Filename: decorator_func_disable.py
* Complexity: easy
* Lines of code to write: 5 lines
* Estimated time: 5 min

English:
    1. Create decorator `disable`
    2. Decorator raises an exception `PermissionError` and does not execute function
    3. Compare result with "Tests" section (see below)

Polish:
    1. Stwórz dekorator `disable`
    2. Dekorator podnosi wyjątek `PermissionError` i nie wywołuje funkcji
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

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


# Solution
def disable(func):
    def wrapper(*args, **kwargs):
        raise PermissionError('Function is disabled')
    return wrapper

