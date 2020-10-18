.. _Introspection:

*************
Introspection
*************

* Introspection is the ability to determine the type of an object at runtime
* Everything in Python is an object and we can examine those objects
* Python ships with a few built-in functions and modules to help us


Introspecting Types
===================

``id()``
--------
.. code-block:: python

    id('Jan Twardowski')                 # 4596416368
    id('Jan Twardowski')                 # 4592969392

.. code-block:: python

    name = 'Jan Twardowski'

    id(name)                            # 4596353264
    id(name)                            # 4596353264

.. code-block:: python

    id('Jan Twardowski')                # 4466061520
    id(str)                             # 4306722176

``type()``
----------
.. code-block:: python

    type('')                            # <type 'str'>
    type(str)                           # <class 'type'>

    type([])                            # <type 'list'>
    type(list)                          # <class 'type'>

    type({})                            # <type 'dict'>
    type(dict)                          # <type 'type'>

    type(3)                             # <type 'int'>
    type(int)                           # <class 'type'>

``isinstance()``
----------------
.. code-block:: python

    my_data = {}
    isinstance(my_data, (set, dict))    # True
    isinstance(my_data, dict)           # True
    isinstance(my_data, set)            # False

.. code-block:: python

    my_data = {1}
    isinstance(my_data, dict)           # False
    isinstance(my_data, set)            # True

.. code-block:: python

    my_data = {1: 1}
    isinstance(my_data, dict)           # True
    isinstance(my_data, set)            # False

``issubclass()``
----------------
.. code-block:: python

    class Cosmonaut:
        pass

    class GieroyCCCP(Cosmonaut):
        pass


    issubclass(Cosmonaut, Cosmonaut)     # True
    issubclass(Cosmonaut, GieroyCCCP)    # False
    issubclass(GieroyCCCP, GieroyCCCP)   # True
    issubclass(GieroyCCCP, Cosmonaut)    # True

``callable()``
--------------
.. code-block:: python

    class Car:
        def setName(self, name):
            self.name = name

    def fun():
        pass

    c = Car()

    callable(fun)                       # True
    callable(c.setName)                 # True
    callable([])                        # False
    callable(1)                         # False


Introspecting Objects
=====================

``dir()``
---------
* Returns a list of attributes and methods belonging to an object

.. code-block:: python

    class Server:
        """Connects to the server"""
        _connection = None

        def __init__(self, host, port):
            """Initializes object"""
            self.host = host
            self.port = port

        def login():
            """logs-in to the server"""

    localhost = Server(host='127.0.0.1', port=1337)

    result = dir(localhost)
    print(result)
    # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
    #  '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
    # '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
    # '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
    # '_connection', 'host', 'login', 'port']

``object.__dict__``
-------------------
* Returns dynamic fields of an object

.. code-block:: python

    class Server:
        """Connects to the server"""
        _connection = None

        def __init__(self, host, port):
            """Initializes object"""
            self.host = host
            self.port = port

        def login():
            """logs-in to the server"""

    localhost = Server(host='127.0.0.1', port=1337)

    localhost.__dict__
    # {'host': '127.0.0.1', 'port': 1337}

``vars()``
----------
.. code-block:: python

    class Server:
        """Connects to the server"""
        _connection = None

        def __init__(self, host, port):
            """Initializes object"""
            self.host = host
            self.port = port

        def login():
            """logs-in to the server"""

    localhost = Server(host='127.0.0.1', port=1337)

    vars(Server)
    # {
    #    '__module__': '__main__',
    #    '__doc__': 'Connects to the server',
    #    '_connection': None,
    #    '__init__': <function Server.__init__ at 0x111f77488>,
    #    'login': <function Server.login at 0x111f77268>,
    #    '__dict__': <attribute '__dict__' of 'Server' objects>,
    #    '__weakref__': <attribute '__weakref__' of 'Server' objects>
    # }

``hasattr()``, ``getattr()``, ``setattr()``
-------------------------------------------
.. code-block:: python

    class Astronaut:
        def __init__(self, **kwargs):
            for name, value in kwargs.items():
                setattr(self, name, value)

        def __str__(self):
            if hasattr(self, 'firstname'):
                firstname = getattr(self, 'firstname')

            lastname = getattr(self, 'lastname', 'n/a')
            return f'My name... {firstname} {lastname}'


     jose = Astronaut(firstname='José', lastname='Jiménez')

     print(jose)
     # My name... José Jiménez

``inspect`` module
------------------
The inspect module also provides several useful functions to get
information about live objects. For example you can check the members of
an object by running:

.. code-block:: python

    import inspect

    inspect.getmembers(str)
    # [('__add__', <slot wrapper '__add__' of ... ...


Introspecting Docstrings
========================

``help()``
----------
.. code-block:: python

    class Server:
        """Connects to the server"""
        _connection = None

        def __init__(self, host, port):
            """Initializes object"""
            self.host = host
            self.port = port

        def login():
            """logs-in to the server"""

    localhost = Server(host='127.0.0.1', port=1337)

    help(localhost)
    # Help on Server in module __main__ object:
    #
    # class Server(builtins.object)
    #  |  Server(host, port)
    #  |
    #  |  Connects to the server
    #  |
    #  |  Methods defined here:
    #  |
    #  |  __init__(self, host, port)
    #  |      Initializes object
    #  |
    #  |  login()
    #  |      logs-in to the server
    #  |
    #  |  ----------------------------------------------------------------------
    #  |  Data descriptors defined here:
    #  |
    #  |  __dict__
    #  |      dictionary for instance variables (if defined)
    #  |
    #  |  __weakref__
    #  |      list of weak references to the object (if defined)

``object.__doc__``
------------------
.. code-block:: python

    class Server:
        """Connects to the server"""
        _connection = None

        def __init__(self, host, port):
            """Initializes object"""
            self.host = host
            self.port = port

        def login():
            """logs-in to the server"""

    localhost = Server(host='127.0.0.1', port=1337)

    localhost.login.__doc__
    # 'logs-in to the server'


Examples
========
.. code-block:: python

    import settings
    from django.db import models

    for app in settings.INSTALLED_APPS:
        models_name = app + ".models"

        try:
            models_module = __import__(models_name, fromlist=["models"])
            attributes = dir(models_module)

            for attr in attributes:
                try:
                    attrib = models_module.__getattribute__(attr)
                    if issubclass(attrib, models.Model) and attrib.__module__== models_name:
                    print(f'{models_name}.{attr}')
                except TypeError, e:
                    pass
        except ImportError, e:
            pass

.. code-block:: python

    from django.contrib import admin
    from . import models
    import inspect

    for name, obj in inspect.getmembers(models):
        if inspect.isclass(obj):
            admin.site.register(getattr(models, name))

