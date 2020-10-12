"""
>>> from inspect import isfunction
>>> assert callable(set_position)
>>> assert isfunction(set_position)

>>> set_position(x=1, y=2)

>>> set_position()
Traceback (most recent call last):
    ...
TypeError: set_position() missing 2 required keyword-only arguments: 'x' and 'y'

>>> set_position(1)
Traceback (most recent call last):
    ...
TypeError: set_position() takes 0 positional arguments but 1 was given

>>> set_position(1, 2)
Traceback (most recent call last):
    ...
TypeError: set_position() takes 0 positional arguments but 2 were given

>>> set_position(1, y=1)
Traceback (most recent call last):
    ...
TypeError: set_position() takes 0 positional arguments but 1 positional argument (and 1 keyword-only argument) were given

>>> set_position(x=1, 2)
Traceback (most recent call last):
    ...
SyntaxError: positional argument follows keyword argument
"""


def set_position(*, x, y):
    ...
