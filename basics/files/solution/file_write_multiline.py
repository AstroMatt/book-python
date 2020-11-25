"""
* Assignment: File Write Multiline
* Filename: file_write_multiline.py
* Complexity: easy
* Lines of code to write: 3 lines
* Estimated time: 3 min

English:
    #. Use data from "Given" section (see below)
    #. Write `DATA` to file `FILE`
    #. Check in your operating system if data was written correctly
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Zapisz `DATA` do pliku `FILE`
    #. Sprawdź w systemie operacyjnym czy dane zapisały się poprawnie
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> open(FILE).read()
    '127.0.0.1       localhost\\n10.13.37.1      nasa.gov esa.int roscosmos.ru\\n255.255.255.255 broadcasthost\\n::1             localhost\\n'
"""

# Given
FILE = r'/tmp/_temporary.txt'
DATA = """127.0.0.1       localhost
10.13.37.1      nasa.gov esa.int roscosmos.ru
255.255.255.255 broadcasthost
::1             localhost
"""

# Solution
with open(FILE, mode='wt') as file:
    file.write(DATA)
