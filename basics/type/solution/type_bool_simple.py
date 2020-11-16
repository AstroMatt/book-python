"""
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

a = True == True
b = True != False
c = not True
d = bool(True) == True
e = bool(False) == False
f = False or False
g = True and True
h = bool(bool(False) == False) or False
i = bool(False) is not bool(False)
