"""
* Assignment name: Type Float Altitude
* Suggested filename: type_float_tax.py
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min

English:
    #. Plane altitude is 10.000 ft
    #. Data uses imperial (US) system
    #. Convert to metric (SI) system
    #. Result round to one decimal place
    #. Compare result with "Tests" section (see below)

Polish:
    #. Wysokość lotu samolotem wynosi 10 000 ft
    #. Dane używają systemu imperialnego (US)
    #. Przelicz je na system metryczny (układ SI)
    #. Wynik zaokrąglij do jednego miejsca po przecinku
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> result / m
    3048.0
"""

# Given
m = 1
FT = 0.3048 * m

# Solution
result = 10_000 * FT
