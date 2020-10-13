"""
>>> from inspect import isfunction
>>> assert isfunction(hello)
>>> assert isfunction(result)
>>> assert not hasattr(__name__, 'check')

>>> hello()
hello from function

>>> result()
hello from wrapper

>>> check()
Traceback (most recent call last):
    ...
NameError: name 'check' is not defined
"""


def check(func: callable):
    def wrapper(*args, **kwargs):
        print('hello from wrapper')
    return wrapper


def hello():
    print('hello from function')


result = check(hello)
del check
result()
