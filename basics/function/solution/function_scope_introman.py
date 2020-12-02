""""
* Assignment: Function Scope Int To Roman
* Filename: function_scope_introman.py
* Complexity: hard
* Lines of code: 15 lines
* Estimated time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. Define function converting integer to roman numerals

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj funkcję przeliczającą liczbę całkowitą na rzymską

Tests:
    >>> roman_to_int('I')
    1
    >>> roman_to_int('IX')
    9
    >>> roman_to_int('MDL')
    1550
    >>> roman_to_int('MXDL')
    1540
    >>> roman_to_int('XIV')
    14
"""

# Given
ROMAN = {
    'I': 1,
    'II': 2,
    'III': 3,
    'IV': 4,
    'V': 5,
    'VI': 6,
    'VII': 7,
    'VIII': 8,
    'IX': 9,
    'X': 10,
    'XX': 20,
    'XXX': 30,
    'XL': 40,
    'L': 50,
    'LX': 60,
    'LXX': 70,
    'LXXX': 80,
    'XC': 90,
    'C': 100,
    'D': 500,
    'M': 1000,
}


# Solution
def roman_to_int(roman: str) -> int:
    arabic = []

    for letter in roman:
        if letter in ROMAN:
            arabic.append(ROMAN[letter])

    last_value = ROMAN['M'] * 2
    result = 0

    for value in arabic:
        if last_value < value:
            result -= 2 * last_value

        result += value
        last_value = value

    return result
