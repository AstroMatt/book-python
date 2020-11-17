"""
>>> assert type(result) is set
>>> result
{0.2, 1.9, 2.7, 3.5, 1.4, 5.8, 5.1, 1.3, 2.8, 4.1, 5.7, 6.3, 5.6, 6.4, 1.5, 4.5, 3.2, 1.8, 2.9}
"""

result = {5.8, 2.7, 5.1, 1.9}

result.add(5.1)
result.add(3.5)
result.add(1.4)
result.add(0.2)

result.update({5.7, 2.8, 4.1, 1.3})
result.update((6.3, 2.9, 5.6, 1.8))
result.update([6.4, 3.2, 4.5, 1.5])
