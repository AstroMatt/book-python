"""
* Assignment name: Type Float Pressure
* Suggested filename: type_float_pressure.py
* Complexity level: medium
* Lines of code to write: 2 lines
* Estimated time of completion: 3 min

English:
    #. Operational pressure of EMU spacesuit: 4.3 PSI
    #. Operational pressure of ORLAN spacesuit: 400 hPa
    #. Calculate operational pressure in kPa for EMU
    #. Calculate operational pressure in PSI for Orlan
    #. Print all results in kPa and PSI rounding to one decimal places
    #. Compare result with "Tests" section (see below)

Polish:
    #. Ciśnienie operacyjne skafandra kosmicznego EMU (NASA): 4.3 PSI
    #. Ciśnienie operacyjne skafandra kosmicznego ORLAN (Roscosmos): 400 hPa
    #. Oblicz ciśnienie operacyjne skafandra EMU w kPa
    #. Oblicz ciśnienie operacyjne skafandra Orlan w PSI
    #. Wypisz wszystkie wyniki w kPa oraz PSI zaokrąglając do jednego miejsca po przecinku
    #. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
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
