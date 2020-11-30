"""

* Assignment: Function Generator Passwd
* Filename: function_generator_passwd.py
* Complexity: medium
* Lines of code to write: 10 lines
* Estimated time: 13 min

English:
    1. Use code from "Input" section (see below)
    2. Split `DATA` by lines and then by colon `:`
    3. Extract system accounts (users with UID [third field] is less than 1000)
    4. Return list of system account logins
    5. Implement solution using function
    6. Implement solution using generator and `yield` keyword
    7. Compare results of both using `sys.getsizeof()`
    8. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Podziel `DATA` po liniach a następnie po dwukropku `:`
    3. Wyciągnij konta systemowe (użytkownicy z UID (trzecie pole) mniejszym niż 1000)
    4. Zwróć listę loginów użytkowników systemowych
    5. Zaimplementuj rozwiązanie wykorzystując funkcję
    6. Zaimplementuj rozwiązanie wykorzystując generator i słowo kluczowe `yield`
    7. Porównaj wyniki obu używając `sys.getsizeof()`
    8. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from sys import getsizeof
    >>> from inspect import isfunction, isgeneratorfunction
    >>> assert isfunction(function)
    >>> assert isgeneratorfunction(generator)
    >>> fun = function(DATA)
    >>> gen = generator(DATA)
    >>> list(fun)
    ['root', 'bin', 'daemon', 'adm', 'shutdown', 'halt', 'nobody', 'sshd']
    >>> list(gen)
    ['root', 'bin', 'daemon', 'adm', 'shutdown', 'halt', 'nobody', 'sshd']
    >>> getsizeof(fun)
    120
    >>> getsizeof(gen)
    112
"""

# Given
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


def function(data: str):
    ...


def generator(data: str):
    ...


# Solution
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

