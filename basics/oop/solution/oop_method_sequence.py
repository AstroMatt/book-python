"""
* Assignment: OOP Method Sequence
* Filename: oop_method_sequence.py
* Complexity: easy
* Lines of code to write: 18 lines
* Estimated time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Create class ``Iris`` with ``features: list[float]`` and ``label: str`` attributes
    3. For each row in ``DATA`` create ``Iris`` instance with row values
    4. Set class attributes at the initialization from positional arguments
    5. Create method which sums values of all ``features``
    6. In ``result`` gather species and sum of each row
    7. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz klasę ``Iris`` z atrybutami ``features: list[float]`` i ``label: str``
    3. Dla każdego wiersza w ``DATA`` twórz instancję ``Iris`` z danymi z wiersza
    4. Ustaw atrybuty klasy przy inicjalizacji z argumentów pozycyjnych
    5. Stwórz metodę sumującą wartości wszystkich ``features``
    6. W ``result`` zbieraj nazwę gatunku i sumę z każdego wiersza
    7. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'setosa': 9.4,
     'versicolor': 16.299999999999997,
     'virginica': 19.3}
"""

# Given
DATA = [(4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica')]

result = {}


# Solution
class Iris:
    def __init__(self, features, label):
        self.features = features
        self.label = label

    def sum(self):
        return sum(self.features)


for *features, label in DATA:
    iris = Iris(features, label)
    result[iris.label] = iris.sum()
