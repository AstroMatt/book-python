"""
* Assignment: Serialization CSV Objects
* Filename: serialization_csv_objects.py
* Complexity: medium
* Lines of code: 7 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Using `csv.DictWriter()` save data to CSV file
    3. Non functional requirements:
        a. All fields must be enclosed by double quote `"` character
        b. Use `,` to separate columns
        c. Use `utf-8` encoding
        d. Use Unix `\n` newline

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Za pomocą `csv.DictWriter()` zapisz dane do pliku CSV
    3. Wymagania niefunkcjonalne:
        a. Wszystkie pola muszą być otoczone znakiem cudzysłowu `"`
        b. Użyj `,` do oddzielenia kolumn
        c. Użyj kodowania `utf-8`
        d. Użyj zakończenia linii Unix `\n`

Tests:
    >>> result = open(FILE).read()
    >>> print(result)
    sepal_length,sepal_width,petal_length,petal_width,species
    5.1,3.5,1.4,0.2,setosa
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor
    6.3,2.9,5.6,1.8,virginica
    6.4,3.2,4.5,1.5,versicolor
    <BLANKLINE>
    >>> from os import remove
    >>> remove(FILE)
"""


# Given
import csv


class Iris:
    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species


FILE = r'_temporary.txt'

DATA = [Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
        Iris(5.8, 2.7, 5.1, 1.9, 'virginica'),
        Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
        Iris(5.7, 2.8, 4.1, 1.3, 'versicolor'),
        Iris(6.3, 2.9, 5.6, 1.8, 'virginica'),
        Iris(6.4, 3.2, 4.5, 1.5, 'versicolor')]


# Result
data = [row.__dict__ for row in DATA]
header = list(data[0].keys())

with open(FILE, mode='w', encoding='utf-8') as file:
    result = csv.DictWriter(file, fieldnames=header, delimiter=',', quotechar='"')
    result.writeheader()
    result.writerows(data)
