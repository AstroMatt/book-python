"""
>>> assert type(result) is list
>>> assert all(type(x) is int for x in result)
>>> result
[6, 8, 10, 12, 14, 16, 18]
"""

result = [x for x in range(5,20) if x % 2 == 0]

