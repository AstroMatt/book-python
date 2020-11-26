"""
* Assignment: Function Lambda Chain
* Filename: function_lambda_chain.py
* Complexity: easy
* Lines of code to write: 2 lines
* Estimated time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Inline functions `odd()` and `cube()` with `lambda` expressions
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wciel kod `odd()` i `cube()` wykorzystując wyrażenia `lambda`
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `mean = sum(...) / len(...)`
    * type cast to `list()` before calculating mean to expand generator

Tests:
    >>> type(result) is float
    True
    >>> result
    11502.0
"""


# Given
def odd(x):
    return x % 2


def cube(x):
    return x ** 3


numbers = (x for x in range(1, 34) if x % 3 == 0)
numbers = filter(odd, numbers)
numbers = map(cube, numbers)
numbers = list(numbers)
result = sum(numbers) / len(numbers)


# Solution
numbers = (x for x in range(1, 34) if x % 3 == 0)
numbers = filter(lambda x: x%2, numbers)
numbers = map(lambda x: x**3, numbers)
numbers = list(numbers)
result = sum(numbers) / len(numbers)
