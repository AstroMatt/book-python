.. _OOP Constructor:

***********
Constructor
***********


Rationale
=========
.. code-block:: python

    my = MyClass()

.. code-block:: python

    instance = MyClass.__new__()
    instance.__init__()


Example
=======
.. code-block:: python

    class Astronaut:
        def __new__(cls):
            return super().__new__(cls)

        def __init__(self):
            pass


    Astronaut()
    # Astronaut.__new__() called
    # Astronaut.__init__() called


New Method
==========
.. highlights::
    * the constructor
    * solely for creating the object
    * ``cls`` as it's first parameter
    * when calling ``__new__()`` you actually don't have an instance yet, therefore no ``self`` exists at that moment

.. code-block:: python

    class Astronaut:
        def __new__(cls):
            print(f'Astronaut.__new__() called')
            return super().__new__(cls)

    Astronaut()
    # Astronaut.__new__() called


Init Method
===========
.. highlights::
    * the initializer
    * for initializing object with data
    * ``self`` as it's first parameter
    * ``__init__()`` is called after ``__new__()`` and the instance is in place, so you can use ``self`` with it
    * it's purpose is just to alter the fresh state of the newly created instance

.. code-block:: python

    class Astronaut:
        def __init__(self):
            print('Astronaut.__init__() called')

    Astronaut()
    # Astronaut.__init__() called


Return
======
.. code-block:: python

    class Astronaut:
        def __new__(cls):
            print('Astronaut.__new__() called')
            return super().__new__(cls)

        def __init__(self):
            print('Astronaut.__init__() called')


    Astronaut()
    # Astronaut.__new__() called
    # Astronaut.__init__() called


.. code-block:: python
    :caption: Missing ``return`` from constructor. The instantiation is evaluated to ``None`` since we don't return anything from the constructor.

    class Astronaut:
        def __new__(cls):
            print('Astronaut.__new__() called')

        def __init__(self):
            print('Astronaut.__init__() called')  # -> is actually never called


    Astronaut()
    # Astronaut.__new__() called

.. code-block:: python
    :caption: Return invalid from constructor

    class Astronaut:
        def __new__(cls):
            print('Astronaut.__new__() called')
            return 1337

    Astronaut()
    # Astronaut.__new__() called
    # 1337

.. code-block:: python
    :caption: Return invalid from initializer

    class Astronaut:
        def __init__(self):
            print('Astronaut.__new__() called')
            return 1337

    Astronaut()
    # Traceback (most recent call last):
    # TypeError: __init__() should return None, not 'int'


Use Cases
=========
* Factory method
* Could be used to implement Singleton

.. code-block:: python

    class PDF:
        pass

    class Docx:
        pass

    class Document:
        def __new__(cls, *args, **kwargs):
            filename, extension = args[0].split('.')

            if extension == 'pdf':
                return PDF()
            elif extension == 'docx':
                return Docx()


    file1 = Document('myfile.pdf')
    file2 = Document('myfile.docx')

    print(file1)
    # <__main__.PDF object at 0x10f89afa0>

    print(file2)
    # <__main__.Docx object at 0x10f6fe9a0>

.. code-block:: python

    DATA = [(5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa')]


    class Iris:
        def __new__(cls, *args, **kwargs):
            *measurements, species = args

            if species == 'setosa':
                cls = Setosa
            elif species == 'versicolor':
                cls = Versicolor
            elif species == 'virginica':
                cls = Virginica
            else:
                raise TypeError

            return super().__new__(cls)

        def __init__(self, sepal_length, sepal_width,
                     petal_length, petal_width, species):

            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width

        def __repr__(self):
            cls = self.__class__.__name__
            args = tuple(self.__dict__.values())
            return f'\n{cls}{args}'

    class Setosa(Iris):
        pass

    class Virginica(Iris):
        pass

    class Versicolor(Iris):
        pass


    result = [Iris(*row) for row in DATA]
    result
    # [Virginica(5.8, 2.7, 5.1, 1.9),
    #  Setosa(5.1, 3.5, 1.4, 0.2),
    #  Versicolor(5.7, 2.8, 4.1, 1.3),
    #  Virginica(6.3, 2.9, 5.6, 1.8),
    #  Versicolor(6.4, 3.2, 4.5, 1.5),
    #  Setosa(4.7, 3.2, 1.3, 0.2)]




Do not trigger methods for user
===============================
* It is better when user can choose a moment when call ``.connect()`` method

.. code-block:: python
    :caption: Let user to call method

    class Server:
        def __init__(self, host, username, password=None):
            self.host = host
            self.username = username
            self.password = password
            self.connect()    # Better ask user to ``connect()`` explicitly

        def connect(self):
            print(f'Logging to {self.host} using: {self.username}:{self.password}')


    connection = Server(
        host='example.com',
        username='myusername',
        password='mypassword')

.. code-block:: python
    :caption: Let user to call method

    class Server:
        def __init__(self, host, username, password=None):
            self.host = host
            self.username = username
            self.password = password

        def connect(self):
            print(f'Logging to {self.host} using: {self.username}:{self.password}')


    connection = Server(
        host='example.com',
        username='myusername',
        password='mypassword')

    connection.connect()

.. code-block:: python
    :caption: However... it is better to use ``self.set_position(position_x, position_y)`` than to set those values one by one and duplicate code. Imagine if there will be a condition boundary checking (for example for negative values)

    class Bad:
        def __init__(self, position_x=0, position_y=0):
            self.position_x = position_x
            self.position_y = position_y

        def set_position(self, x, y):
            self.position_x = x
            self.position_y = y


    class Good:
        def __init__(self, position_x=0, position_y=0):
            self.set_position(position_x, position_y)

        def set_position(self, x, y):
            self.position_x = x
            self.position_y = y

.. code-block:: python

    class Bad:
        def __init__(self, position_x=0, position_y=0):
            self.position_x = min(1024, max(0, position_x))
            self.position_y = min(1024, max(0, position_y))

        def set_position(self, x, y):
            self.position_x = min(1024, max(0, x))
            self.position_y = min(1024, max(0, y))


    class Good:
        def __init__(self, position_x=0, position_y=0):
            self.set_position(position_x, position_y)

        def set_position(self, x, y):
            self.position_x = min(1024, max(0, x))
            self.position_y = min(1024, max(0, y))

Use Cases
=========
.. code-block:: python
    :caption: Note, that this unfortunately does not work this way. ``Path()`` always returns ``PosixPath``

    from pathlib import Path

    Path('/etc/passwd')
    # PosixPath('/etc/passwd')

    Path('c:\\Users\\Admin\\myfile.txt')
    # WindowsPath('c:\\Users\\Admin\\myfile.txt')

    Path(r'C:\Users\Admin\myfile.txt')
    # WindowsPath('C:\\Users\\Admin\\myfile.txt')

    Path(r'C:/Users/Admin/myfile.txt')
    # WindowsPath('C:/Users/Admin/myfile.txt')


Assignments
===========

.. literalinclude:: assignments/oop_constructor_syntax.py
    :caption: :download:`Solution <assignments/oop_constructor_syntax.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_constructor_passwd.py
    :caption: :download:`Solution <assignments/oop_constructor_passwd.py>`
    :end-before: # Solution
