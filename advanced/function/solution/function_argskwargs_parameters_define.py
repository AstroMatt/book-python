def mean(*numbers):
    """
    >>> mean(1)
    1.0
    >>> mean(1, 3)
    2.0
    >>> mean()
    Traceback (most recent call last):
        ...
    ValueError: Not enough arguments
    """
    if not numbers:
        raise ValueError('Not enough arguments')

    return sum(numbers) / len(numbers)
