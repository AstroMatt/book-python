""""
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


def abspath(func):
    def wrapper(path):
        current_directory = Path().cwd()
        path = Path(current_directory, path)
        return func(path)
    return wrapper


@abspath
def display(path):
    return str(path)
