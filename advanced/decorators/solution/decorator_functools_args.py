"""
* Assignment: Decorator Functools Args
* Filename: decorator_functools_args.py
* Complexity: easy
* Lines of code to write: 2 lines
* Estimated time: 3 min

English:
    1. Use code from "Given" section (see below)
    2. Use `functools.wraps` in correct place
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Użyj `functools.wraps` w odpowiednim miejscu
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> @mydecorator(happy=False)
    ... def hello():
    ...     '''Hello Docstring'''
    >>> hello.__name__
    'hello'
    >>> hello.__doc__
    'Hello Docstring'
"""


# Given
def mydecorator(happy=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Solution
from functools import wraps


def mydecorator(happy=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator
