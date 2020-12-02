"""
* Assignment: Function Arguments Numbers to Human
* Filename: function_args_numhuman.py
* Complexity: hard
* Lines of code: 15 lines
* Estimated time: 21 min

English:
    1. Define function converting `int` or `float` to text form
    2. Text form must be in proper grammar form
    3. Max 6 digits before decimal separator (point `.`)
    4. Max 5 digits after decimal separator (point `.`)
    5. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj funkcję konwertującą `int` lub `float` na formę tekstową
    2. Forma tekstowa musi być poprawna gramatycznie
    3. Max 6 cyfr przed separatorem dziesiętnym (point `.`)
    4. Max 5 cyfr po separatorze dziesiętnym (point `.`)
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> number_to_str(1969)
    'one thousand nine hundred sixty nine'
    >>> number_to_str(31337)
    'thirty one thousand three hundred thirty seven'
    >>> number_to_str(13.37)
    'thirteen and thirty seven hundredths'
    >>> number_to_str(31.337)
    'thirty one and three hundreds thirty seven thousands'
    >>> number_to_str(-1969)
    'minus one thousand nine hundred sixty nine'
    >>> number_to_str(-31.337)
    'minus thirty one and three hundreds thirty seven thousands'
    >>> number_to_str(-49.35)
    'minus forty nine and thirty five hundreds'
"""

# Given
NUMBER = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '.': 'and',
    '-': 'minus'}

def number_to_str(number):
    """TODO"""

# Solution
def number_to_str(number):
    """TODO"""
