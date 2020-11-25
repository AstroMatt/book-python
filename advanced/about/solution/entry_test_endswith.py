"""
* Assignment: Loop Unpacking Endswith
* Filename: loop_unpacking_endswith.py
* Complexity: medium
* Lines of code to write: 4 lines
* Estimated time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Define `result: set[str]`
    3. Iterating over data unpack row to `*features` and `label`
    4. Append to `result` species with endings in `suffixes`
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj `result: set[str]`
    3. Iterując po danych rozpakuj wiersz do `*features` oraz `label`
    4. Dodaj do `result` nazwy gatunków z końcówkami w `suffixes`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'set'>
    >>> 'virginica' in result
    True
    >>> 'setosa' in result
    True
    >>> 'versicolor' in result
    False
"""

# Given
DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, {'virginica'}),
    (5.1, 3.5, 1.4, 0.2, {'setosa'}),
    (5.7, 2.8, 4.1, 1.3, {'versicolor'}),
    (6.3, 2.9, 5.6, 1.8, {'virginica'}),
    (6.4, 3.2, 4.5, 1.5, {'versicolor'}),
    (4.7, 3.2, 1.3, 0.2, {'setosa'}),
    (7.0, 3.2, 4.7, 1.4, {'versicolor'}),
    (7.6, 3.0, 6.6, 2.1, {'virginica'}),
    (4.6, 3.1, 1.5, 0.2, {'setosa'}),
]

result: set = set()
suffixes = ('ca', 'osa')

# Solution
for *features, label in DATA[1:]:
    species = label.pop()

    if species.endswith(suffixes):
        result.add(species)
