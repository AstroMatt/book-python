*********************************
Function Decorator with Functions
*********************************


Syntax
======
* ``mydecorator`` is a decorator name
* ``my_function`` is a function name
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments

Syntax:
    .. code-block:: python

        @mydecorator
        def my_function(*args, **kwargs):
            pass

Is equivalent to:
    .. code-block:: python

        my_function = mydecorator(my_function)


Definition
==========
* ``func`` is a pointer to function which is being decorated
* By calling ``func(*args, **kwargs)`` you actually run original (wrapped) function with it's original arguments
* Decorator must return pointer to ``wrapper``
* ``wrapper`` is a closure function
* ``wrapper`` name is a convention, but you can name it anyhow
* ``wrapper`` gets arguments passed to ``function``

.. code-block:: python

    def mydecorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

.. code-block:: python

    @mydecorator
    def echo(x):
        print(x)


    echo('hello')
    # hello


Examples
========
.. code-block:: python
    :caption: File exists

    import os


    def if_file_exists(func):
        def wrapper(filename):
            if os.path.exists(filename):
                return func(filename)
            else:
                print(f'File "{filename}" does not exists')
        return wrapper


    @if_file_exists
    def print_file(filename):
        with open(filename) as file:
            content = file.read()
            print(content)


    if __name__ == '__main__':
        print_file('/etc/passwd')
        print_file('/tmp/passwd')

.. code-block:: python
    :caption: Debug

    from datetime import datetime
    import logging

    logging.basicConfig(
        level='DEBUG',
        datefmt='"%Y-%m-%d", "%H:%M:%S"',
        format='{asctime}, "{levelname}", "{message}"',
        style='{'
    )


    def timeit(func):
        def wrapper(*args, **kwargs):
            time_start = datetime.now()
            result = func(*args, **kwargs)
            time_end = datetime.now()
            time = time_end - time_start
            logging.debug(f'Time: {time}')
            return result

        return wrapper


    def debug(func):
        def wrapper(*args, **kwargs):
            function = func.__name__
            logging.debug(f'Calling: {function=}, {args=}, {kwargs=}')
            result = func(*args, **kwargs)
            logging.debug(f'Result: {result}')
            return result

        return wrapper


    @timeit
    @debug
    def add_numbers(a, b):
        return a + b


    add_numbers(1, 2)
    # [DEBUG] Calling: function='add_numbers', args=(1, 2), kwargs={}
    # [DEBUG] Result: 3
    # [DEBUG] Time: 0:00:00.000105

    add_numbers(1, b=2)
    # [DEBUG] Calling: function='add_numbers', args=(1,), kwargs={'b': 2}
    # [DEBUG] Result: 3
    # [DEBUG] Time: 0:00:00.000042

    add_numbers(a=1, b=2)
    # [DEBUG] Calling: function='add_numbers', args=(), kwargs={'a': 1, 'b': 2}
    # [DEBUG] Result: 3
    # [DEBUG] Time: 0:00:00.000040

.. code-block:: python
    :caption: Cache with exposed cache

    _cache = {}

    def cache(func):
        def wrapper(n):
            if n not in _cache:
                _cache[n] = func(n)
            return _cache[n]
        return wrapper


    @cache
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)


    factorial(5)
    # 120

    print(_cache)
    # {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120}

.. code-block:: python
    :caption: Cache with hidden cache

    def cache(func):
        _cache = {}
        def wrapper(n):
            if n not in _cache:
                _cache[n] = func(n)
            return _cache[n]
        return wrapper


    @cache
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)


    factorial(5)
    # 120

