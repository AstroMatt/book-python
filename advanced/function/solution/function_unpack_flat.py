"""
>>> ip
'10.13.37.1'
>>> hosts
['nasa.gov', 'esa.int', 'roscosmos.ru']
"""

DATA = '10.13.37.1      nasa.gov esa.int roscosmos.ru'

ip, *hosts = DATA.split()
