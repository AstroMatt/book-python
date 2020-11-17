"""
>>> result  # doctest: +NORMALIZE_WHITESPACE
{'Sepal length': 5.8,
 'Sepal width': 2.7,
 'Petal length': 5.1,
 'Petal width': 1.9,
 'Species': 'virginica'}
"""

KEYS = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
VALUES = [5.8, 2.7, 5.1, 1.9, 'virginica']

result = dict(zip(KEYS, VALUES))

