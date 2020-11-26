.. _OOP Monkey Patching:

***************
Monkey Patching
***************


Recap information about classes and objects
===========================================
.. code-block:: python

    class User:
        def __init__(self):
            self.name = 'José Jiménez'

        def hello(self):
            print(f'My name... {self.name}')

    u = User()
    u.hello()
    # My name... José Jiménez

.. code-block:: python

    class User:
        def __init__(self):
            self.name = 'José Jiménez'

        def hello(self):
            print(f'My name... {self.name}')

    User.hello()
    # Traceback (most recent call last):
    # TypeError: hello() missing 1 required positional argument: 'self'

.. code-block:: python

    class User:
        def __init__(self):
            self.name = 'José Jiménez'

        @staticmethod
        def hello():
            print(f'My name...')

    User.hello()
    # My name...


Injecting fields
================
.. code-block:: python

    class User:
        def __init__(self):
            self.name = 'José Jiménez'

        def hello(self):
            print(f'My name... {self.name}')


    User.agency = 'NASA'    # Injecting field

    print(User.agency)
    # NASA

    User.__dict__
    # mappingproxy({
    #   '__module__': '__main__',
    #   '__init__': <function User.__init__ at 0x10fb9f5e0>,
    #   'hello': <function User.hello at 0x10fb9f4c0>,
    #   '__dict__': <attribute '__dict__' of 'User' objects>,
    #   '__weakref__': <attribute '__weakref__' of 'User' objects>,
    #   '__doc__': None,
    #   'agency': 'NASA',
    # })

    dir(User)
    # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
    #  '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
    #  '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
    #  '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
    #  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
    #  '__weakref__', 'agency', 'hello']


Injecting methods
=================

Static Methods
--------------
.. code-block:: python
    :caption: Note, that there is no ``self`` as a first argument to ``function``

    class User:
        def hello(self):
            print('Old version')


    def myfunction():
        print('New version')


    User.hello = myfunction
    User.hello()
    # New version

.. code-block:: python

    class User:
        def hello(self):
            print('Old version')


    def myfunction(self):
        print('New version')


    u1 = User()
    u2 = User()

    u1.hello()      # Old version
    u2.hello()      # Old version

    User.hello = myfunction

    u1.hello()      # New version
    u2.hello()      # New version

.. code-block:: python

    class User:
        def hello(self):
            print('Old version')


    def myfunction():
        print('New version')


    u1 = User()
    u2 = User()

    u1.hello()      # Old version
    u2.hello()      # Old version

    u1.hello = myfunction

    u1.hello()      # New version
    u2.hello()      # Old version

.. code-block:: python
    :caption: Injecting static and dynamic methods to class

    class User:
        pass


    def my_staticmethod():
        print('My Static Method')

    def my_dynamicmethod(self):
        print('My Dynamic Method')

    User.my_staticmethod = my_staticmethod
    User.my_dynamicmethod = my_dynamicmethod
    User.my_staticlambda = lambda: print('My Static Lambda')
    User.my_dynamiclambda = lambda self: print('My Dynamic Lambda')


    User.my_staticmethod()      # My Static Method
    User.my_dynamicmethod()     # TypeError: my_dynamicmethod() missing 1 required positional argument: 'self'
    User.my_staticlambda()      # My Static Lambda
    User.my_dynamiclambda()     # TypeError: <lambda>() missing 1 required positional argument: 'self'

    u = User()

    u.my_staticmethod()         # TypeError: my_staticmethod() takes 0 positional arguments but 1 was given
    u.my_dynamicmethod()        # My Dynamic Method
    u.my_staticlambda()         # TypeError: <lambda>() takes 0 positional arguments but 1 was given
    u.my_dynamiclambda()        # My Dynamic Lambda

