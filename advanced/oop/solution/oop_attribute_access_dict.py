"""
>>> result  # doctest: +NORMALIZE_WHITESPACE
[{'name': 'Virginica',  'mean': 3.88},
 {'name': 'Setosa',     'mean': 2.55},
 {'name': 'Versicolor', 'mean': 3.48},
 {'name': 'Virginica',  'mean': 4.15},
 {'name': 'Versicolor', 'mean': 3.9},
 {'name': 'Setosa',     'mean': 2.35}]
"""

DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]


class Iris:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
        self._sepal_length = sepal_length
        self._sepal_width = sepal_width
        self._petal_length = petal_length
        self._petal_width = petal_width

    def __repr__(self):
        return str({
            'name': self.__class__.__name__,
            'mean': round(self.mean(), 2)})

    def values(self):
        return list(self.__dict__.values())

    def mean(self):
        return sum(self.values()) / len(self.values())


class Setosa(Iris):
    pass


class Versicolor(Iris):
    pass


class Virginica(Iris):
    pass


result = [iris(*features)
          for *features, label in DATA[1:]
          if (species := label.capitalize())
          and (iris := globals()[species])]


# Solution 2
result = []
for *features, label in DATA[1:]:
    species = label.capitalize()
    iris = globals()[species]
    result.append(iris(*features))
