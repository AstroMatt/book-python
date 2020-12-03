"""
* Assignment: Function Arguments Divide
* Filename: function_args_divide.py
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Define function `divide`
    2. Function takes two arguments
    3. Function divides its arguments and returns the result
    4. Call function with `divide(4, 2)`
    5. Call function with `divide(4, 0)`
    6. Print returned values
    7. What to do in case of error?

Polish:
    1. Zdefiniuj funkcję `divide`
    2. Funkcja przyjmuje dwa argumenty
    3. Funkcja dzieli oba argumenty przez siebie i zwraca wynik dzielenia
    4. Wywołaj funkcję z `divide(4, 2)`
    5. Wywołaj funkcję z `divide(4, 0)`
    6. Wypisz zwracane wartości
    7. Co zrobić w przypadku błędu?

Tests:
    >>> divide(4, 0)
    >>> divide(4, 2)
    2.0
"""


# Solution
def divide(a, b):
    if b != 0:
        return a / b
