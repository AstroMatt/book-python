"""
* Assignment: Sequence Slice Text
* Filename: sequence_slice_text.py
* Complexity: easy
* Lines of code to write: 8 lines
* Estimated time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Remove title and military rank in each variable
    3. Remove also whitespaces at the beginning and end of a text
    4. Use only `slice` to clean text
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Usuń tytuł naukowy i stopień wojskowy z każdej zmiennej
    3. Usuń również białe znaki na początku i końcu tekstu
    4. Użyj tylko `slice` do oczyszczenia tekstu
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> example
    'Mark Watney'
    >>> a
    'Jan Twardowski'
    >>> b
    'Jan Twardowski'
    >>> c
    'Mark Watney'
    >>> d
    'Melissa Lewis'
    >>> e
    'Ryan Stone'
    >>> f
    'Ryan Stone'
    >>> g
    'Jan Twardowski'
"""

# Given
example = 'lt. Mark Watney, PhD'
a = 'dr hab. inż. Jan Twardowski, prof. AATC'
b = 'gen. pil. Jan Twardowski'
c = 'Mark Watney, PhD'
d = 'lt. col. ret. Melissa Lewis'
e = 'dr n. med. Ryan Stone'
f = 'Ryan Stone, MD-PhD'
g = 'lt. col. Jan Twardowski\t'

example = example[4:-5]

# Solution
a = a[13:-12]
b = b[10:]
c = c[:-5]
d = d[14:]
e = e[11:]
f = f[:-8]
g = g[9:-1]
