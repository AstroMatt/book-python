"""
* Assignment: File Read CSV
* Filename: file_read_csv.py
* Complexity: easy
* Lines of code: 15 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Write `DATA` to file `FILE`
    3. Read `FILE`
    4. Separate header from data
    5. Write header (first line) to `header`
    6. Read file and for each line:
        a. Strip whitespaces
        b. Split line by coma `,`
        c. Convert measurements do `tuple[float]`
        d. Append measurements to `features`
        e. Append species name to `labels`
    7. Print `header`, `features` and `labels`
    8. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zapisz `DATA` do pliku `FILE`
    3. Wczytaj `FILE`
    4. Odseparuj nagłówek od danych
    5. Zapisz nagłówek (pierwsza linia) do `header`
    6. Zaczytaj plik i dla każdej linii:
        a. Usuń białe znaki z początku i końca linii
        b. Podziel linię po przecinku `,`
        c. Przekonwertuj pomiary do `tuple[float]`
        d. Dodaj pomiary do `features`
        e. Dodaj gatunek do `labels`
    7. Wyświetl `header`, `features` i `labels`
    8. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

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
    >>> labels
    ['setosa', 'virginica', 'versicolor', 'virginica', 'versicolor', 'setosa']
    >>> from os import remove
    >>> remove(FILE)
"""

# Given
FILE = r'_temporary.csv'

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
        labels.append(y)
