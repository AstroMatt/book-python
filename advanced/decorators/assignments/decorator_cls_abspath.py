"""
* Assignment: Decorator Class Abspath
* Filename: decorator_cls_abspath.py
* Complexity: easy
* Lines of code: 10 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Absolute path is when `path` starts with `current_directory`
    3. Create class decorator `Abspath`
    4. If `path` is relative, then `Abspath` will convert it to absolute
    5. If `path` is absolute, then `Abspath` will not modify it
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Ścieżka bezwzględna jest gdy `path` zaczyna się od `current_directory`
    3. Stwórz klasę dekorator `Abspath`
    4. Jeżeli `path` jest względne, to `Abspath` zamieni ją na bezwzględną
    5. Jeżeli `path` jest bezwzględna, to `Abspath` nie będzie jej modyfikował
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `path = Path(CURRENT_DIR, filename)`

Tests:
    >>> @Abspath
    ... def display(path):
    ...     return str(path)

    >>> display('iris.csv').startswith(str(CURRENT_DIR))
    True
    >>> display('iris.csv').endswith('iris.csv')
    True
    >>> display('/home/python/iris.csv')
    '/home/python/iris.csv'
"""

# Given
from pathlib import Path

CURRENT_DIR = Path().cwd()


# Solution
class Abspath:
    def __init__(self, func):
        self._func = func

    def __call__(self, file):
        file = Path(CURRENT_DIR, file)
        return self._func(file)

