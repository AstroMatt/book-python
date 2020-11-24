"""
* Assignment: Sequence Slice Sequence
* Filename: sequence_slice_sequence.py
* Complexity: easy
* Lines of code to write: 2 lines
* Estimated time: 3 min

English:
    1. Use data from "Given" section (see below)
    3. Create set `result` with every second element from `a` and `b`
    4. Print `result`
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    3. Stwórz zbiór `result` z co drugim elementem `a` i `b`
    4. Wypisz `result`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'set'>
    >>> result
    {0, 2, 4}
"""

# Given
a = (0, 1, 2, 3)
b = [2, 3, 4, 5]

# Solution
result = set()
result.update(a[::2], b[::2])
