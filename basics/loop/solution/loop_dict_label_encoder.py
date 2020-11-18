"""
>>> assert type(features) is list
>>> assert type(labels) is list
>>> assert type(label_encoder) is dict

>>> assert all(type(x) is tuple for x in features)
>>> assert all(type(x) is int for x in labels)
>>> assert all(type(x) is int for x in label_encoder.keys())
>>> assert all(type(x) is str for x in label_encoder.values())

>>> features  # doctest: +NORMALIZE_WHITESPACE
[(5.8, 2.7, 5.1, 1.9),
 (5.1, 3.5, 1.4, 0.2),
 (5.7, 2.8, 4.1, 1.3),
 (6.3, 2.9, 5.6, 1.8),
 (6.4, 3.2, 4.5, 1.5),
 (4.7, 3.2, 1.3, 0.2)]

>>> labels
[0, 1, 2, 0, 2, 1]

>>> label_encoder  # doctest: +NORMALIZE_WHITESPACE
{0: 'virginica',
 1: 'setosa',
 2: 'versicolor'}
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

features = []
labels = []
label_encoder = {}
lookup = {}

header, *data = DATA
i = 0

for *X,y in data:
    if y not in lookup:
        label_encoder[i] = y
        lookup[y] = i
        i += 1

    labels.append(lookup[y])
    features.append(tuple(X))


print(features)
print(labels)
print(label_encoder)


## Alternative solution
# s = set(x[-1] for x in DATA[1:])
# label_encoder = dict(zip(s, range(0, len(s))))

## Alternative solution
# In numerical analysis you can find this
# label_encoder = dict(enumerate(set(x[-1] for x in DATA[1:])))
