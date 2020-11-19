"""
>>> type(result) is float
True
>>> result
11502.0
"""

numbers = (x for x in range(1, 34) if x % 3 == 0)
numbers = filter(lambda x: x%2, numbers)
numbers = map(lambda x: x**3, numbers)
numbers = list(numbers)
result = sum(numbers) / len(numbers)
