"""
* Assignment: File Read Dict
* Filename: file_read_dict.py
* Complexity: medium
* Lines of code to write: 10 lines
* Estimated time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Write `DATA` to file `FILE`
    3. Read `FILE` and for each line:
        a. Remove leading and trailing whitespaces
        b. Skip line if it is empty
        c. Split line by whitespace
        d. Separate IP address and hosts names
        e. Append IP address and hosts names to `result`
    4. Merge hostnames for the same IP
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zapisz `DATA` do pliku `FILE`
    3. Wczytaj `FILE` i dla każdej linii:
        a. Usuń białe znaki na początku i końcu linii
        b. Pomiń linię, jeżeli jest pusta
        c. Podziel linię po białych znakach
        d. Odseparuj adres IP i nazwy hostów
        e. Dodaj adres IP i nazwy hostów do `result`
    4. Scal nazwy hostów dla tego samego IP
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `str.isspace()`
    * `str.split()`

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'127.0.0.1': ['localhost'],
     '10.13.37.1': ['nasa.gov', 'esa.int', 'roscosmos.ru'],
     '255.255.255.255': ['broadcasthost'],
     '::1': ['localhost']}
"""

# Given
FILE = r'/tmp/_temporary.txt'

DATA = """127.0.0.1       localhost
10.13.37.1      nasa.gov esa.int roscosmos.ru
255.255.255.255 broadcasthost
::1             localhost
"""

with open(FILE, mode='w') as file:
    file.write(DATA)


result = {}

# Solution
with open(FILE) as file:
    for line in file:
        ip, *hosts = line.strip().split()

        if ip in result:
            result[ip] += hosts
        else:
            result[ip] = hosts
