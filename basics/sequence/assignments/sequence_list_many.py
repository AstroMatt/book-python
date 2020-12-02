"""
* Assignment: Sequence List Many
* Filename: sequence_list_many.py
* Complexity: easy
* Lines of code: 3 lines
* Estimated time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Create list `a` with data from row 1
    3. Create list `b` with data from row 2
    4. Create list `c` with data from row 3
    5. Do not use `str.split()`, `slice`, `getitem`, `for`, `while` or any other control-flow statement
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz listę `a` z danymi z wiersza 1
    3. Stwórz listę `b` z danymi z wiersza 2
    4. Stwórz listę `c` z danymi z wiersza 3
    5. Nie używaj `str.split()`, `slice`, `getitem`, `for`, `while` lub jakiejkolwiek innej instrukcji sterującej
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(a)
    <class 'list'>
    >>> type(b)
    <class 'list'>
    >>> type(c)
    <class 'list'>
    >>> len(a)
    5
    >>> len(b)
    5
    >>> len(c)
    5
    >>> (5.8 in a
    ...  and 2.7 in a
    ...  and 5.1 in a
    ...  and 1.9 in a
    ...  and 'virginica' in a)
    True
    >>> (5.1 in b
    ...  and 3.5 in b
    ...  and 1.4 in b
    ...  and 0.2 in b
    ...  and 'setosa' in b)
    True
    >>> (5.7 in c
    ...  and 2.8 in c
    ...  and 4.1 in c
    ...  and 1.3 in c
    ...  and 'versicolor' in c)
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
a = [5.8, 2.7, 5.1, 1.9, 'virginica']
b = [5.1, 3.5, 1.4, 0.2, 'setosa']
c = [5.7, 2.8, 4.1, 1.3, 'versicolor']
