"""
>>> from inspect import isclass, ismethod
>>> assert isclass(File)
>>> assert hasattr(File, 'append')
>>> assert hasattr(File, '__enter__')
>>> assert hasattr(File, '__exit__')
>>> assert ismethod(File(None).append)
>>> assert ismethod(File(None).__enter__)
>>> assert ismethod(File(None).__exit__)

>>> with File('_temporary.txt') as file:
...    file.append('One')
...    file.append('Two')

>>> open('_temporary.txt').read()
'One\\nTwo\\n'
"""


class File:
    filename: str
    content: list[str]

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.content = list()

    def append(self, line: str) -> None:
        self.content.append(line + '\n')

    def __enter__(self) -> 'File':
        return self

    def __exit__(self, *arg) -> None:
        with open(self.filename, mode='w') as file:
            file.writelines(self.content)
