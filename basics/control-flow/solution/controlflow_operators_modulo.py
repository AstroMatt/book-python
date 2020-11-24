"""
* Assignment: Conditional Operators Modulo
* Filename: controlflow_operators_modulo.py
* Complexity: easy
* Lines of code to write: 3 lines
* Estimated time: 3 min

English:
    1. Read a number from user
    2. User will input `int` and will not try to input invalid data
    3. Define `result: bool` with parity check of input number
    4. Number is even, when divided modulo (`%`) by 2 reminder equal to 0
    5. Print `result`
    6. Do not use `if` statement

Polish:
    1. Wczytaj liczbę od użytkownika
    2. Użytkownika poda `int` i nie będzie próbował wprowadzać niepoprawnych danych
    3. Zdefiniuj `result: bool` z wynikiem sprawdzania parzystości liczby wprowadzonej
    4. Liczba jest parzysta, gdy dzielona modulo (`%`) przez 2 ma resztę równą 0
    5. Wypisz `result`
    6. Nie używaj instrukcji `if`

Hints:
    * `%` has different meaning for `int` and `str`
    * `%` on `str` is overloaded as a string formatting
    * `%` on `int` is overloaded as a modulo division

Tests:
    >>> type(result)
    <class 'bool'>
    >>> result in (True, False)
    True
"""

# Given
number = input('What is your number?: ')

# Solution
result = float(number) % 2 == 0
