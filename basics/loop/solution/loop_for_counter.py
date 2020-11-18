"""
>>> assert type(result) is dict
>>> assert all(type(x) is int for x in result.keys())
>>> assert all(type(x) is int for x in result.values())
>>> result
{1: 7, 4: 8, 6: 4, 7: 4, 5: 4, 0: 7, 9: 5, 8: 6, 2: 2, 3: 3}
"""

DATA = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0, 0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
        2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9, 1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
        4, 8, 1, 9, 6, 3]

result = {}

for digit in DATA:

    if digit not in result:
        result[digit] = 1
    else:
        result[digit] += 1
