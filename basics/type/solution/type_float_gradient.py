"""
* Assignment name: Type Float Gradient
* Suggested filename: type_float_gradient.py
* Complexity level: hard
* Lines of code to write: 7 lines
* Estimated time of completion: 8 min

English:
    #. At what altitude above sea level, pressure is equal to partial pressure of Oxygen
    #. Print result in meters rounding to two decimal places
    #. To calculate partial pressure use ratio (100% is 1013.25 hPa, 20.946% is how many hPa?)
    #. Calculated altitude is pressure at sea level minis oxygen partial pressure divided by gradient
    #. Mind the operator precedence
    #. Compare result with "Output" section (see below)

Polish:
    #. Na jakiej wysokości nad poziomem morza panuje ciśnienie równe ciśnieniu parcjalnemu tlenu?
    #. Wypisz rezultat w metrach zaokrąglając do dwóch miejsc po przecinku
    #. Aby policzyć ciśnienie parcjalne skorzystaj z proporcji (100% to 1013.25 hPa, 20.946% to ile hPa?)
    #. Wyliczona wysokość to ciśnienie atmosferyczne na poziomie morza minus ciśnienie parcjalne tlenu podzielone przez gradient
    #. Zwróć uwagę na kolejność wykonywania działań
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Hints:
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
    >>> round(result/m, 2)
    7088.63
"""

# Given
m = 1
Pa = 1
hPa = 100 * Pa
ata = 1013.25 * hPa

# Solution
pO2 = 20.946/100 * ata
gradient = 11.3 * Pa / m
result = (ata - pO2) / gradient
