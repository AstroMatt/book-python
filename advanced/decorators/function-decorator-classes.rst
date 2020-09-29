*******************************
Function Decorator with Classes
*******************************


Syntax
======
* ``mydecorator`` is a decorator name
* ``MyClass`` is a class name

Syntax:
    .. code-block:: python

        @mydecorator
        class MyClass:
            pass

Is equivalent to:
    .. code-block:: python

        MyClass = mydecorator(MyClass)


Definition
==========
.. code-block:: python

    def decorator(cls):
        class Wrapper(cls):
            attribute = 'some value...'
        return Wrapper

.. code-block:: python

    @decorator
    class MyClass:
        pass


    print(MyClass.attribute)
    # some value...


Examples
========
.. code-block:: python
    :caption: Singleton using functional wrapper

    def singleton(cls):

        def wrapper(*args, **kwargs):
            if not hasattr(cls, '_instance'):
                print('First use, creating instance')
                instance = object.__new__(cls, *args, **kwargs)
                setattr(cls, '_instance', instance)
            else:
                print('Reusing instance')
            return getattr(cls, '_instance')

        return wrapper


    @singleton
    class DatabaseConnection:
        def connect(self):
            print(f'Connecting... using {self._instance}')


    a = DatabaseConnection()    # First use, creating instance
    a.connect()                 # Connecting... using <__main__.singleton.<locals>.Wrapper object at 0x10372d310>

    b = DatabaseConnection()    # Reusing instance
    b.connect()                 # Connecting... using <__main__.singleton.<locals>.Wrapper object at 0x10372d310>

.. code-block:: python
    :caption: Singleton using class wrapper

    def singleton(cls):

        class Wrapper(cls):
            def __new__(cls, *args, **kwargs):

                if not hasattr(cls, '_instance'):
                    print('First use, creating instance')
                    instance = object.__new__(cls, *args, **kwargs)
                    setattr(cls, '_instance', instance)
                else:
                    print('Reusing instance')
                return getattr(cls, '_instance')

        return Wrapper


    @singleton
    class DatabaseConnection:
        def connect(self):
            print(f'Connecting... using {self._instance}')


    a = DatabaseConnection()    # First use, creating instance
    a.connect()                 # Connecting... using <__main__.singleton.<locals>.Wrapper object at 0x10372d310>

    b = DatabaseConnection()    # Reusing instance
    b.connect()                 # Connecting... using <__main__.singleton.<locals>.Wrapper object at 0x10372d310>


Assignments
===========
.. todo:: Create assignments