.. code-block:: python
    :caption: Injecting static methods with parameters

    class User:
        pass


    def my_staticmethod(*args, **kwargs):
        print(f'My Static Method, args: {args}, kwargs: {kwargs}')

    User.my_staticmethod = my_staticmethod
    User.my_staticlambda = lambda *args, **kwargs: print(f'My Static Lambda, args: {args}, kwargs: {kwargs}')


    User.my_staticmethod()
    # My Static Method, args: (), kwargs: {}

    User.my_staticmethod(1, 2, 3, d=4, e=5, f=6)
    # My Static Method, args: (1, 2, 3), kwargs: {'d': 4, 'e': 5, 'f': 6}

    User.my_staticlambda()
    # My Static Lambda, args: (), kwargs: {}

    User.my_staticlambda(1, 2, 3, d=4, e=5, f=6)
    # My Static Lambda, args: (1, 2, 3), kwargs: {'d': 4, 'e': 5, 'f': 6}

Dynamic Methods
---------------
.. code-block:: python
    :caption: Note, that there is no ``self`` as a first argument to ``lambda``

    class User:
        pass


    u = User()
    u.hello = lambda name: print(f'My name... {name}')

    u.hello('José Jiménez')
    # My name... José Jiménez

.. code-block:: python
    :caption: Note, although there is ``self`` in ``lambda``, it is not passed as an argument

    class User:
        def __init__(self):
            self.name = 'Jan Twardowski'


    u = User()
    u.hello = lambda self: print(f'My name... {self.name}')

    u.hello()
    # Traceback (most recent call last):
    # TypeError: <lambda>() missing 1 required positional argument: 'self'

    u.hello('José Jiménez')
    # Traceback (most recent call last):
    # AttributeError: 'str' object has no attribute 'name'

.. code-block:: python
    :caption: Note, the ``self`` argument to ``lambda``

    class User:
        pass


    User.hello = lambda self: print(f'My name... {self.name}')

    u = User()
    u.name = 'José Jiménez'

    u.hello()
    # My name... José Jiménez


Backups
=======
.. code-block:: python

    class User:
        def hello(self):
            print('Old version')


    def my_function():
        print('New version')


    User._old_hello = User.hello
    User.hello = my_function
    User.hello()
    # New version

    User.hello = User._old_hello
    User.hello()
    # Traceback (most recent call last):
    # TypeError: hello() missing 1 required positional argument: 'self'


Create Missing Method
=====================
.. code-block:: python

    class User:
        def hello(self):
            print('hello')

        def __getattr__(self, name):
            print(f'Attribute "{name}" not found')
            setattr(self, name, lambda: print(f'Now I have "{name}"'))
            return super().__getattribute__(name)

        def __getattribute__(self, name):
            print(f'Accessing: "{name}"')
            return super().__getattribute__(name)


    u = User()
    u.x()
    u.x()

    # Accessing: x
    # Attribute "x" not found
    # Now I have "x"


Object Initialization
=====================
.. code-block:: python

    class User:
        def __init__(self):
            self.name = 'Jan'

        def hello(self):
            print('hello')

    u = User()
    u.hello()
    # hello

.. code-block:: python

    class User:
        pass


    u = User()
    u.name = 'Jan'
    u.hello = lambda: print('hello')

    u.hello()
    # hello


User Cases
==========
.. code-block:: python

    from datetime import datetime
    import json

    json.dumps({'gagarin': datetime(1961, 4, 12, 6, 7)})
    # Traceback (most recent call last):
    # TypeError: Object of type datetime is not JSON serializable

    json.JSONEncoder.default = lambda self, dt: dt.isoformat()
    json.dumps({'gagarin': datetime(1961, 4, 12, 6, 7)})
    # '{"gagarin": "1961-04-12T06:07:00"}'

.. code-block:: python

    import numpy as np

    numpy.array = debug(numpy.array)
    numpy.array = trace_usage(numpy.array)
    numpy.array = profiling(numpy.array)

.. code-block:: python

    from datetime import date, datetime
    import json


    def datetime_encoder(self, value):
        if type(value) is date:
            return f'{value:%Y-%m-%d}'
        if type(value) is datetime:
            return value.isoformat()
        else:
            return str(value)

    json.JSONEncoder.default = datetime_encoder

    json.dumps({'gagarin': date(1961, 4, 12)})
    # {"gagarin": "1961-04-12"}


Assignments
===========
.. todo:: Create assignments
