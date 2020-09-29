"""
>>> hello.__name__
'hello'

>>> hello.__doc__
'Hello Docstring'
"""

from functools import wraps


def mydecorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@mydecorator
def hello():
    """Hello Docstring"""
