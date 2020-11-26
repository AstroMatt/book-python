.. _Control Flow Exceptions:

**********
Exceptions
**********


Rationale
=========
.. highlights::
    * Used when error occurs
    * You can catch exception and handles erroneous situation
    * Exception example situations:

        * File does not exists
        * No permissions to read file
        * Function argument is invalid type (ie. ``int('one')``)
        * Value is incorrect (ie. negative Kelvin temperature)
        * Network or database connection could not be established


Most Common Exceptions
======================
.. code-block:: python
    :caption: ``AttributeError`` - Attribute reference or assignment fails
    :emphasize-lines: 5

    name = 'Jan'
    name.append('Twardowski')
    # Traceback (most recent call last):
    # AttributeError: 'str' object has no attribute 'append'

.. code-block:: python
    :caption: ``ImportError``, ``ModuleNotFoundError`` - Module could not be located
    :emphasize-lines: 5

    import math
    import match
    # Traceback (most recent call last):
    # ModuleNotFoundError: No module named 'match'

.. code-block:: python
    :caption: ``IndexError`` - Sequence subscript is out of range
    :emphasize-lines: 5

    DATA = ['a', 'b', 'c']
    DATA[100]
    # Traceback (most recent call last):
    # IndexError: list index out of range

.. code-block:: python
    :caption: ``KeyError`` - Dictionary key is not found
    :emphasize-lines: 5

    DATA = {'a': 1, 'b': 2}
    DATA['x']
    # Traceback (most recent call last):
    # KeyError: 'x'

.. code-block:: python
    :caption: ``NameError`` - Local or global name is not found
    :emphasize-lines: 4

    print(firstname)
    # Traceback (most recent call last):
    # NameError: name 'firstname' is not defined

.. code-block:: python
    :caption: ``SyntaxError`` - Parser encounters a syntax error
    :emphasize-lines: 7

    if True
        print('Yes')
    # Traceback (most recent call last):
    #   File "<stdin>", line 1
    #     if True
    #           ^
    # SyntaxError: invalid syntax

.. code-block:: python
    :caption: ``IndentationError`` - Syntax errors related to incorrect indentation
    :emphasize-lines: 9

    if True:
       print('Hello!')
        print('My name...')
       print('José Jiménez')
    # Traceback (most recent call last):
    #   File "<stdin>", line 1
    #     print('My name...')
    #     ^
    # IndentationError: unexpected indent

.. code-block:: python
    :caption: ``TypeError`` - Operation or function is applied to an object of inappropriate type
    :emphasize-lines: 4,9,14,19

    42 + 'a'
    # Traceback (most recent call last):
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'

    'a' + 42
    # Traceback (most recent call last):
    # TypeError: can only concatenate str (not "int") to str

    a[1.5]
    # Traceback (most recent call last):
    # TypeError: list indices must be integers or slices, not float

    a, b = 1
    # Traceback (most recent call last):
    # TypeError: cannot unpack non-iterable int object

.. code-block:: python
    :caption: ``ValueError`` Argument has an invalid value
    :emphasize-lines: 4,9,14,19

    a, b, c = 1, 2
    # Traceback (most recent call last):
    # ValueError: not enough values to unpack (expected 3, got 2)

    a, b = 1, 2, 3
    # Traceback (most recent call last):
    # ValueError: too many values to unpack (expected 2)

    float('one')
    # Traceback (most recent call last):
    # ValueError: could not convert string to float: 'one'

    int('one')
    # Traceback (most recent call last):
    # ValueError: invalid literal for int() with base 10: 'one'


