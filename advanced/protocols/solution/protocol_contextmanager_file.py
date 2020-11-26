"""
* Assignment: Protocol ContextManager File
* Filename: protocol_contextmanager_file.py
* Complexity: easy
* Lines of code to write: 13 lines
* Estimated time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Define class `File` with parameter: `filename: str`
    3. `File` must implement Context Manager protocol
    4. `File` buffers lines added using `File.append(text: str)` method
    5. On `with` block exit `File` class opens file and write buffer
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz klasę `File` z parametrem: `filename: str`
    3. `File` ma implementować protokół Context Manager
    4. `File` buforuje linie dodawane za pomocą metody `File.append(text: str)`
    5. Na wyjściu z bloku `with` klasa `File` otwiera plik i zapisuje bufor
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * Append newline character (`\n`) before adding to buffer

Tests:
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

# Solution
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
