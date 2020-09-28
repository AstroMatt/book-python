def take_damage(dmg, /):
    """
    >>> take_damage(1)

    >>> take_damage(1, 2)
    Traceback (most recent call last):
        ...
    TypeError: take_damage() takes 1 positional argument but 2 were given

    >>> take_damage()
    Traceback (most recent call last):
        ...
    TypeError: take_damage() missing 1 required positional argument: 'dmg'

    >>> take_damage(dmg=1)
    Traceback (most recent call last):
        ...
    TypeError: take_damage() got some positional-only arguments passed as keyword arguments: 'dmg'
    """
    return None
