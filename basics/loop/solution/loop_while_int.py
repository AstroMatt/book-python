"""
* Assignment: Loop While to Int
* Filename: loop_while_int.py
* Complexity: easy
* Lines of code to write: 6 lines
* Estimated time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Create `result: list[int]`
    3. Use `while` to iterate over `DATA`
    4. Convert all elements of `DATA` to `int`
    5. Converted values add to `result`
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz `result: list[int]`
    3. Użyj `while` do iterowania po `DATA`
    4. Przekonwertuj wszystkie elementy `DATA` do `int`
    5. Przekonwertowane wartości dodaj do `result`
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> assert type(result) is list
    >>> assert all(type(x) is int for x in result)
    >>> result
    [1, 2, 3]
"""

# Given
DATA = ['1', '2', '3']

# Solution
i = 0
result = []

while i < len(DATA):
    value = int(DATA[i])
    result.append(value)
    i += 1
