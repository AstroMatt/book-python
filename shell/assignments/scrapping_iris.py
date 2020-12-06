from pprint import pprint
from bs4 import BeautifulSoup
import requests


URL = 'https://github.com/AstroMatt/book-python/blob/master/numerical-analysis/data/iris-dirty.csv'
HEADER = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
result = list()


with open('/tmp/iris-dirty.html', mode='rw') as file:
    response = requests.get(URL)
    file.write(response.text)

with open('/tmp/iris-dirty.html', mode='r') as file:
    html = BeautifulSoup(file, 'lxml')


table = html.find_all('table')[0]

table_rows = table.find_all('tr')
table_header = table_rows[0]
table_body = table_rows[1:]

species = table_header.text.split()[2:]

for cell in table_body:
    values = cell.text.split()
    values = dict(zip(HEADER, values))
    species_id = int(values['Species'])
    values['Species'] = species[species_id]
    result.append(values)

pprint(result)
