"""
* Assignment: Function Doctest Distance
* Filename: function_doctest_distance.py
* Complexity: easy
* Lines of code: 21 lines
* Time: 13 min

English:
    1. Write functions which convert distance given in kilometers to meters
    2. 1 km = 1000 m
    3. Distance cannot be negative
    4. Returned value must by float
    5. Write doctests
    6. All tests must pass

Polish:
    1. Napisz funkcję, która przeliczy dystans podany w kilometrach na metry
    2. 1 km = 1000 m
    3. Dystans nie może być ujemny
    4. Zwracany dystans musi być float
    5. Napisz doctesty
    6. Wszystkie testy muszą przechodzić

Tests:
    1. Valid arguments:
        a. `int`
        b. `float`
    2. Invalid argument -> expect `TypeError`
        a. `bool`
        b. `str`
        c. `list[int]`
        d. `list[float]`
        e. any other type
"""


# Given
def km_to_meters(kilometers):
    ...


# Solution
def km_to_meters(kilometers):
    """
    >>> km_to_meters(1)
    1000.0
    >>> km_to_meters(0)
    0.0
    >>> km_to_meters(-1)
    Traceback (most recent call last):
    ValueError: Argument must be not negative
    >>> km_to_meters([1, 2])
    Traceback (most recent call last):
    TypeError: Invalid argument type
    >>> km_to_meters('one')
    Traceback (most recent call last):
    TypeError: Invalid argument type
    >>> km_to_meters(1.5)
    1500.0
    >>> km_to_meters(True)
    Traceback (most recent call last):
    TypeError: Invalid argument type
    """
    if type(kilometers) not in {int, float}:
        raise TypeError('Invalid argument type')

    if kilometers < 0:
        raise ValueError('Argument must be not negative')

    return float(kilometers * 1000)
