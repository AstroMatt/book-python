"""
* Assignment: Protocol Context Manager AutoSave
* Filename: protocol_contextmanager_autosave.py
* Complexity: hard
* Lines of code: 32 lines
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
"""

# Solution
import logging
from threading import Timer

logging.basicConfig(
    level='DEBUG',
    datefmt='"%Y-%m-%d", "%H:%M:%S"',
    format='{asctime}, "{levelname}", "{message}"',
    # filename='_temporary.log',
    style='{')

log = logging.getLogger(__name__)


class File:
    AUTOSAVE_SECONDS: float = 1.0

    filename: str
    content: list[str]
    exit: bool

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.content = list()
        self.exit = False

    def append(self, line: str) -> None:
        self.content.append(line + '\n')

    def _write(self):
        with open(self.filename, mode='a') as file:
            file.writelines(self.content)
        self.content = []

    def _autosave(self):
        log.debug('Setting autosave timer')
        if self.content:
            self._write()
        if not self.exit:
            self._timer = Timer(interval=self.AUTOSAVE_SECONDS,
                                function=self._autosave)
            self._timer.start()

    def __enter__(self) -> 'File':
        with open(self.filename, mode='w') as file:
            file.writelines(self.content)
        self.exit = False
        self._autosave()
        return self

    def __exit__(self, *arg) -> None:
        self.exit = True
        self._write()
        self._timer.join()
