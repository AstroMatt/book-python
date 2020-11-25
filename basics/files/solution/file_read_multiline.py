"""
* Assignment: File Read Multiline
* Filename: file_read_multiline.py
* Complexity: easy
* Lines of code to write: 3 lines
* Estimated time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Write `DATA` to file `FILE`
    3. Read `FILE` to `result: list[str]`
    4. Print `result`
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zapisz `DATA` do pliku `FILE`
    3. Wczytaj `FILE` do `result: list[str]`
    4. Wypisz `result`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> assert type(result) is list
    >>> assert all(type(x) is str for x in result)
    >>> result
    ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
"""

# Given
FILE = r'/tmp/_temporary.txt'
DATA = 'sepal_length\nsepal_width\npetal_length\npetal_width\nspecies\n'

with open(FILE, mode='wt') as file:
    file.write(DATA)

# Solution
with open(FILE, mode='rt') as file:
    result = [x.strip() for x in file.readlines()]

