"""
* Assignment: File Read List of Dicts
* Filename: file_read_listdict.py
* Complexity: hard
* Lines of code to write: 15 lines
* Estimated time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Define `result: list[dict]`
    3. Using `file.write()` save input data from listing below to file `hosts-advanced.txt`
    4. Read file and for each line:
        a. Skip line if it's empty, is whitespace or starts with comment `#`
        b. Remove leading and trailing whitespaces
        c. Split line by whitespace
        d. Separate IP address and hosts names
        e. Use one line `if` to check whether dot `.` is in the IP address
        f. If is present then protocol is IPv4 otherwise IPv6
        g. Append IP address and hosts names to `result`
    5. Merge hostnames for the same IP
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj `result: list[dict]`
    3. Używając `file.write()` zapisz dane wejściowe z listingu poniżej do pliku `hosts-advanced.txt`
    4. Przeczytaj plik i dla każdej linii:
        a. Pomiń linię jeżeli jest pusta, jest białym znakiem lub zaczyna się od komentarza `#`
        b. Usuń białe znaki na początku i końcu linii
        c. Podziel linię po białych znakach
        d. Odseparuj adres IP i nazwy hostów
        e. Wykorzystaj jednolinikowego `if` do sprawdzenia czy jest kropka `.` w adresie IP
        f. Jeżeli jest obecna to protokół  jest IPv4, w przeciwnym przypadku IPv6
        g. Dodaj adres IP i nazwy hostów do `result`
    5. Scal nazwy hostów dla tego samego IP
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `str.split()`
    * `str.isspace()`
    * `value = True if ... else False`

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'ip': '127.0.0.1', 'hostnames': ['localhost', ['astromatt']], 'protocol': 'IPv4'},
     {'ip': '10.13.37.1', 'hostnames': ['nasa.gov', 'esa.int', 'roscosmos.ru'], 'protocol': 'IPv4'},
     {'ip': '255.255.255.255', 'hostnames': ['broadcasthost'], 'protocol': 'IPv4'},
     {'ip': '::1', 'hostnames': ['localhost'], 'protocol': 'IPv6'}]
"""

# Given
FILE = r'/tmp/_temporary.txt'

DATA = """
##
# `/etc/hosts` structure:
#   - IPv4 or IPv6
#   - Hostnames
 ##

127.0.0.1       localhost
127.0.0.1       astromatt
10.13.37.1      nasa.gov esa.int roscosmos.ru
255.255.255.255 broadcasthost
::1             localhost
"""

with open(FILE, mode='w') as file:
    file.write(DATA)


result = []

# Solution
try:
    with open(FILE) as file:
        hosts_file = file.readlines()
except FileNotFoundError:
    print('File does not exist')
except PermissionError:
    print('Permission denied')


for line in hosts_file:
    line = line.strip()

    if len(line) == 0 or line.startswith('#'):
        continue

    ip, *hostnames = line.split()
    found = False

    for host in result:
        if host['ip'] == ip:
            host['hostnames'].append(hostnames)
            found = True
            break

    if not found:
        result.append({
            'ip': ip,
            'hostnames': list(hostnames),
            'protocol': 'IPv4' if '.' in ip else 'IPv6'
        })


## Alternative solution
# for record in result:
#     if record['ip'] == ip:
#         record['hostnames'].update(hostnames)
#         break
# else:
#     result.append({
#         'hostnames': set(hostnames),
#         'protocol': 'IPv4' if '.' in ip else 'IPv6',
#         'ip': ip,
#     })

