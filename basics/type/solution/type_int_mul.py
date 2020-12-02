"""
* Assignment: Type Int Mul
* Filename: type_int_mul.py
* Complexity: easy
* Lines of code: 3 lines
* Estimated time: 3 min

English:
    1. Calculate altitude in meters:
        a. Armstrong Line: 18 km
        b. Stratosphere: 20 km
        c. USAF Space Line: 80 km
        d. IAF Space Line: 100 km
    2. Compare result with "Tests" section (see below)

Polish:
    1. Oblicz wysokości w metrach:
        a. Linia Armstronga: 18 km
        b. Stratosfera: 20 km
        c. Granica kosmosu wg. USAF: 80 km
        d. Granica kosmosu wg. IAF 100 km
    2. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * 1 km = 1000 m

Tests:
    >>> armstrong_line
    18000
    >>> stratosphere
    20000
    >>> usaf_space
    80000
    >>> iaf_space
    100000
"""

# Given
m = 1
km = 1000 * m

# Solution
armstrong_line = 18 * km
stratosphere = 20 * km
usaf_space = 80 * km
iaf_space = 100 * km
