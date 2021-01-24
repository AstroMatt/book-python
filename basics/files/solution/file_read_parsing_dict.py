FILE = r'/tmp/hosts-simple.txt'
DATA = """
127.0.0.1       localhost
127.0.0.1       astromatt
10.13.37.1      nasa.gov esa.int roscosmos.ru
255.255.255.255 broadcasthost
::1             localhost
"""

result = {}

with open(FILE, mode='w') as file:
    file.write(DATA)

with open(FILE) as file:
    for line in file:
        if line.isspace():
            continue

        ip, *hosts = line.strip().split()

        if ip in result:
            result[ip] += hosts
        else:
            result[ip] = hosts


print(result)
# {'127.0.0.1': ['localhost', 'astromatt'],
#  '10.13.37.1': ['nasa.gov', 'esa.int', 'roscosmos.ru'],
#  '255.255.255.255': ['broadcasthost'],
#  '::1': ['localhost']}
