*******************************
Function Decorator with Classes
*******************************


Rationale
=========
* ``mydecorator`` is a decorator name
* ``MyClass`` is a class name

Syntax:
    .. code-block:: python

        @mydecorator
        class MyClass:
            ...

Is equivalent to:
    .. code-block:: python

        MyClass = mydecorator(MyClass)


Syntax
======
* ``mydecorator`` is a decorator name
* ``MyClass`` is a class name

.. code-block:: python
    :caption: Definiton

    def decorator(cls):
        class Wrapper(cls):
            def __new__(cls, *args, **kwargs):
                ...
        return Wrapper


    def decorator(cls):
        def wrapper(*args, **kwargs):
            ...
        return wrapper

.. code-block:: python
    :caption: Decoration

    @decorator
    class MyClass:
        ...

.. code-block:: python
    :caption: Usage

    my = MyClass()


Example
=======
.. code-block:: python

    def run(cls):
        def wrapper(*args, **kwargs):
            return method(instance, *args, **kwargs)
        return wrapper


    @run
    class Astronaut:
        def hello(self, name):
            return f'My name... {name}'


    astro = Astronaut()
    astro.hello('José Jiménez')
    # 'My name... José Jiménez'


Use Case
========
.. code-block:: python
    :caption: Add attribute

    def mydecorator(cls):
        class Wrapper(cls):
            attribute = 'some value...'
        return Wrapper


    @mydecorator
    class MyClass:
        pass


    print(MyClass.attribute)
    # some value...

.. code-block:: python
    :caption: Singleton using functional wrapper

    def singleton(cls):
        def wrapper(*args, **kwargs):
            if not hasattr(cls, '_instance'):
                instance = object.__new__(cls, *args, **kwargs)
                setattr(cls, '_instance', instance)
            return getattr(cls, '_instance')
        return wrapper


    @singleton
    class DatabaseConnection:
        def connect(self):
            print(f'Connecting... using {self._instance}')


    a = DatabaseConnection()  # Creating instance
    a.connect()
    # Connecting... using <__main__.singleton.<locals>.Wrapper object at 0x10372d310>

    b = DatabaseConnection()  # Reusing instance
    b.connect()
    # Connecting... using <__main__.singleton.<locals>.Wrapper object at 0x10372d310>

.. code-block:: python
    :caption: Singleton using class wrapper

    def singleton(cls):
        class Wrapper(cls):
            def __new__(cls, *args, **kwargs):
                if not hasattr(cls, '_instance'):
                    instance = object.__new__(cls, *args, **kwargs)
                    setattr(cls, '_instance', instance)
                return getattr(cls, '_instance')
        return Wrapper


    @singleton
    class DatabaseConnection:
        def connect(self):
            print(f'Connecting... using {self._instance}')


    a = DatabaseConnection()  # Creating instance
    a.connect()
    # Connecting... using <__main__.singleton.<locals>.Wrapper object at 0x10372d310>

    b = DatabaseConnection()  # Reusing instance
    b.connect()
    # Connecting... using <__main__.singleton.<locals>.Wrapper object at 0x10372d310>


Assignments
===========
.. todo:: Create assignments