.. code-block:: python
    :caption: Memoize

    def cache(func):
        def wrapper(n):
            cache = getattr(wrapper, '__cache__', {})
            if n not in cache:
                print(f'"n={n}" Not in cache. Calculating...')
                cache[n] = func(n)
                setattr(wrapper, '__cache__', cache)
            else:
                print(f'"n={n}" Found in cache. Fetching...')
            return cache[n]
        return wrapper


    @cache
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)


    print(factorial(3))
    # "n=3" Not in cache. Calculating...
    # "n=2" Not in cache. Calculating...
    # "n=1" Not in cache. Calculating...
    # "n=0" Not in cache. Calculating...
    # 6

    print(factorial.__cache__)
    # {3: 6}

    print(factorial(5))
    # "n=5" Not in cache. Calculating...
    # "n=4" Not in cache. Calculating...
    # "n=3" Found in cache. Fetching...
    # 120

    print(factorial.__cache__)
    # {3: 6, 4: 24, 5: 120}

    print(factorial(6))
    # "n=6" Not in cache. Calculating...
    # "n=5" Found in cache. Fetching...
    # 720

    print(factorial.__cache__)
    # {3: 6, 4: 24, 5: 120, 6: 720}

    print(factorial(4))
    # "n=4" Found in cache. Fetching...
    # 24

    print(factorial.__cache__)
    # {3: 6, 4: 24, 5: 120, 6: 720}

.. code-block:: python
    :caption: Flask URL Routing

    from flask import json
    from flask import Response
    from flask import render_template
    from flask import Flask

    app = Flask(__name__)


    @app.route('/summary')
    def summary():
        data = {'firstname': 'Jan', 'lastname': 'Twardowski'}
        return Response(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )

    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        post = ... # get post from Database by post_id
        return render_template('post.html', post=post)

    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html', name=name)

.. code-block:: python
    :caption: FastAPI URL routing

    from typing import Optional
    from fastapi import FastAPI

    app = FastAPI()


    @app.get("/")
    async def read_root():
        return {"Hello": "World"}


    @app.get("/items/{item_id}")
    async def read_item(item_id: int, q: Optional[str] = None):
        return {"item_id": item_id, "q": q}

.. code-block:: python
    :caption: Django Login Required. Decorator checks whether user is_authenticated. If not, user will be redirected to login page.

    from django.shortcuts import render


    def edit_profile(request):
        if not request.user.is_authenticated:
            return render(request, 'templates/login_error.html')
        else:
            return render(request, 'templates/edit-profile.html')


    def delete_profile(request):
        if not request.user.is_authenticated:
            return render(request, 'templates/login_error.html')
        else:
            return render(request, 'templates/delete-profile.html')

.. code-block:: python

    from django.shortcuts import render
    from django.contrib.auth.decorators import login_required


    @login_required
    def edit_profile(request):
        return render(request, 'templates/edit-profile.html')


    @login_required
    def delete_profile(request):
        return render(request, 'templates/delete-profile.html')


Assignments
===========

Decorator Function Allowed
--------------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/decorator_func_allowed.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create decorator ``if_allowed``
    #. Decorator calls function, only when ``_allowed`` is ``True``
    #. Else raise an exception ``PermissionError``
    #. Run program and check what happend
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Stwórz dekorator ``if_allowed``
    #. Dekorator wywołuje funkcję, tylko gdy ``_allowed`` jest ``True``
    #. W przeciwnym przypadku podnieś wyjątek ``PermissionError``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        @if_allowed
        def echo(text):
            print(text)

:Output:
    .. code-block:: python

        """
        >>> _allowed = True
        >>> echo('hello')
        hello

        >>> _allowed = False
        >>> echo('hello')
        Traceback (most recent call last):
            ...
        PermissionError
        """

Decorator Function Astronauts
-----------------------------
* Complexity level: easy
* Lines of code to write: 7 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/decorator_func_astronauts.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create decorator ``check_astronauts``
    #. To answer if person is an astronaut check field ``is_astronaut`` in ``crew: List[dict]``
    #. Decorator will call decorated function, only if all crew members are astronauts
    #. If any member is not an astronaut raise ``PermissionError`` and print his first name and last name
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Stwórz dekorator ``check_astronauts``
    #. Aby odpowiedzieć czy osoba jest astronautą sprawdź pole ``is_astronaut`` in ``crew: List[dict]``
    #. Dekorator wywoła dekorowaną funkcję, tylko gdy wszyscy członkowe załogi są astronautami
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


        @check_astronauts
        def launch(crew):
            crew = ', '.join(astro['name'] for astro in crew)
            print(f'Launching {crew}')

