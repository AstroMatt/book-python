"""
* Assignment name: Type Float Percent
* Suggested filename: type_float_percent.py
* Complexity level: medium
* Lines of code to write: 2 lines
* Estimated time of completion: 3 min

English:
    1. International Standard Atmosphere (ISA) at sea level is 1 ata = 1013.25 hPa
    2. Calculate ``pO2`` - partial pressure of Oxygen at sea level
    3. Print result in kPa rounding to two decimal places
    4. To calculate partial pressure use ratio (100% is 1013.25 hPa, 20.946% is how many hPa?)
    5. Compare result with "Tests" section (see below)

Polish:
    1. International Standard Atmosphere (ISA) na poziomie morza wynosi 1 ata = 1013.25 hPa
    2. Oblicz ``pO2`` - ciśnienie parcjalne tlenu na poziomie morza
    3. Wynik wypisz w kPa zaokrąglając do dwóch miejsc po przecinku
    4. Aby policzyć ciśnienie parcjalne skorzystaj z proporcji (100% to 1013.25 hPa, 20.946% to ile hPa?)
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * 1 hPa = 100 Pa
    * 1 kPa = 1000 Pa
    * 1 ata = 1013.25 hPa (ISA - International Standard Atmosphere)
    * Atmosphere gas composition:

        * Nitrogen 78.084%
        * Oxygen 20.946%
        * Argon 0.9340%
        * Carbon Dioxide 0.0407%
        * Others 0.001%

Tests:
    >>> type(pO2)
    <class 'float'>
    >>> pO2
    21223.5345
    >>> round(pO2/kPa, 2)
    21.22
"""

# Given
Pa = 1
hPa = 100 * Pa
kPa = 1000 * Pa
ata = 1013.25 * hPa
O2 = 20.946

# Solution
pO2 = O2/100 * ata
