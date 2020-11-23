"""
* Assignment: Function Unpack Nested
* Filename: sequence_unpack_nested.py
* Complexity: easy
* Lines of code to write: 1 lines
* Estimated time of completion: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Separate header and records
    3. Use asterisk ``*`` notation
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Odseparuj nagłówek od danych
    3. Skorzystaj z konstrukcji z gwiazdką ``*``
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(header)
    <class 'tuple'>
    >>> type(data)
    <class 'list'>
    >>> assert all(type(x) is str for x in header)
    >>> assert all(type(row) is tuple for row in data)
    >>> header
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species')
    >>> data  # doctest: +NORMALIZE_WHITESPACE
    [(5.8, 2.7, 5.1, 1.9, 'virginica'),
     (5.1, 3.5, 1.4, 0.2, 'setosa'),
     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
     (6.3, 2.9, 5.6, 1.8, 'virginica'),
     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
     (4.7, 3.2, 1.3, 0.2, 'setosa')]
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

# Solution
header, *data = DATA
