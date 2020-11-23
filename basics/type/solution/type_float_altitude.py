"""
* Assignment name: Type Float Altitude
* Suggested filename: type_float_tax.py
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min

English:
    1. Plane altitude is 10.000 ft
    2. Data uses imperial (US) system
    3. Convert to metric (SI) system
    4. Result round to one decimal place
    5. Compare result with "Tests" section (see below)

Polish:
    1. Wysokość lotu samolotem wynosi 10 000 ft
    2. Dane używają systemu imperialnego (US)
    3. Przelicz je na system metryczny (układ SI)
    4. Wynik zaokrąglij do jednego miejsca po przecinku
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> result / m
    3048.0
"""

# Given
m = 1
FT = 0.3048 * m

# Solution
result = 10_000 * FT
