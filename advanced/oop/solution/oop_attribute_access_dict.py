"""
* Assignment: OOP Attribute Access Dict
* Filename: oop_attribute_access_dict.py
* Complexity: medium
* Lines of code to write: 35 lines
* Estimated time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. Create `result: list[Iris]`
    3. Iterate over `DATA` skipping header
    4. Separate `features` from `species` in each row
    5. Append to `result`:
        a. if `species` is "setosa" append instance of a class `Setosa`
        b. if `species` is "versicolor" append instance of a class `Versicolor`
        c. if `species` is "virginica" append instance of a class `Virginica`
    6. Initialize instances with `features` using `*args` notation
    7. Print instance class name and then both sum and mean
    8. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz `result: list[Iris]`
    3. Iterując po `DATA` pomijając header
    4. Odseparuj `features` od `species` w każdym wierszu
    5. Dodaj do `result`:
        a. jeżeli `species` jest "setosa" to dodaj instancję klasy `Setosa`
        b. jeżeli `species` jest "versicolor" to dodaj instancję klasy `Versicolor`
        c. jeżeli `species` jest "virginica" to dodaj instancję klasy `Virginica`
    6. Instancje inicjalizuj danymi z `features` używając notacji `*args`
    7. Wypisz nazwę stworzonej klasy oraz średnią z pomiarów
    8. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `self.__class__.__name__`
    * `self.__dict__.values()`
    * `globals()[classname]`

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'name': 'Virginica',  'mean': 3.88},
     {'name': 'Setosa',     'mean': 2.55},
     {'name': 'Versicolor', 'mean': 3.48},
     {'name': 'Virginica',  'mean': 4.15},
     {'name': 'Versicolor', 'mean': 3.9},
     {'name': 'Setosa',     'mean': 2.35}]
"""

# Given
DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa')]



class Iris:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
        self._sepal_length = sepal_length
        self._sepal_width = sepal_width
        self._petal_length = petal_length
        self._petal_width = petal_width

    def __repr__(self):
        raise NotImplementedError

    def values(self):
        raise NotImplementedError

    def mean(self):
        return sum(self.values()) / len(self.values())


class Setosa(Iris):
    pass


class Versicolor(Iris):
    pass


class Virginica(Iris):
    pass


# Solution
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
