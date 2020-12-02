"""
* Assignment: OOP Abstract Syntax
* Filename: oop_abstract_syntax.py
* Complexity: easy
* Lines of code: 10 lines
* Estimated time: 5 min

English:
    1. Create abstract class `Iris`
    2. Create abstract method `get_name()` in `Iris`
    3. Create class `Setosa` inheriting from `Iris`
    4. Try to create instance of a class `Setosa`
    5. Try to create instance of a class `Iris`
    6. Compare result with "Tests" section (see below)

Polish:
    1. Stwórz klasę abstrakcyjną `Iris`
    2. Stwórz metodę abstrakcyjną `get_name()` w `Iris`
    3. Stwórz klasę `Setosa` dziedziczące po `Iris`
    4. Spróbuj stworzyć instancje klasy `Setosa`
    5. Spróbuj stworzyć instancję klasy `Iris`
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> iris = Iris()
    Traceback (most recent call last):
    TypeError: Can't instantiate abstract class Iris with abstract method get_name
    >>> setosa = Setosa()

Warning:
    * Last line of doctest, second to last word of `TypeError` message
    * In Python 3.7, 3.8 there is "methods" word in doctest
    * In Python 3.9 there is "method" word in doctest
    * So it differs by "s" at the end of "method" word
"""

# Solution
from abc import ABC, abstractmethod


class Iris(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Setosa(Iris):
    def get_name(self):
        pass
