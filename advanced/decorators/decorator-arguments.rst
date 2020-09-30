************************
Decorator with Arguments
************************


Rationale
=========
Decorator:
    .. code-block:: python

        @mydecorator(a, b)
        def myfunction(*args, **kwargs):
            pass

Is equivalent to:
    .. code-block:: python

        mydecorator = mydecorator(a, b)(myfunction)


Syntax
======
.. code-block:: python
    :caption: Definition

    def mydecorator(a=1, b=2):
        def decorator(func):
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator

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
                    func(*args, **kwargs)
                except TimeoutError:
                    print(error_message)
                finally:
                    alarm(0)
            return wrapper
        return decorator


    @timeout(seconds=3.0, error_message='Sorry, timeout')
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


    def timeout(seconds=3.0, error_message='Timeout'):
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


    @timeout(seconds=3.0, error_message='Sorry, timeout')
    def countdown(n):
        for i in reversed(range(n)):
            print(i)
            sleep(1)
        print('countdown finished')

    countdown(5)
    # 4
    # 3
    # 2
    # TimeoutError: Timeout


Assignments
===========

Decorator Arguments Astronauts
------------------------------
* Assignment name: Decorator Arguments Astronauts
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/decorator_arguments_astronauts.py`
* Last update: 2020-10-01


:English:
    #. Use data from "Input" section (see below)
    #. Create decorator ``check_astronauts``
    #. To answer if person is an astronaut check field ``is_astronaut`` in ``crew: list[dict]``
    #. Decorator will call decorated function, only if all crew members has field with specified value
    #. Both field name and value are given as keyword arguments to decorator
    #. If any member is not an astronaut raise ``PermissionError`` and print his first name and last name
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Stwórz dekorator ``check_astronauts``
    #. Aby odpowiedzieć czy osoba jest astronautą sprawdź pole ``is_astronaut`` in ``crew: list[dict]``
    #. Dekorator wywoła dekorowaną funkcję tylko wtedy, gdy każdy członek załogi ma pole o podanej wartości
    #. Zarówno nazwa pola jak i wartość są podawane jako argumenty nazwane do dekoratora
    #. Jeżeli, jakikolwiek członek nie jest astronautą, podnieś wyjątek ``PermissionError`` i wypisz jego imię i nazwisko
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        CREW_PRIMARY = [
            {'is_astronaut': True, 'name': 'Jan Twardowski'},
            {'is_astronaut': True, 'name': 'Mark Watney'},
            {'is_astronaut': True, 'name': 'Melissa Lewis'}]

        CREW_BACKUP = [
            {'is_astronaut': True, 'name': 'Melissa Lewis'},
            {'is_astronaut': True, 'name': 'Mark Watney'},
            {'is_astronaut': False, 'name': 'Alex Vogel'}]


        @check(field='is_astronaut', value=True)
        def launch(crew):
            crew = ', '.join(astro['name'] for astro in crew)
            return f'Launching: {crew}'

:Output:
    .. code-block:: python

        """
        >>> launch(CREW_PRIMARY)
        Launching: Jan Twardowski, Mark Watney, Melissa Lewis

        >>> launch(CREW_BACKUP)
        Traceback (most recent call last):
            ...
        PermissionError: Alex Vogel is not an astronaut
        """

Decorator Arguments Type Check
------------------------------
* Assignment name: Decorator Arguments Type Check
* Complexity level: medium
* Lines of code to write: 20 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/decorator_arguments_typecheck.py`
* Last update: 2020-10-01

:English:
    #. Use data from "Input" section (see below)
    #. Create decorator function ``typecheck``
    #. Decorator checks types of all arguments (``*args`` oraz ``**kwargs``)
    #. Decorator checks return type only if ``check_return`` is ``True``
    #. In case when received type is not expected throw an exception ``TypeError`` with:

        * argument name
        * actual type
        * expected type

    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz dekorator funkcję ``typecheck``
    #. Dekorator sprawdza typy wszystkich argumentów (``*args`` oraz ``**kwargs``)
    #. Dekorator sprawdza typ zwracany tylko gdy ``check_return`` jest ``True``
    #. W przypadku gdy otrzymany typ nie jest równy oczekiwanemu wyrzuć wyjątek ``TypeError`` z:

        * nazwa argumentu
        * aktualny typ
        * oczekiwany typ

    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        @typecheck(check_return=True)
        def echo(a: str, b: int, c: float = 0.0) -> bool:
            return bool(a * b)

:Output:
    .. code-block:: text

        >>> echo('one', 1)
        True
        >>> echo('one', 1, 1.1)
        True
        >>> echo('one', b=1)
        True
        >>> echo('one', 1, c=1.1)
        True
        >>> echo('one', b=1, c=1.1)
        True
        >>> echo(a='one', b=1, c=1.1)
        True
        >>> echo(c=1.1, b=1, a='one')
        True
        >>> echo(b=1, c=1.1, a='one')
        True
        >>> echo('one', c=1.1, b=1)
        True

        >>> echo(1, 1)
        Traceback (most recent call last):
        ...
        TypeError: "a" is <class 'int'>, but <class 'str'> was expected

        >>> echo('one', 'two')
        Traceback (most recent call last):
        ...
        TypeError: "b" is <class 'str'>, but <class 'int'> was expected

        >>> echo('one', 1, 'two')
        Traceback (most recent call last):
        ...
        TypeError: "c" is <class 'str'>, but <class 'float'> was expected

        >>> echo(b='one', a='two')
        Traceback (most recent call last):
        ...
        TypeError: "b" is <class 'str'>, but <class 'int'> was expected

        >>> echo('one', c=1.1, b=1.1)
        Traceback (most recent call last):
        ...
        TypeError: "b" is <class 'float'>, but <class 'int'> was expected

:Hints:
    .. code-block:: python

        echo.__annotations__
        # {'a': <class 'str'>, 'b': <class 'int'>, 'c': <class 'float'>, 'return': <class 'bool'>}
