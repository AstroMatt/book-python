"""
* Assignment: Unpacking Assignment Flat
* Filename: unpacking_assignment_flat.py
* Complexity: easy
* Lines of code: 1 lines
* Estimated time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Using `str.split()` split input data by white space
    3. Separate ip address and host names
    4. Use asterisk `*` notation
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Używając `str.split()` podziel dane wejściowe po białych znakach
    3. Odseparuj adres ip i nazw hostów
    4. Skorzystaj z notacji z gwiazdką `*`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * Use `str.split()` without any argument

Tests:
    >>> type(ip)
    <class 'str'>
    >>> type(hosts)
    <class 'list'>
    >>> assert all(type(host) is str for host in hosts)
    >>> '' not in hosts
    True
    >>> ip
    '10.13.37.1'
    >>> hosts
    ['nasa.gov', 'esa.int', 'roscosmos.ru']
"""

# Given
DATA = '10.13.37.1      nasa.gov esa.int roscosmos.ru'

ip: str
hosts: list

# Solution
ip, *hosts = DATA.split()
