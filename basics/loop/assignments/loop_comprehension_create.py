"""
* Assignment: Loop Comprehension Create
* Filename: loop_comprehension_create.py
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Use list comprehension
    2. Generate `result: list[int]` of even numbers from 5 to 20
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj rozwinięcia listowego
    2. Wygeneruj `result: list[int]` parzystych liczb z przedziału 5 do 20
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> assert type(result) is list
    >>> assert all(type(x) is int for x in result)
    >>> result
    [6, 8, 10, 12, 14, 16, 18]
"""

# Given
result: list

# Solution
result = [x for x in range(5,20) if x % 2 == 0]

