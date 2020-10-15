*********
IPv4/IPv6
*********


IP
==

IPv4
----
* ``socket.AF_INET``

.. figure:: img/tcp-ipv4-packet.png
    :width: 75%
    :align: center

    IPv4 packet

IPv6
----
* ``socket.AF_INET6``

.. figure:: img/tcp-ipv6-packet.png
    :width: 75%
    :align: center

    IPv6 packet


``ipaddress``
=============
* In stdlib since Python 3.3

IP Addresses
------------
.. code-block:: python

    import ipaddress

    ipaddress.ip_address('192.168.0.1')
    # IPv4Address('192.168.0.1')

    ipaddress.ip_address('2001:db8::')
    # IPv6Address('2001:db8::')

.. code-block:: python

    import ipaddress

    ipaddress.IPv4Address('192.168.0.1')
    # IPv4Address('192.168.0.1')

    ipaddress.IPv4Address(3232235521)
    # IPv4Address('192.168.0.1')

    ipaddress.IPv4Address(b'\xC0\xA8\x00\x01')
    # IPv4Address('192.168.0.1')

Comparision
^^^^^^^^^^^
.. code-block:: python

    IPv4Address('127.0.0.2') > IPv4Address('127.0.0.1')
    # True

    IPv4Address('127.0.0.2') == IPv4Address('127.0.0.1')
    # False

    IPv4Address('127.0.0.2') != IPv4Address('127.0.0.1')
    # True

.. code-block:: python

    IPv4Address('127.0.0.2') + 3
    # IPv4Address('127.0.0.5')

    IPv4Address('127.0.0.2') - 3
    # IPv4Address('126.255.255.255')

    IPv4Address('255.255.255.255') + 1
    # Traceback (most recent call last):
    #     ...
    # ipaddress.AddressValueError: 4294967296 (>= 2**32) is not permitted as an IPv4 address

The name of the reverse DNS PTR record for the IP address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    ipaddress.ip_address("127.0.0.1").reverse_pointer
    # '1.0.0.127.in-addr.arpa'

    ipaddress.ip_address("2001:db8::1").reverse_pointer
    # '1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa'

IP Network
----------
.. code-block:: python

    import ipaddress

    ipaddress.ip_network('192.168.0.0/28')
    # IPv4Network('192.168.0.0/28')

.. code-block:: python

    list(ip_network('192.0.2.0/29').hosts())  #doctest: +NORMALIZE_WHITESPACE
    # [IPv4Address('192.0.2.1'), IPv4Address('192.0.2.2'),
    #  IPv4Address('192.0.2.3'), IPv4Address('192.0.2.4'),
    #  IPv4Address('192.0.2.5'), IPv4Address('192.0.2.6')]

    list(ip_network('192.0.2.0/31').hosts())
    # [IPv4Address('192.0.2.0'), IPv4Address('192.0.2.1')]

.. code-block:: python

    n1 = ip_network('192.0.2.0/28')
    n2 = ip_network('192.0.2.1/32')

    list(n1.address_exclude(n2))
    # [IPv4Network('192.0.2.8/29'), IPv4Network('192.0.2.4/30'),
    #  IPv4Network('192.0.2.2/31'), IPv4Network('192.0.2.0/32')]

Subnet
^^^^^^
.. code-block:: python

    list(ip_network('192.0.2.0/24').subnets())
    # [IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/25')]

    list(ip_network('192.0.2.0/24').subnets(prefixlen_diff=2))
    # [
    #   IPv4Network('192.0.2.0/26'),
    #   IPv4Network('192.0.2.64/26'),
    #   IPv4Network('192.0.2.128/26'),
    #   IPv4Network('192.0.2.192/26')
    # ]

    list(ip_network('192.0.2.0/24').subnets(new_prefix=26))
    # [
    #   IPv4Network('192.0.2.0/26'),
    #   IPv4Network('192.0.2.64/26'),
    #   IPv4Network('192.0.2.128/26'),
    #   IPv4Network('192.0.2.192/26')
    # ]

    list(ip_network('192.0.2.0/24').subnets(new_prefix=23))
    # Traceback (most recent call last):
    #     ...
    # ValueError: new prefix must be longer

    list(ip_network('192.0.2.0/24').subnets(new_prefix=25))
    # [
    #    IPv4Network('192.0.2.0/25'),
    #    IPv4Network('192.0.2.128/25')
    # ]

