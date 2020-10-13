FILE = r'/tmp/_temporary.txt'
DATA = """
127.0.0.1       localhost
10.13.37.1      nasa.gov esa.int roscosmos.ru
255.255.255.255 broadcasthost
::1             localhost
"""

with open(FILE, mode='wt') as file:
    file.write(DATA)
