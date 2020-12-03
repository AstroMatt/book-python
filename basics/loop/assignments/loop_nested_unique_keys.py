"""
* Assignment: Loop Nested Unique Keys
* Filename: loop_nested_unique_keys.py
* Complexity: medium
* Lines of code: 3 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Collect keys from all rows in one sequence `result`
    3. Sort `result`
    4. Print unique keys
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zbierz klucze z wszystkich wierszy w jednej sekwencji `result`
    3. Posortuj `result`
    4. Wypisz unikalne klucze
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `row.keys()`
    * Compare solutions with :ref:`Micro-benchmarking use case`

Tests:
    >>> result is not Ellipsis
    True
    >>> type(result) in (set, list, tuple, frozenset)
    True
    >>> sorted(result)
    ['Petal length', 'Petal width', 'Sepal length', 'Sepal width', 'Species']
"""

# Given
DATA = [{'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
        {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
        {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
        {'Sepal length': 5.0, 'Petal width': 0.2, 'Species': 'setosa'},
        {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
        {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'}]

result = ...

# Solution
result = set()

for row in DATA:
    result.update(row.keys())
