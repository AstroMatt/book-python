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

    * Function Decorators
    * Class Decorators

By wrapper type:

    * Wrapper function
    * Wrapper class
    * Wrapper method (``__call__``)

By decorated object:

    * Decorating function
    * Decorating class
    * Decorating methods

By number of arguments:

    * Without arguments
    * With arguments

Usage
=====
.. code-block:: python
    :caption: Function Decorate Function

    @mydecorator
    def myfunction(*args, **kwargs):
        pass

.. code-block:: python
    :caption: Function Decorate Method

    class MyClass:

        @mydecorator
        def my_method(self, *args, **kwargs):
            pass

.. code-block:: python
    :caption: Function Decorate Class

    @mydecorator
    class MyClass:
        pass

.. code-block:: python
    :caption: Class Decorate Function

    @MyDecorator
    def myfunction(*args, **kwargs):
        pass

.. code-block:: python
    :caption: Decorator with arguments

    @mydecorator(a, b)
    def myfunction(*args, **kwargs):
        pass


Decorator library
=================
* https://wiki.python.org/moin/PythonDecoratorLibrary
