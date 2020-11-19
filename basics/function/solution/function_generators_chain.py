"""
>>> type(result) is float
True
>>> result
11502.0
"""


def odd(x):
    return x % 2


def cube(x):
    return x ** 3


numbers = (x for x in range(1, 34) if x % 3 == 0)
numbers = filter(odd, numbers)
numbers = map(cube, numbers)
numbers = list(numbers)
result = sum(numbers) / len(numbers)

