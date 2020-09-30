FILE = r'../data/etc-hosts.txt'
result = []


with open(FILE) as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        if line.startswith('#'):
            continue

        ip, *hosts = line.split()

        for record in result:
            if record['ip'] == ip:
                record['hostnames'].update(hosts)
                break
        else:
            result.append({
                'hostnames': set(hosts),
                'protocol': 'IPv4' if '.' in ip else 'IPv6',
                'ip': ip,
            })

print(result)

## Alternative solution
# found = False
#
# for x in hosts:
#     if result['ip'] == ip:
#         found = True
#         result['hostnames'].update(hosts)
#
# if not found:
#     result.append({
#         'ip': ip,
#         'hostnames': set(hostnames),
#         'protocol': 'IPv4' if '.' in ip else 'IPv6'
#     })
#
