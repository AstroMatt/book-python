"""
* Assignment: Exception Custom
* Filename: controlflow_exception_custom.py
* Complexity: easy
* Lines of code to write: 5 lines
* Estimated time: 3 min

English:
    1. Ask user to input angle in degrees
    2. Cotangent for 180 degrees is infinite
    3. Define own exception `CotangentError`
    4. If user typed angle equal to 180, raise your exception

Polish:
    1. Poproś użytkownika o wprowadzenie kąta
    2. Cotangens dla konta 180 ma nieskończoną wartość
    3. Zdefiniuj własny wyjątek `CotangentError`
    4. Jeżeli użytkownik wprowadził kąt równy 180, podnieś swój wyjątek

Tests:
    TODO: Doctests
"""

degrees = input('Type angle [deg]: ')


class CotangentError(Exception):
    pass


if int(degrees) == 180:
    raise CotangentError('Cotangent for 180 degrees is infinite')
