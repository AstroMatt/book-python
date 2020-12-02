def average(args):
    if all(isinstance(x, float) for x in args):
        return sum(args) / len(args)


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
values = {}


for row in data:
    for i, _ in enumerate(header):
        key = header[i]
        value = row[i]

        if key in values:
            values[key] += [value]
        else:
            values[key] = [value]


## Alternative version
# header, *data = DATA
# values = {name: list() for name in header}
#
# for row in data:
#     for i, name in enumerate(values):
#         values[name].append(row[i])


for name, measurements in values.items():
    print(f'Name: {name}, avg: {average(measurements)}')
