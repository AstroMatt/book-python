"""
>>> from inspect import isfunction, isgeneratorfunction
>>> assert isfunction(function)
>>> assert isgeneratorfunction(generator)

>>> result  # doctest: +NORMALIZE_WHITESPACE
{'function x1': 88,
 'function x10': 256,
 'function x100': 1664,
 'generator x1': 112,
 'generator x10': 112,
 'generator x100': 112}
"""

from sys import getsizeof


DATA = [
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]


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


result = {
    'function x1': getsizeof(function(DATA, 'setosa')),
    'function x10': getsizeof(function(DATA * 10, 'setosa')),
    'function x100': getsizeof(function(DATA * 100, 'setosa')),
    'generator x1': getsizeof(generator(DATA, 'setosa')),
    'generator x10': getsizeof(generator(DATA * 10, 'setosa')),
    'generator x100': getsizeof(generator(DATA * 100, 'setosa')),
}
