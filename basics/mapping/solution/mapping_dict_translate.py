"""
* Assignment: Mapping Dict Translate
* Filename: mapping_dict_translate.py
* Complexity: easy
* Lines of code: 2 lines
* Estimated time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Ask user to input single letter
    3. Convert to lowercase
    4. If letter is in `PL` then use conversion value as letter
    5. Print letter

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Poproś użytkownika o wprowadzenie jednej litery
    3. Przekonwertuj literę na małą
    4. Jeżeli litera jest w `PL` to użyj skonwertowanej wartości jako litera
    5. Wypisz literę

Example:
    | Input | Output |
    |-------|--------|
    |   A   |    a   |
    |   x   |    x   |
    |   ś   |    s   |
    |   Ź   |    z   |

Tests:
    TODO: Doctests
    >>> type(result)
    <class 'str'>
    >>> result not in PL.keys()
    True
    >>> import string
    >>> result in string.ascii_letters
    True
"""

# Given
PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
      'ł': 'l', 'ń': 'n', 'ó': 'o',
      'ś': 's', 'ż': 'z', 'ź': 'z'}

# Solution
letter = input('Type single letter: ').strip().lower()
result = PL.get(letter, letter)
