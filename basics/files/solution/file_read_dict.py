"""
* Assignment: File Read Dict
* Filename: file_read_dict.py
* Complexity: medium
* Lines of code to write: 10 lines
* Estimated time: 8 min

English:
    #. Use data from "Given" section (see below)
    #. Write `DATA` to file `FILE`
    #. Read `FILE` and for each line:

        * Remove leading and trailing whitespaces
        * Skip line if it is empty
        * Split line by whitespace
        * Separate IP address and hosts names
        * Append IP address and hosts names to `result`

    #. Merge hostnames for the same IP
    #. Compare result with "Tests" section (see below)

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Zapisz `DATA` do pliku `FILE`
    #. Wczytaj `FILE` i dla każdej linii:

        * Usuń białe znaki na początku i końcu linii
        * Pomiń linię, jeżeli jest pusta
        * Podziel linię po białych znakach
        * Odseparuj adres IP i nazwy hostów
        * Dodaj adres IP i nazwy hostów do `result`

    #. Scal nazwy hostów dla tego samego IP
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

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
