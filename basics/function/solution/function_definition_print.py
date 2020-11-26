"""
* Assignment: Function Definition Print
* Filename: function_definition_print.py
* Complexity: easy
* Lines of code to write: 5 lines
* Estimated time: 3 min

English:
    1. Define function ``call`` without parameters
    2. Function prints ``Beetlejuice``
    3. Call function three times

Polish:
    1. Zdefiniuj funkcję ``call`` bez parametrów
    2. Funkcja wypisuje ``Beetlejuice``
    3. Wywołaj funkcję trzy razy

Tests:
    >>> from inspect import isfunction
    >>> isfunction(call)
    True
    >>> call()
    Beetlejuice
"""


# Solution
def call():
    print('Beetlejuice')


call()
call()
call()
