"""
* Assignment: Exception Raise
* Filename: controlflow_exception_raise.py
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Ask user to input temperature in Kelvins
    2. User will always type proper `int` or `float`
    3. Raise `ValueError` exception if temperature is less than 0

Polish:
    1. Poproś użytkownika o wprowadzenie temperatury w Kelwinach
    2. Użytkownik zawsze poda poprawne `int` lub `float`
    3. Podnieś wyjątek `ValueError` jeżeli temperatura jest poniżej 0

Tests:
    TODO: Doctests
    >>> type(temperature)
    <class 'float'>
    >>> import sys
    >>> sys.modules[__name__]
"""

# Given
# temperature = input('Type temperature: ')
temperature = 10
temperature = float(temperature)

# Solution
if temperature < 0:
    raise ValueError
