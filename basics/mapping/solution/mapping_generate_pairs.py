"""
* Assignment: Mapping Generate Pairs
* Filename: mapping_generate_pairs.py
* Complexity: easy
* Lines of code to write: 1 lines
* Estimated time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Create `result: dict`
    3. Convert `DATA` to `dict` and assign to `result`
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz `result: dict`
    3. Przekonwertuj `DATA` do `dict` i przypisz do `result`
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'Sepal length': 5.8,
     'Sepal width': 2.7,
     'Petal length': 5.1,
     'Petal width': 1.9,
     'Species': 'virginica'}
"""

# Given
DATA = [
    ('Sepal length', 5.8),
    ('Sepal width', 2.7),
    ('Petal length', 5.1),
    ('Petal width', 1.9),
    ('Species', 'virginica')
]

# Solution
result = dict(DATA)

