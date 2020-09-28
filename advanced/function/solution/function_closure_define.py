"""
>>> assert callable(check)
>>> assert callable(check(lambda x: x))
>>> result = check(lambda x: x).__call__()
>>> result is None
True
"""


def check(func):
    def wrapper(*args, **kwargs):
        return None
    return wrapper

