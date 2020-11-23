"""
* Assignment name: Type Bool True or False
* Suggested filename: type_bool_true_or_false.py
* Complexity level: easy
* Lines of code to write: 16 lines
* Estimated time of completion: 5 min

English:
    #. Use data from "Given" section (see below)
    #. Which variables are ``True``?
    #. Which variables are ``False``?

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Które zmienne są ``True``?
    #. Które zmienne są ``False``?

Tests:
    >>> a
    False
    >>> b
    True
    >>> c
    False
    >>> d
    False
    >>> e
    False
    >>> f
    False
    >>> g
    True
    >>> h
    True
    >>> i
    True
    >>> j
    True
    >>> k
    False
    >>> l
    True
    >>> m
    False
    >>> n
    False
    >>> o
    False
    >>> p
    True
    >>> q
    False
"""

# Given
a = bool(False)
b = bool(True)

c = bool(0)
d = bool(0.0)
e = bool(-0)
f = bool(-0.0)

g = bool('a')
h = bool('.')
i = bool('0')
j = bool('0.0')
k = bool('')
l = bool(' ')

m = bool(int('0'))
n = bool(float(str(-0)))

o = bool(-0.0 + 0.0j)
p = bool('-0.0+0.0j')
q = bool(complex('-0.0+0.0j'))

# Solution
