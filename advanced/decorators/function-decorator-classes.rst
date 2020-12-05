.. _Decorator Function with Cls:

***************************
Decorator Function with Cls
***************************


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
    :caption: Definition

    def decorator(cls):
        class Wrapper(cls):
            def __new__(cls, *args, **kwargs):
                ...
        return Wrapper


    def decorator(cls):
        def wrapper(*args, **kwargs):
            instance = cls.__new__(cls, *args, **kwargs)
            return instance
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
            instance = cls.__new__(cls, *args, **kwargs)
            return instance
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

Logger
------
.. code-block:: python

    import logging

    def logger(cls):
        class Wrapper(cls):
            logger = logging.getLogger(cls.__name__)
        return Wrapper


    @logger
    class Astronaut:
        pass


    print(Astronaut.logger)
    # <Logger Astronaut (WARNING)>

Object Birthday
---------------
.. code-block:: python

    from time import time

    def since(cls):
        class Wrapper(cls):
            _instance_created = time()
        return Wrapper


    @since
    class Astronaut:
        pass


    print(Astronaut._instance_created)
    # 1607187641.3407109

Singleton with Function Wrapper
-------------------------------
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
    # Connecting... using <__main__.DatabaseConnection object at 0x10cd56fa0>

    b = DatabaseConnection()  # Reusing instance
    b.connect()
    # Connecting... using <__main__.DatabaseConnection object at 0x10cd56fa0>

Singleton with Class Wrapper
----------------------------
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
    # Connecting... using <__main__.singleton.<locals>.Wrapper object at 0x1085b6fa0>

    b = DatabaseConnection()  # Reusing instance
    b.connect()
    # Connecting... using <__main__.singleton.<locals>.Wrapper object at 0x1085b6fa0>


Assignments
===========
.. todo:: Create assignments

