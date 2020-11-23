"""
* Assignment: Sequence List Many
* Filename: sequence_list_many.py
* Complexity: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Create list ``a`` with data from row 1
    3. Create list ``b`` with data from row 2
    4. Create list ``c`` with data from row 3
    5. Do not use values from "Row" column
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz listę ``a`` z danymi z wiersza 1
    3. Stwórz listę ``b`` z danymi z wiersza 2
    4. Stwórz listę ``c`` z danymi z wiersza 3
    5. Nie używaj wartości z kolumny "Row"
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(a)
    <class 'list'>
    >>> type(b)
    <class 'list'>
    >>> type(c)
    <class 'list'>
    >>> a
    [5.8, 2.7, 5.1, 1.9, 'virginica']
    >>> b
    [5.1, 3.5, 1.4, 0.2, 'setosa']
    >>> c
    [5.7, 2.8, 4.1, 1.3, 'versicolor']
"""

# Given
DATA = """
    '5.8', '2.7', '5.1', '1.9', 'virginica',   # row 1
    '5.1', '3.5', '1.4', '0.2', 'setosa',      # row 2
    '5.7', '2.8', '4.1', '1.3', 'versicolor',  # row 3
"""

# Solution
a = [5.8, 2.7, 5.1, 1.9, 'virginica']
b = [5.1, 3.5, 1.4, 0.2, 'setosa']
c = [5.7, 2.8, 4.1, 1.3, 'versicolor']
