"""
* Assignment: File Write CSV
* Filename: file_write_csv.py
* Complexity: medium
* Lines of code to write: 6 lines
* Estimated time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Separate header from data
    3. Write data to file: `FILE`
    4. First line in file must be a header (first line of `DATA`)
    5. For each row, convert it's values to `str`
    6. Use coma (`,`) as a value separator
    7. Add line terminator (`\n`) to each row
    8. Save row values to file

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Odseparuj nagłówek od danych
    3. Zapisz dane do pliku: `FILE`
    4. Pierwsza linia w pliku musi być nagłówkiem (pierwsza linia `DATA`)
    5. Dla każdego wiersza przekonwertuj jego wartości do `str`
    6. Użyj przecinka (`,`) jako separatora wartości
    7. Użyj `\n` jako koniec linii w każdym wierszu
    8. Zapisz do pliku wartości z wiersza

Hints:
    * `[str(x) for x in ...]`

Tests:
    >>> open(FILE).read()
    'Sepal length,Sepal width,Petal length,Petal width,Species\\n5.8,2.7,5.1,1.9,virginica\\n5.1,3.5,1.4,0.2,setosa\\n5.7,2.8,4.1,1.3,versicolor\\n6.3,2.9,5.6,1.8,virginica\\n6.4,3.2,4.5,1.5,versicolor\\n4.7,3.2,1.3,0.2,setosa\\n'
"""

# Given
FILE = r'/tmp/_temporary.csv'
DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa')]

# Solution
header, *data = DATA
header = ','.join(header) + '\n'
data = [','.join(map(str, row))+'\n' for row in data]

with open(FILE, mode='w') as file:
    file.write(header)
    file.writelines(data)
