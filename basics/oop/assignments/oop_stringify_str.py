"""
* Assignment: OOP Stringify Str
* Filename: oop_stringify_str.py
* Complexity: easy
* Lines of code: 3 lines
* Estimated time: 5 min

English:
    1. Use code from "Given" section (see below)
    2. While printing object show: species name and a sum of `self.features`
    3. Result of sum round to one decimal place
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Przy wypisywaniu obiektu pokaż: nazwę gatunku i sumę `self.features`
    3. Wynik sumowania zaokrąglij do jednego miejsca po przecinku
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> for *features, label in DATA:
    ...    iris = Iris(features, label)
    ...    print(iris)
    setosa 9.4
    versicolor 16.3
    virginica 19.3
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

    def __str__(self):
        total = sum(self.features)
        return f'{self.label} {total:.1f}'
