************************
Decorator with Arguments
************************


Syntax
======
Decorator:
    .. code-block:: python

        @mydecorator(a, b)
        def myfunction(*args, **kwargs):
            pass

Is equivalent to:
    .. code-block:: python

        mydecorator = mydecorator(a, b)(myfunction)


Definition
==========
.. code-block:: python

    def mydecorator(a=1, b=2):
        def decorator(func):

            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper

        return decorator


    @mydecorator(a=0)
    def echo(name):
        print(name)


    echo('Mark Watney')
    # Mark Watney


Examples
========
.. code-block:: python
    :caption: Deprecated

    def deprecated(removed_in_version=None):
        def decorator(func):
            def wrapper(*args, **kwargs):
                name = func.__name__
                file = func.__code__.co_filename
                line = func.__code__.co_firstlineno + 1
                message = f"Call to deprecated function {name} in {file} at line {line}"
                message += f'\nIt will be removed in {removed_in_version}'

                import warnings
                warnings.warn(message, DeprecationWarning)
                return func(*args, **kwargs)

            return wrapper
        return decorator


    @deprecated(removed_in_version=2.0)
    def myfunction():
        pass


    myfunction()
    # /tmp/my_script.py:11: DeprecationWarning: Call to deprecated function myfunction in /tmp/my_script.py at line 19
    # It will be removed in 2.0

.. code-block:: python
    :caption: Timeout

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


    if __name__ == '__main__':
        countdown(5)
    # 4
    # 3
    # 2
    # Sorry, timeout

.. code-block:: python
    :caption: Timeout

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


    if __name__ == '__main__':
        countdown(5)
    # 4
    # 3
    # 2
    # TimeoutError: Timeout


Assignments
===========

Decorator Arguments Astronauts
------------------------------
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/decorator_arguments_astronauts.py`


:English:
    #. Use data from "Input" section (see below)
    #. Create decorator ``check_astronauts``
    #. To answer if person is an astronaut check field ``is_astronaut`` in ``crew: List[dict]``
    #. Decorator will call decorated function, only if all crew members has field with specified value
    #. Both field name and value are given as keyword arguments to decorator
    #. If any member is not an astronaut raise ``PermissionError`` and print his first name and last name
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Stwórz dekorator ``check_astronauts``
    #. Aby odpowiedzieć czy osoba jest astronautą sprawdź pole ``is_astronaut`` in ``crew: List[dict]``
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
* Complexity level: medium
* Lines of code to write: 20 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/decorator_arguments_typecheck.py`

:English:
    .. todo:: English translation

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz dekorator do sprawdzania typów
    #. Dekorator ma sprawdzać typy danych, wszystkich parametrów wchodzących do funkcji
    #. Jeżeli, którykolwiek się nie zgadza, wyrzuć wyjątek ``TypeError``
    #. Dekorator może przyjmować argument ``check_return: bool``
    #. Jeżeli argument jest ``True`` to sprawdź również poprawność typu danych zwracanych przez funkcję
    #. Wyjątek ma wypisywać:

        * nazwę parametru
        * typ, który parametr ma (nieprawidłowy)
        * typ, który był oczekiwany

:Input:
    .. code-block:: python

        @check_types(check_return=True)
        def echo(a: str, b: int, c: float = 0) -> bool:
            print('Function run as expected')
            return a * b


        echo('a', 2)
        echo('a', 2)
        echo('b', 2)
        echo(a='b', b=2)
        echo(b=2, a='b')
        echo('b', b=2)

:Hint:
    .. code-block:: python

        echo.__annotations__
        # {'a': <class 'str'>, 'b': <class 'int'>, 'c': <class 'float'>, 'return': <class 'bool'>}
