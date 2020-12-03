"""
* Assignment: File Write Iris
* Filename: file_write_iris.py
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Write `DATA` to file `FILE`
    3. Check in your operating system if data was written correctly
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zapisz `DATA` do pliku `FILE`
    3. Sprawdź w systemie operacyjnym czy dane zapisały się poprawnie
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> open(FILE).read()
    '5.8,2.7,5.1,1.9,virginica\\n5.1,3.5,1.4,0.2,setosa\\n5.7,2.8,4.1,1.3,versicolor\\n'
"""

# Given
FILE = r'/tmp/_temporary.txt'
DATA = [(5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor')]

# Solution
result = []

for row in DATA:
    line = ','.join(str(x) for x in row) + '\n'
    result.append(line)

with open(FILE, mode='wt') as file:
    file.writelines(result)
