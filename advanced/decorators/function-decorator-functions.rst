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

Usage
=====
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

    log = logging.getLogger(__name__)
    log.setLevel('DEBUG')


    def timeit(func):
        def wrapper(*args, **kwargs):
            time_start = datetime.now()
            result = func(*args, **kwargs)
            time_end = datetime.now()
            time = time_end - time_start
            log.debug(f'Time: {time}\n')
            return result
        return wrapper


    def debug(func):
        def wrapper(*args, **kwargs):
            function = func.__name__
            log.debug(f'Calling: {function=}, {args=}, {kwargs=}')
            result = func(*args, **kwargs)
            log.debug(f'Result: {result}')
            return result
        return wrapper


    @timeit
    @debug
    def add_numbers(a, b):
        return a + b


    add_numbers(1, 2)
    # DEBUG:__main__:Calling: function='add_numbers', args=(1, 2), kwargs={}
    # DEBUG:__main__:Result: 3
    # DEBUG:__main__:Time: 0:00:00.000117

    add_numbers(1, b=2)
    # DEBUG:__main__:Calling: function='add_numbers', args=(1,), kwargs={'b': 2}
    # DEBUG:__main__:Result: 3
    # DEBUG:__main__:Time: 0:00:00.000059

    add_numbers(a=1, b=2)
    # DEBUG:__main__:Calling: function='add_numbers', args=(), kwargs={'a': 1, 'b': 2}
    # DEBUG:__main__:Result: 3
    # DEBUG:__main__:Time: 0:00:00.000044

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

    print(CACHE)
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
        data = {'first_name': 'Jan', 'last_name': 'Twardowski'}
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

Decorator Function Memoization
------------------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/decorator_func_memoization.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create function ``factorial_cache(n: int) -> int``
    #. Create ``CACHE: Dict[int, int]`` with computation results from function

        * key: function argument
        * value: computation result

    #. Create decorator ``@cache``
    #. Decorator must check before running function, if for given argument the computation was already done:

        * if yes, return from ``CACHE``
        * if not, calculate new result, update cache and return computed value

    #. Using ``timeit``

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Stwórz funkcję ``factorial_cache(n: int) -> int``
    #. Stwórz ``CACHE: Dict[int, int]`` z wynikami wyliczenia funkcji

        * klucz: argument funkcji
        * wartość: wynik obliczeń

    #. Stwórz dekorator ``@cache``
    #. Decorator ma sprawdzać przed uruchomieniem funkcji, czy dla danego argumenu wynik został już wcześniej obliczony:

        * jeżeli tak, to zwraca dane z ``CACHE``
        * jeżeli nie, to oblicza, aktualizuje ``CACHE``, a następnie zwraca wartość

    #. Wykorzystując ``timeit`` porównaj prędkość działania z obliczaniem na bieżąco dla parametru 100


:Input:
    .. code-block:: python

        import sys
        from timeit import timeit

        sys.setrecursionlimit(5000)


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
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/decorator_func_abspath.py`

:English:
    #. Create function ``print_file(filename: str) -> str`` which prints file content (filename given as an argument)
    #. Create decorator ``to_absolute_path``
    #. Decorator converts to absolute path (``path`` + ``filename``), if filename given as an argument is a relative path

:Polish:
    #. Stwórz funkcję ``print_file(filename: str) -> str`` która wyświetla zawartość pliku (nazwa pliku podana jako argument)
    #. Stwórz dekorator ``to_absolute_path``
    #. Dekorator zamienia ścieżkę na bezwzględną (``path`` + ``filename``), jeżeli nazwa pliku podana jako argument jest względna

:Hint:
    * ``__file__``
    * ``os.path.dirname()``
    * ``os.path.join()``

Decorator Function Type Check
-----------------------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
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
        def echo(a: str, b: int, c: int = 0) -> bool:
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
        # {'a': <class 'str'>, 'return': <class 'bool'>, 'b': <class 'int'>}
