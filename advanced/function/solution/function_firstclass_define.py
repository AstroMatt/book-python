"""
>>> from inspect import isfunction
>>> assert isfunction(check)
>>> assert isfunction(wrapper)
>>> assert isfunction(check(lambda: None))
>>> check(lambda: None)()
hello from wrapper
"""


def wrapper(*args, **kwargs):
    print('hello from wrapper')


def check(func):
    return wrapper
