"""
* Assignment name: Type Int Bytes
* Last update: 2020-11-22
* Complexity level: easy
* Lines of code to write: 7 lines
* Estimated time of completion: 3 min

English:
    1. File size is 100 megabytes
    2. Calculate size in megabits
    3. Compare result with "Tests" section (see below)

Polish:
    1. Wielkość pliku to 100 megabajtów
    2. Oblicz wielkość w megabitach
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * 1 Kb = 1024 b
    * 1 Mb = 1024 Kb
    * 1 B = 8 b
    * 1 KB = 1024 B
    * 1 MB = 1024 KB

Tests:
    >>> size // MB
    100
    >>> size // Mb
    800

"""

# Given
b = 1
B = 8 * b

# Solution
kb = 1024 * b
Mb = 1024 * kb
kB = 1024 * B
MB = 1024 * kB

size = 100 * MB
