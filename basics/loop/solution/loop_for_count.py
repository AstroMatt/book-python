"""
* Assignment: Loop For Count
* Filename: loop_for_count.py
* Complexity: easy
* Lines of code to write: 7 lines
* Estimated time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Count occurrences of each color
    3. Compare results with "Output" section below

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zlicz wystąpienia każdego z kolorów
    3. Porównaj wynik z sekcją "Output" poniżej

Tests:
    >>> type(red)
    <class 'int'>
    >>> type(green)
    <class 'int'>
    >>> type(blue)
    <class 'int'>
    >>> red
    3
    >>> green
    2
    >>> blue
    2
"""

# Given
DATA = ['red', 'green', 'blue', 'red', 'green', 'red', 'blue']

red: int = 0
green: int = 0
blue: int = 0

# Solution
for color in DATA:
    if color == 'red':
        red += 1
    elif color == 'green':
        green += 1
    elif color == 'blue':
        blue += 1
