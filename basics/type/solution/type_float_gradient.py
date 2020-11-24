"""
* Assignment: Type Float Gradient
* Filename: type_float_gradient.py
* Complexity: hard
* Lines of code to write: 7 lines
* Estimated time: 8 min

English:
    1. At what altitude above sea level, pressure is equal to partial pressure of Oxygen
    2. Print result in meters rounding to two decimal places
    3. To calculate partial pressure use ratio (100% is 1013.25 hPa, 20.946% is how many hPa?)
    4. Calculated altitude is pressure at sea level minis oxygen partial pressure divided by gradient
    5. Mind the operator precedence
    6. Compare result with "Tests" section (see below)

Polish:
    1. Na jakiej wysokości nad poziomem morza panuje ciśnienie równe ciśnieniu parcjalnemu tlenu?
    2. Wypisz rezultat w metrach zaokrąglając do dwóch miejsc po przecinku
    3. Aby policzyć ciśnienie parcjalne skorzystaj z proporcji (100% to 1013.25 hPa, 20.946% to ile hPa?)
    4. Wyliczona wysokość to ciśnienie atmosferyczne na poziomie morza minus ciśnienie parcjalne tlenu podzielone przez gradient
    5. Zwróć uwagę na kolejność wykonywania działań
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * pressure gradient (decrease) = 11.3 Pa / 1 m
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
    >>> type(gradient)
    <class 'float'>
    >>> type(result)
    <class 'float'>
    >>> pO2
    21223.5345
    >>> gradient
    11.3
    >>> round(result/m, 2)
    7088.63
"""

# Given
m = 1
Pa = 1
hPa = 100 * Pa
ata = 1013.25 * hPa
O2 = 20.946

# Solution
pO2 = O2/100 * ata
gradient = 11.3 * Pa / m
result = (ata - pO2) / gradient
