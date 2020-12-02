from typing import List, Tuple, Dict


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
    (7.1, 3.0, 5.9, 2.1, 'virginica'),
    (4.6, 3.4, 1.4, 0.3, 'setosa'),
    (5.4, 3.9, 1.7, 0.4, 'setosa'),
    (5.7, 2.8, 4.5, 1.3, 'versicolor'),
    (5.0, 3.6, 1.4, 0.3, 'setosa'),
    (5.5, 2.3, 4.0, 1.3, 'versicolor'),
    (6.5, 3.0, 5.8, 2.2, 'virginica'),
    (6.5, 2.8, 4.6, 1.5, 'versicolor'),
    (6.3, 3.3, 6.0, 2.5, 'virginica'),
    (6.9, 3.1, 4.9, 1.5, 'versicolor'),
    (4.6, 3.1, 1.5, 0.2, 'setosa'),
]


header = DATA[0]
data = DATA[1:]

features: List[Tuple[float]] = []
labels: List[int] = []

label_encoder: Dict[int, str] = {}


for row in data:
    measurements = row[0:4]
    species = row[4]
    features.append(tuple(measurements))

    if species not in label_encoder.values():
        number = len(label_encoder)
        label_encoder[number] = species

    for number, name in label_encoder.items():
        if name == species:
            labels.append(number)


print(features)
print()
print(labels)
print()
print(label_encoder)


## Alternative Version
# header, *data = DATA
#
# features = []
# labels = []
# species = {}
#
# for *measurements, kind in data:
#     if kind not in species:
#         species[kind] = len(species)
#
#     features.append(tuple(measurements))
#     labels.append(species[kind])
#
# species = {v:k for k,v in species.items()}
#
# print(features)
# print(labels)
# print(species)

## Alternative Version
# s = set(x[-1] for x in DATA[1:])
# label_encoder = dict(zip(s, range(0, len(s))))


## Alternative Version
# In numerical analysis you can find this
# label_encoder = dict(enumerate(set(x[-1] for x in DATA[1:])))


## Alternative Version
# label_encoder = dict(zip(label_encoder.values(), label_encoder.keys()))
