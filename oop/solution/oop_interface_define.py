"""
>>> assert hasattr(IrisInterface, 'mean')
>>> assert hasattr(IrisInterface, 'sum')
>>> assert hasattr(IrisInterface, 'len')

>>> IrisInterface.__annotations__  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': <class 'float'>,
 'sepal_width': <class 'float'>,
 'petal_length': <class 'float'>,
 'petal_width': <class 'float'>}

>>> iris = IrisInterface(5.8, 2.7, 5.1, 1.9)
Traceback (most recent call last):
    ...
NotImplementedError
"""

class IrisInterface:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    def __init__(self,
                 sepal_length: float,
                 sepal_width: float,
                 petal_length: float,
                 petal_width: float) -> None:

        raise NotImplementedError

    def mean(self) -> float:
        raise NotImplementedError

    def sum(self) -> float:
        raise NotImplementedError

    def len(self) -> int:
        raise NotImplementedError
