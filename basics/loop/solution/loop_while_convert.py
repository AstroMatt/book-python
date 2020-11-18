"""
>>> assert type(result) is list
>>> assert all(type(x) is float for x in result)
>>> result
[2.0, 3.0, 3.5, 4.0, 4.5, 5.0]
"""

DATA = (2, 3, 3.5, 4, 4.5, 5)
i = 0
result = []

while i < len(DATA):
    value = float(DATA[i])
    result.append(value)
    i += 1
