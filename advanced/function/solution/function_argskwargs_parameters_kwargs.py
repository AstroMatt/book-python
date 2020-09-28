"""
>>> isnumeric()
False
>>> isnumeric(0)
True
>>> isnumeric(1)
True
>>> isnumeric(-1)
True
>>> isnumeric(1.1)
True
>>> isnumeric('one')
False
>>> isnumeric([1, 1.1])
False
>>> isnumeric(1, 1.1)
True
>>> isnumeric(1, 'one')
False
>>> isnumeric(1, 'one', 'two')
False
>>> isnumeric(True)
False
>>> isnumeric(a=1)
True
>>> isnumeric(a=1.1)
True
>>> isnumeric(a='one')
False
"""


def isnumeric(*args, **kwargs) -> bool:
    arguments = args + tuple(kwargs.values())

    if len(arguments) == 0:
        return False

    for arg in arguments:
        if type(arg) not in (float, int):
            return False

    return True
