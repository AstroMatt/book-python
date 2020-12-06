from csv import DictReader, QUOTE_NONE


FILE = r'_temporary.csv'

FIELDNAMES = [
    'Sepal Length',
    'Sepal Width',
    'Petal Length',
    'Petal Width',
    'Species',
]

with open(FILE) as file:
    header = file.readline()

    result = DictReader(
        f=file,
        fieldnames=FIELDNAMES,
        delimiter=',',
        quoting=QUOTE_NONE)

    for row in result:
        print(row)
