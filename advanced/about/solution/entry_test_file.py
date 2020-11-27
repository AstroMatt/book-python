"""
* Assignment: Entry Test File
* Filename: entry_test_file.py
* Complexity: hard
* Lines of code to write: 15 lines
* Estimated time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Skip comments (`#`) and empty lines
    3. Extract from each line: ip, host and protocol and add to `result: list[dict]`
    4. Each line must be a separate dict
    5. Merge host names with the same IP
    6. IPv4 protocol address is when dot (`.`) is in ip address
    7. `result` must be list of dicts (`list[dict]`)
    8. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Pomiń komentarze (`#`) i puste linie
    3. Wyciągnij z każdej linii: ip, host i protokół i dodaj do `result: list[dict]`
    4. Każda linia ma być osobnym słownikiem
    5. Protokół IPv4 jest gdy kropka (`.`) znajduje się w adresie
    6. Scal nazwy hostów dla tego samego IP
    7. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> assert type(result) is list
    >>> assert all(type(row) is dict for row in result)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'ip': '127.0.0.1', 'hosts': ['localhost', 'astromatt'], 'protocol': 'ipv4'},
     {'ip': '10.13.37.1', 'hosts': ['nasa.gov', 'esa.int', 'roscosmos.ru'], 'protocol': 'ipv4'},
     {'ip': '255.255.255.255', 'hosts': ['broadcasthost'], 'protocol': 'ipv4'},
     {'ip': '::1', 'hosts': ['localhost'], 'protocol': 'ipv6'}]
"""

# Given
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

result = []

# Solution
for line in DATA.splitlines():
    line = line.strip()

    if len(line) == 0:
        continue
    elif line.startswith('#'):
        continue

    ip, *hosts = line.split()

    for row in result:
        if row['ip'] == ip:
            row['hosts'] += hosts
            break
    else:
        result.append({
            'ip': ip,
            'hosts': hosts,
            'protocol': 'ipv4' if '.' in ip else 'ipv6'
        })
