"""
* Assignment: Type Float Velocity
* Filename: type_float_velocity.py
* Complexity: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 3 min

English:
    1. Speed limit is 75 MPH
    2. Data uses imperial (US) system
    3. Convert to metric (SI) system
    4. Speed limit print in KPH (km/h)
    5. Result round to one decimal place
    6. Compare result with "Tests" section (see below)

Polish:
    1. Ograniczenie prędkości wynosi 75 MPH
    2. Dane używają systemu imperialnego (US)
    3. Przelicz je na system metryczny (układ SI)
    4. Ograniczenie prędkości wypisz w KPH (km/h)
    5. Wynik zaokrąglij do jednego miejsca po przecinku
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(kph)
    <class 'float'>
    >>> type(mph)
    <class 'float'>
    >>> type(result)
    <class 'float'>
    >>> round(kph, 3)
    0.278
    >>> round(mph, 3)
    0.447
    >>> round(result/mph, 1)
    75.0
    >>> round(result/kph, 1)
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
kph = km / HOUR
mph = mi / HOUR

result = 75 * mph
