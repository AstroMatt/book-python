"""
* Assignment: Serialization CSV DictWriter
* Filename: serialization_csv_dictwriter.py
* Complexity: easy
* Lines of code: 5 lines
* Time: 7 min

English:
    1. Use data from "Given" section (see below)
    2. Using `csv.DictWriter()` save `DATA` to file
    3. Open file in your spreadsheet program like Microsoft Excel / Libre Office / Numbers etc.
    4. Open file in simple in your IDE and simple text editor (like Notepad, vim, gedit)
    5. Non functional requirements:
        a. All fields must be enclosed by double quote `"` character
        b. Use `,` to separate columns
        c. Use `utf-8` encoding
        d. Use Unix `\n` newline
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Za pomocą `csv.DictWriter()` zapisz `DATA` do pliku
    3. Spróbuj otworzyć plik w arkuszu kalkulacyjnym tj. Microsoft Excel / Libre Office / Numbers itp
    4. Spróbuj otworzyć plik w IDE i prostym edytorze tekstu tj. Notepad, vim lub gedit
    5. Wymagania niefunkcjonalne:
        a. Wszystkie pola muszą być otoczone znakiem cudzysłowu `"`
        b. Użyj `,` do oddzielenia kolumn
        c. Użyj kodowania `utf-8`
        d. Użyj zakończenia linii Unix `\n`
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> open(FILE).read()
    "firstname","lastname"
    "Jan","Twardowski"
    "José","Jiménez"
    "Mark","Watney"
    "Ivan","Ivanovic"
    "Melissa","Lewis"
    >>> from os import remove
    >>> remove(FILE)
"""

from csv import DictWriter, QUOTE_ALL


FILE = r'_temporary.csv'
DATA = [{'firstname': 'Jan', 'lastname': 'Twardowski'},
        {'firstname': 'José', 'lastname': 'Jiménez'},
        {'firstname': 'Mark', 'lastname': 'Watney'},
        {'firstname': 'Ivan', 'lastname': 'Ivanovic'},
        {'firstname': 'Melissa', 'lastname': 'Lewis'}]


with open(FILE, mode='w', encoding='utf-8') as file:
    writer = DictWriter(
        f=file,
        fieldnames=['firstname', 'lastname'],
        delimiter=',',
        quotechar='"',
        quoting=QUOTE_ALL,
        lineterminator='\n')

    writer.writeheader()
    writer.writerows(DATA)
