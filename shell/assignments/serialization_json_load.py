import json
from pprint import pprint

FILE = r'_temporary.json'
result = list()


with open(FILE) as file:
    DATA = json.load(file)


## Naive Solution
header = tuple(DATA[0].keys())
result.append(header)

for row in DATA:
    measurements = row.values()
    result.append(tuple(measurements))

pprint(result)


## Proper solution
header = set()
result = list()

for row in DATA:
    header.update(row.keys())


result.append(header)

for row in DATA:
    result.append(tuple(
        row.get(head, None)
            for head in header
    ))

print(result)
