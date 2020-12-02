"""
* Assignment: Mapping Generate Enumerate
* Filename: mapping_generate_enumerate.py
* Complexity: easy
* Lines of code: 1 lines
* Estimated time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Create `result: dict`
    3. Using `enumerate()` convert data to `dict` and assign to `result`
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz `result: dict`
    3. Używając `enumerate()` przekonwertuj dane do `dict` i przypisz do `result`
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'dict'>
    >>> all(type(x) is int for x in result.keys())
    True
    >>> all(type(x) is str for x in result.values())
    True
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {0: 'setosa',
     1: 'versicolor',
     2: 'virginica'}
"""

# Given
DATA = ['setosa', 'versicolor', 'virginica']

# Solution
result = dict(enumerate(DATA))
