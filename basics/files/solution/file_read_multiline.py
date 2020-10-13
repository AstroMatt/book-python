FILE = r'/tmp/_temporary.txt'
DATA = 'sepal_length\nsepal_width\npetal_length\npetal_width\nspecies\n'

with open(FILE, mode='wt') as file:
    file.write(DATA)

with open(FILE, mode='rt') as file:
    result = [x.strip() for x in file.readlines()]

print(result)
