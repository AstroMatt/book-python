"""
* Assignment: Exception Custom
* Filename: controlflow_exception_custom.py
* Complexity: easy
* Lines of code: 4 lines
* Estimated time: 3 min

English:
    1. Ask user to input angle in degrees
    2. Define custom exception `NegativeKelvin`
    3. If input temperature is lower than 0, raise `NegativeKelvin`

Polish:
    1. Poproś użytkownika o wprowadzenie kąta
    2. Zdefiniuj własny wyjątek `NegativeKelvin`
    3. Jeżeli wprowadzona temperature jest mniejsza niż 0, podnieś `NegativeKelvin`

Tests:
    >>> type(temperature)
    <class 'float'>
    >>> from inspect import isclass
    >>> isclass(NegativeKelvin)
    True
    >>> issubclass(NegativeKelvin, Exception)
    True
"""

# Given
temperature = input('Type temperature: ')
temperature = float(temperature)


# Solution
class NegativeKelvin(Exception):
    pass


if temperature < 0:
    raise NegativeKelvin
