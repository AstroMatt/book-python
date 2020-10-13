"""
>>> from inspect import isfunction
>>> assert isfunction(check)
>>> assert isfunction(check(lambda: None))
>>> assert isfunction(echo)
>>> assert hasattr(echo, 'disabled')

>>> echo.disabled = False
>>> echo('hello')
hello

>>> echo.disabled = True
>>> echo('hello')
Traceback (most recent call last):
    ...
PermissionError: Function is disabled
"""


def check(func):
    def wrapper(*args, **kwargs):
        if not wrapper.disabled:
            return func(*args, **kwargs)
        else:
            raise PermissionError('Function is disabled')
    return wrapper


@check
def echo(text):
    print(text)
