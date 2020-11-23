"""
* Assignment name: Type Float Distance
* Suggested filename: type_float_distance.py
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min

English:
    1. Use code from "Given" section (see below)
    2. Convert units
    3. Instead ``...`` substitute calculated and converted values
    4. Note the number of decimal places
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Przekonwertuj jednostki
    3. Zamiast ``...`` podstaw wyliczone i przekonwertowane wartości
    4. Zwróć uwagę na ilość miejsc po przecinku
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> print(result)  # doctest: +NORMALIZE_WHITESPACE
    Meters: 1337
    Kilometers: 1.337
    Miles: 0.83
    Nautical Miles: 0.722
    All: km: 1, mi: 0.8, nm: 0.72
"""

# Given
m = 1
km = 1000 * m
mi = 1609.344 * m
nm = 1852 * m

distance = 1337

result = f"""Meters: {...}
Kilometers: {...}
Miles: {...}
Nautical Miles: {...}
All: km: {...}, mi: {...}, nm: {...}"""

# Solution
distance_m = distance / m
distance_km = distance / km
distance_mi = distance / mi
distance_nm = distance / nm

result = f"""Meters: {distance_m:.0f}
Kilometers: {distance_km:.3f}
Miles: {distance_mi:.2f}
Nautical Miles: {distance_nm:.3f}
All: km: {distance_km:.0f}, mi: {distance_mi:.1f}, nm: {distance_nm:.2f}"""
