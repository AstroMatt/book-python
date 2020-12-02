"""
* Assignment: OOP Abstract Interface
* Filename: oop_abstract_interface.py
* Complexity: easy
* Lines of code: 14 lines
* Estimated time: 13 min

English:
    1. Define abstract class `IrisAbstract`
    2. Attributes: `sepal_length, sepal_width, petal_length, petal_width`
    3. Methods: `sum()`, `len()`, `mean()`
    4. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj klasę abstrakcyjną `IrisAbstract`
    2. Atrybuty: `sepal_length, sepal_width, petal_length, petal_width`
    3. Metody: `sum()`, `len()`, `mean()`
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isabstract
    >>> assert isabstract(IrisAbstract)
    >>> assert hasattr(IrisAbstract, 'mean')
    >>> assert hasattr(IrisAbstract, 'sum')
    >>> assert hasattr(IrisAbstract, 'len')
"""

# Solution
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
