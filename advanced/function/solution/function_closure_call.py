"""
>>> add(1, 2)
3
>>> add(-1.1, 1.1)
0.0

>>> result()
hello

>>> check()
Traceback (most recent call last):
    ...
NameError: name 'check' is not defined
"""


def add(a, b):
    return a + b


def check(func):
    def wrapper(*args, **kwargs):
        print('hello')
    return wrapper


result = check(add)
del check
result()
# hello
