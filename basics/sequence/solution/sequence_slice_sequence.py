"""
>>> assert type(result) is set
>>> result
{0, 2, 4}
"""

a = (0, 1, 2, 3)
b = [2, 3, 4, 5]

result = set()
result.update(a[::2], b[::2])
