"""
* Assignment: Function Parameters Default
* Filename: function_parameters_default.py
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define function `default` with two parameters
    2. Parameter `a` is required
    3. Parameter `b` is optional and has default value `None`
    4. If only one argument was passed, consider second equal to the first one
    5. Print `a` i `b`
    6. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj funkcję `default` z dwoma parametrami
    2. Parametr `a` jest wymagany
    3. Parametr `b` jest opcjonalny i ma domyślną wartość `None`
    4. Jeżeli tylko jeden argument był podany, przyjmij drugi równy pierwszemu
    5. Wypisz `a` i `b`
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> default(1)
    a=1 b=1
    >>> default(2, 3)
    a=2 b=3
"""


# Solution
def default(a, b=None):
    if b is None:
        b = a
    print(f'{a=} {b=}')
