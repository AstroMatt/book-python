.. _Protocol Context Manager:

***************
Context Manager
***************


Rationale
=========
* Files
* Buffering data
* Database connection
* Database transactions
* Database cursors
* Locks
* Network sockets
* Network streams
* HTTP sessions


Protocol
========
* ``__enter__(self) -> self``
* ``__exit__(self, *args) -> None``

.. code-block:: python

    class ContextManager:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return None

.. code-block:: python

    with ContextManager as cm:
        ...


Example
=======
.. code-block:: python

    class MyClass:
        def __enter__(self):
            print('Entering the block')
            return self

        def __exit__(self, *args):
            print('Exiting the block')
            return None

        def do_something(self):
            print('I am inside')


    with MyClass() as my:
        my.do_something()

    # Entering the block
    # I am inside
    # Exiting the block

.. code-block:: python

    class Rocket:
        def __enter__(self):
            print('Launching')
            return self

        def __exit__(self, *args):
            print('Landing')

        def fly_to_space(self):
            print('I am in space!')


    with Rocket() as rocket:
        rocket.fly_to_space()

    # Launching
    # I am in space!
    # Landing


Inheritance
===========
.. code-block:: python

    from contextlib import ContextDecorator
    from time import time


    class Timeit(ContextDecorator):
        def __enter__(self):
            self.start = time()
            return self

        def __exit__(self, *args):
            end = time()
            print(f'Duration {end-self.start:.2f} seconds')


    @Timeit()
    def myfunction():
        list(range(100_000_000))


    myfunction()
    # Duration 3.90 seconds


Decorator
=========
* Split function for before and after ``yield``
* Code before ``yield`` becomes ``__enter__()``
* Code after ``yield`` becomes ``__exit__()``

.. code-block:: python

    from contextlib import contextmanager
    from time import time


    @contextmanager
    def timeit():
        start = time()
        yield
        end = time()
        print(f'Duration {end-start:.4f} seconds')


    with timeit():
        list(range(100_000_000))

    # Duration 4.0250 seconds

.. code-block:: python

    from contextlib import contextmanager


    @contextmanager
    def tag(name):
        print(f'<{name}>')
        yield
        print(f'</{name}>')


    with tag('p'):
        print('foo')

    # <p>
    # foo
    # </p>


Use Cases
=========

Files
-----
.. code-block:: python

    f = open(FILE)

    try:
        content = f.read()
    finally:
        f.close()

.. code-block:: python

    with open(FILE) as f:
        content = f.read()

Database
--------
.. code-block:: python

    import sqlite3


    SQL_CREATE_TABLE = """
        CREATE TABLE IF NOT EXISTS astronauts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pesel INTEGER UNIQUE,
            firstname TEXT,
            lastname TEXT)"""
    SQL_INSERT = 'INSERT INTO astronauts VALUES (NULL, :pesel, :firstname, :lastname)'
    SQL_SELECT = 'SELECT * from astronauts'

    DATA = [
        {'pesel': '61041212345', 'firstname': 'José', 'lastname': 'Jiménez'},
        {'pesel': '61041212346', 'firstname': 'Jan', 'lastname': 'Twardowski'},
        {'pesel': '61041212347', 'firstname': 'Melissa', 'lastname': 'Lewis'},
        {'pesel': '61041212348', 'firstname': 'Alex', 'lastname': 'Vogel'},
        {'pesel': '61041212349', 'firstname': 'Ryan', 'lastname': 'Stone'},
    ]


    with sqlite3.connect(':memory:') as db:
        db.execute(SQL_CREATE_TABLE)
        db.executemany(SQL_INSERT, DATA)

        for row in db.execute(SQL_SELECT):
            print(row)

Lock
----
.. code-block:: python

    from threading import Lock

    # Make lock
    lock = Lock()

    # Use lock
    lock.acquire()

    try:
        print('Critical section 1')
        print('Critical section 2')
    finally:
        lock.release()

.. code-block:: python

    from threading import Lock

    # Make lock
    lock = Lock()

    # Use lock
    with lock:
        print('Critical section 1')
        print('Critical section 2')

String Microbenchmark
---------------------

.. code-block:: python

    from time import time


    class Timeit:
        def __init__(self, name):
            self.name = name

        def __enter__(self):
            self.start = time()
            return self

        def __exit__(self, *arg):
            end = time()
            print(f'Duration of {self.name} is {end-self.start:.2f} second')


    a = 1
    b = 2
    repetitions = int(1e7)


    with Timeit('f-string'):
        for _ in range(repetitions):
            f'{a}{b}'

    with Timeit('string concat'):
        for _ in range(repetitions):
            a + b

    with Timeit('str.format()'):
        for _ in range(repetitions):
            '{0}{1}'.format(a, b)

    with Timeit('str.format()'):
        for _ in range(repetitions):
            '{}{}'.format(a, b)

    with Timeit('str.format()'):
        for _ in range(repetitions):
            '{a}{b}'.format(a=a, b=b)

    with Timeit('%-style'):
        for _ in range(repetitions):
            '%s%s' % (a, b)

    with Timeit('%-style'):
        for _ in range(repetitions):
            '%d%d' % (a, b)

    with Timeit('%-style'):
        for _ in range(repetitions):
            '%f%f' % (a, b)

    # Duration of f-string is 2.70 second
    # Duration of string concat is 0.68 second
    # Duration of str.format() is 3.46 second
    # Duration of str.format() is 3.37 second
    # Duration of str.format() is 4.85 second
    # Duration of %-style is 2.59 second
    # Duration of %-style is 2.59 second
    # Duration of %-style is 3.82 second


