"""
>>> assert issubclass(Setosa, IrisInterface)
>>> assert hasattr(Setosa, 'mean')
>>> assert hasattr(Setosa, 'sum')
>>> assert hasattr(Setosa, 'len')

>>> Setosa.__annotations__  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': <class 'float'>,
 'sepal_width': <class 'float'>,
 'petal_length': <class 'float'>,
 'petal_width': <class 'float'>}

>>> setosa = Setosa(5.1, 3.5, 1.4, 0.2)
>>> setosa.len()
4
>>> setosa.sum()
10.2
>>> setosa.mean()
2.55
"""

class IrisInterface:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
        raise NotImplementedError

    def avg(self):
        raise NotImplementedError

    def sum(self):
        raise NotImplementedError

    def len(self):
        raise NotImplementedError


class Setosa(IrisInterface):
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width

    def len(self):
        return len(self.__dict__)

    def sum(self):
        return sum(self.__dict__.values())

    def mean(self):
        return self.sum() / self.len()
