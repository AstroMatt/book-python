"""
* Assignment: Loop Comprehension Split
* Filename: loop_comprehension_split.py
* Complexity: medium
* Lines of code to write: 9 lines
* Estimated time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Calculate pivot point: length of data times given percent (60%/40%, see below)
    3. Using List Comprehension split data to:
        a. `features: list[tuple]` - list of measurements (each measurement row is a tuple)
        b. `labels: list[str]` - list of species names
    4. Split those data structures with proportion:
        a. `features_train: list[tuple]` - features to train - 60%
        b. `features_test: list[tuple]` - features to test - 40%
        c. `labels_train: list[str]` - labels to train - 60%
        d. `labels_test: list[str]` - labels to test - 40%
    5. Compare results with "Tests" section below

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wylicz punkt podziału: długość danych razy zadany procent (60%/40%, patrz poniżej)
    3. Używając List Comprehension podziel dane na:
        a. `features: list[tuple]` - lista pomiarów (każdy wiersz z pomiarami ma być tuple)
        b. `labels: list[str]` - lista nazw gatunków
    4. Podziel te struktury danych w proporcji:
        a. `features_train: list[tuple]` - features do uczenia - 60%
        b. `features_test: list[tuple]` - features do testów - 40%
        c. `labels_train: list[str]` - labels do uczenia - 60%
        d. `labels_test: list[str]` - labels do testów - 40%
    5. Porównaj wynik z sekcją "Tests" poniżej

Tests:
    >>> assert type(features_train) is list
    >>> assert type(features_test) is list
    >>> assert type(labels_train) is list
    >>> assert type(labels_test) is list
    >>> assert all(type(x) is tuple for x in features_train), 'features_train: expected type list[tuple]'
    >>> assert all(type(x) is tuple for x in features_test), 'features_test: expected type list[tuple]'
    >>> assert all(type(x) is str for x in labels_train)
    >>> assert all(type(x) is str for x in labels_test)
    >>> features_train  # doctest: +NORMALIZE_WHITESPACE
    [(5.8, 2.7, 5.1, 1.9),
     (5.1, 3.5, 1.4, 0.2),
     (5.7, 2.8, 4.1, 1.3),
     (6.3, 2.9, 5.6, 1.8),
     (6.4, 3.2, 4.5, 1.5),
     (4.7, 3.2, 1.3, 0.2)]
    >>> features_test  # doctest: +NORMALIZE_WHITESPACE
    [(7.0, 3.2, 4.7, 1.4),
     (7.6, 3.0, 6.6, 2.1),
     (4.9, 3.0, 1.4, 0.2),
     (4.9, 2.5, 4.5, 1.7)]
    >>> labels_train
    ['virginica', 'setosa', 'versicolor', 'virginica', 'versicolor', 'setosa']
    >>> labels_test
    ['versicolor', 'virginica', 'setosa', 'virginica']
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
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
]

features_train: list
features_test: list
labels_train: list
labels_test: list

# Solution
RATIO = 0.6
header, *data = DATA
pivot = int(len(data) * RATIO)
features_train = [tuple(X) for *X, y in data[:pivot]]
features_test = [tuple(X) for *X, y in data[pivot:]]
labels_train = [y for *X, y in data[:pivot]]
labels_test = [y for *X, y in data[pivot:]]

## Alternative Solution
# features = [tuple(measurements) for *measurements,_ in data]
# features_train = features[:pivot]
# features_test = features[pivot:]
#
# labels = [species for *_,species in data]
# labels_train = labels[:pivot]
# labels_test = labels[pivot:]
