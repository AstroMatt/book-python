"""
>>> assert type(ip) is str
>>> assert type(hosts) is list
>>> assert all(type(host) is str for host in hosts)

>>> ip
'10.13.37.1'
>>> hosts
['nasa.gov', 'esa.int', 'roscosmos.ru']
"""

DATA = '10.13.37.1      nasa.gov esa.int roscosmos.ru'

ip, *hosts = DATA.split()

print(ip)
print(hosts)
