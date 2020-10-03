"""
>>> iris = Iris()
Traceback (most recent call last):
  ...
TypeError: Can't instantiate abstract class Iris with abstract methods get_name

>>> setosa = Setosa()
"""

from abc import ABC, abstractmethod


class Iris(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Setosa(Iris):
    def get_name(self):
        pass
