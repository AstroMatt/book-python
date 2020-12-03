"""
* Assignment: Exception Else
* Filename: controlflow_exception_else.py
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Ask user to input age
    2. If user has less than 18 years
    3. Raise an exception `PermissionError` with message "Adults only"

Polish:
    1. Poproś użytkownika o wprowadzenie wieku
    2. Jeżeli użytkownik ma mniej niż 18 lat
    3. Wyrzuć wyjątek `PermissionError` z komunikatem "Adults only"

Tests:
    TODO: Doctests
"""

# Given
ADULT = 18
age = input('Type age: ')

# Solution
if float(age) < ADULT:
    raise PermissionError('Adults only')
