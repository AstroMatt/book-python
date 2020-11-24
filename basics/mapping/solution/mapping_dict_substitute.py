"""
* Assignment: Mapping Dict Substitute
* Filename: mapping_dict_substitute.py
* Complexity: easy
* Lines of code to write: 2 lines
* Estimated time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Ask user to input single letter
    3. Convert to lowercase
    4. If letter is in ``PL`` then use conversion value as letter
    5. Print letter

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Poproś użytkownika o wprowadzenie jednej litery
    3. Przekonwertuj literę na małą
    4. Jeżeli litera jest w ``PL`` to użyj przekonwertowanej wartości jako litera
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
"""

# Given
PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
      'ł': 'l', 'ń': 'n', 'ó': 'o',
      'ś': 's', 'ż': 'z', 'ź': 'z'}

# Solution
letter = input('Type single letter: ').strip().lower()
result = PL.get(letter, letter)
