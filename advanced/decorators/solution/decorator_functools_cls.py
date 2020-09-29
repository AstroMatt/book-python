"""
>>> hello = Hello()
>>> hello.__name__
'Hello'
>>> hello.__doc__
'Hello Docstring'
"""

def mydecorator(cls):
    class Wrapper(cls):
        __doc__ = cls.__doc__
        __name__ = cls.__name__
    return Wrapper


@mydecorator
class Hello:
    """Hello Docstring"""
