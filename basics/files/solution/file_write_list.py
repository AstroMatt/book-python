FILE = r'/tmp/_temporary.txt'
DATA = ['hello', 'world']
result = '\n'.join(DATA) + '\n'

with open(FILE, mode='wt') as file:
    file.write(result)
