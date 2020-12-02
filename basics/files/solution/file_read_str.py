"""
* Assignment: File Read Str
* Filename: file_read_str.py
* Complexity: easy
* Lines of code: 2 lines
* Estimated time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Write `DATA` to file `FILE`
    3. Read `FILE` to `result: str`
    4. Print `result`
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zapisz `DATA` do pliku `FILE`
    3. Wczytaj `FILE` do `result: str`
    4. Wypisz `result`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> assert type(result) is str
    >>> result
    'hello'
"""

# Given
FILE = r'/tmp/_temporary.txt'
DATA = 'hello'

with open(FILE, mode='wt') as file:
    file.write(DATA)

# Solution
with open(FILE, mode='rt') as file:
    result = file.read()
