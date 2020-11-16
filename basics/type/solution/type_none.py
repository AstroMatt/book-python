"""
>>> a
True
>>> b
False
>>> c
True
>>> d
False
>>> e
False
"""

a = None is None
b = None is not None
c = bool(bool(None) is not bool(None)) == False
d = (bool(bool(None) is not bool(None)) == False and bool(None))
e = (bool(bool(None) is not bool(None)) == False and bool(None)) and (None is not None)
