"""
* Assignment: Type Float Pressure
* Filename: type_float_pressure.py
* Complexity: medium
* Lines of code: 2 lines
* Estimated time: 3 min

English:
    1. Operational pressure of EMU spacesuit: 4.3 PSI
    2. Operational pressure of ORLAN spacesuit: 400 hPa
    3. Calculate operational pressure in kPa for EMU
    4. Calculate operational pressure in PSI for Orlan
    5. Print all results in kPa and PSI rounding to one decimal places
    6. Compare result with "Tests" section (see below)

Polish:
    1. Ciśnienie operacyjne skafandra kosmicznego EMU (NASA): 4.3 PSI
    2. Ciśnienie operacyjne skafandra kosmicznego ORLAN (Roscosmos): 400 hPa
    3. Oblicz ciśnienie operacyjne skafandra EMU w kPa
    4. Oblicz ciśnienie operacyjne skafandra Orlan w PSI
    5. Wypisz wszystkie wyniki w kPa oraz PSI zaokrąglając do jednego miejsca po przecinku
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(emu)
    <class 'float'>
    >>> type(orlan)
    <class 'int'>
    >>> emu
    29647.455099999996
    >>> orlan
    40000
    >>> emu / psi
    4.3
    >>> orlan / kPa
    40.0
    >>> round(emu/kPa, 1)
    29.6
    >>> round(orlan/psi, 1)
    5.8
"""

# Given
Pa = 1
hPa = 100 * Pa
kPa = 1000 * Pa
psi = 6894.757 * Pa

# Solution
emu = 4.3 * psi
orlan = 400 * hPa
