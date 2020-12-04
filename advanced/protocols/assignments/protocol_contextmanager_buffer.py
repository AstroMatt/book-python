"""
* Assignment: Protocol ContextManager Buffer
* Filename: protocol_contextmanager_buffer.py
* Complexity: medium
* Lines of code: 21 lines
* Time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. Define class configuration attribute `BUFFER_LIMIT: int = 100` bytes
    3. File has to be written to disk every X bytes of buffer
    4. Writing and reading takes time, how to make buffer save data in the background, but it could be still used?
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj klasowy atrybut konfiguracyjny `BUFFER_LIMIT: int = 100` bajtów
    3. Plik na dysku ma być zapisywany co X bajtów bufora
    4. Operacje zapisu i odczytu trwają, jak zrobić, aby do bufora podczas zapisu na dysk, nadal można było pisać?
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `sys.getsizeof(obj)` returns `obj` size in bytes

Tests:
    >>> from inspect import isclass, ismethod
    >>> assert isclass(File)
    >>> assert hasattr(File, 'append')
    >>> assert hasattr(File, 'BUFFER_LIMIT')
    >>> assert hasattr(File, '__enter__')
    >>> assert hasattr(File, '__exit__')
    >>> assert ismethod(File(None).append)
    >>> assert ismethod(File(None).__enter__)
    >>> assert ismethod(File(None).__exit__)
    >>> assert File.BUFFER_LIMIT == 100

    >>> with File('_temporary.txt') as file:
    ...    file.append('One')
    ...    file.append('Two')
    ...    file.append('Three')
    ...    file.append('Four')
    ...    file.append('Five')
    ...    file.append('Six')

    >>> open('_temporary.txt').read()
    'One\\nTwo\\nThree\\nFour\\nFive\\nSix\\n'
    >>> from os import remove
    >>> remove('_temporary.txt')
"""

# Given
from sys import getsizeof


# Solution
class File:
    BUFFER_LIMIT: int = 100
    _content: list[str]
    filename: str

    def __init__(self, filename):
        self.filename = filename
        self._content = list()

    def __enter__(self):
        with open(self.filename, mode='w') as file:
            file.write('')
        return self

    def __exit__(self, *args):
        self._writefile()

    def _writefile(self):
        with open(self.filename, mode='a') as file:
            file.writelines(self._content)
            self._content = []

    def append(self, line):
        self._content.append(line + '\n')
        if getsizeof(self._content) > self.BUFFER_LIMIT:
            self._writefile()
