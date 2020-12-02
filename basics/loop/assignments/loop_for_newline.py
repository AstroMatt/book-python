"""
* Assignment: Loop For Newline
* Filename: loop_for_newline.py
* Complexity: easy
* Lines of code: 2 lines
* Estimated time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Define `result: str`
    3. Use `for` to iterate over `DATA`
    4. Join lines of text with newline (`\n`) character
    5. Do not use `str.join()`
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj `result: str`
    3. Użyj `for` do iterowania po `DATA`
    4. Połącz linie tekstu znakiem końca linii (`\n`)
    5. Nie używaj `str.join()`
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> assert type(result) is str
    >>> result.count('\\n')
    3
    >>> result
    'We choose to go to the Moon.\\nWe choose to go to the Moon in this decade and do the other things.\\nNot because they are easy, but because they are hard.\\n'
"""

# Given
DATA = ['We choose to go to the Moon.',
        'We choose to go to the Moon in this decade and do the other things.',
        'Not because they are easy, but because they are hard.']

result: str = ''

# Solution
for line in DATA:
    result += line + '\n'
