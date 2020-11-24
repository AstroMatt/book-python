"""
* Assignment: Type Int Bits
* Filename: type_int_truediv.py
* Complexity: easy
* Lines of code to write: 3 lines
* Estimated time: 3 min

English:
    1. Calculate altitude in kilometers:
        a. Kármán Line Earth: 100000 m
        b. Kármán Line Mars: 80000 m
        c. Kármán Line Venus: 250000 m
    2. In Calculations use truediv (`//`)
    3. Compare result with "Tests" section (see below)

Polish:
    1. Oblicz wysokości w kilometrach:
        a. Linia Kármána Ziemia: 100000 m
        b. Linia Kármána Mars: 80000 m
        c. Linia Kármána Wenus: 250000 m
    2. W obliczeniach użyj truediv (`//`)
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * 1 km = 1000 m

Tests:
    >>> type(karman_line_earth)
    <class 'int'>
    >>> type(karman_line_mars)
    <class 'int'>
    >>> type(karman_line_venus)
    <class 'int'>
    >>> karman_line_earth
    100
    >>> karman_line_mars
    80
    >>> karman_line_venus
    250
"""

# Given
m = 1
km = 1000 * m

# Solution
karman_line_earth = 100000 // km
karman_line_mars = 80000 // km
karman_line_venus = 250000 // km

