"""
>>> isnumeric()
False
>>> isnumeric(1)
True
>>> isnumeric(1, 1.5)
True
>>> isnumeric(True)
False
>>> isnumeric('one', 1)
False
>>> isnumeric([])
False
>>> isnumeric([1, 1.5])
False
"""

def isnumeric(*args) -> bool:
    if not args:
        return False

    for arg in args:
        # if not isinstance(arg, (int, float)):
        if type(arg) not in (int, float):
            return False

    return True
