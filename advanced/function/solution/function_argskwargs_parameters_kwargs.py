def isnumeric(*args, **kwargs) -> bool:
    """
    >>> isnumeric(1)
    True
    >>> isnumeric(1.5)
    True
    >>> isnumeric('one', a=1)
    False
    >>> isnumeric([1, 1.5])
    False
    >>> isnumeric()
    False
    >>> isnumeric(True)
    False
    >>> isnumeric(a=1)
    True
    >>> isnumeric(a='one')
    False
    """
    arguments = args + tuple(kwargs.values())

    if len(arguments) == 0:
        return False

    for arg in arguments:
        if type(arg) not in (float, int):
            return False

    return True
