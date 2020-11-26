"""
* Assignment: Function Parameter Syntax Args
* Filename: function_parameter_syntax_args.py
* Complexity: easy
* Lines of code to write: 2 lines
* Estimated time: 5 min
* Warning: This assignment will work only in Python 3.8+

English:
    1. Create function `take_damage`
    2. Function takes one argument `dmg` and always returns `None`
    3. Argument must be passed only as positional
    4. Test function by running with positional arguments
    5. Test function by running with keyword arguments
    6. Compare result with "Tests" section (see below)

Polish:
    1. Stwórz funkcję `take_damage`
    2. Funkcja przyjmuje jeden argument `dmg` i zawsze zwraca `None`
    3. Argument można podawać tylko pozycyjnie
    4. Przetestuj funkcję uruchamiając z pozycyjnymi parametrami
    5. Przetestuj funkcję uruchamiając z nazwanymi parametrami
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isfunction
    >>> assert callable(take_damage)
    >>> assert isfunction(take_damage)

    >>> take_damage(1)
    >>> take_damage(1, 2)
    Traceback (most recent call last):
        ...
    TypeError: take_damage() takes 1 positional argument but 2 were given
    >>> take_damage()
    Traceback (most recent call last):
        ...
    TypeError: take_damage() missing 1 required positional argument: 'dmg'
    >>> take_damage(dmg=1)
    Traceback (most recent call last):
        ...
    TypeError: take_damage() got some positional-only arguments passed as keyword arguments: 'dmg'
"""


# Solution
def take_damage(dmg, /):
    ...
