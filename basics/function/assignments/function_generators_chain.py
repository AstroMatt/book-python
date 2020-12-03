"""
* Assignment: Function Generator Chain
* Filename: function_generators_chain.py
* Complexity: easy
* Lines of code: 10 lines
* Time: 13 min

English:
    1. Use generator expression to create `numbers`
    2. In generator use `range()` to get numbers from 1 to 33 (inclusive) divisible by 3
    3. Use `filter()` to get odd numbers from `numbers`
    4. Use `map()` to cube all numbers in `numbers`
    5. Create `result: float` with arithmetic mean of `numbers`
    6. Do not use `lambda` expressions
    7. Compare result with "Tests" section (see below)

Polish:
    1. Użyj wyrażenia generatorowego do stworzenia `numbers`
    2. W generatorze użyj `range()` aby otrzymać liczby od 1 do 33 (włącznie) podzielne przez 3
    3. Użyj `filter()` aby otrzymać liczby nieparzyste z `numbers`
    4. Użyj `map()` aby podnieść wszystkie liczby w `numbers` do sześcianu
    5. Stwórz `result: float` ze średnią arytmetyczną z `numbers`
    6. Nie używaj wyrażeń lambda
    7. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * type cast to `list()` before calculating mean to expand generator
    * `mean = sum(...) / len(...)`

Tests:
    >>> type(result) is float
    True
    >>> result
    11502.0
"""


# Solution
def odd(x):
    return x % 2


def cube(x):
    return x ** 3


numbers = (x for x in range(1, 34) if x % 3 == 0)
numbers = filter(odd, numbers)
numbers = map(cube, numbers)
numbers = list(numbers)
result = sum(numbers) / len(numbers)

