"""
>>> mean(1)
1.0
>>> mean(1, 3)
2.0
>>> mean(1, 2, 3)
2.0
>>> mean()
Traceback (most recent call last):
    ...
ValueError: At least one argument is required

>>> result
... # doctest: +NORMALIZE_WHITESPACE
[('virginica', 3.875),
 ('setosa', 2.65),
 ('versicolor', 3.475),
 ('virginica', 6.0),
 ('versicolor', 3.95),
 ('setosa', 4.7)]
"""


def mean(*args):
    if not args:
        raise ValueError('At least one argument is required')

    return sum(args) / len(args)


DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 5.7, 'virginica'),
    (6.4, 1.5, 'versicolor'),
    (4.7,  'setosa'),
]

header, *data = DATA

result = [(label, mean(*features))
          for *features, label in data]
