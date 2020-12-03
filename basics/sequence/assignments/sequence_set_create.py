"""
* Assignment: Sequence Set Create
* Filename: sequence_set_create.py
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Create set `result` with elements:
        a. `'a'`
        b. `1`
        c. `2.2`
    2. Compare result with "Tests" section (see below)

Polish:
    1. Stwórz zbiór `result` z elementami:
        a. `'a'`
        b. `1`
        c. `2.2`
    2. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'set'>
    >>> len(result)
    3
    >>> 'a' in result
    True
    >>> 1 in result
    True
    >>> 2.2 in result
    True
"""

# Solution
result = {'a', 1, 2.2}
