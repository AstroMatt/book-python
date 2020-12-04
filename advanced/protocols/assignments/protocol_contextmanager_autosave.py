"""
* Assignment: Protocol Context Manager AutoSave
* Filename: protocol_contextmanager_autosave.py
* Complexity: hard
* Lines of code: 28 lines
* Time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. Define class configuration attribute `AUTOSAVE_SECONDS: float = 1.0`
    3. Save buffer content to file every `AUTOSAVE_SECONDS` seconds
    4. Writing and reading takes time, how to make buffer save data in the background, but it could be still used?
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj klasowy atrybut konfiguracyjny `AUTOSAVE_SECONDS: float = 1.0`
    3. Zapisuj zawartość bufora do pliku co `AUTOSAVE_SECONDS` sekund
    4. Operacje zapisu i odczytu trwają, jak zrobić, aby do bufora podczas zapisu na dysk, nadal można było pisać?
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hint:
    * `from threading import Timer`
    * `timer = Timer(interval, function)`
    * `timer.start()`
    * `timer.cancel()`
    * `ctrl+c` or stop button kills infinite loop

Tests:
    >>> from inspect import isclass, ismethod
    >>> assert isclass(File)
    >>> assert hasattr(File, 'append')
    >>> assert hasattr(File, 'AUTOSAVE_SECONDS')
    >>> assert hasattr(File, '__enter__')
    >>> assert hasattr(File, '__exit__')
    >>> assert ismethod(File(None).append)
    >>> assert ismethod(File(None).__enter__)
    >>> assert ismethod(File(None).__exit__)
    >>> assert File.AUTOSAVE_SECONDS == 1.0

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
from threading import Timer


# Solution
class File:
    AUTOSAVE_SECONDS: float = 1.0
    _content: list[str]
    _timer: Timer
    filename: str

    def __init__(self, filename):
        self.filename = filename
        self._content = list()

    def _set_timer(self):
        if hasattr(self, '_timer'):
            self._timer.cancel()
        self._timer = Timer(self.AUTOSAVE_SECONDS, self._writefile)
        self._timer.start()

    def __enter__(self):
        with open(self.filename, mode='w') as file:
            file.write('')
        self._set_timer()
        return self

    def __exit__(self, *args):
        self._writefile()
        self._timer.cancel()

    def _writefile(self):
        with open(self.filename, mode='a') as file:
            file.writelines(self._content)
        self._content = []
        self._set_timer()

    def append(self, line):
        self._content.append(line+'\n')
