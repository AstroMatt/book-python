"""
>>> from inspect import isfunction
>>> assert isfunction(check)
>>> assert isfunction(check(lambda: None))
>>> assert isfunction(echo)

>>> echo('hello')
Traceback (most recent call last):
    ...
PermissionError: Function is disabled
"""


def check(func):
    def wrapper(*args, **kwargs):
        raise PermissionError('Function is disabled')
    return wrapper


@check
def echo(text):
    print(text)
