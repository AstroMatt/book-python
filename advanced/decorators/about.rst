****************
About Decorators
****************


Rationale
=========
* Introduced in :pep:`318` - Decorators for Functions and Methods in 2003 for Python 2.4
* Decorator is an object, which takes another object as it's argument
* Decorators can:

    * Do things before call
    * Do things after call
    * Modify arguments
    * Modify returned value
    * Avoid calling
    * Modify globals
    * Add or change metadata

.. code-block:: python

    def mydecorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper


    @mydecorator
    def myfunction(*args, **kwargs):
        pass


Convention
==========
* ``func`` is a pointer to function which is being decorated
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments
* By calling ``func(*args, **kwargs)`` you actually run original (wrapped) function with it's original arguments


Types of decorators
===================
By type:

    * Function decorators
    * Class decorators

By decorated object:

    * Decorating function
    * Decorating class
    * Decorating methods

By wrapper type:

    * Wrapper function
    * Wrapper class

By number of arguments:

    * Without arguments
    * With arguments


Decorator Types
===============
* Function decorators
* Class decorators

.. code-block:: python

    def mydecorator(x):
        ...

.. code-block:: python

    class MyDecorator:
        def __init__(self, x):
            ...


Decorated Object
================
* Decorating function
* Decorating class
* Decorating methods

.. code-block:: python

    def mydecorator(func):
        ...

    def mydecorator(cls):
        ...

    def mydecorator(mth):
        ...

.. code-block:: python

    class MyDecorator:
        def __init__(self, func):
            ...

    class MyDecorator:
        def __init__(self, cls):
            ...

    class MyDecorator:
        def __init__(self, mth):
            ...


Wrapper Type
============
* Wrapper function
* Wrapper class

.. code-block:: python

    def mydecorator(x):
        def wrapper(*args, **kwargs)
            ...
        return wrapper

    def mydecorator(x):
        class Wrapper:
            def __init__(*args, **kwargs)
                ...
        return Wrapper


Arguments
=========
* Without arguments
* With arguments

.. code-block:: python

    @mydecorator
    def myfunction(*args, **kwargs):
        ...

    @mydecorator(a, b)
    def myfunction(*args, **kwargs):
        ...

.. code-block:: python

    @MyClass
    def myfunction(*args, **kwargs):
        ...

    @MyClass(a, b)
    def myfunction(*args, **kwargs):
        ...


Usage
=====
* Decorating function
* Decorating class
* Decorating methods

.. code-block:: python

    @mydecorator
    def myfunction(*args, **kwargs):
        ...

    class MyClass:
        @mydecorator
        def my_method(self, *args, **kwargs):
            ...

    @mydecorator
    class MyClass:
        ...

.. code-block:: python

    @MyDecorator
    def myfunction(*args, **kwargs):
        ...

    @MyDecorator
    class MyClass:
        ...



Decorator library
=================
* https://wiki.python.org/moin/PythonDecoratorLibrary
