""""
* Assignment: Decorator Function Abspath
* Filename: decorator_func_abspath.py
* Complexity: easy
* Lines of code to write: 1 lines
* Estimated time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Absolute path is when `path` starts with `current_directory`
    3. Create function decorator `abspath`
    4. If `path` is relative, then `abspath` will convert it to absolute
    5. If `path` is absolute, then `abspath` will not modify it
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Ścieżka bezwzględna jest gdy `path` zaczyna się od `current_directory`
    3. Stwórz funkcję dekorator `abspath`
    4. Jeżeli `path` jest względne, to `abspath` zamieni ją na bezwzględną
    5. Jeżeli `path` jest bezwzględna, to `abspath` nie będzie jej modyfikował
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `path = Path(CURRENT_DIR, filename)`

Tests:
    >>> @abspath
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
def abspath(func):
    def wrapper(path):
        path = Path(CURRENT_DIR, path)
        return func(path)
    return wrapper
