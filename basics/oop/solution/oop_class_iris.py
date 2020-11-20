"""
>>> from inspect import isclass
>>> assert isclass(Iris)
>>> assert isinstance(setosa, Iris)
>>> assert isinstance(versicolor, Iris)
>>> assert isinstance(virginica, Iris)
"""


class Iris:
    pass


setosa = Iris()
versicolor = Iris()
virginica = Iris()
