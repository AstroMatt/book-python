Context Manager
===============


Rationale
---------
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
--------
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
-------
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
-----------
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
---------
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


Use Case - Files
----------------
.. code-block:: python

    f = open(FILE)

    try:
        content = f.read()
    finally:
        f.close()

.. code-block:: python

    with open(FILE) as f:
        content = f.read()

.. code-block:: text

    uint32_max = 4_294_967_295
    char* file[uint32_max];

    file[0] = '/tmp/myfile1.txt'
    file[1] = '/tmp/myfile2.txt'
    file[2] = '/tmp/myfile3.txt'
    ...
    file[4_294_967_295] = '/tmp/myfileX.txt'
    file[4_294_967_296] -> KernelPanic


Use Case - Database
-------------------
.. code-block:: python

    import sqlite3

    SQL_CREATE_TABLE = """
        CREATE TABLE IF NOT EXISTS astronauts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            age INTEGER
        )
    """

    SQL_INSERT = """
        INSERT INTO astronauts VALUES(NULL, :firstname, :lastname, :age)
    """

    SQL_SELECT = """
        SELECT * FROM astronauts
    """

    DATA = [
        {'firstname': 'Jan', 'lastname': 'Twardowski', 'age': 44},
        {'firstname': 'Mark', 'lastname': 'Watney', 'age': 33},
        {'firstname': 'Melissa', 'lastname': 'Lewis', 'age': 36},
    ]


    with sqlite3.connect('/tmp/mydatabase.db') as db:
        db.execute(SQL_CREATE_TABLE)
        db.executemany(SQL_INSERT, DATA)
        db.row_factory = sqlite3.Row
        for row in db.execute(SQL_SELECT):
            print(dict(row))

    # {'id': 1, 'firstname': 'Jan', 'lastname': 'Twardowski', 'age': 44}
    # {'id': 2, 'firstname': 'Mark', 'lastname': 'Watney', 'age': 33}
    # {'id': 3, 'firstname': 'Melissa', 'lastname': 'Lewis', 'age': 36}


Use Case - Lock
---------------
.. code-block:: python

    from threading import Lock


    lock = Lock()
    lock.acquire()

    try:
        print('Critical section 1')
        print('Critical section 2')
    finally:
        lock.release()

.. code-block:: python

    from threading import Lock

    lock = Lock()

    with lock:
        print('Critical section 1')
        print('Critical section 2')


Use Case - Microbenchmark
-------------------------
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
            print(f'Duration of {self.name} is {end - self.start:.2f} second')


    a = 1
    b = 2
    repetitions = int(1e7)

    with Timeit('f-string'):
        for _ in range(repetitions):
            f'{a}{b}'

    with Timeit('string concat'):
        for _ in range(repetitions):
            str(a) + str(b)

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

    # Duration of f-string is 2.94 second
    # Duration of string concat is 5.30 second
    # Duration of str.format() is 3.62 second
    # Duration of str.format() is 3.48 second
    # Duration of str.format() is 5.02 second
    # Duration of %-style is 2.60 second
    # Duration of %-style is 2.71 second
    # Duration of %-style is 4.02 second


Assignments
-----------
.. literalinclude:: assignments/protocol_contextmanager_a.py
    :caption: :download:`Solution <assignments/protocol_contextmanager_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/protocol_contextmanager_b.py
    :caption: :download:`Solution <assignments/protocol_contextmanager_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/protocol_contextmanager_c.py
    :caption: :download:`Solution <assignments/protocol_contextmanager_c.py>`
    :end-before: # Solution
