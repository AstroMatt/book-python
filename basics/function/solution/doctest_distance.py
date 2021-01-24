from typing import Union


def km_to_meters(kilometers: Union[int, float]) -> float:
    """
    >>> km_to_meters(1)
    1000.0

    >>> km_to_meters(0)
    0.0

    >>> km_to_meters(-1)
    Traceback (most recent call last):
        ...
    ValueError: Argument must be not negative

    >>> km_to_meters([1, 2])
    Traceback (most recent call last):
        ...
    TypeError: Invalid Type of an Argument

    >>> km_to_meters('one')
    Traceback (most recent call last):
        ...
    TypeError: Invalid type of an Argument

    >>> km_to_meters(1.5)
    1500.0

    >>> km_to_meters(True)
    Traceback (most recent call last):
        ...
    TypeError: Invalid type of an Argument

    """
    if type(kilometers) not in {int, float}:
        raise TypeError('Invalid type of an Argument')

    if kilometers < 0:
        raise ValueError('Argument must be not negative')

    return float(kilometers * 1000)
