"""
>>> assert type(result) is list
>>> assert all(type(x) is float for x in result)
>>> result
[3.9, 2.5, 3.5, 4.1, 3.9, 2.4]
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


class Stats:
    def mean(self, data):
        mean = sum(data) / len(data)
        return round(mean, 1)


stats = Stats()

# Solution 1
result = [stats.mean(X) for *X,y in DATA[1:]]

# Solution 2
# result = []
# for *features, label in DATA[1:]:
#     result.append(stats.mean(features))

