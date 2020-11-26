"""
* Assignment: Decorator Functools Func
* Filename: decorator_functools_func.py
* Complexity: easy
* Lines of code to write: 2 lines
* Estimated time: 3 min

English:
    1. Use code from "Input" section (see below)
    2. Use `functools.wraps` in correct place
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Input" (patrz poniżej)
    2. Użyj `functools.wraps` w odpowiednim miejscu
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> @mydecorator
    ... def hello():
    ...     '''Hello Docstring'''

    >>> hello.__name__
    'hello'
    >>> hello.__doc__
    'Hello Docstring'
"""


# Given
def mydecorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


# Solution
from functools import wraps


def mydecorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
