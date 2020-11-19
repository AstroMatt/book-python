"""
>>> assert type(features_train) is list
>>> assert type(features_test) is list
>>> assert type(labels_train) is list
>>> assert type(labels_test) is list

>>> assert all(type(x) is tuple for x in features_train)
>>> assert all(type(x) is tuple for x in features_test)
>>> assert all(type(x) is str for x in labels_train)
>>> assert all(type(x) is str for x in labels_test)

>>> features_train  # doctest: +NORMALIZE_WHITESPACE
[(5.8, 2.7, 5.1, 1.9),
 (5.1, 3.5, 1.4, 0.2),
 (5.7, 2.8, 4.1, 1.3),
 (6.3, 2.9, 5.6, 1.8),
 (6.4, 3.2, 4.5, 1.5),
 (4.7, 3.2, 1.3, 0.2)]

>>> features_test  # doctest: +NORMALIZE_WHITESPACE
[(7.0, 3.2, 4.7, 1.4),
 (7.6, 3.0, 6.6, 2.1),
 (4.9, 3.0, 1.4, 0.2),
 (4.9, 2.5, 4.5, 1.7)]

>>> labels_train
['virginica', 'setosa', 'versicolor', 'virginica', 'versicolor', 'setosa']

>>> labels_test
['versicolor', 'virginica', 'setosa', 'virginica']
"""

DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
]


RATIO = 0.6
header, *data = DATA
pivot = int(len(data) * RATIO)

features = [tuple(measurements) for *measurements,_ in data]
features_train = features[:pivot]
features_test = features[pivot:]

labels = [species for *_,species in data]
labels_train = labels[:pivot]
labels_test = labels[pivot:]


## Alternative solution
# features_train = [X for *X,y in data[:pivot]]
# features_test = [X for *X,y in data[pivot:]]
# labels_train = [y for *X,y in data[:pivot]]
# labels_test = [y for *X,y in data[pivot:]]
