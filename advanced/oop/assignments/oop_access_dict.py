"""
* Assignment: OOP Protected Dict
* Filename: oop_protected_dict.py
* Complexity: medium
* Lines of code: 35 lines
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
    7. Compare result with "Tests" section (see below)

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
    7. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `globals()[classname]`

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [Virginica(5.8, 2.7, 5.1, 1.9),
     Setosa(5.1, 3.5, 1.4, 0.2),
     Versicolor(5.7, 2.8, 4.1, 1.3),
     Virginica(6.3, 2.9, 5.6, 1.8),
     Versicolor(6.4, 3.2, 4.5, 1.5),
     Setosa(4.7, 3.2, 1.3, 0.2)]
"""


# Given
from dataclasses import dataclass


DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa')]


@dataclass(repr=False)
class Iris:
    _sepal_length: float
    _sepal_width: float
    _petal_length: float
    _petal_width: float

    def __repr__(self):
        name = self.__class__.__name__
        args = tuple(self.__dict__.values())
        return f'{name}{args}'


class Setosa(Iris):
    pass


class Versicolor(Iris):
    pass


class Virginica(Iris):
    pass


result: list = []


# Solution
result = [iris(*features)
          for *features, label in DATA[1:]
          if (classname := label.capitalize())
          and (iris := globals()[classname])]


# Solution 2
for *features, label in DATA[1:]:
    if label == 'setosa':
        iris = Setosa(*features)
    elif label == 'virginica':
        iris = Virginica(*features)
    elif label == 'versicolor':
        iris = Versicolor(*features)
    result.append(iris)
