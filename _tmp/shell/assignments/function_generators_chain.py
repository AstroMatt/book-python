"""
* Assignment: Function Generator Chain
* Filename: function_generators_chain.py
* Complexity: easy
* Lines of code: 10 lines
* Time: 8 min

English:
    1. Use generator expression to create `result`
    2. In generator use `range()` to get numbers from 1 to 33 (inclusive) divisible by 3
    3. Use `filter()` to get odd numbers from `result`
    4. Use `map()` to cube all numbers in `result`
    5. Set `result` with arithmetic mean of `result`
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj wyrażenia generatorowego do stworzenia `result`
    2. W generatorze użyj `range()` aby otrzymać liczby od 1 do 33 (włącznie) podzielne przez 3
    3. Użyj `filter()` aby otrzymać liczby nieparzyste z `result`
    4. Użyj `map()` aby podnieść wszystkie liczby w `result` do sześcianu
    5. Ustaw `result` ze średnią arytmetyczną z `result`
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * type cast to `list()` to expand generator before calculating mean
    * `mean = sum(...) / len(...)`

Tests:
    >>> result
    11502.0
"""


# Given
def odd(x):
    return x % 2


def cube(x):
    return x ** 3


result: float

# Solution
numbers = (x for x in range(1, 34) if x % 3 == 0)
numbers = filter(odd, numbers)
numbers = map(cube, numbers)
numbers = list(numbers)
result = sum(numbers) / len(numbers)
