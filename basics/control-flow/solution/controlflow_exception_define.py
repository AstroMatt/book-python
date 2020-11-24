"""
* Assignment: Exception Define
* Filename: controlflow_exception_define.py
* Complexity: easy
* Lines of code to write: 6 lines
* Estimated time: 5 min

English:
    1. Ask user to input temperature in Kelvins
    2. User will always type proper `int` or `float`
    3. Define exception for negative temperature
    4. Raise your exception if temperature is less than 0

Polish:
    1. Poproś użytkownika o wprowadzenie temperatury w Kelwinach
    2. Użytkownik zawsze poda poprawne `int` lub `float`
    3. Zdefiniuj wyjątek dla temperatur ujemnych
    4. Podnieś własny wyjątek jeżeli temperatura jest poniżej 0

Tests:
    TODO: Doctests
"""

temperature = input('Type temperature: ')


class NegativeKelvinError(Exception):
    pass


if float(temperature) < 0:
    raise NegativeKelvinError
