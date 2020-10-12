"""
>>> assert type(result) is list
>>> assert all(type(row) is dict for row in result)
>>> result  # doctest: +NORMALIZE_WHITESPACE
[{'ip': '127.0.0.1', 'hosts': ['localhost', 'astromatt'], 'protocol': 'ipv4'},
 {'ip': '10.13.37.1', 'hosts': ['nasa.gov', 'esa.int', 'roscosmos.ru'], 'protocol': 'ipv4'},
 {'ip': '255.255.255.255', 'hosts': ['broadcasthost'], 'protocol': 'ipv4'},
 {'ip': '::1', 'hosts': ['localhost'], 'protocol': 'ipv6'}]
"""

DATA = """
##
# ``/etc/hosts`` structure:
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

for line in DATA.splitlines():
    line = line.strip()

    if len(line) == 0:
        continue

    if line.startswith('#'):
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

print(result)