Assignments
===========

Protocol ContextManager File
----------------------------
* Assignment name: Protocol ContextManager File
* Last update: 2020-10-02
* Complexity level: easy
* Lines of code to write: 13 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/protocol_contextmanager_file.py`

:English:
    #. Use data from "Input" section (see below)
    #. Define class ``File`` with parameter: ``filename: str``
    #. ``File`` must implement Context Manager protocol
    #. ``File`` buffers lines added using ``File.append(text: str)`` method
    #. On ``with`` block exit ``File`` class opens file and write buffer
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz klasę ``File`` z parametrem: ``filename: str``
    #. ``File`` ma implementować protokół Context Manager
    #. ``File`` buforuje linie dodawane za pomocą metody ``File.append(text: str)``
    #. Na wyjściu z bloku ``with`` klasa ``File`` otwiera plik i zapisuje bufor
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

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

:Hint:
    * Append newline character (``\n``) before adding to buffer

Protocol ContextManager Buffer
-----------------------------
* Assignment name: Protocol ContextManager Buffer
* Last update: 2020-10-16
* Complexity level: medium
* Lines of code to write: 22 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/protocol_contextmanager_buffer.py`

:English:
    #. Use data from "Input" section (see below)
    #. Define class configuration attribute ``BUFFER_LIMIT: int = 100`` bytes
    #. File has to be written to disk every X bytes of buffer
    #. Writing and reading takes time, how to make buffer save data in the background, but it could be still used?
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj klasowy atrybut konfiguracyjny ``BUFFER_LIMIT: int = 100`` bajtów
    #. Plik na dysku ma być zapisywany co X bajtów bufora
    #. Operacje zapisu i odczytu trwają, jak zrobić, aby do bufora podczas zapisu na dysk, nadal można było pisać?
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        >>> from inspect import isclass, ismethod
        >>> assert isclass(File)
        >>> assert hasattr(File, 'append')
        >>> assert hasattr(File, 'BUFFER_LIMIT')
        >>> assert hasattr(File, '__enter__')
        >>> assert hasattr(File, '__exit__')
        >>> assert ismethod(File(None).append)
        >>> assert ismethod(File(None).__enter__)
        >>> assert ismethod(File(None).__exit__)
        >>> assert FILE.BUFFER_LIMIT == 100

        >>> with File('_temporary.txt') as file:
        ...    file.append('One')
        ...    file.append('Two')
        ...    file.append('Three')
        ...    file.append('Four')
        ...    file.append('Five')
        ...    file.append('Six')

        >>> open('_temporary.txt').read()
        'One\\nTwo\\nThree\\nFour\\nFive\\nSix\\n'

:Hint:
    * ``sys.getsizeof()``

Protocol ContextManager AutoSave
--------------------------------
* Assignment name: Protocol Context Manager AutoSave
* Last update: 2020-10-16
* Complexity level: hard
* Lines of code to write: 32 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/protocol_contextmanager_autosave.py`

:English:
    #. Use data from "Input" section (see below)
    #. Define class configuration attribute ``AUTOSAVE_SECONDS: float = 2.0``
    #. Save buffer content to file every ``AUTOSAVE_SECONDS`` seconds
    #. Writing and reading takes time, how to make buffer save data in the background, but it could be still used?
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj klasowy atrybut konfiguracyjny ``AUTOSAVE_SECONDS: float = 2.0``
    #. Zapisuj zawartość bufora do pliku co ``AUTOSAVE_SECONDS`` sekund
    #. Operacje zapisu i odczytu trwają, jak zrobić, aby do bufora podczas zapisu na dysk, nadal można było pisać?
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        >>> from inspect import isclass, ismethod
        >>> assert isclass(File)
        >>> assert hasattr(File, 'append')
        >>> assert hasattr(File, 'AUTOSAVE_SECONDS')
        >>> assert hasattr(File, '__enter__')
        >>> assert hasattr(File, '__exit__')
        >>> assert ismethod(File(None).append)
        >>> assert ismethod(File(None).__enter__)
        >>> assert ismethod(File(None).__exit__)
        >>> assert FILE.AUTOSAVE_SECONDS == 2.0

        >>> with File('_temporary.txt') as file:
        ...    file.append('One')
        ...    file.append('Two')
        ...    file.append('Three')
        ...    file.append('Four')
        ...    file.append('Five')
        ...    file.append('Six')

        >>> open('_temporary.txt').read()
        'One\\nTwo\\nThree\\nFour\\nFive\\nSix\\n'
