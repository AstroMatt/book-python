FILE = r'/tmp/_temporary.txt'
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

with open(FILE, mode='w') as file:
    file.write(DATA)

try:
    with open(FILE) as file:
        hosts_file = file.readlines()

except FileNotFoundError:
    print('File does not exist')

except PermissionError:
    print('Permission denied')


for line in hosts_file:
    line = line.strip()

    if line == '' or line.startswith('#'):
        continue

    ip, *hostnames = line.split()
    found = False

    for host in result:
        if host['ip'] == ip:
            host['hostnames'].update(hostnames)
            found = True
            break

    if not found:
        result.append({
            'ip': ip,
            'hostnames': set(hostnames),
            'protocol': 'IPv4' if '.' in ip else 'IPv6'
        })

print(result)
# [{'ip': '127.0.0.1', 'hostnames': {'astromatt', 'localhost'}, 'protocol': 'IPv4'},
#  {'ip': '10.13.37.1', 'hostnames': {'nasa.gov', 'esa.int', 'roscosmos.ru'}, 'protocol': 'IPv4'},
#  {'ip': '255.255.255.255', 'hostnames': {'broadcasthost'}, 'protocol': 'IPv4'},
#  {'ip': '::1', 'hostnames': {'localhost'}, 'protocol': 'IPv6'}]


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

