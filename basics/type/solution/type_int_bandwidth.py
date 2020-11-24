"""
* Assignment: Type Int Bandwidth
* Filename: type_int_bandwidth.py
* Complexity: easy
* Lines of code to write: 10 lines
* Estimated time: 3 min

English:
    1. Having internet connection with speed 100 Mb/s
    2. How long will take to download 100 MB?
    3. Note, that all values must be `int` (type cast if needed)
    3. In Calculations use truediv (`//`)
    4. Compare result with "Tests" section (see below)

Polish:
    1. Mając łącze internetowe 100 Mb/s
    2. Ile zajmie ściągnięcie pliku 100 MB?
    3. Zwróć uwagę, że wszystkie wartości mają być `int` (rzutuj typ jeżeli potrzeba)
    3. W obliczeniach użyj truediv (`//`)
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * 1 Kb = 1024 b
    * 1 Mb = 1024 Kb
    * 1 B = 8 b
    * 1 KB = 1024 B
    * 1 MB = 1024 KB

Tests:
    >>> type(kb)
    <class 'int'>
    >>> type(Mb)
    <class 'int'>
    >>> type(kB)
    <class 'int'>
    >>> type(MB)
    <class 'int'>
    >>> type(size)
    <class 'int'>
    >>> type(speed)
    <class 'int'>
    >>> type(result)
    <class 'int'>
    >>> result // SECOND
    8
"""

# Given
SECOND = 1
b = 1
B = 8 * b


# Solution
kb = 1024 * b
Mb = 1024 * kb
kB = 1024 * B
MB = 1024 * kB

speed = int(100 * Mb / SECOND)
size = int(100 * MB)
result = int(size // speed)
