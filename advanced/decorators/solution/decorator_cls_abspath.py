"""
>>> from pathlib import Path
>>> cwd = str(Path().cwd())
>>> display('iris.csv').startswith(cwd)
True
>>> display('iris.csv').endswith('iris.csv')
True
>>> display('/home/python/iris.csv')
'/home/python/iris.csv'
"""

from pathlib import Path


class Abspath:
    def __init__(self, func):
        self._func = func

    def __call__(self, file):
        current_directory = Path().cwd()
        file = Path(current_directory, file)
        return self._func(file)


@Abspath
def display(path):
    return str(path)
