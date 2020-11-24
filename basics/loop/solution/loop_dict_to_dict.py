"""
* Assignment: Loop Dict To Dict
* Filename: loop_dict_to_dict.py
* Complexity: easy
* Lines of code to write: 3 lines
* Estimated time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Convert to `result: dict[str, str]`
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Przekonwertuj do `result: dict[str, str]`
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'dict'>
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'Doctorate': '6',
     'Prof-school': '6',
     'Masters': '5',
     'Bachelor': '5',
     'Engineer': '5',
     'HS-grad': '4',
     'Junior High': '3',
     'Primary School': '2',
     'Kindergarten': '1'}
"""

# Given
DATA = {
    6: ['Doctorate', 'Prof-school'],
    5: ['Masters', 'Bachelor', 'Engineer'],
    4: ['HS-grad'],
    3: ['Junior High'],
    2: ['Primary School'],
    1: ['Kindergarten'],
}

result: dict = {}

# Solution
for idx, titles in DATA.items():
    for title in titles:
        result[title] = str(idx)
