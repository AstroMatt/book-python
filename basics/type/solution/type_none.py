"""
* Assignment: Type None
* Filename: type_none.py
* Complexity: easy
* Lines of code: 5 lines
* Estimated time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. What you need to put in expressions to get the expected outcome?
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Co należy podstawić w wyrażeniach aby otrzymać wartość oczekiwaną?
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> bool(a)
    True
    >>> bool(b)
    False
    >>> bool(c)
    True
    >>> bool(d)
    False
    >>> bool(e)
    False
"""

# Given
a = ... is None
b = ... is not None
c = bool(bool(...) is not bool(...)) == False
d = (bool(bool(...) is not bool(...)) == False and bool(...))
e = (bool(bool(...) is not bool(...)) == False and bool(...)) and (... is not None)

# Solution
a = None is None
b = None is not None
c = bool(bool(None) is not bool(None)) == False
d = (bool(bool(None) is not bool(None)) == False and bool(None))
e = (bool(bool(None) is not bool(None)) == False and bool(None)) and (None is not None)