:Output:
    .. code-block:: python

        """
        >>> launch(CREW_PRIMARY)
        Launching Jan Twardowski, Mark Watney, Melissa Lewis

        >>> launch(CREW_BACKUP)
        Traceback (most recent call last):
            ...
        PermissionError: Alex Vogel is not an astronaut
        """

Decorator Function Memoization
------------------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/decorator_func_memoization.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create decorator ``@cache``
    #. Decorator must check before running function, if for given argument the computation was already done:

        * if yes, return from ``_cache``
        * if not, calculate new result, update cache and return computed value

    #. Compare execution time using ``timeit``

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Stwórz dekorator ``@cache``
    #. Decorator ma sprawdzać przed uruchomieniem funkcji, czy dla danego argumenu wynik został już wcześniej obliczony:

        * jeżeli tak, to zwraca dane z ``_cache``
        * jeżeli nie, to oblicza, aktualizuje ``_cache``, a następnie zwraca wartość

    #. Porównaj prędkość działania za pomocą ``timeit``

:Input:
    .. code-block:: python

        import sys
        from timeit import timeit
        sys.setrecursionlimit(5000)


        def cache(func):
            _cache = {}
            raise NotImplementedError


        @cache
        def fn1(n):
            if n == 0:
                return 1
            else:
                return n * fn1(n-1)


        def fn2(n):
            if n == 0:
                return 1
            else:
                return n * fn2(n-1)


        duration_cache = timeit(stmt='fn1(500); fn1(400); fn1(450); fn1(350)', globals=globals(), number=100_000)
        duration_nocache = timeit(stmt='fn2(500); fn2(400); fn2(450); fn2(350)', globals=globals(), number=100_000)
        duration_ratio = duration_nocache / duration_cache

        print(f'With Cache time: {duration_cache:.4f} seconds')
        print(f'Without Cache time: {duration_nocache:.3f} seconds')
        print(f'Cached solution is {duration_ratio:.1f} times faster')

Decorator Function Abspath
--------------------------
* Complexity level: easy
* Lines of code to write: 7 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/decorator_func_abspath.py`

:English:
    #. Ask user to input file path
    #. Create function ``display(file: str) -> str`` which prints file content
    #. Create decorator ``abspath``
    #. Decorator converts to absolute path (``current_directory`` + ``filename``), if filename given as an argument is a relative path

:Polish:
    #. Poproś użytkownika o podanie ścieżki do pliku
    #. Stwórz funkcję ``display(file: str) -> str`` która wyświetla zawartość pliku
    #. Stwórz dekorator ``abspath``
    #. Dekorator zamienia ścieżkę na bezwzględną (``current_directory`` + ``filename``), jeżeli nazwa pliku podana jako argument jest względna

:Output:
    .. code-block:: python

        @abspath
        def display(file):
            print(f'Reading file {file}')


        display('iris.csv')
        # Reading file /home/python/iris.csv

        display('/home/python/iris.csv')
        # Reading file /home/python/iris.csv

:Hint:
    * ``intput()``
    * ``from pathlib import Path``
    * ``current_directory = Path.cwd()``
    * ``path = Path(current_directory, filename)``

Decorator Function Type Check
-----------------------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/decorator_func_typecheck.py`

:English:
    .. todo:: English translation

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz dekorator ``check_types``
    #. Dekorator ma sprawdzać typy danych, wszystkich parametrów wchodzących do funkcji
    #. Jeżeli, którykolwiek się nie zgadza, wyrzuć wyjątek ``TypeError``
    #. Wyjątek ma wypisywać:

        * nazwę parametru
        * typ, który parametr ma (nieprawidłowy)
        * typ, który był oczekiwany

:Input:
    .. code-block:: python

        @check_types
        def echo(a: str, b: int, c: float = 0.0) -> bool:
            print('Function run as expected')
            return bool(a * b)


        print(echo('a', 2))
        print(echo('a', 2))
        print(echo('b', 2))
        print(echo(a='b', b=2))
        print(echo(b=2, a='b'))
        print(echo('b', b=2))

:Hint:
    .. code-block:: python

        echo.__annotations__
        # {'a': <class 'str'>, 'b': <class 'int'>, 'c': <class 'float'>, 'return': <class 'bool'>}
