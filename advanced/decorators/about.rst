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


Syntax
======
* ``func`` is a pointer to function which is being decorated
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments
* By calling ``func(*args, **kwargs)`` you actually run original (wrapped) function with it's original arguments

.. code-block:: python

    def mydecorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper


    @mydecorator
    def myfunction(*args, **kwargs):
        pass


Types of decorators
===================
By type:

    * Function decorators
    * Class decorators

By decorated object:

    * Decorating function
    * Decorating class
    * Decorating method

By wrapper type:

    * Wrapper function
    * Wrapper class
    * Wrapper method

By number of arguments:

    * Without arguments
    * With arguments


Decorator Types
===============
* Function decorators
* Class decorators
* In this example:

    * ``obj`` is a decorated object
    * doesn't matter, whether is a function, class or method

.. code-block:: python

    def mydecorator(obj):
        ...

.. code-block:: python

    class MyDecorator:
        def __init__(self, obj):
            ...


Wrapper Type
============
* Wrapper function
* Wrapper class
* Wrapper method
* In this example:

    * ``obj`` is a decorated object
    * doesn't matter, whether is a function, class or method

* If ``obj`` and ``Wrapper`` are classes, ``Wrapper`` can inherit from ``obj`` (to extend it)

.. code-block:: python

    def mydecorator(obj):
        def wrapper(*args, **kwargs)
            ...
        return wrapper

.. code-block:: python

    def mydecorator(obj):
        class Wrapper:
            def __init__(*args, **kwargs)
                ...
        return Wrapper

.. code-block:: python

    class MyDecorator:
        def __init__(self, obj):
            ...

        def __call__(*args, **kwargs):
            ...

Decorated Object
================
* Decorating function (by convention ``func`` or ``fn``)
* Decorating class (by convention ``cls``)
* Decorating method (by convention ``mth``, ``meth`` or ``method``)

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


Usage
=====
.. code-block:: python

    @mydecorator
    def myfunction(*args, **kwargs):
        ...

    class MyClass:
        @mydecorator
        def mymethod(self, *args, **kwargs):
            ...

    @mydecorator
    class MyClass:
        ...

.. code-block:: python

    @MyDecorator
    def myfunction(*args, **kwargs):
        ...

    class MyClass:
        @MyDecorator
        def mymethod(self, *args, **kwargs):
            ...

    @MyDecorator
    class MyClass:
        ...


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



Decorator library
=================
* https://wiki.python.org/moin/PythonDecoratorLibrary
