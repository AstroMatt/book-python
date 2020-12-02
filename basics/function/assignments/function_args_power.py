"""
* Assignment: Function Arguments Power
* Filename: function_args_power.py
* Complexity: easy
* Lines of code: 6 lines
* Estimated time: 3 min

English:
    1. Define function `power`
    2. Function takes two arguments
    3. Second argument is optional
    4. Function returns power of the first argument to the second
    5. If only one argument was passed, consider second equal to the first one
    6. Print returned values
    7. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj funkcję `power`
    2. Funkcja przyjmuje dwa argumenty
    3. Drugi argument jest opcjonalny
    4. Funkcja zwraca wynik pierwszego argumentu do potęgi drugiego
    5. Jeżeli tylko jeden argument był podany, przyjmij drugi równy pierwszemu
    6. Wypisz zwracane wartości
    7. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> power(4, 3)
    64
    >>> power(3)
    27
"""


# Solution
def power(a, b=None):
    if b is None:
        b = a
    return a ** b
