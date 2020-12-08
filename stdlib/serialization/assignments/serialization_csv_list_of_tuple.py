"""
* Assignment: Serialization CSV List of Tuples
* Filename: serialization_csv_list_of_tuple.py
* Complexity: easy
* Lines of code: 6 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Convert `DATA` to `list[dict]`
    3. Using `csv.DictWriter()` save `DATA` to file
    4. Non functional requirements:
        a. Do not use quotes in output CSV file
        b. Use `,` to separate columns
        c. Use `utf-8` encoding
        d. Use Unix `\n` newline
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Przekonwertuj `DATA` do `list[dict]`
    3. Za pomocą `csv.DictWriter()` zapisz `DATA` do pliku
    4. Wymagania niefunkcjonalne:
        a. Nie używaj cudzysłowów w wynikowym pliku CSV
        b. Użyj `,` do oddzielenia kolumn
        c. Użyj kodowania `utf-8`
        d. Użyj zakończenia linii Unix `\n`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> result = open(FILE).read()
    >>> print(result)
    Sepal length,Sepal width,Petal length,Petal width,Species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor
    6.3,2.9,5.6,1.8,virginica
    6.4,3.2,4.5,1.5,versicolor
    4.7,3.2,1.3,0.2,setosa
    7.0,3.2,4.7,1.4,versicolor
    7.6,3.0,6.6,2.1,virginica
    4.9,3.0,1.4,0.2,setosa
    <BLANKLINE>
    >>> from os import remove
    >>> remove(FILE)
"""

# Given
import csv

FILE = r'_temporary.csv'
DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),]


# Solution
header, *data = DATA
data = [dict(zip(header, row)) for row in data]

with open(FILE, mode='w', encoding='utf-8') as file:
    result = csv.DictWriter(file, fieldnames=header, delimiter=',', quotechar='"')
    result.writeheader()
    result.writerows(data)
