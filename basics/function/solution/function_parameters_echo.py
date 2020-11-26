"""
* Assignment: Function Parameters Echo
* Filename: function_parameters_echo.py
* Complexity: easy
* Lines of code to write: 2 lines
* Estimated time: 3 min

English:
    1. Define function ``echo`` with two parameters
    2. Parameter ``a`` is required
    3. Parameter ``b`` is required
    4. Wypisz ``a`` i ``b``
    5. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj funkcję ``echo`` z dwoma parametrami
    2. Parametr ``a`` jest wymagany
    3. Parametr ``b`` jest wymagany
    4. Wypisz ``a`` i ``b``
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> echo(1, 2)
    a=1 b=2
    >>> echo(3, 4)
    a=3 b=4
"""


# Solution
def echo(a, b):
    print(f'{a=} {b=}')
