********
Warnings
********


Usage
=====
.. code-block:: python

    import warnings

    warnings.warn('Wersja API jest już nieaktualna', PendingDeprecationWarning)

.. code-block:: python

    import warnings

    def sumuj(a, b):
        warnings.warn('You should english name ``sum()``.', PendingDeprecationWarning)
        return a + b

    def sum(a, b):
        return a + b


    sumuj(1, 2)
    sum(1, 2)


Running
=======
.. code-block:: console

    $ python -W all myfile.py
    filename.py:5: PendingDeprecationWarning: You should english name ``sum()``.
      warnings.warn('You should english name ``sum()``.', PendingDeprecationWarning)


Examples
========
.. code-block:: python

    import warnings


    def ariane5():
        warnings.warn('ariane5(), is deprecated, please use ariane6() instead', PendingDeprecationWarning)
        print('Launching rocket Ariane 5')

    def ariane6():
        print('Launching rocket Ariane 6')


    ariane5()
    ariane6()

.. code-block:: console

    $ python __notepad__.py

.. code-block:: console

    $ python -W all myfile.py
    __notepad__.py:5: PendingDeprecationWarning: ariane5(), is deprecated, please use ariane6() instead

Example 2
---------
.. code-block:: python

    import warnings
    import functools


    def deprecated(func):
        """
        This is a decorator which can be used to mark functions
        as deprecated. It will emit warning when the function is used.
        """

        @functools.wraps(func)
        def new_func(*args, **kwargs):
            warnings.warn_explicit(
                f"Call to deprecated function {func.__name__}.",
                category=DeprecationWarning,
                filename=func.func_code.co_filename,
                lineno=func.func_code.co_firstlineno + 1)
            return func(*args, **kwargs)
        return new_func


    ## Usage examples ##
    @deprecated
    def my_func():
        pass

    @other_decorators_must_be_upper
    @deprecated
    def my_func():
        pass

Example 3
---------
.. code-block:: python

    def deprecated(removed_in_version=None):
        def decorator(fn):
            def write_message(*args, **kwargs):
                name = fn.__name__
                file = fn.__code__.co_filename
                line = fn.__code__.co_firstlineno + 1
                message = f"Call to deprecated function {name} in {file} at line {line}"
                message += f'\nIt will be removed in {removed_in_version}'

                import warnings
                warnings.warn(message, DeprecationWarning)
                return fn(*args, **kwargs)

            return write_message
        return decorator


    class Dragon:
        def __init__(self, name):
            self.name = name

        @deprecated(removed_in_version=2.0)
        def move_dragon(self):
            return ...

        def move(self):
            return ...


    red = Dragon('Red')

    red.move()
    red.move_dragon()
    # myfile.py:14: DeprecationWarning: Call to deprecated function move_dragon in scratch.py at line 26
    # It will be removed in 2.0
    #   warnings.warn(message, DeprecationWarning)

Example 4
---------
.. code-block:: python

    import warnings


    class RemovedInVersion20(DeprecationWarning):
        pass


    def sumuj(a, b):
        warnings.warn('Use ``sum`` function', RemovedInVersion20)
        return a + b

    def sum(a, b):
        return a + b


    sumuj(1, 2)
    sum(1, 2)


Example 4
---------
.. code-block:: python

    import warnings

    class RemovedInVersion20(DeprecationWarning):
        pass


    class Dragon:
        def __init__(self, name):
            self.name = name

        def move_dragon(self):
            warnings.warn('Use Dragon.move()', RemovedInVersion20)
            return ...

        def move(self):
            return ...


    red = Dragon('Red')

    red.move()
    red.move_dragon()
    # myfile.py:12: RemovedInVersion20: Use Dragon.move()
    #   warnings.warn('Use Dragon.move()', RemovedInVersion20)
