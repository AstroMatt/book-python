"""
* Assignment: Type Bool Simple
* Filename: type_bool_simple.py
* Complexity: easy
* Lines of code: 9 lines
* Estimated time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. What you need to put in expressions to get the expected outcome?
    3. In place of ellipsis (`...`) insert only `True` or `False`
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Co należy podstawić w wyrażeniach aby otrzymać wartość oczekiwaną?
    3. W miejsce trzech kropek (`...`) wstawiaj tylko `True` lub `False`
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> bool(a)
    True
    >>> bool(b)
    True
    >>> bool(c)
    False
    >>> bool(d)
    True
    >>> bool(e)
    True
    >>> bool(f)
    False
    >>> bool(g)
    True
    >>> bool(h)
    True
    >>> bool(i)
    False
"""

# Given
a = True == ...
b = True != ...
c = not ...
d = bool(...) == True
e = bool(...) == False
f = ... or ...
g = ... and ...
h = bool(bool(...) == ...) or False
i = bool(...) is not bool(False)

# Solution
a = True == True
b = True != False
c = not True
d = bool(True) == True
e = bool(False) == False
f = False or False
g = True and True
h = bool(bool(False) == False) or False
i = bool(False) is not bool(False)
