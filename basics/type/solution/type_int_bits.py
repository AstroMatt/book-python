"""
* Assignment name: Type Int Bits
* Suggested filename: type_int_bits.py
* Complexity level: medium
* Lines of code to write: 4 lines
* Estimated time of completion: 3 min

English:
    1. File size is 1.337 megabit
    2. Calculate size in bits
    3. Calculate size in kilobits
    4. Compare result with "Tests" section (see below)

Polish:
    1. Wielkość pliku to 1.337 megabit
    2. Oblicz wielkość w bitach
    3. Oblicz wielkość w kilobitach
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * 1 Kb = 1024 b
    * 1 Mb = 1024 Kb

Tests:
    >>> b
    1
    >>> kb
    1024
    >>> Mb
    1048576
    >>> size // b
    1401946112
    >>> size // kb
    1369088
    >>> size // Mb
    1337
"""

# Given
b = 1

# Solution
kb = 1024 * b
Mb = 1024 * kb

size = 1337 * Mb
