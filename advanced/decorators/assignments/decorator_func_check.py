"""
* Assignment: Decorator Function Check
* Filename: decorator_func_check.py
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Create decorator `check`
    3. Decorator calls function, only when `echo.disabled` is `False`
    4. Note that decorators overwrite pointers and in `wrapper`
       you must check if `wrapper.disabled` is `False`
    5. Else raise an exception `PermissionError`
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Stwórz dekorator `check`
    3. Dekorator wywołuje funkcję, tylko gdy `echo.disabled` jest `False`
    4. Zwróć uwagę, że dekoratory nadpisują wskaźniki i we `wrapper`
       musisz sprawdzić czy `wrapper.disabled` jest `False`
    5. W przeciwnym przypadku podnieś wyjątek `PermissionError`
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> @check
    ... def echo(text):
    ...     print(text)

    >>> from inspect import isfunction
    >>> assert isfunction(check)
    >>> assert isfunction(check(lambda: None))
    >>> assert isfunction(echo)

    >>> echo.disabled = False
    >>> echo('hello')
    hello

    >>> echo.disabled = True
    >>> echo('hello')
    Traceback (most recent call last):
    PermissionError: Function is disabled

    >>> assert hasattr(echo, 'disabled')
"""


# Given
def check(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


# Solution
def check(func):
    def wrapper(*args, **kwargs):
        if not wrapper.disabled:
            return func(*args, **kwargs)
        else:
            raise PermissionError('Function is disabled')
    return wrapper
