"""
* Assignment: Serialization CSV DictWriter
* Filename: serialization_csv_dictwriter.py
* Complexity: easy
* Lines of code: 5 lines
* Time: 7 min

English:
    #. Use data from "Given" section (see below)
    #. Using `csv.DictWriter()` save `DATA` to file
    #. Open file in your spreadsheet program like Microsoft Excel / Libre Office / Numbers etc.
    #. Open file in simple in your IDE and simple text editor (like Notepad, vim, gedit)
    #. Compare result with "Tests" section (see below)
    #. Non functional requirements:
        * All fields must be enclosed by double quote `"` character
        * Use `,` to separate columns
        * Use `utf-8` encoding
        * Use Unix `\n` newline

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Za pomocą `csv.DictWriter()` zapisz `DATA` do pliku
    #. Spróbuj otworzyć plik w arkuszu kalkulacyjnym tj. Microsoft Excel / Libre Office / Numbers itp
    #. Spróbuj otworzyć plik w IDE i prostym edytorze tekstu tj. Notepad, vim lub gedit
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)
    #. Wymagania niefunkcjonalne:
        * Wszystkie pola muszą być otoczone znakiem cudzysłowu `"`
        * Użyj `,` do oddzielenia kolumn
        * Użyj kodowania `utf-8`
        * Użyj zakończenia linii Unix `\n`
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
