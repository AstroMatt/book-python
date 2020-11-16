"""
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

a = None is None
b = None is not None
c = bool(bool(None) is not bool(None)) == False
d = (bool(bool(None) is not bool(None)) == False and bool(None))
e = (bool(bool(None) is not bool(None)) == False and bool(None)) and (None is not None)