Exception Hierarchy
===================
.. code-block:: text

    BaseException
     +-- SystemExit
     +-- KeyboardInterrupt
     +-- GeneratorExit
     +-- Exception
          +-- StopIteration
          +-- StopAsyncIteration
          +-- ArithmeticError
          |    +-- FloatingPointError
          |    +-- OverflowError
          |    +-- ZeroDivisionError
          +-- AssertionError
          +-- AttributeError
          +-- BufferError
          +-- EOFError
          +-- ImportError
          +-- LookupError
          |    +-- IndexError
          |    +-- KeyError
          +-- MemoryError
          +-- NameError
          |    +-- UnboundLocalError
          +-- OSError
          |    +-- BlockingIOError
          |    +-- ChildProcessError
          |    +-- ConnectionError
          |    |    +-- BrokenPipeError
          |    |    +-- ConnectionAbortedError
          |    |    +-- ConnectionRefusedError
          |    |    +-- ConnectionResetError
          |    +-- FileExistsError
          |    +-- FileNotFoundError
          |    +-- InterruptedError
          |    +-- IsADirectoryError
          |    +-- NotADirectoryError
          |    +-- PermissionError
          |    +-- ProcessLookupError
          |    +-- TimeoutError
          +-- ReferenceError
          +-- RuntimeError
          |    +-- NotImplementedError
          |    +-- RecursionError
          +-- SyntaxError
          |    +-- IndentationError
          |         +-- TabError
          +-- SystemError
          +-- TypeError
          +-- ValueError
          |    +-- UnicodeError
          |         +-- UnicodeDecodeError
          |         +-- UnicodeEncodeError
          |         +-- UnicodeTranslateError
          +-- Warning
               +-- DeprecationWarning
               +-- PendingDeprecationWarning
               +-- RuntimeWarning
               +-- SyntaxWarning
               +-- UserWarning
               +-- FutureWarning
               +-- ImportWarning
               +-- UnicodeWarning
               +-- BytesWarning
               +-- ResourceWarning


Raising Exceptions
==================
.. code-block:: python
    :caption: Raise Exception without message
    :emphasize-lines: 4

    raise RuntimeError
    # Traceback (most recent call last):
    # RuntimeError

.. code-block:: python
    :caption: Exception with additional message
    :emphasize-lines: 4

    raise RuntimeError('Some message')
    # Traceback (most recent call last):
    # RuntimeError: Some message


Use Case
========
.. code-block:: python
    :emphasize-lines: 5

    temperature = input('Type temperature [Kelvin]: ')
    # Type temperature [Kelvin]: -10<ENTER>

    if float(temperature) < 0:
        raise ValueError('Kelvin temperature cannot be negative')
    # Traceback (most recent call last):
    # ValueError: Kelvin temperature cannot be negative

.. code-block:: python

    def convert(temperature):
        if type(temperature) not in {float, int}:
            raise TypeError('Temperature must be int or float')
        if temperature < 0:
            raise ValueError('Kelvin temperature cannot be negative')
        return temperature

.. code-block:: python
    :emphasize-lines: 2

    def apollo13():
        raise RuntimeError('Oxygen tank explosion')


    apollo13()
    # Traceback (most recent call last):
    # RuntimeError: Oxygen tank explosion

.. code-block:: python
    :emphasize-lines: 2

    def apollo18():
        raise NotImplementedError('Mission dropped due to budget cuts')


    apollo18()
    # Traceback (most recent call last):
    # NotImplementedError: Mission dropped due to budget cuts


Assertion
=========
* Raises ``AssertionError`` if argument is ``False``
* Can have optional message

.. code-block:: python

    assert type(header) is tuple
    assert type(train) is list
    assert type(test) is list
    assert all(type(x) is tuple for x in train)
    assert all(type(x) is tuple for x in test)

.. code-block:: python
    :emphasize-lines: 3,8

    import sys

    assert sys.version_info >= (3, 8)
    # Traceback (most recent call last):
    # AssertionError

    assert sys.version_info >= (3, 8), "Python 3.8+ required."
    # Traceback (most recent call last):
    # AssertionError: Python 3.8+ required.


Traceback Analysis
==================
.. highlights::
    * Stacktrace is 8 levels deep, it's not Java's 200 ;)

.. code-block:: python
    :emphasize-lines: 3

    raise RuntimeError
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # RuntimeError

.. code-block:: python
    :emphasize-lines: 3

    raise RuntimeError('Huston we have a problem')
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # RuntimeError: Huston we have a problem

.. code-block:: python
    :emphasize-lines: 6-7

    def apollo13():
        raise RuntimeError('Oxygen tank explosion')


    apollo13()
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    #   File "<stdin>", line 2, in apollo13
    # RuntimeError: Oxygen tank explosion

.. code-block:: python
    :emphasize-lines: 6-9

    def apollo13():
        raise RuntimeError('Oxygen tank explosion')


    apollo13()
    # Traceback (most recent call last):
    #   File "/home/watney/myscript.py", line 4, in <module>
    #     apollo13()
    #   File "/home/watney/myscript.py", line 2, in apollo13
    #     raise RuntimeError('Oxygen tank explosion')
    # RuntimeError: Oxygen tank explosion

