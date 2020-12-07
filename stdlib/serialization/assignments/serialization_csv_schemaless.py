"""
* Assignment: Serialization CSV Schemaless
* Filename: serialization_csv_schemaless.py
* Complexity: medium
* Lines of code: 7 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Using `csv.DictWriter()` write variable schema data to CSV file
    3. `fieldnames` must be automatically generated from `DATA`
    4. `fieldnames` must always be in the same order
    5. Non functional requirements:
        a. All fields must be enclosed by double quote `"` character
        b. Use `;` to separate columns
        c. Use `utf-8` encoding
        d. Use Unix `\n` newline
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Za pomocą `csv.DictWriter()` zapisz do pliku CSV dane o zmiennej strukturze
    3. `fieldnames` musi być generowane automatycznie na podstawie `DATA`
    4. `fieldnames` ma być zawsze w takiej samej kolejności
    5. Wymagania niefunkcjonalne:
        a. Wszystkie pola muszą być otoczone znakiem cudzysłowu `"`
        b. Użyj `,` do oddzielenia kolumn
        c. Użyj kodowania `utf-8`
        d. Użyj zakończenia linii Unix `\n`
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> result = open(FILE).read()
    >>> print(result)
    "Petal length","Petal width","Sepal length","Sepal width","Species"
    "","","5.1","3.5","setosa"
    "4.1","1.3","","","versicolor"
    "","1.8","6.3","","virginica"
    "","0.2","5.0","","setosa"
    "4.1","","","2.8","versicolor"
    "","1.8","","2.9","virginica"
    <BLANKLINE>
    >>> from os import remove
    >>> remove(FILE)
"""


# Given
from csv import DictWriter, QUOTE_ALL

FILE = r'_temporary.csv'
DATA = [{'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
        {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
        {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
        {'Sepal length': 5.0, 'Petal width': 0.2, 'Species': 'setosa'},
        {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
        {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'}]


# Solution
fieldnames = set()

for row in DATA:
    fieldnames.update(row.keys())

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
