"""
* Assignment name: Type Float Volume
* Suggested filename: type_float_volume.py
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 3 min

English:
    1. Bottle volume is 20 Fl Oz
    2. Data uses imperial (US) system
    3. Convert to metric (SI) system
    4. Compare result with "Output" section (see below)

Polish:
    1. Objętość butelki wynosi 20 Fl Oz
    2. Dane używają systemu imperialnego (US)
    3. Przelicz je na system metryczny (układ SI)
    4. Porównaj wyniki z sekcją "Output" (patrz poniżej)

Tests:
    >>> result / LITER
    0.5914688
"""

# Given
LITER = 1
FLOZ = 0.02957344 * LITER

# Solution
result = 20 * FLOZ

