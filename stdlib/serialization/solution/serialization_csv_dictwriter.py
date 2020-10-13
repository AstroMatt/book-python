from csv import DictWriter, QUOTE_ALL


FILE = r'/tmp/_temporary.csv'
DATA = [
    {'firstname': 'Jan', 'lastname': 'Twardowski'},
    {'firstname': 'José', 'lastname': 'Jiménez'},
    {'firstname': 'Mark', 'lastname': 'Watney'},
    {'firstname': 'Ivan', 'lastname': 'Ivanovic'},
    {'firstname': 'Melissa', 'lastname': 'Lewis'},
]


with open(FILE, mode='w', encoding='utf-8') as file:
    result = DictWriter(
        f=file,
        fieldnames=['firstname', 'lastname'],
        delimiter=',',
        quotechar='"',
        quoting=QUOTE_ALL,
        lineterminator='\n')

    result.writeheader()
    result.writerows(DATA)
