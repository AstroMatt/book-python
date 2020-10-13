FILE = r'/tmp/_temporary.txt'
DATA = (5.1, 3.5, 1.4, 0.2, 'setosa')
result = ','.join(str(x) for x in DATA) + '\n'

with open(FILE, mode='wt') as file:
    file.write(result)
