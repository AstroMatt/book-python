"""
>>> hello.__name__
'hello'

>>> hello.__doc__
'Hello Docstring'
"""

from functools import wraps


def mydecorator(happy=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator


@mydecorator(happy=False)
def hello():
    """Hello Docstring"""
