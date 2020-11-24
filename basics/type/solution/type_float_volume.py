"""
* Assignment: Type Float Volume
* Filename: type_float_volume.py
* Complexity: easy
* Lines of code to write: 4 lines
* Estimated time: 3 min

English:
    1. Bottle volume is 20 Fl Oz
    2. Data uses imperial (US) system
    3. Convert to metric (SI) system
    4. Compare result with "Tests" section (see below)

Polish:
    1. Objętość butelki wynosi 20 Fl Oz
    2. Dane używają systemu imperialnego (US)
    3. Przelicz je na system metryczny (układ SI)
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'float'>
    >>> result / floz
    20.0
    >>> result / liter
    0.5914688
"""

# Given
liter = 1
floz = 0.02957344 * liter

# Solution
result = 20 * floz

