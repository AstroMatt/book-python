FILE = r'/tmp/_temporary.txt'
DATA = [
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor')]

result = []

for row in DATA:
    line = ','.join(str(x) for x in row) + '\n'
    result.append(line)

with open(FILE, mode='wt') as file:
    file.writelines(result)
