"""
>>> from inspect import isabstract
>>> assert isabstract(IrisAbstract)
>>> assert hasattr(IrisAbstract, 'mean')
>>> assert hasattr(IrisAbstract, 'sum')
>>> assert hasattr(IrisAbstract, 'len')
"""
from abc import ABCMeta, abstractmethod


class IrisAbstract(metaclass=ABCMeta):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    @abstractmethod
    def __init__(self,
                 sepal_length: float,
                 sepal_width: float,
                 petal_length: float,
                 petal_width: float) -> None:
        ...

    @abstractmethod
    def mean(self) -> float:
        ...

    @abstractmethod
    def sum(self) -> float:
        ...

    @abstractmethod
    def len(self) -> int:
        ...
