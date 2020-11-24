"""
* Assignment: Loop Dict Label Encoder
* Filename: loop_dict_label_encoder.py
* Complexity: hard
* Lines of code to write: 9 lines
* Estimated time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Define:
        a. `features: list[tuple]` - measurements
        b. `labels: list[int]` - species
        c. `label_encoder: dict[int, str]` - dictionary with encoded (as numbers) species names
    3. Separate header from data
    4. To encode and decode `labels` (species) we need `label_encoder: dict[int, str]`:
        a. key - id (incremented integer value)
        b. value - species name
    5. `label_encoder` must be generated from `DATA`
    6. For each row add appropriate data to `features`, `labels` and `label_encoder`
    7. Print `features`, `labels` and `label_encoder`
    8. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj:
        a. `features: list[tuple]` - pomiary
        b. `labels: list[int]` - gatunki
        c. `label_encoder: dict[int, str]` - słownik zakodowanych (jako cyfry) nazw gatunków
    3. Odseparuj nagłówek od danych
    4. Aby móc zakodować i odkodować `labels` (gatunki) potrzebny jest `label_encoder: dict[int, str]`:
        a. key - identyfikator (kolejna liczba rzeczywista)
        b. value - nazwa gatunku
    5. `label_encoder` musi być wygenerowany z `DATA`
    6. Dla każdego wiersza dodawaj odpowiednie dane do `feature`, `labels` i `label_encoder`
    7. Wypisz `feature`, `labels` i `label_encoder`
    8. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * Reversed lookup dict

Tests:
    >>> assert type(features) is list
    >>> assert type(labels) is list
    >>> assert type(label_encoder) is dict
    >>> assert all(type(x) is tuple for x in features)
    >>> assert all(type(x) is int for x in labels)
    >>> assert all(type(x) is int for x in label_encoder.keys())
    >>> assert all(type(x) is str for x in label_encoder.values())
    >>> features  # doctest: +NORMALIZE_WHITESPACE
    [(5.8, 2.7, 5.1, 1.9),
     (5.1, 3.5, 1.4, 0.2),
     (5.7, 2.8, 4.1, 1.3),
     (6.3, 2.9, 5.6, 1.8),
     (6.4, 3.2, 4.5, 1.5),
     (4.7, 3.2, 1.3, 0.2)]
    >>> labels
    [0, 1, 2, 0, 2, 1]
    >>> label_encoder  # doctest: +NORMALIZE_WHITESPACE
    {0: 'virginica',
     1: 'setosa',
     2: 'versicolor'}
"""

# Given
DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

features: list = []
labels: list = []
label_encoder: dict = {}

# Solution
lookup = {}
i = 0

for *X,y in DATA[1:]:
    if y not in lookup:
        label_encoder[i] = y
        lookup[y] = i
        i += 1

    labels.append(lookup[y])
    features.append(tuple(X))
