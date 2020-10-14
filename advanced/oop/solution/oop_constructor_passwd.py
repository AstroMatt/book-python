"""
>>> result  # doctest: +NORMALIZE_WHITESPACE
[SystemAccount(username='root'),
 SystemAccount(username='bin'),
 SystemAccount(username='daemon'),
 SystemAccount(username='adm'),
 SystemAccount(username='shutdown'),
 SystemAccount(username='halt'),
 SystemAccount(username='nobody'),
 SystemAccount(username='sshd'),
 UserAccount(username='twardowski'),
 UserAccount(username='jimenez'),
 UserAccount(username='ivanovic'),
 UserAccount(username='lewis')]
"""
from dataclasses import dataclass

DATA = """root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
nobody:x:99:99:Nobody:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
twardowski:x:1000:1000:Jan Twardowski:/home/twardowski:/bin/bash
jimenez:x:1001:1001:José Jiménez:/home/jimenez:/bin/bash
ivanovic:x:1002:1002:Иван Иванович:/home/ivanovic:/bin/bash
lewis:x:1002:1002:Melissa Lewis:/home/lewis:/bin/bash"""


class Account:
    def __new__(cls, username: str, uid: int):
        if int(uid) >= 1000:
            return UserAccount(username)
        else:
            return SystemAccount(username)


@dataclass
class SystemAccount:
    username: str


@dataclass
class UserAccount:
    username: str


result = [Account(username, uid)
          for line in DATA.splitlines()
          if (fields := line.strip().split(':'))
          and (username := fields[0])
          and (uid := fields[2])]

# result = []
# for line in DATA.splitlines():
#     username, _, uid, *_ = line.strip().split(':')
#     result.append(Account(username, uid))