.. code-block:: python
    :emphasize-lines: 11-14

    def apollo13():
        raise RuntimeError('Oxygen tank explosion')


    apollo13()
    # Traceback (most recent call last):
    #   File "<input>", line 1, in <module>
    #   File "/Applications/PyCharm 2019.2 EAP.app/Contents/helpers/pydev/_pydev_bundle/pydev_umd.py", line 197, in runfile
    #     pydev_imports.execfile(filename, global_vars, local_vars)  # execute the script
    #   File "/Applications/PyCharm 2019.2 EAP.app/Contents/helpers/pydev/_pydev_imps/_pydev_execfile.py", line 18, in execfile
    #     exec(compile(contents+"\n", file, 'exec'), glob, loc)
    #   File "/home/watney/myscript.py", line 4, in <module>
    #     apollo13()
    #   File "/home/watney/myscript.py", line 2, in apollo13
    #     raise RuntimeError('Oxygen tank explosion')
    # RuntimeError: Oxygen tank explosion


Change Verbosity Level
======================
.. highlights::
    * Change level with ``sys.tracebacklimit``
    * From time to time you can have problems somewhere in the middle, but it's rare
    * Last lines are the most important, in most cases error is there

.. code-block:: python
    :emphasize-lines: 1,2

    import sys
    sys.tracebacklimit = 2


    def apollo13():
        raise RuntimeError('Oxygen tank explosion')

    apollo13()
    # Traceback (most recent call last):
    #   File "/home/watney/myscript.py", line 4, in <module>
    #     apollo13()
    #   File "/home/watney/myscript.py", line 2, in apollo13
    #     raise RuntimeError('Oxygen tank explosion')
    # RuntimeError: Oxygen tank explosion


Catching Exceptions
===================
.. highlights::
    * ``try``
    * ``except``
    * ``else``
    * ``finally``
    * ``try`` is required and then one of the others blocks

.. code-block:: python

    try:
        # try to execute
    except Exception:
        # what to do if exception occurs
    else:
        # what to do if no exception occurs
    finally:
        # What to do either if exception occurs or not

.. code-block:: python
    :caption: Catch single exception
    :emphasize-lines: 7-8

    def apollo13():
        raise RuntimeError('Oxygen tank explosion')


    try:
        apollo13()
    except RuntimeError:
        print('Houston we have a problem!')

    # Houston we have a problem!

.. code-block:: python
    :caption: Catch many exceptions with the same handling
    :emphasize-lines: 7-8

    def apollo13():
        raise RuntimeError('Oxygen tank explosion')


    try:
        apollo13()
    except (RuntimeError, TypeError, NameError):
        print('Houston we have a problem!')

    # Houston we have a problem!

.. code-block:: python
    :caption: Catch many exceptions with different handling
    :emphasize-lines: 4-7

    try:
        with open(r'/tmp/my-file.txt') as file:
            print(file.read())
    except FileNotFoundError:
        print('File does not exist')
    except PermissionError:
        print('Permission denied')

    # File does not exist

.. code-block:: python
    :caption: Exceptions logging
    :emphasize-lines: 9,10

    import logging


    def apollo13():
        raise RuntimeError('Oxygen tank explosion')

    try:
        apollo13()
    except RuntimeError as err:
        logging.error(err)

    # ERROR:root:Oxygen tank explosion


Else and Finally
================
* ``else`` is executed when no exception occurred
* ``finally`` is executed always (even if there was exception)
* Used to close file, connection or transaction to database

.. code-block:: python

    try:
        file = open('/tmp/myfile.txt')
    except Exception:
        print('Error')
    finally:
        file.close()

.. code-block:: python
    :caption: ``else`` is executed when no exception occurred
    :emphasize-lines: 8,9

    def apollo11():
        print('Try landing on the Moon')

    try:
        apollo11()
    except Exception:
        print('Abort')
    else:
        print('Landing a man on the Moon')

    # Try landing on the Moon
    # Landing a man on the Moon

.. code-block:: python
    :caption: ``finally`` is executed always (even if there was exception)
    :emphasize-lines: 8,9

    def apollo11():
        print('Try landing on the Moon')

    try:
        apollo11()
    except Exception:
        print('Abort')
    finally:
        print('Returning safely to the Earth')

    # Try landing on the Moon
    # Returning safely to the Earth

