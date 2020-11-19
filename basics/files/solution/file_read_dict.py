"""
>>> result  # doctest: +NORMALIZE_WHITESPACE
{'127.0.0.1': ['localhost'],
 '10.13.37.1': ['nasa.gov', 'esa.int', 'roscosmos.ru'],
 '255.255.255.255': ['broadcasthost'],
 '::1': ['localhost']}
"""

FILE = r'/tmp/_temporary.txt'
DATA = """127.0.0.1       localhost
10.13.37.1      nasa.gov esa.int roscosmos.ru
255.255.255.255 broadcasthost
::1             localhost
"""

result = {}

with open(FILE, mode='w') as file:
    file.write(DATA)

with open(FILE) as file:
    for line in file:
        ip, *hosts = line.strip().split()

        if ip in result:
            result[ip] += hosts
        else:
            result[ip] = hosts
