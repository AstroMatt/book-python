"""
* Assignment: Sequence Tuple Select
* Filename: sequence_tuple_select.py
* Complexity: easy
* Lines of code to write: 1 lines
* Estimated time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Create a `tuple` representing all species
    3. To convert table use multiline select with `alt` key in your IDE
    4. Do not use `slice`, `getitem`, `for`, `while` or any other control-flow statement
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz `tuple` z nazwami gatunków
    3. Do konwersji tabelki wykorzystaj zaznaczanie wielu linijek za pomocą klawisza `alt` w Twoim IDE
    4. Nie używaj `slice`, `getitem`, `for`, `while` lub jakiejkolwiek innej instrukcji sterującej
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `ALT` + `left mouse button` = multiple select
    * `ALT` + `SHIFT` + `left mouse button drag` = vertical selection

Tests:
    >>> type(result)
    <class 'tuple'>
    >>> all(type(x) is str for x in result)
    True
    >>> ('sepal_length' not in result
    ...  and 'sepal_width' not in result
    ...  and 'petal_length' not in result
    ...  and 'petal_width' not in result
    ...  and 'species' not in result)
    True
    >>> len(result)
    5
    >>> result.count('virginica')
    2
    >>> result.count('setosa')
    1
    >>> result.count('versicolor')
    2
"""

# Given
DATA = [
    'sepal_length,sepal_width,petal_length,petal_width,species',
    '5.8,2.7,5.1,1.9,virginica',
    '5.1,3.5,1.4,0.2,setosa',
    '5.7,2.8,4.1,1.3,versicolor',
    '6.3,2.9,5.6,1.8,virginica',
    '6.4,3.2,4.5,1.5,versicolor',
]

# Solution
result = ('virginica', 'setosa', 'versicolor', 'virginica', 'versicolor')