.. code-block:: python
    :emphasize-lines: 11-18

    def apollo11():
        print('Program P63 - Landing Manoeuvre Approach Phase')
        raise RuntimeError('1201 Alarm')
        raise RuntimeError('1202 Alarm')
        print('Contact lights')
        print('The Eagle has landed!')
        print("That's one small step for [a] man, one giant leap for mankind.")

    try:
        apollo11()
    except RuntimeError:
        print("You're GO for landing")
    except Exception:
        print('Abort')
    else:
        print('Landing a man on the Moon')
    finally:
        print('Returning safely to the Earth')

    # Program P63 - Landing Manoeuvre Approach Phase
    # You're GO for landing
    # Returning safely to the Earth


Pokemon Exception Handling
==========================
* "Gotta catch 'em all"
* ``Ctrl-C`` raises ``KeyboardInterrupt``

.. code-block:: python
    :caption: User cannot simply kill program with ``Ctrl-C``
    :emphasize-lines: 4

    while True:
        try:
            number = float(input('Type number: '))
        except:
            continue

.. code-block:: python
    :caption: User can kill program with ``Ctrl-C``
    :emphasize-lines: 4

    while True:
        try:
            number = float(input('Type number: '))
        except Exception:
            continue


Defining Own Exceptions
=======================
* class which inherits from ``Exception``

.. code-block:: python
    :emphasize-lines: 1,2

    class MyError(Exception):
        pass


    raise MyError
    # Traceback (most recent call last):
    # MyError

    raise MyError('More verbose description')
    # Traceback (most recent call last):
    # MyError: More verbose description

.. code-block:: python
    :caption: Django Framework Use-case of Custom Exceptions
    :emphasize-lines: 10

    from django.contrib.auth.models import User


    def login(request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username, password)
        except User.DoesNotExist:
            print('Sorry, no such user in database')

.. code-block:: python
    :caption: Django Framework Use-case of Custom Exceptions
    :emphasize-lines: 13

    class Dragon:
        def take_damage(self, damage):
            raise self.IsDead

        class IsDead(Exception):
            pass


    wawelski = Dragon()

    try:
        wawelski.take_damage(10)
    except Dragon.IsDead:
        print('Dragon is dead')


Exit Status Code
================
.. highlights::
    * exit status ``0`` - no error
    * any other exit status - error
    * This will not work in Jupyter

.. code-block:: python
    :emphasize-lines: 5

    try:
        float('hello')
    except ValueError:
        print('Cannot type cast to float')
        exit(1)

    # Cannot type cast to float
    # [...] program exited with status 1

.. code-block:: console

    $ python3.9 -m doctest myscript.py
    $ echo $?
    0

.. code-block:: console

    $ python3.9 -m doctest myscript.py
    **********************************************************************
    File "/home/watney/myscript.py", line 41, in myscript
    Failed example:
        1 + 2
    Expected:
        3
    Got:
        4
    **********************************************************************
    1 items had failures:
       1 of   2 in myscript
    ***Test Failed*** 1 failures.

    $ echo $?
    1


Assignments
===========

.. literalinclude:: solution/controlflow_exception_assert.py
    :caption: :download:`Solution <solution/controlflow_exception_assert.py>`
    :end-before: # Solution

.. literalinclude:: solution/controlflow_exception_raise.py
    :caption: :download:`Solution <solution/controlflow_exception_raise.py>`
    :end-before: # Solution

.. literalinclude:: solution/controlflow_exception_except.py
    :caption: :download:`Solution <solution/controlflow_exception_except.py>`
    :end-before: # Solution

.. literalinclude:: solution/controlflow_exception_finally.py
    :caption: :download:`Solution <solution/controlflow_exception_finally.py>`
    :end-before: # Solution

.. literalinclude:: solution/controlflow_exception_else.py
    :caption: :download:`Solution <solution/controlflow_exception_else.py>`
    :end-before: # Solution

.. literalinclude:: solution/controlflow_exception_custom.py
    :caption: :download:`Solution <solution/controlflow_exception_custom.py>`
    :end-before: # Solution

.. literalinclude:: solution/controlflow_exception_input.py
    :caption: :download:`Solution <solution/controlflow_exception_input.py>`
    :end-before: # Solution
