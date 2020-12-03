"""
* Assignment: Sequence Set Many
* Filename: sequence_set_many.py
* Complexity: easy
* Lines of code: 9 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Non-functional requirements:
        a. Assignmnet verifies creation of `set()` and method `.add()` and `.update()` usage
        b. For simplicity numerical values type as `floats`
        c. Do not use `str.split()`, `slice`, `getitem`, `for`, `while` or any other control-flow statement
        d. Example: instead of '5.8' just type 5.8
    3. Create set `result` representing row with index 1
    4. Values from row at index 2 add to `result` using `.add()` (five calls)
    5. From row at index 3 create `set` and add it to `result` using `.update()` (one call)
    6. From row at index 4 `tuple` and add it to `result` using `.update()` (one call)
    7. From row at index 5 `list` and add it to `result` using `.update()` (one call)
    8. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wymagania niefunkcjonalne:
        a. Zadanie sprawdza tworzenie `set()` oraz użycie metod `.add()` i `.update()`
        b. Dla uproszczenia wartości numeryczne wypisuj jako `float`
        c. Nie używaj `str.split()`, `slice`, `getitem`, `for`, `while` lub jakiejkolwiek innej instrukcji sterującej
        d. Przykład: zamiast '5.8' zapisz 5.8
    3. Stwórz zbiór `result` reprezentujący wiersz o indeksie 1
    4. Wartości z wiersza o indeksie 2 dodawaj do `result` używając `.add()` (pięć wywołań)
    5. Na podstawie wiersza o indeksie 3 stwórz `set` i dodaj go do `result` używając `.update()` (jedno wywołanie)
    6. Na podstawie wiersza o indeksie 4 stwórz `tuple` i dodaj go do `result` używając `.update()` (jedno wywołanie)
    7. Na podstawie wiersza o indeksie 5 stwórz `list` i dodaj go do `result` używając `.update()` (jedno wywołanie)
    8. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'set'>
    >>> ('sepal_length' not in result
    ...  and 'sepal_width' not in result
    ...  and 'petal_length' not in result
    ...  and 'petal_width' not in result
    ...  and 'species' not in result)
    True
    >>> len(result)
    22
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
DATA = ['sepal_length,sepal_width,petal_length,petal_width,species',
        '5.8,2.7,5.1,1.9,virginica',
        '5.1,3.5,1.4,0.2,setosa',
        '5.7,2.8,4.1,1.3,versicolor',
        '6.3,2.9,5.6,1.8,virginica',
        '6.4,3.2,4.5,1.5,versicolor']

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
