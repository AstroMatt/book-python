"""
* Assignment: Loop Dict To List
* Filename: loop_dict_to_list.py
* Complexity: medium
* Lines of code: 4 lines
* Estimated time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Print `list[dict]`:
        a. key - name from the header
        b. value - measurement or species
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wypisz `list[dict]`:
        a. klucz: nazwa z nagłówka
        b. wartość: wyniki pomiarów lub gatunek
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'list'>
    >>> assert all(type(x) is dict for x in result)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'Sepal length': 5.8, 'Sepal width': 2.7, 'Petal length': 5.1, 'Petal width': 1.9, 'Species': 'virginica'},
     {'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
     {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
     {'Sepal length': 6.3, 'Sepal width': 2.9, 'Petal length': 5.6, 'Petal width': 1.8, 'Species': 'virginica'},
     {'Sepal length': 6.4, 'Sepal width': 3.2, 'Petal length': 4.5, 'Petal width': 1.5, 'Species': 'versicolor'},
     {'Sepal length': 4.7, 'Sepal width': 3.2, 'Petal length': 1.3, 'Petal width': 0.2, 'Species': 'setosa'}]
"""

# Given
DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa')]

result: list = []

# Solution
header, *data = DATA

for values in data:
    pair = zip(header, values)
    result.append(dict(pair))
