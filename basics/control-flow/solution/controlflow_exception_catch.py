"""
* Assignment: Exception Catch
* Filename: controlflow_exception_catch.py
* Complexity: easy
* Lines of code to write: 6 lines
* Estimated time: 5 min

English:
    1. Ask user to input temperature in Kelvins
    2. Convert temperature to `float`
    3. If cannot type cast to `float`, then print 'Invalid temperature' and exit with status code 1
    4. Print temperature

Polish:
    1. Poproś użytkownika o wprowadzenie temperatury w Kelwinach
    2. Przekonwertuj temperaturę do `float`
    3. Jeżeli nie można rzutować do `float`, to wypisz "Invalid temperature" i wyjdź z kodem błędu 1
    4. Wypisz temperaturę

Tests:
    TODO: Doctests
"""

temperature = input('Type temperature: ')

try:
    float(temperature)
except ValueError:
    print('Invalid temperature')
    exit(1)
else:
    print(temperature)
