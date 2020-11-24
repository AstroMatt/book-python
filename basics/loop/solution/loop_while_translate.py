"""
* Assignment: Loop While Translate
* Filename: loop_while_translate.py
* Complexity: medium
* Lines of code to write: 8 lines
* Estimated time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Define `result: list`
    3. Use `while` to iterate over `DATA`
    4. If letter is in `PL` then use conversion value as letter
    5. Add letter to `result`
    #. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Użyj `while` do iteracji po `DATA`
    3. Jeżeli litera jest w `PL` to użyj skonwertowanej wartości jako litera
    4. Dodaj literę do `result`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> assert type(result) is str
    >>> result
    'zazolc gesla jazn'
"""

# Given
PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
      'ł': 'l', 'ń': 'n', 'ó': 'o',
      'ś': 's', 'ż': 'z', 'ź': 'z'}

DATA = 'zażółć gęślą jaźń'

# Solution
result = []
i = 0

while i < len(DATA):
    letter = DATA[i]
    letter = PL.get(letter, letter)
    result.append(letter)
    i += 1

result = ''.join(result)
