"""
* Assignment: Sequence Set Many
* Filename: sequence_set_many.py
* Complexity: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Create set `result` representing first row
    3. Values from second row add to `result` using `.add()`
    4. From third row create `set` and add it to `result` using `.update()`
    5. From fourth row create `tuple` and add it to `result` using `.update()`
    6. From fifth row create `list` and add it to `result` using `.update()`
    7. Print `result`
    8. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz zbiór `result` reprezentujący pierwszy wiersz
    3. Wartości z drugiego wiersza dodawaj do `result` używając `.add()`
    4. Na podstawie trzeciego wiersza stwórz `set` i dodaj go do `result` używając `.update()`
    5. Na podstawie czwartego wiersza stwórz `tuple` i dodaj go do `result` używając `.update()`
    6. Na podstawie piątego wiersza stwórz `list` i dodaj go do `result` używając `.update()`
    7. Wypis `result`
    8. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'set'>
    >>> result >= {5.8, 2.7, 5.1, 1.9, 'virginica'}
    True
    >>> result >= {5.1, 3.5, 1.4, 0.2, 'setosa'}
    True
    >>> result >= {5.7, 2.8, 4.1, 1.3, 'versicolor'}
    True
    >>> result >= {6.3, 2.9, 5.6, 1.8, 'virginica'}
    True
    >>> result >= {6.4, 3.2, 4.5, 1.5, 'versicolor'}
    True
"""

# Given
DATA = """
    '5.8', '2.7', '5.1', '1.9', 'virginica',   # row 1
    '5.1', '3.5', '1.4', '0.2', 'setosa',      # row 2
    '5.7', '2.8', '4.1', '1.3', 'versicolor',  # row 3
    '6.3', '2.9', '5.6', '1.8', 'virginica',   # row 4
    '6.4', '3.2', '4.5', '1.5', 'versicolor',  # row 5
"""

# Solution
result = {5.8, 2.7, 5.1, 1.9, 'virginica'}

result.add(5.1)
result.add(3.5)
result.add(1.4)
result.add(0.2)
result.add('setosa')

result.update({5.7, 2.8, 4.1, 1.3, 'versicolor'})
result.update((6.3, 2.9, 5.6, 1.8, 'virginica'))
result.update([6.4, 3.2, 4.5, 1.5, 'versicolor'])
