"""
* Assignment: Type Int Add
* Filename: type_int_add.py
* Complexity: easy
* Lines of code: 4 lines
* Estimated time: 3 min

English:
    1. One Kelvin is equal to 1 Celsius degree (1K = 1°C)
    2. Zero Celsius degrees is equal to 273.15 Kelvins
    3. For calculation use round number 273 (0°K = -273K)
    4. How many Kelvins has average temperatures at surface [1]:
        a. Mars highest: 20 °C
        b. Mars lowest: -153 °C
        c. Mars average: −63 °C
    5. Compare result with "Tests" section (see below)

Polish:
    1. Jeden Kelwin to jeden stopień Celsiusza (1K = 1°C)
    2. Zero stopni Celsiusza to 273.15 Kelwiny
    3. W zadaniu przyjmij równe 273°C (0°K = -273K)
    4. Ile Kelwinów wynoszą średnie temperatury powierzchni [1]:
        a. Mars najwyższa: 20 °C
        b. Mars najniższa: -153 °C
        c. Mars średnia: −63 °C
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

References:
    [1] Centro de Astrobiología (CSIC-INTA).
        Rover Environmental Monitoring Station, Mars Science Laboratory (NASA).
        Year: 2019. Accessed: 2019-08-06. URL: http://cab.inta-csic.es/rems/marsweather.html

Tests:
    >>> type(mars_max)
    <class 'int'>
    >>> type(mars_min)
    <class 'int'>
    >>> type(mars_avg)
    <class 'int'>
    >>> mars_max
    293
    >>> mars_min
    120
    >>> mars_avg
    210
"""

# Given
Kelvin = 273

# Solution
mars_max = 20 + Kelvin
mars_min = -153 + Kelvin
mars_avg = -63 + Kelvin
