"""
* Assignment: Mapping Dict Items
* Filename: mapping_dict_items.py
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Define `keys: list[str]` with list of `DATA` keys
    3. Define `values: list[str]` with list of `DATA` values
    4. Define `keys: list[tuple]` with list of `DATA` key-value pairs
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj `keys: list[str]` z listą kluczy z `DATA`
    3. Zdefiniuj `values: list[str]` z listą wartości z `DATA`
    4. Zdefiniuj `keys: list[tuple]` z listą par klucz-wartość z `DATA`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(keys)
    <class 'list'>
    >>> type(values)
    <class 'list'>
    >>> type(items)
    <class 'list'>
    >>> all(type(x) is tuple for x in items)
    True
    >>> keys
    ['Sepal length', 'Sepal width', 'Petal length', 'Petal width']
    >>> values
    [5.8, 2.7, 5.1, 1.9]
    >>> items  # doctest: +NORMALIZE_WHITESPACE
    [('Sepal length', 5.8),
     ('Sepal width', 2.7),
     ('Petal length', 5.1),
     ('Petal width', 1.9)]
"""

# Given
DATA = {
    'Sepal length': 5.8,
    'Sepal width': 2.7,
    'Petal length': 5.1,
    'Petal width': 1.9,
}

# Solution
keys = list(DATA.keys())
values = list(DATA.values())
items = list(DATA.items())

