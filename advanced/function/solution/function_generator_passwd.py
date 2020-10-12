"""
>>> from inspect import isfunction, isgeneratorfunction
>>> assert isfunction(function)
>>> assert isgeneratorfunction(generator)

>>> list(function(DATA))
['root', 'bin', 'daemon', 'adm', 'shutdown', 'halt', 'nobody', 'sshd']
>>> list(generator(DATA))
['root', 'bin', 'daemon', 'adm', 'shutdown', 'halt', 'nobody', 'sshd']

>>> result
{'function': 120, 'generator': 112}
"""

from sys import getsizeof


DATA = """root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
nobody:x:99:99:Nobody:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash
jimenez:x:1001:1001:José Jiménez:/home/jimenez:/bin/bash
ivanovic:x:1002:1002:Иван Иванович:/home/ivanovic:/bin/bash
lewis:x:1003:1002:Melissa Lewis:/home/ivanovic:/bin/bash"""


def function(data):
    result = []
    for line in data.splitlines():
        username, _, uid, *_ = line.split(':')
        if int(uid) < 1000:
            result.append(username)
    return result


def generator(data):
    for line in data.splitlines():
        username, _, uid, *_ = line.split(':')
        if int(uid) < 1000:
            yield username


result = {
    'function': getsizeof(function(DATA)),
    'generator': getsizeof(generator(DATA)),
}
