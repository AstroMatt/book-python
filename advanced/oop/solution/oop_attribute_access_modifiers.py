"""
>>> result  # doctest: +NORMALIZE_WHITESPACE
[{'species', 'virginica'},
 {'species', 'setosa'},
 {'species', 'versicolor'}]
"""


class Iris:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
        self._sepal_width = sepal_width
        self._sepal_length = sepal_length
        self._petal_width = petal_width
        self._petal_length = petal_length
        self.species = species


DATA = [
    Iris(5.8, 2.7, 5.1, 1.9, 'virginica'),
    Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
    Iris(5.7, 2.8, 4.1, 1.3, 'versicolor'),
]

result = [{attrname, attrvalue}
          for row in DATA
          for attrname, attrvalue in row.__dict__.items()
          if not attrname.startswith('_')]
