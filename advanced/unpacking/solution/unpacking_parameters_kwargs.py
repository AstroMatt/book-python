"""
* Assignment: Unpacking Parameters Kwargs
* Filename: unpacking_parameters_kwargs.py
* Complexity: medium
* Lines of code to write: 8 lines
* Estimated time: 5 min

English:
    1. Create function `isnumeric`
    2. Function can have arbitrary number of positional **and keyword arguments**
    3. Arguments can be of any type
    4. Return `True` if all arguments are `int` or `float` only
    5. Return `False` if any argument is different type
    6. Do not use `all()` and `any()`
    7. Compare using `type()` and `isinstance()` passing `True` as an argument
    8. Run the function without any arguments
    9. Compare result with "Tests" section (see below)

Polish:
    1. Stwórz funkcję `isnumeric`
    2. Funkcja może przyjmować dowolną liczbę argumentów pozycyjnych **i nazwanych**
    3. Podawane argumenty mogą być dowolnego typu
    4. Zwróć `True` jeżeli wszystkie argumenty są tylko typów `int` lub `float`
    5. Zwróć `False` jeżeli którykolwiek jest innego typu
    6. Nie używaj `all()` oraz `any()`
    7. Porównaj użycie `type()` i `isinstance()` podając argument do funkcji `True`
    8. Uruchom funkcję bez podawania argumentów
    9. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `isinstance(obj, (type1, type2))`
    * `type(obj)`

Tests:
    >>> isnumeric()
    False
    >>> isnumeric(0)
    True
    >>> isnumeric(1)
    True
    >>> isnumeric(-1)
    True
    >>> isnumeric(1.1)
    True
    >>> isnumeric('one')
    False
    >>> isnumeric([1, 1.1])
    False
    >>> isnumeric(1, 1.1)
    True
    >>> isnumeric(1, 'one')
    False
    >>> isnumeric(1, 'one', 'two')
    False
    >>> isnumeric(True)
    False
    >>> isnumeric(a=1)
    True
    >>> isnumeric(a=1.1)
    True
    >>> isnumeric(a='one')
    False
"""


# Solution
def isnumeric(*args, **kwargs) -> bool:
    arguments = args + tuple(kwargs.values())

    if len(arguments) == 0:
        return False

    for arg in arguments:
        if type(arg) not in (float, int):
            return False

    return True
