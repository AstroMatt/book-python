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

from typing import List

FILE = r'/tmp/_temporary.json'


class BufferedFile:
    def __init__(self, file: str, max_buffer_size: int = 100) -> None:
        self._file: str = file
        self._max_buffer_size = max_buffer_size

    def __enter__(self):
        self._buffer: List[str] = []
        self.write(mode='w')
        return self

    def __exit__(self, *args):
        self.write(mode='a')
        self._buffer = []

    def write(self, mode='w'):
        data, self._buffer = self._buffer, []

        with open(self._file, mode=mode) as file:
            file.writelines(data)

    def append_line(self, line):
        self._buffer.append(line + '\n')

        if file._buffer.__sizeof__() >= self._max_buffer_size:
            self.write(mode='a')

    def truncate(self):
        self._buffer = []

    def read(self):
        with open(self._file) as file:
            return file.read()


with BufferedFile(FILE) as file:
    file.append_line('One')
    file.append_line('Two')
    file.append_line('Three')
    file.append_line('Four')
    file.append_line('Five')
    file.append_line('Six')

    print(file.read())

    # file.truncate()
    # print(file.read())
