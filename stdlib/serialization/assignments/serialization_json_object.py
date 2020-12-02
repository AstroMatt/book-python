import json
from dataclasses import dataclass
from pprint import pprint

FILE = r'/tmp/_temporary.json'

@dataclass
class Iris:
    sepalLength: float
    sepalWidth: float
    petalLength: float
    petalWidth: float


class Setosa(Iris):
    pass


class Virginica(Iris):
    pass


class Versicolor(Iris):
    pass


with open(FILE, encoding='utf-8') as file:
    data = json.load(file)


result = []

for iris in data:
    species = iris.pop('species')

    if species == 'setosa':
        cls = Setosa
    elif species == 'versicolor':
        cls = Versicolor
    elif species == 'virginica':
        cls = Virginica
    else:
        print('Not supported')

    result.append(cls(**iris))

pprint(result)
