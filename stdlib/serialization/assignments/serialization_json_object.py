"""
* Assignment: Serialization JSON Object
* Filename: serialization_json_object.py
* Complexity: medium
* Lines of code: 15 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Convert from JSON format to Python
    3. Reading file create instances of `Setosa`, `Virginica`, `Versicolor`
       classes based on value in field "species"
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Przekonwertuj dane z JSON do Python
    3. Czytając plik twórz obiekty klas `Setosa`, `Virginica`, `Versicolor`
       w zależności od wartości pola "species"
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [Virginica(sepalLength=5.8, sepalWidth=2.7, petalLength=5.1, petalWidth=1.9),
     Setosa(sepalLength=5.1, sepalWidth=3.5, petalLength=1.4, petalWidth=0.2),
     Versicolor(sepalLength=5.7, sepalWidth=2.8, petalLength=4.1, petalWidth=1.3),
     Virginica(sepalLength=6.3, sepalWidth=2.9, petalLength=5.6, petalWidth=1.8),
     Versicolor(sepalLength=6.4, sepalWidth=3.2, petalLength=4.5, petalWidth=1.5),
     Setosa(sepalLength=4.7, sepalWidth=3.2, petalLength=1.3, petalWidth=0.2),
     Versicolor(sepalLength=7.0, sepalWidth=3.2, petalLength=4.7, petalWidth=1.4),
     Virginica(sepalLength=7.6, sepalWidth=3.0, petalLength=6.6, petalWidth=2.1),
     Setosa(sepalLength=4.9, sepalWidth=3.0, petalLength=1.4, petalWidth=0.2)]
    >>> from os import remove
    >>> remove(FILE)
"""

# Given
import json
from dataclasses import dataclass


FILE = r'_temporary.json'
DATA = """
    [{"sepalLength": 5.8, "sepalWidth": 2.7, "petalLength": 5.1, "petalWidth": 1.9, "species": "virginica"},
     {"sepalLength": 5.1, "sepalWidth": 3.5, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
     {"sepalLength": 5.7, "sepalWidth": 2.8, "petalLength": 4.1, "petalWidth": 1.3, "species": "versicolor"},
     {"sepalLength": 6.3, "sepalWidth": 2.9, "petalLength": 5.6, "petalWidth": 1.8, "species": "virginica"},
     {"sepalLength": 6.4, "sepalWidth": 3.2, "petalLength": 4.5, "petalWidth": 1.5, "species": "versicolor"},
     {"sepalLength": 4.7, "sepalWidth": 3.2, "petalLength": 1.3, "petalWidth": 0.2, "species": "setosa"},
     {"sepalLength": 7.0, "sepalWidth": 3.2, "petalLength": 4.7, "petalWidth": 1.4, "species": "versicolor"},
     {"sepalLength": 7.6, "sepalWidth": 3.0, "petalLength": 6.6, "petalWidth": 2.1, "species": "virginica"},
     {"sepalLength": 4.9, "sepalWidth": 3.0, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"}]"""


@dataclass
class Iris:
    sepalLength: float
    sepalWidth: float
    petalLength: float
    petalWidth: float


class Setosa(Iris):
    pass


class Virginica(Iris):
    pass


class Versicolor(Iris):
    pass


result = []

# Solution
for iris in json.loads(DATA):
    species = iris.pop('species')

    if species == 'setosa':
        cls = Setosa
    elif species == 'versicolor':
        cls = Versicolor
    elif species == 'virginica':
        cls = Virginica
    else:
        print('Not supported')

    result.append(cls(**iris))
