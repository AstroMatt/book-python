"""
* Assignment: Function Generator Iris
* Filename: function_generator_iris.py
* Complexity: easy
* Lines of code: 8 lines
* Estimated time: 8 min

English:
    1. Use code from "Given" section (see below)
    2. Write filter for `DATA` which returns `features` for given `species`
    3. Implement solution using function
    4. Implement solution using generator and `yield` keyword
    5. Compare results of both using `sys.getsizeof()`
    6. What will happen if input data will be bigger?
    7. Note, that in different Python versions you'll get slightly
       different values for getsizeof generator and function:
        a. 112 for generator in Python 3.9
        b. 112 for generator in Python 3.8
        c. 128 for generator in Python 3.7
    8. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Napisz filtr dla `DATA` zwracający `features` dla danego gatunku `species`
    3. Zaimplementuj rozwiązanie wykorzystując funkcję
    4. Zaimplementuj rozwiązanie wykorzystując generator i słowo kluczowe `yield`
    5. Porównaj wyniki obu używając `sys.getsizeof()`
    6. Co się stanie, gdy ilość danych będzie większa?
    7. Zwróć uwagę, że w zależności od wersji Python wartości getsizeof
       dla funkcji i generatora mogą się nieznaczenie różnić:
        a. 112 dla generator w Python 3.9
        b. 112 dla generator w Python 3.8
        c. 128 dla generator w Python 3.7
    8. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from sys import getsizeof
    >>> from inspect import isfunction, isgeneratorfunction
    >>> assert isfunction(function)
    >>> assert isgeneratorfunction(generator)

    >>> list(function(DATA, 'setosa'))
    [[5.1, 3.5, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]]
    >>> list(generator(DATA, 'setosa'))
    [[5.1, 3.5, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]]

    >>> getsizeof(function(DATA, 'setosa'))
    88
    >>> getsizeof(function(DATA*10, 'setosa'))
    248
    >>> getsizeof(function(DATA*100, 'setosa'))
    1656
    >>> getsizeof(generator(DATA, 'setosa'))
    112
    >>> getsizeof(generator(DATA*10, 'setosa'))
    112
    >>> getsizeof(generator(DATA*100, 'setosa'))
    112
"""

# Given
DATA = [(5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa')]


def function(data: list, species: str):
    ...


def generator(data: list, species: str):
    ...


# Solution
def function(data: list, species: str):
    result = []
    for *features, label in data:
        if label == species:
            result.append(features)
    return result


def generator(data: list, species: str):
    for *features, label in data:
        if label == species:
            yield features
