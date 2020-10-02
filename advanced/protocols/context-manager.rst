.. _Context Managers:

****************
Context Managers
****************


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


    astronauts = [
        {'pesel': '61041212345', 'firstname': 'José', 'lastname': 'Jiménez'},
        {'pesel': '61041212346', 'firstname': 'Jan', 'lastname': 'Twardowski'},
        {'pesel': '61041212347', 'firstname': 'Melissa', 'lastname': 'Lewis'},
        {'pesel': '61041212348', 'firstname': 'Alex', 'lastname': 'Vogel'},
        {'pesel': '61041212349', 'firstname': 'Ryan', 'lastname': 'Stone'},
    ]


    with sqlite3.connect(':memory:') as db:
        db.execute(SQL_CREATE_TABLE)
        db.executemany(SQL_INSERT, astronauts)

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


Contextmanager decorator
========================
* Split function for before and after ``yield``
* Code before ``yield`` becomes ``__enter__()``
* Code after ``yield`` becomes ``__exit__()``

``contextmanager`` decorator
----------------------------
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

ContextDecorator class
----------------------
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

.. code-block:: python

    from time import time


    class Timeit:
        def __init__(self, name):
            self.name = name

        def __enter__(self):
            self.start = time()
            return self

        def __exit__(self, *arg, **kwargs):
            end = time()
            duration = (end - self.start) * 10e6
            print(f'Duration of {self.name} is {duration:.2f} µs (microsecond)')


    a = 'a'
    b = 'b'

    with Timeit('f-string'):
        f'result of a+b is: {a} {b}'

    with Timeit('string concat'):
        'result of a+b is: ' + a + b

    with Timeit('str.format()'):
        'result of a+b is: {0}{1}'.format(a, b)

    with Timeit('%-style'):
        'result of a+b is: %s%s' % (a, b)

    # Duration of f-string is 21.46 µs (microsecond)
    # Duration of string concat is 9.54 µs (microsecond)
    # Duration of str.format() is 30.99 µs (microsecond)
    # Duration of %-style is 21.46 µs (microsecond)


Assignments
===========

Protocol ContextManager File
----------------------------
* Assignment name: Protocol ContextManager File
* Last update: 2020-10-02
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/protocol_contextmanager_file.py`

:English:
    #. Use kodu from "Input" section (see below)
    #. Define class ``File`` with parameter: ``filename: str``
    #. ``File`` must implement Context Manager protocol
    #. ``File`` buffers lines added using ``File.append(text: str)`` method
    #. On ``with`` block exit ``File`` class opens file and write buffer

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Stwórz klasę ``File`` z parametrem: ``filename: str``
    #. ``File`` ma implementować protokół Context Manager
    #. ``File`` buforuje linie dodawane za pomocą metody ``File.append(text: str)``
    #. Na wyjściu z bloku ``with`` klasa ``File`` otwiera plik i zapisuje bufor

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

Protocol ContextManagerBuffer
-----------------------------
* Assignment name: Protocol Context Manager Buffer
* Last update: 2020-10-02
* Complexity level: easy
* Lines of code to write: 32 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/protocol_contextmanager_buffer.py`

:English:
    #. Use kodu from "Input" section (see below)
    #. Set max buffer limit to 100 bytes
    #. File has to be written to disk every X bytes of buffer
    #. How to make buffer save data every X seconds?
    #. Writing and reading takes time, how to make buffer save data in the background, but it could be still used?

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Ustaw maksymalny limit bufora na 100 bajtów
    #. Plik na dysku ma być zapisywany co X bajtów bufora
    #. Jak zrobić, aby bufor zapisywał dane na dysku co X sekund?
    #. Operacje zapisu i odczytu trwają, jak zrobić, aby do bufora podczas zapisu na dysk, nadal można było pisać?

:Input:

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
        ...    file.append('Three')
        ...    file.append('Four')
        ...    file.append('Five')
        ...    file.append('Six')

