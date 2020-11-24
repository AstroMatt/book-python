"""
* Assignment: Sequence Frozenset Newline
* Filename: sequence_frozenset_newline.py
* Complexity: easy
* Lines of code to write: 1 lines
* Estimated time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Define `result: str`
    3. Use `str.join()` to join lines of text with newline (`\n`) character
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj `result: str`
    3. Użyj `str.join()` aby połączyć linie tekstu znakiem końca linii (`\n`)
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'str'>
    >>> len(result)
    150
    >>> 'We choose to go to the Moon.' in result
    True
    >>> 'We choose to go to the Moon in this decade and do the other things.' in result
    True
    >>> 'Not because they are easy, but because they are hard.' in result
    True
    >>> result.count('\\n')
    2
"""

# Given
DATA = frozenset({
    'We choose to go to the Moon.',
    'We choose to go to the Moon in this decade and do the other things.',
    'Not because they are easy, but because they are hard.'})

# Solution
result = '\n'.join(DATA)
