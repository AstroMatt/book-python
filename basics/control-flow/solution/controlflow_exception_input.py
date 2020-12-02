"""
* Assignment: Exception Input
* Filename: controlflow_exception_input.py
* Complexity: easy
* Lines of code: 9 lines
* Estimated time: 5 min

English:
    1. Ask user to input angle in degrees
    2. User can input any value from keyboard (even nonnumeric)
    2. Cotangent for 180 degrees is infinite
    3. Define own exception `CotangentError`
    4. If user typed angle equal to 180, raise your exception

Polish:
    1. Poproś użytkownika o wprowadzenie kąta
    2. Uwaga, użytkownik może podać dowolną wartość z klawiatury (nawet nienumeryczną)
    2. Cotangens dla konta 180 ma nieskończoną wartość
    3. Zdefiniuj własny wyjątek `CotangentError`
    4. Jeżeli użytkownik wprowadził kąt równy 180, podnieś swój wyjątek

Tests:
    TODO: Doctests
"""

# Given
degrees = input('Type angle [deg]: ')


# Solution
try:
    degrees = float(degrees)
except ValueError:
    print('Degrees expects int or float')
    exit(1)


class CotangentError(Exception):
    pass


if degrees == 180:
    raise CotangentError
