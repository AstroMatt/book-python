"""
* Assignment: Serialization CSV DictReader
* Filename: :download:`assignments/serialization_csv_dictreader.py`
* Complexity: easy
* Lines of code: 9 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Using `csv.DictReader` read the `FILE` content
    3. Use explicit `encoding`, `delimiter` and `quotechar`
    4. Replace column names to `FIELDNAMES`
    5. Skip the first line (header)
    6. Print rows with data
    7. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Korzystając z `csv.DictReader` wczytaj zawartość pliku `FILE`
    3. Podaj jawnie `encoding`, `delimiter` oraz `quotechar`
    4. Podmień nazwy kolumn na `FIELDNAMES`
    5. Pomiń pierwszą linię (nagłówek)
    6. Wypisz wiersze z danymi
    7. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'list'>
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'Sepal Length': '5.8', 'Sepal Width': '2.7', 'Petal Length': '5.1', 'Petal Width': '1.9', 'Species': 'virginica'},
     {'Sepal Length': '5.1', 'Sepal Width': '3.5', 'Petal Length': '1.4', 'Petal Width': '0.2', 'Species': 'setosa'},
     {'Sepal Length': '5.7', 'Sepal Width': '2.8', 'Petal Length': '4.1', 'Petal Width': '1.3', 'Species': 'versicolor'}]
    >>> from os import remove
    >>> remove(FILE)
"""

# Given
from csv import DictReader, QUOTE_NONE


FILE = r'_temporary.csv'
FIELDNAMES = ['Sepal Length', 'Sepal Width',
              'Petal Length', 'Petal Width', 'Species']

DATA = """sepal_length,sepal_width,petal_length,petal_width,species
5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor"""

with open(FILE, mode='w') as file:
    file.write(DATA)


result = []

# Solution
with open(FILE) as file:
    header = file.readline()
    data = DictReader(
        f=file,
        fieldnames=FIELDNAMES,
        delimiter=',',
        quoting=QUOTE_NONE)

    for row in data:
        result.append(row)
