"""
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


def numeric(func):
    def wrapper(a, b):
        if type(a) not in (int, float):
            raise TypeError('Argument "a" must be int or float')
        if type(b) not in (int, float):
            raise TypeError('Argument "b" must be int or float')
        return func(a, b)
    return wrapper
