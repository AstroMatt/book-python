"""
>>> assert callable(check)
>>> assert callable(check(lambda x: x))
>>> result = check(lambda x: x).__call__()
>>> result is None
True
"""


def wrapper(*args, **kwargs):
    return None


def check(func):
    return wrapper
