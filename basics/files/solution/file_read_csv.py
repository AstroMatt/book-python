"""
* Assignment: File Read CSV
* Filename: file_read_csv.py
* Complexity: easy
* Lines of code to write: 15 lines
* Estimated time: 8 min

English:
    #. Use data from "Given" section (see below)
    #. Write `DATA` to file `FILE`
    #. Read `FILE`
    #. Separate header from data
    #. Write header (first line) to `header`
    #. Read file and for each line:

        * Strip whitespaces
        * Split line by coma `,`
        * Convert measurements do `tuple[float]`
        * Append measurements to `features`
        * Append species name to `labels`

    #. Print `header`, `features` and `labels`
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Zapisz `DATA` do pliku `FILE`
    #. Wczytaj `FILE`
    #. Odseparuj nagłówek od danych
    #. Zapisz nagłówek (pierwsza linia) do `header`
    #. Zaczytaj plik i dla każdej linii:

        * Usuń białe znaki z początku i końca linii
        * Podziel linię po przecinku `,`
        * Przekonwertuj pomiary do `tuple[float]`
        * Dodaj pomiary do `features`
        * Dodaj gatunek do `labels`

    #. Wyświetl `header`, `features` i `labels`
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `tuple(float(x) for x in X)`

Tests:
    >>> header
    ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    >>> features  # doctest: +NORMALIZE_WHITESPACE
    [(5.4, 3.9, 1.3, 0.4),
     (5.9, 3.0, 5.1, 1.8),
     (6.0, 3.4, 4.5, 1.6),
     (7.3, 2.9, 6.3, 1.8),
     (5.6, 2.5, 3.9, 1.1),
     (5.4, 3.9, 1.3, 0.4)]
    >>> label
    ['setosa', 'virginica', 'versicolor', 'virginica', 'versicolor', 'setosa']
"""

# Given
FILE = r'/tmp/_temporary.csv'

DATA = """sepal_length,sepal_width,petal_length,petal_width,species
5.4,3.9,1.3,0.4,setosa
5.9,3.0,5.1,1.8,virginica
6.0,3.4,4.5,1.6,versicolor
7.3,2.9,6.3,1.8,virginica
5.6,2.5,3.9,1.1,versicolor
5.4,3.9,1.3,0.4,setosa
"""

header = []
features = []
labels = []

with open(FILE, mode='w') as file:
    file.write(DATA)

# Solution
with open(FILE) as file:
    header = file.readline().strip().split(',')

    for line in file:
        *X,y = line.strip().split(',')
        X = [float(x) for x in X]
        # X = map(float, X)

        features.append(tuple(X))
        label.append(y)
