"""
* Assignment: OOP Stringify Repr
* Filename: oop_stringify_repr.py
* Complexity: easy
* Lines of code to write: 3 lines
* Estimated time: 5 min

English:
    1. Use code from "Given" section (see below)
    2. Print representation of each instance with values (use `repr()`)
    3. Result of sum round to two decimal places
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Wypisz reprezentację każdej z instancji z wartościami (użyj `repr()`)
    3. Wynik sumowania zaokrąglij do dwóch miejsc po przecinku
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> result = [Iris(X,y) for *X,y in DATA]
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [Iris(features=[4.7, 3.2, 1.3, 0.2], label='setosa'),
     Iris(features=[7.0, 3.2, 4.7, 1.4], label='versicolor'),
     Iris(features=[7.6, 3.0, 6.6, 2.1], label='virginica')]
"""

# Given
DATA = [(4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica')]


class Iris:
    def __init__(self, features, label):
        self.features = features
        self.label = label


# Solution
class Iris:
    def __init__(self, features, label):
        self.features = features
        self.label = label

    def __repr__(self):
        features = self.features
        label = self.label
        return f'Iris({features=}, {label=})'
