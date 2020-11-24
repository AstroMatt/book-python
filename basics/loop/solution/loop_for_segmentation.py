"""
* Assignment: Loop For Segmentation
* Filename: loop_for_segmentation.py
* Complexity: easy
* Lines of code to write: 10 lines
* Estimated time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Count occurrences of each group
    3. Define groups:
        a. `small` - numbers in range [0-3)
        b. `medium` - numbers in range [3-7)
        c. `large` - numbers in range [8-9]
    4. Print `result: dict[str, int]`:
        a. key - group
        b. value - number of occurrences
    5. Compare results with "Output" section below

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Policz wystąpienia każdej z group
    3. Zdefiniuj grupy
        a. `small` - liczby z przedziału <0-3)
        b. `medium` - liczby z przedziału <3-7)
        c. `large` - liczby z przedziału <7-9>
    4. Wypisz `result: dict[str, int]`:
        a. klucz - grupa
        b. wartość - liczba wystąpień
    5. Porównaj wynik z sekcją "Output" poniżej

Tests:
    >>> type(result)
    <class 'dict'>
    >>> assert all(type(x) is str for x in result.keys())
    >>> assert all(type(x) is int for x in result.values())
    >>> result
    {'small': 16, 'medium': 19, 'large': 15}
"""

# Given
DATA = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
        0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
        2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
        1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
        4, 8, 1, 9, 6, 3]

result: dict = {
    'small': 0,
    'medium': 0,
    'large': 0}

# Solution
SMALL = [0, 1, 2]
MEDIUM = [3, 4, 5, 6]
LARGE = [7, 8, 9]

for digit in DATA:
    if digit in SMALL:
        result['small'] += 1
    elif digit in MEDIUM:
        result['medium'] += 1
    elif digit in LARGE:
        result['large'] += 1
