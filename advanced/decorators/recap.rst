.. _Decorators Recap:

****************
Decorators Recap
****************


Function Decorators with Function Wrappers
==========================================
.. code-block:: python

    def mydecorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    def mydecorator(method):
        def wrapper(instance, *args, **kwargs):
            return method(instance, *args, **kwargs)
        return wrapper

    def mydecorator(cls):
        def wrapper(*args, **kwargs):
            return cls(*args, **kwargs)
        return wrapper


Function Decorators with Class Wrappers
=======================================
.. code-block:: python

    def mydecorator(func):
        class Wrapper:
            ...
        return Wrapper

    def mydecorator(method):
        class Wrapper:
            ...
        return Wrapper

    def mydecorator(cls):
        class Wrapper(cls):
            ...
        return Wrapper


Class Decorators
================
.. code-block:: python

    class MyDecorator:
        def __init__(self, func):
            self._func = func

        def __call__(self, *args, **kwargs):
            ...

    class MyDecorator:
        def __init__(self, method):
            self._method = method

        def __call__(self, *args, **kwargs):
            ...

    class MyDecorator:
        def __init__(self, cls):
            self._cls = cls

        def __call__(self, *args, **kwargs):
            ...