Supernet
^^^^^^^^
.. code-block:: python

    ip_network('192.0.2.0/24').supernet()
    # IPv4Network('192.0.2.0/23')

    ip_network('192.0.2.0/24').supernet(prefixlen_diff=2)
    # IPv4Network('192.0.0.0/22')

    ip_network('192.0.2.0/24').supernet(new_prefix=20)
    # IPv4Network('192.0.0.0/20')

Comparision
^^^^^^^^^^^
.. code-block:: python

    a = ip_network('192.168.1.0/24')
    b = ip_network('192.168.1.128/30')
    b.subnet_of(a)
    # True

.. code-block:: python

    ip_network('192.0.2.1/32').compare_networks(ip_network('192.0.2.2/32'))
    # -1

    ip_network('192.0.2.1/32').compare_networks(ip_network('192.0.2.0/32'))
    # 1

    ip_network('192.0.2.1/32').compare_networks(ip_network('192.0.2.1/32'))
    # 0

Iteration
^^^^^^^^^
.. code-block:: python

    for addr in IPv4Network('192.0.2.0/28'):
         addr

    # IPv4Address('192.0.2.0')
    # IPv4Address('192.0.2.1')
    # IPv4Address('192.0.2.2')
    # IPv4Address('192.0.2.3')
    # IPv4Address('192.0.2.4')
    # IPv4Address('192.0.2.5')
    # IPv4Address('192.0.2.6')
    # IPv4Address('192.0.2.7')
    # IPv4Address('192.0.2.8')
    # IPv4Address('192.0.2.9')
    # IPv4Address('192.0.2.10')
    # IPv4Address('192.0.2.11')
    # IPv4Address('192.0.2.12')
    # IPv4Address('192.0.2.13')
    # IPv4Address('192.0.2.14')
    # IPv4Address('192.0.2.15')

.. code-block:: python

    IPv4Network('192.0.2.0/28')[0]
    # IPv4Address('192.0.2.0')

    IPv4Network('192.0.2.0/28')[15]
    # IPv4Address('192.0.2.15')

    IPv4Address('192.0.2.6') in IPv4Network('192.0.2.0/28')
    # True

    IPv4Address('192.0.3.6') in IPv4Network('192.0.2.0/28')
    # False

Interface
---------
* ``ipaddress.IPv4Interface``
* ``ipaddress.IPv6Interface``

.. code-block:: python

    interface = IPv4Interface('192.0.2.5/24')
    interface.ip
    # IPv4Address('192.0.2.5')

.. code-block:: python

    interface = IPv4Interface('192.0.2.5/24')
    interface.network
    # IPv4Network('192.0.2.0/24')

.. code-block:: python

    interface = IPv4Interface('192.0.2.5/24')
    interface.with_prefixlen
    # '192.0.2.5/24'

.. code-block:: python

    interface = IPv4Interface('192.0.2.5/24')
    interface.with_netmask
    # '192.0.2.5/255.255.255.0'

.. code-block:: python

    interface = IPv4Interface('192.0.2.5/24')
    interface.with_hostmask
    # '192.0.2.5/0.0.0.255'


``netaddr``
===========
* 3rd party
* https://yamakira.github.io/python-network-programming/libraries/netaddr/index.html

Installation
------------
.. code-block:: console

    $ pip install netaddr

Layer 3 addressing (IP)
-----------------------
.. code-block:: python

    from netaddr import IPAddress

    ip = IPAddress('192.21.8.11')

    ip.version
    # 4

    dir(ip)
    # [ ... Snipped... 'bin', 'bits', 'format', 'info', 'ipv4', 'ipv6',
    # 'is_hostmask', 'is_ipv4_compat', 'is_ipv4_mapped', 'is_link_local',
    # 'is_loopback', 'is_multicast', 'is_netmask', 'is_private', 'is_reserved',
    # 'is_unicast', 'key', 'netmask_bits', 'packed', 'reverse_dns', 'sort_key',
    # 'value', 'version', 'words']

.. code-block:: python

    ip.bin
    # '0b11000000000101010000100000001011'

    ip.bits()
    # '11000000.00010101.00001000.00001011'

    ip.words
    # (192, 21, 8, 11)

    ip.packed
    # '\xc0\x15\x08\x0b'

.. code-block:: python

    ip.version
    # 6

    ip.is_unicast()
    # True

    ip.is_link_local()
    # True

IPNetwork
---------
.. code-block:: python

    from netaddr import IPNetwork

    ip_range = IPNetwork('192.241.21.6/24')

    dir(ip_range)
    # [ ... snipped ...  'broadcast', 'cidr', 'first', 'hostmask', 'info',
    # 'ip', 'ipv4', 'ipv6', 'is_ipv4_compat', 'is_ipv4_mapped', 'is_link_local',
    # 'is_loopback', 'is_multicast', 'is_private', 'is_reserved', 'is_unicast',
    # 'iter_hosts', 'key', 'last', 'netmask', 'network', 'next', 'prefixlen',
    # 'previous', 'size', 'sort_key', 'subnet', 'supernet', 'value', 'version']

