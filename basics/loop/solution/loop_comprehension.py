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


RATIO = 0.6

header, *data = DATA
pivot = int(len(data) * RATIO)

features = [tuple(measurements) for *measurements,_ in data]
features_train = features[:pivot]
features_test = features[pivot:]

labels = [species for *_,species in data]
labels_train = labels[:pivot]
labels_test = labels[pivot:]

output = features_train, features_test, labels_train, labels_test
print(output)




## Alternative solution
## not optimized (4 loops)
# features_train = [X for *X,y in data[:pivot]]
# features_test = [X for *X,y in data[pivot:]]
# labels_train = [y for *X,y in data[:pivot]]
# labels_test = [y for *X,y in data[pivot:]]
# output = features_train, features_test, labels_train, labels_test
# print(output)


## Alternative solution
## not optimized (4 loops)
# output = (
#     [X for *X,y in data[:pivot]],
#     [X for *X,y in data[pivot:]],
#     [y for *X,y in data[:pivot]],
#     [y for *X,y in data[pivot:]],
# )
# print(output)


## Alternative solution
## not optimized (4 loops)
# print(
#     [X for *X,y in data[:pivot]],
#     [X for *X,y in data[pivot:]],
#     [y for *X,y in data[:pivot]],
#     [y for *X,y in data[pivot:]],
# )
