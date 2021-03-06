"""
* Assignment: OOP Abstract Annotate
* Complexity: easy
* Lines of code: 13 lines
* Time: 13 min

English:
    1. Define abstract class `IrisAbstract`
    2. Attributes: `sepal_length, sepal_width, petal_length, petal_width`
    3. Abstract methods: `__init__`, `sum()`, `len()`, `mean()`
    4. Add type annotation to all methods and attibutes
    5. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj klasę abstrakcyjną `IrisAbstract`
    2. Atrybuty: `sepal_length, sepal_width, petal_length, petal_width`
    3. Metody abstrakcyjne: `__init__`, `sum()`, `len()`, `mean()`
    4. Dodaj anotację typów do wszystkich metod i atrybutów
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isabstract
    >>> assert isabstract(IrisAbstract)
    >>> assert hasattr(IrisAbstract, '__init__')
    >>> assert hasattr(IrisAbstract, 'mean')
    >>> assert hasattr(IrisAbstract, 'sum')
    >>> assert hasattr(IrisAbstract, 'len')
    >>> assert IrisAbstract.__init__.__isabstractmethod__
    >>> assert IrisAbstract.mean.__isabstractmethod__
    >>> assert IrisAbstract.sum.__isabstractmethod__
    >>> assert IrisAbstract.len.__isabstractmethod__

    >>> IrisAbstract.__annotations__  # doctest: +NORMALIZE_WHITESPACE
    {'sepal_length': <class 'float'>,
     'sepal_width': <class 'float'>,
     'petal_length': <class 'float'>,
     'petal_width': <class 'float'>}

    >>> IrisAbstract.__init__.__annotations__  # doctest: +NORMALIZE_WHITESPACE
    {'sepal_length': <class 'float'>,
     'sepal_width': <class 'float'>,
     'petal_length': <class 'float'>,
     'petal_width': <class 'float'>,
     'return': None}

     >>> IrisAbstract.mean.__annotations__
     {'return': <class 'float'>}

     >>> IrisAbstract.sum.__annotations__
     {'return': <class 'float'>}

     >>> IrisAbstract.len.__annotations__
     {'return': <class 'int'>}
"""


# Given
from abc import ABCMeta, abstractmethod


# Solution
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
