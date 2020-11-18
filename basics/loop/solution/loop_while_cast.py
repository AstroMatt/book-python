"""
>>> assert type(result) is list
>>> assert all(type(x) is int for x in result)
>>> result
[1, 2, 3]
"""

DATA = ['1', '2', '3']
i = 0
result = []

while i < len(DATA):
    value = int(DATA[i])
    result.append(value)
    i += 1
