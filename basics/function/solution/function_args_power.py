"""
>>> power(4, 3)
64
>>> power(3)
27
"""

def power(a, b=None):
    if b is None:
        b = a
    return a ** b
