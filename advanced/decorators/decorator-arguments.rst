.. _Decorator Arguments:

*******************
Decorator Arguments
*******************


Rationale
=========
Decorator:
    .. code-block:: python

        @mydecorator(a, b)
        def myfunction(*args, **kwargs):
            pass

Is equivalent to:
    .. code-block:: python

        myfunction = mydecorator(a, b)(myfunction)


Syntax
======
.. code-block:: python
    :caption: Definition

    def mydecorator(a=1, b=2):
        def decorator(func):
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return mydecorator

.. code-block:: python
    :caption: Decoration

    @mydecorator(a=0)
    def myfunction():
        ...

.. code-block:: python
    :caption: Usage

    myfunction()


Example
=======
.. code-block:: python

    def run(lang='en'):
        def decorator(func):
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator


    @run(lang='en')
    def hello(name):
        return f'My name... {name}'


    hello('José Jiménez')
    # 'My name... José Jiménez'


Use Cases
=========
.. code-block:: python
    :caption: Deprecated

    import warnings


    def deprecated(removed_in_version=None):
        def decorator(func):
            def wrapper(*args, **kwargs):
                name = func.__name__
                file = func.__code__.co_filename
                line = func.__code__.co_firstlineno + 1
                message = f"Call to deprecated function {name} in {file} at line {line}"
                message += f'\nIt will be removed in {removed_in_version}'
                warnings.warn(message, DeprecationWarning)
                return func(*args, **kwargs)
            return wrapper
        return decorator


    @deprecated(removed_in_version=2.0)
    def myfunction():
        pass


    myfunction()
    # /home/python/myscript.py:11: DeprecationWarning: Call to deprecated function myfunction in /home/python/myscript.py at line 19
    # It will be removed in 2.0

.. code-block:: python
    :caption: Timeout using ``signal(SIGALRM)``

    from signal import signal, alarm, SIGALRM
    from time import sleep


    def timeout(seconds=2.0, error_message='Timeout'):
        def on_timeout(signum, frame):
            raise TimeoutError

        def decorator(func):
            def wrapper(*args, **kwargs):
                signal(SIGALRM, on_timeout)
                alarm(int(seconds))
                try:
                    return func(*args, **kwargs)
                except TimeoutError:
                    print(error_message)
                finally:
                    alarm(0)
            return wrapper
        return decorator


    @timeout(seconds=3.0)
    def countdown(n):
        for i in reversed(range(n)):
            print(i)
            sleep(1)
        print('countdown finished')

    countdown(5)
    # 4
    # 3
    # 2
    # Sorry, timeout

.. code-block:: python
    :caption: Timeout using ``threading.Timer``

    from _thread import interrupt_main
    from threading import Timer
    from time import sleep


    def timeout(seconds=2.0, error_message='Timeout'):
        def decorator(func):
            def wrapper(*args, **kwargs):
                timer = Timer(seconds, interrupt_main)
                timer.start()
                try:
                    result = func(*args, **kwargs)
                except KeyboardInterrupt:
                    raise TimeoutError(error_message)
                finally:
                    timer.cancel()
                return result
            return wrapper
        return decorator


    @timeout(seconds=3.0)
    def countdown(n):
        for i in reversed(range(n)):
            print(i)
            sleep(1)
        print('countdown finished')

    countdown(5)
    # 4
    # 3
    # 2
    # Traceback (most recent call last):
    # TimeoutError: Timeout


Assignments
===========

.. literalinclude:: solution/decorator_arguments_syntax.py
    :caption: :download:`Solution <solution/decorator_arguments_syntax.py>`
    :end-before: # Solution

.. literalinclude:: solution/decorator_arguments_astronauts.py
    :caption: :download:`Solution <solution/decorator_arguments_astronauts.py>`
    :end-before: # Solution

.. literalinclude:: solution/decorator_arguments_typecheck.py
    :caption: :download:`Solution <solution/decorator_arguments_typecheck.py>`
    :end-before: # Solution
