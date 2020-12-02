import csv

FILE = r'/tmp/_temporary.txt'


class Iris:
    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species


DATA = [Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
        Iris(5.8, 2.7, 5.1, 1.9, 'virginica'),
        Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
        Iris(5.7, 2.8, 4.1, 1.3, 'versicolor'),
        Iris(6.3, 2.9, 5.6, 1.8, 'virginica'),
        Iris(6.4, 3.2, 4.5, 1.5, 'versicolor')]

data = [row.__dict__ for row in DATA]
header = list(data[0].keys())

with open(FILE, mode='w', encoding='utf-8') as file:
    result = csv.DictWriter(file, fieldnames=header, delimiter=',', quotechar='"')
    result.writeheader()
    result.writerows(data)
