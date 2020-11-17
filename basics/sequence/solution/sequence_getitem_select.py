"""
>>> assert type(header) is tuple
>>> assert type(result) is list
>>> header
('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species')
>>> result  # doctest: +NORMALIZE_WHITESPACE
[[5.1, 3.5, 1.4, 0.2, 'setosa'],
 (6.3, 2.9, 5.6, 1.8, 'virginica'),
 {1.3, 2.8, 4.1, 5.7, 'versicolor'},
 frozenset({1.5, 3.2, 4.5, 6.4, 'versicolor'}),
 [],
 (),
 set(),
 frozenset()]
"""

DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

header = DATA[0]
result = []

result.append(list(DATA[2]))
result.append(tuple(DATA[4]))
result.append(set(DATA[-4]))
result.append(frozenset(DATA[-2]))

result.append(list())
result.append(tuple())
result.append(set())
result.append(frozenset())

