"""
* Assignment: Loop Nested Mean
* Filename: loop_nested_mean.py
* Complexity: easy
* Lines of code: 5 lines
* Estimated time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Calculate mean `Sepal length` value
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wylicz średnią wartość `Sepal length`
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> result is not Ellipsis
    True
    >>> type(result)
    <class 'float'>
    >>> result
    5.911111111111111
"""

# Given
DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
        (4.6, 3.1, 1.5, 0.2, 'setosa')]

result: float = ...

# Solution
sepal_length = []

for row in DATA[1:]:
    sepal_length.append(row[0])

result = sum(sepal_length) / len(sepal_length)
