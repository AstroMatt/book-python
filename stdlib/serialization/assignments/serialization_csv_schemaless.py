from csv import DictWriter, QUOTE_ALL

FILE = r'/tmp/_temporary.csv'
DATA = [{'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
        {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
        {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
        {'Sepal length': 5.0, 'Petal width': 0.2, 'Species': 'setosa'},
        {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
        {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'}]

fieldnames = set()

for row in DATA:
    fieldnames.update(row.keys())

# fieldnames == {'Sepal length', 'Sepal width', 'Petal length', 'Species', 'Petal width'}

with open(FILE, mode='w') as file:
    result = DictWriter(
        f=file,
        fieldnames=sorted(fieldnames),
        delimiter=',',
        quotechar='"',
        quoting=QUOTE_ALL,
        lineterminator='\n')

    result.writeheader()
    result.writerows(DATA)
