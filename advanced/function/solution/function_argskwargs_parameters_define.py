"""
>>> mean(1)
1.0
>>> mean(1, 3)
2.0
>>> mean(1, 2, 3)
2.0
>>> mean()
Traceback (most recent call last):
    ...
ValueError: At least one argument is required
"""


def mean(*args):
    if not args:
        raise ValueError('At least one argument is required')

    return sum(args) / len(args)
