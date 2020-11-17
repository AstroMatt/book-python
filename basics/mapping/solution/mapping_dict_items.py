"""
>>> assert type(keys) is list
>>> assert type(values) is list
>>> assert type(items) is list
>>> assert all(type(x) is tuple for x in items)

>>> keys
['Sepal length', 'Sepal width', 'Petal length', 'Petal width']
>>> values
[5.8, 2.7, 5.1, 1.9]
>>> items  # doctest: +NORMALIZE_WHITESPACE
[('Sepal length', 5.8),
 ('Sepal width', 2.7),
 ('Petal length', 5.1),
 ('Petal width', 1.9)]
"""

DATA = {
    'Sepal length': 5.8,
    'Sepal width': 2.7,
    'Petal length': 5.1,
    'Petal width': 1.9,
}

keys = list(DATA.keys())
values = list(DATA.values())
items = list(DATA.items())

