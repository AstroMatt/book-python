"""
* Assignment: Loop For Counter
* Filename: loop_for_counter.py
* Complexity: easy
* Lines of code to write: 5 lines
* Estimated time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Iterate over `DATA`
    3. Count occurrences of each number
    4. Create empty `result: dict[int, int]`:
        a. key - digit
        b. value - number of occurrences
    5. Iterating over numbers check if number is already in `result`
        a. If first occurrence, then add it to `result` with value 1
        b. If exists, then increment the value by 1
    6. Compare results with "Output" section below

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Iteruj po `DATA`
    3. Policz wystąpienia każdej z cyfr
    4. Stwórz pusty `result: dict[int, int]`:
        a. klucz - cyfra
        b. wartość - liczba wystąpień
    5. Iterując po cyfrach sprawdź czy cyfra znajduje się już w `result`
        a. Jeżeli pierwsze wystąpienie, to dodaj ją do `result` z wartością 1
        b. Jeżeli istnieje, to zwiększ w wartość o 1
    6. Porównaj wynik z sekcją "Output" poniżej

Tests:
    >>> assert type(result) is dict
    >>> assert all(type(x) is int for x in result.keys())
    >>> assert all(type(x) is int for x in result.values())
    >>> assert all(x in result.keys() for x in range(0, 10))
    >>> result
    {1: 7, 4: 8, 6: 4, 7: 4, 5: 4, 0: 7, 9: 5, 8: 6, 2: 2, 3: 3}
"""

# Given
DATA = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0, 0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
        2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9, 1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
        4, 8, 1, 9, 6, 3]

result: dict = {}

# Solution
for digit in DATA:
    if digit not in result:
        result[digit] = 1
    else:
        result[digit] += 1
