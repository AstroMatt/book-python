"""
* Assignment: Decorator Functools Cls
* Filename: decorator_functools_cls.py
* Complexity: easy
* Lines of code to write: 2 lines
* Estimated time: 5 min

English:
    1. Use code from "Given" section (see below)
    2. Modify code to restore docstring and name from decorated class
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Zmodyfikuj kod aby przywrócić docstring oraz nazwę z dekorowanej klasy
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> @mydecorator
    ... class Hello:
    ...     '''Hello Docstring'''
    >>> hello = Hello()
    >>> hello.__name__
    'Hello'
    >>> hello.__doc__
    'Hello Docstring'
"""


# Given
def mydecorator(cls):
    class Wrapper(cls):
        pass
    return Wrapper


# Solution
def mydecorator(cls):
    class Wrapper(cls):
        __doc__ = cls.__doc__
        __name__ = cls.__name__
    return Wrapper
