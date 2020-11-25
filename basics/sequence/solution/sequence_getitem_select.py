"""
* Assignment: Sequence GetItem Select
* Filename: sequence_getitem_select.py
* Complexity: easy
* Lines of code to write: 10 lines
* Estimated time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Write header (row with index 0) to `header: tuple` variable
    3. Create `result: list`
    4. Select row at index 2, convert it to `list` and add to `result`
    5. Select row at index 4, convert it to `tuple` and add to `result`
    6. Select row at index -2, convert it to `set` and add to `result`
    7. Select row at index -4, convert it to `frozenset` and add to `result`
    8. Append to `result`: empty `list`, empty `tuple`, empty `set` and empty `frozenset`
    9. Use only indexes (`getitem`)
    10. Do not use `str.split()`, `slice`, `for`, `while` or any other control-flow statement
    11. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zapisz nagłówek (wiersz o indeksie 0) do zmiennej `header: tuple`
    3. Stwórz `result: list`
    4. Wybierz wiersz o indeksie 2, przekonwertuj go do `list` i dodaj do `result`
    5. Wybierz wiersz o indeksie 4, przekonwertuj go do `tuple` i dodaj do `result`
    6. Wybierz wiersz o indeksie -4, przekonwertuj go do `set` i dodaj do `result`
    7. Wybierz wiersz o indeksie -2, przekonwertuj go do `frozenset` i dodaj do `result`
    8. Dodaj na koniec `result`: pustą `list`, pustą `tuple`, pusty `set`, pusty `frozenset`
    9. Korzystaj tylko z indeksów (`getitem`)
    10. Nie używaj `str.split()`, `slice`, `getitem`, `for`, `while` lub jakiejkolwiek innej instrukcji sterującej
    11. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(header)
    <class 'tuple'>
    >>> type(result)
    <class 'list'>
    >>> ('sepal_length' not in result
    ...  and 'sepal_width' not in result
    ...  and 'petal_length' not in result
    ...  and 'petal_width' not in result
    ...  and 'species' not in result)
    True
    >>> len(result)
    8
    >>> header
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species')
    >>> [5.1, 3.5, 1.4, 0.2, 'setosa'] in result
    True
    >>> (6.3, 2.9, 5.6, 1.8, 'virginica') in result
    True
    >>> {1.3, 2.8, 4.1, 5.7, 'versicolor'} in result
    True
    >>> frozenset({1.5, 3.2, 4.5, 6.4, 'versicolor'}) in result
    True
    >>> list() in result
    True
    >>> tuple() in result
    True
    >>> set() in result
    True
    >>> frozenset() in result
    True
"""

# Given
DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa')]

# Solution
header = DATA[0]
result = []

result.append(list(DATA[2]))
result.append(tuple(DATA[4]))
result.append(set(DATA[-4]))
result.append(frozenset(DATA[-2]))

result.append(list())
result.append(tuple())
result.append(set())
result.append(frozenset())

