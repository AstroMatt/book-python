"""
* Assignment: Sequence Tuple Mean
* Filename: sequence_tuple_mean.py
* Complexity: medium
* Lines of code to write: 8 lines
* Estimated time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Calculate mean for each numerical values column
    3. To convert table use multiline select with `alt` key in your IDE
    7. Do not use `str.split()`, `slice`, `getitem`, `for`, `while` or any other control-flow statement
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wylicz średnią arytmetyczną dla każdej z kolumn numerycznych
    3. Do konwersji tabelki wykorzystaj zaznaczanie wielu linijek za pomocą klawisza `alt` w Twoim IDE
    4. Nie używaj `str.split()`, `slice`, `getitem`, `for`, `while` lub jakiejkolwiek innej instrukcji sterującej
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `mean = sum(...) / len(...)`
    * `ALT` + `left mouse button` = multiple select
    * `ALT` + `SHIFT` + `left mouse button drag` = vertical selection
    * `ALT` + `SHIFT` + `right` = select word to the right (macOS)
    * `ALT` + `SHIFT` + `left` = select word to the left (macOS)
    * `CTRL` + `SHIFT` + `right` = select word to the right (Windows)
    * `CTRL` + `SHIFT` + `left` = select word to the left (Windows)
    * `CTRL` + `right` = jump over the word to the right
    * `CTRL` + `left` = jump over the word to the left
    * `CTRL` + `ALT` + L = Reformat Code on Windows
    * `CMD` + `ALT` + L = Reformat Code on macOS

Tests:
    >>> type(sepal_length)
    <class 'float'>
    >>> type(sepal_width)
    <class 'float'>
    >>> type(petal_length)
    <class 'float'>
    >>> type(petal_width)
    <class 'float'>
    >>> sepal_length
    5.859999999999999
    >>> sepal_width
    3.0200000000000005
    >>> petal_length
    4.14
    >>> petal_width
    1.34
"""

# Given
DATA = ['sepal_length,sepal_width,petal_length,petal_width,species',
        '5.8,2.7,5.1,1.9,virginica',
        '5.1,3.5,1.4,0.2,setosa',
        '5.7,2.8,4.1,1.3,versicolor',
        '6.3,2.9,5.6,1.8,virginica',
        '6.4,3.2,4.5,1.5,versicolor']

# Solution
sepal_length = (5.8, 5.1, 5.7, 6.3, 6.4)
sepal_width = (2.7, 3.5, 2.8, 2.9, 3.2)
petal_length = (5.1, 1.4, 4.1, 5.6, 4.5)
petal_width = (1.9, 0.2, 1.3, 1.8, 1.5)

sepal_length = sum(sepal_length) / len(sepal_length)
sepal_width = sum(sepal_width) / len(sepal_width)
petal_length = sum(petal_length) / len(petal_length)
petal_width = sum(petal_width) / len(petal_width)
