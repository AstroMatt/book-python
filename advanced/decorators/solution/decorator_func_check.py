"""
* Assignment: Decorator Function Check
* Filename: decorator_func_check.py
* Complexity: easy
* Lines of code to write: 5 lines
* Estimated time: 5 min

English:
    1. Create decorator `check`
    2. Decorator calls function, only when `echo.disabled` is `False`
    3. Note that decorators overwrite pointers and in `wrapper` you must check if `wrapper.disabled` is `False`
    4. Else raise an exception `PermissionError`
    5. Compare result with "Tests" section (see below)

Polish:
    1. Stwórz dekorator `check`
    2. Dekorator wywołuje funkcję, tylko gdy `echo.disabled` jest `False`
    3. Zwróć uwagę, że dekoratory nadpisują wskaźniki i we `wrapper` musisz sprawdzić czy `wrapper.disabled` jest `False`
    4. W przeciwnym przypadku podnieś wyjątek `PermissionError`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

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


# Solution
def check(func):
    def wrapper(*args, **kwargs):
        if not wrapper.disabled:
            return func(*args, **kwargs)
        else:
            raise PermissionError('Function is disabled')
    return wrapper
