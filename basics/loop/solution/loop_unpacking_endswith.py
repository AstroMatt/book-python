DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, {'virginica'}),
    (5.1, 3.5, 1.4, 0.2, {'setosa'}),
    (5.7, 2.8, 4.1, 1.3, {'versicolor'}),
    (6.3, 2.9, 5.6, 1.8, {'virginica'}),
    (6.4, 3.2, 4.5, 1.5, {'versicolor'}),
    (4.7, 3.2, 1.3, 0.2, {'setosa'}),
    (7.0, 3.2, 4.7, 1.4, {'versicolor'}),
    (7.6, 3.0, 6.6, 2.1, {'virginica'}),
    (4.6, 3.1, 1.5, 0.2, {'setosa'}),
]

header, *data = DATA
suffixes = ('osa', 'ca')

# Solution 1
for *X,y in data:
    species = y.pop()

    if species.endswith(suffixes):
        print(species)


# Solution 2
for row in data:
    species = row[4].pop()

    if species.endswith('ca') or species.endswith('sa'):
        print(species)


# Solution 3
for *_, species in data:
    species = species.pop()

    if species.endswith('ca') or species.endswith('sa'):
        print(species)


# Solution 4
for *features, label in data:
    species = label.pop()

    if any(species.endswith(x) for x in suffixes):
        print(species)


# Solution 5
result = [species
          for *X,y in data
          if (species := y.pop())
          and species.endswith(suffixes)]
print(result)