.. code-block:: python

    ip_range.network
    # IPAddress('192.241.21.0')

    ip_range.hostmask
    # IPAddress('0.0.0.255')

    ip_range.netmask
    # IPAddress('255.255.255.0')

    ip_range.broadcast
    # IPAddress('192.241.21.255')

    ip_range.size
    # 256

.. code-block:: python

    for i in ip_range:
         print(i)

    # 192.241.21.0
    # 192.241.21.1
    # ... snipped ...
    # 192.241.21.255

List operations on IPNetwork object
-----------------------------------
.. code-block:: python

    ip_range = IPNetwork('192.0.2.16/29')

    ip_range_list = list(ip_range)

    len(ip_range_list)
    # 8

    ip_range_list
    # [IPAddress('192.0.2.16'), IPAddress('192.0.2.17'), ...snipped... IPAddress('192.0.2.23')]

    ip_range_list[6]        # indexing
    # IPAddress('192.0.2.22')

    ip_range_list[2:5]      # slicing
    # [IPAddress('192.0.2.18'), IPAddress('192.0.2.19'), IPAddress('192.0.2.20')]

IPRange
-------
.. code-block:: python

    ip_range = IPRange('192.168.1.0', '192.168.1.20')

    for i in ip_range:
         print(i)

    # 192.168.1.0
    # ... snipped ...
    # 192.168.1.19
    # 192.168.1.20

IP sets
-------
.. code-block:: python

    IPSet(['192.0.2.0'])
    # IPSet(['192.0.2.0/32'])

    IPSet([IPAddress('192.0.2.0')])
    # IPSet(['192.0.2.0/32'])

    IPSet([IPNetwork('192.0.2.0/24')])
    # IPSet(['192.0.2.0/24'])

    IPSet(IPRange("10.0.0.0", "10.0.1.31"))
    # IPSet(['10.0.0.0/24', '10.0.1.0/27'])

.. code-block:: python

    for ip in IPSet(['192.0.2.0/28']):
         print(ip)

    # 192.0.2.0
    # 192.0.2.1
    # ... snipped ...
    # 192.168.2.15

Adding and removing set elements
--------------------------------
.. code-block:: python

    from netaddr import IPSet

    s1 = IPSet()

    s1.add('192.168.1.0/30')
    s1.size
    # 4

    '192.168.1.3' in s1
    # True

    s1.remove('192.168.1.3')
    s1.size
    # 3

.. code-block:: python

    scan1 = IPSet(['192.168.1.0/30'])

    scan1
    # IPSet(['192.168.1.0/30'])

    scan1.size
    # 4

    scan2 = IPSet(['192.168.1.0/31'])

    scan2.size
    # 2

    scan1 | scan2
    # IPSet(['192.168.1.0/30'])

    scan1 & scan2
    # IPSet(['192.168.1.0/31'])

    scan1 ^ scan2
    # IPSet(['192.168.1.2/31'])

Layer 2 addressing (MAC)
------------------------
.. code-block:: python

    mac = EUI('ec:f4:bb:87:2d:0c')

    dir(mac)
    # ... snipped ... 'bin', 'bits', 'dialect', 'ei', 'eui64', 'iab',
    # 'info', 'ipv6', 'ipv6_link_local', 'is_iab', 'modified_eui64', 'oui',
    # 'packed', 'value', 'version', 'words']

    str(mac), str(mac.ei), str(mac.oui), str(mac.version)
    # ('EC-F4-BB-87-2D-0C', '87-2D-0C', 'EC-F4-BB', '48')

.. code-block:: python

    mac.info
    # {'OUI': {'address': ['one dell way',
    #              'MS:RR5-45',
    #              'Round rock Texas 78682',
    #              'UNITED STATES'],
    #  'idx': 15529147,
    #  'offset': 3429092,
    #  'org': 'Dell Inc',
    #  'oui': 'EC-F4-BB',
    #  'size': 141}}

.. code-block:: python

    oui = mac.oui

    dir(oui)
    # [ ... snipped ... 'records', 'reg_count', 'registration']

    oui.registration().org
    # 'Dell Inc'

    oui.registration().address
    # ['one dell way', 'MS:RR5-45', 'Round rock Texas 78682', 'UNITED STATES']
