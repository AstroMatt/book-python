*********************
Object initialization
*********************


``__call__()``
==============
* ``__call__()`` method invokes the following:

    * ``__new__()``
    * ``__init__()``

.. code-block:: python
    :caption: Intuition definition of ``__new__()`` and ``__init__()``

    class Iris:
        def __call__(cls):
            iris = Iris.__new__(cls)
            iris.__init__()

.. code-block:: python

    class Astronaut:
        pass


    twardowski = Astronaut      # Creates alias to class (not an instance)
    twardowski()                # Creates instance by calling ``.__call__()``

    twardowski = Astronaut()    # Creates instance by calling ``.__call__()``


``__new__()``
=============
* the constructor
* solely for creating the object
* ``cls`` as it's first parameter
* when calling ``__new__()`` you actually don't have an instance yet, therefore no ``self`` exists at that moment

.. code-block:: python
    :emphasize-lines: 2,3,4

    class Iris:
        def __new__(cls):
            print("Iris.__new__() called")
            return super().__new__(cls)

    Iris()
    # Iris.__new__() called


``__init__()``
==============
* the initializer
* for initializing object with data
* ``self`` as it's first parameter
* ``__init__()`` is called after ``__new__()`` and the instance is in place, so you can use ``self`` with it
* it's purpose is just to alter the fresh state of the newly created instance

.. code-block:: python
    :emphasize-lines: 2,3

    class Iris:
        def __init__(self):
            print("Iris.__init__() called")

    Iris()
    # Iris.__init__() called

Example usage
=============
.. code-block:: python
    :emphasize-lines: 3,4

    class Iris:
        def __call__(cls):
            iris = Iris.__new__(cls)
            iris.__init__()

        def __new__(cls):
            print("Iris.__new__() called")
            return super().__new__(cls)

        def __init__(self):
            print("Iris.__init__() called")

    Iris()
    # Iris.__new__() called
    # Iris.__init__() called


Proxy methods
=============
.. code-block:: python
    :caption: One of the most common use of ``*args``, ``**kwargs`` is for proxy methods.

    class Point2D:
        def __init__(self, x, y):
            self.x = x
            self.y = y


    class Point3D(Point2D):
        def __init__(self, z, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.z = z



Returning values
================

Missing ``return`` from constructor
-----------------------------------
.. code-block:: python
    :emphasize-lines: 3

    class Iris:
        def __new__(cls):
            print("Iris.__new__() called")

        def __init__(self):
            print("Iris.__init__() called")  # -> is actually never called

    Iris()
    # Iris.__new__() called
    # None

The instantiation is evaluated to ``None`` since we don't return anything from the constructor.

Return invalid from constructor
-------------------------------
.. code-block:: python
    :emphasize-lines: 4

    class Iris:
        def __new__(cls):
            print("Iris.__new__() called")
            return 29

    Iris()
    # Iris.__new__() called
    # 29

Return invalid from initializer
-------------------------------
.. code-block:: python
    :emphasize-lines: 4

    class Iris:
        def __init__(self):
            print("Iris.__new__() called")
            return 33

    Iris()
    # TypeError: __init__ should return None

Why?
====
* Factory method
* Could be used to implement Singleton

.. code-block:: python

    class PDF:
        pass

    class Docx:
        pass

    class Document:
        def __call__(self, *args, **kwargs):
            Document.__new__(*args, **kwargs)

        def __new__(cls, *args, **kwargs):
            filename, extension = args[0].split('.')

            if extension == 'pdf':
                return PDF()
            elif extension == 'docx':
                return Docx()


    file1 = Document('myfile.pdf')
    # <__main__.PDF object at 0x1092460f0>

    file2 = Document('myfile.docx')
    # <__main__.DOCX object at 0x107a6c160>


Initial arguments mutability and shared state
=============================================

.. _Initial arguments mutability and shared state:

Bad
---
.. code-block:: python
    :caption: Initial arguments mutability and shared state

    class Astronaut:
        def __init__(self, name, locations=[]):
            self.name = name
            self.locations = locations


    watney = Astronaut('Mark Watney')
    watney.locations.append('Johnson Space Center')
    print(watney.addresses)
    # ['Johnson Space Center']

    twardowski = Astronaut('Jan Twardowski')
    print(twardowski.locations)
    # ['Johnson Space Center']

Good
----
.. code-block:: python
    :caption: Initial arguments mutability and shared state

    class Contact:
        def __init__(self, name, locations=()):
            self.name = name
            self.locations = list(locations)


    watney = Astronaut('Mark Watney')
    watney.locations.append('Johnson Space Center')
    print(watney.locations)
    # ['Johnson Space Center']

    twardowski = Astronaut('Jan Twardowski')
    print(twardowski.locations)
    # []

Do not run methods in ``__init__()``
====================================
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


    localhost = Server(
        host='localhost',
        username='admin',
        password='admin'
    )

    # This is better
    localhost.connect()
