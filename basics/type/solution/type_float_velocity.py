"""
* Assignment name: Type Float Velocity
* Suggested filename: type_float_velocity.py
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 3 min

English:
    1. Speed limit is 75 MPH
    2. Data uses imperial (US) system
    3. Convert to metric (SI) system
    4. Speed limit print in KPH (km/h)
    5. Result round to one decimal place
    6. Compare result with "Output" section (see below)

Polish:
    1. Ograniczenie prędkości wynosi 75 MPH
    2. Dane używają systemu imperialnego (US)
    3. Przelicz je na system metryczny (układ SI)
    4. Ograniczenie prędkości wypisz w KPH (km/h)
    5. Wynik zaokrąglij do jednego miejsca po przecinku
    6. Porównaj wyniki z sekcją "Output" (patrz poniżej)

Tests:
    >>> round(result/KPH, 1)
    120.7
"""

# Given
SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE

m = 1
km = 1000 * m
mi = 1609.344 * m

# Solution
KPH = km / HOUR
MPH = mi / HOUR

result = 75 * MPH
