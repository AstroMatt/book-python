"""
* Assignment: Unpacking Arguments Define
* Filename: unpacking_arguments_define.py
* Complexity: medium
* Lines of code to write: 15 lines
* Estimated time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Create function `mean(*args)`, which calculates arithmetic mean for `args`
    3. Do not import any libraries and modules
    4. Define `result: list[tuple[str, float]]`
    5. Iterate over `DATA` separating `features` from `label`
    6. To `result` append `label` and arithmetic mean of `features`
    7. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Stwórz funkcję `mean(*args)`, która liczy średnią arytmetyczną dla `args`
    3. Nie importuj żadnych bibliotek i modułów
    4. Zdefiniuj `result: list[tuple[str, float]]`
    5. Iteruj po `DATA` separując `features` od `label`
    6. Do `result` dodawaj `label` oraz wynik średniej arytmetycznej `features`
    7. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> mean(1)
    1.0
    >>> mean(1, 3)
    2.0
    >>> mean(1, 2, 3)
    2.0
    >>> mean()
    Traceback (most recent call last):
    ValueError: At least one argument is required

    >>> assert type(result) is list
    >>> assert all(type(row) is tuple for row in result)

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [('virginica', 3.875),
     ('setosa', 2.65),
     ('versicolor', 3.475),
     ('virginica', 6.0),
     ('versicolor', 3.95),
     ('setosa', 4.7)]

"""

# Given
DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 5.7, 'virginica'),
        (6.4, 1.5, 'versicolor'),
        (4.7,  'setosa')]


# Solution
def mean(*args):
    if not args:
        raise ValueError('At least one argument is required')

    return sum(args) / len(args)


result = [(label, mean(*features))
          for *features, label in DATA[1:]]
