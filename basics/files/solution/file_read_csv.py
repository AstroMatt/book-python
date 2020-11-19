"""
>>> header
['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
>>> features  # doctest: +NORMALIZE_WHITESPACE
[(5.4, 3.9, 1.3, 0.4),
 (5.9, 3.0, 5.1, 1.8),
 (6.0, 3.4, 4.5, 1.6),
 (7.3, 2.9, 6.3, 1.8),
 (5.6, 2.5, 3.9, 1.1),
 (5.4, 3.9, 1.3, 0.4)]
>>> label
['setosa', 'virginica', 'versicolor', 'virginica', 'versicolor', 'setosa']
"""

FILE = r'/tmp/_temporary.csv'
DATA = """sepal_length,sepal_width,petal_length,petal_width,species
5.4,3.9,1.3,0.4,setosa
5.9,3.0,5.1,1.8,virginica
6.0,3.4,4.5,1.6,versicolor
7.3,2.9,6.3,1.8,virginica
5.6,2.5,3.9,1.1,versicolor
5.4,3.9,1.3,0.4,setosa
"""

features = []
label = []

with open(FILE, mode='w') as file:
    file.write(DATA)

with open(FILE) as file:
    header = file.readline().strip().split(',')

    for line in file:
        *X,y = line.strip().split(',')
        X = [float(x) for x in X]
        # X = map(float, X)

        features.append(tuple(X))
        label.append(y)
