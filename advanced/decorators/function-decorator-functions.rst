*********************************
Function Decorator with Functions
*********************************


Syntax
======
Syntax:
    .. code-block:: python

        @mydecorator
        def myfunction(*args, **kwargs):
            pass

Is equivalent to:
    .. code-block:: python

        myfunction = mydecorator(myfunction)


Definition
==========
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


Single Decorator
================
.. code-block:: python
    :caption: File exists


    def if_file_exists(func):
        def wrapper(file):
            import os
            if os.path.exists(file):
                return func(file)
            else:
                print(f'File "{file}" does not exists')
        return wrapper


    @if_file_exists
    def display(file):
        with open(file) as f:
            print(f.read())


    if __name__ == '__main__':
        display('/etc/passwd')
        display('/tmp/passwd')

.. code-block:: python

    from datetime import datetime


    def timeit(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            func(*args, **kwargs)
            end = datetime.now()
            print(f'Time: {end-start}')
        return wrapper


    @timeit
    def add_numbers(a, b):
        return a + b


    add_numbers(1, 2)
    # Time: 0:00:00.000007

    add_numbers(1, b=2)
    # Time: 0:00:00.000007

    add_numbers(a=1, b=2)
    # Time: 0:00:00.000007


.. code-block:: python

    import logging

    log = logging.getLogger()
    log.setLevel('DEBUG')


    def debug(func):
        def wrapper(*args, **kwargs):
            function = func.__name__
            log.debug(f'Calling: {function=}, {args=}, {kwargs=}')
            result = func(*args, **kwargs)
            log.debug(f'Result: {result}')
            return result

        return wrapper


    @debug
    def add_numbers(a, b):
        return a + b


    add_numbers(1, 2)
    # DEBUG:root:Calling: function='add_numbers', args=(1, 2), kwargs={}
    # DEBUG:root:Result: 3
    # 3

    add_numbers(1, b=2)
    # DEBUG:root:Calling: function='add_numbers', args=(1,), kwargs={'b': 2}
    # DEBUG:root:Result: 3
    # 3

    add_numbers(a=1, b=2)
    # DEBUG:root:Calling: function='add_numbers', args=(), kwargs={'a': 1, 'b': 2}
    # DEBUG:root:Result: 3
    # 3


Stack Decorators
================
.. code-block:: python
    :caption: Debug

    from datetime import datetime
    import logging

    logging.basicConfig(
        level='DEBUG',
        datefmt='"%Y-%m-%d", "%H:%M:%S"',
        format='{asctime}, "{levelname}", "{message}"',
        style='{')


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


Scope
=====
.. code-block:: text

    4! = 4 * 3!
    3! = 3 * 2!
    2! = 2 * 1!
    1! = 1 * 0!
    0! = 1

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
            return n * factorial(n-1)


    factorial(5)
    # 120

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
            return n * factorial(n-1)


    factorial(5)
    # 120

    print(_cache)
    # {0: 1,
    #  1: 1,
    #  2: 2,
    #  3: 6,
    #  4: 24,
    #  5: 120}

.. code-block:: python
    :caption: Memoize

    def cache(func):
        def wrapper(n):
            if n not in wrapper._cache:
                wrapper._cache[n] = func(n)
            return wrapper._cache[n]
        if not hasattr(wrapper, '_cache'):
            setattr(wrapper, '_cache', {})
        return wrapper


    @cache
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)


    print(factorial(4))
    # 24

    print(factorial._cache)
    # {0: 1,
    #  1: 1,
    #  2: 2,
    #  3: 6,
    #  4: 24}

    print(factorial(6))
    # 720

    print(factorial._cache)
    # {3: 6, 4: 24, 5: 120}

    print(factorial(6))
    # 720

    print(factorial._cache)
    # {0: 1,
    #  1: 1,
    #  2: 2,
    #  3: 6,
    #  4: 24,
    #  5: 120,
    #  6: 720}

    print(factorial(3))
    # 6

    print(factorial._cache)
    # {0: 1,
    #  1: 1,
    #  2: 2,
    #  3: 6,
    #  4: 24,
    #  5: 120,
    #  6: 720}


Examples
========
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
    .. code-block:: text

        >>> _allowed = True
        >>> echo('hello')
        hello

        >>> _allowed = False
        >>> echo('hello')
        Traceback (most recent call last):
            ...
        PermissionError

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
    #. Compare result with "Output" section (see below)

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
    .. code-block:: text

        >>> launch(CREW_PRIMARY)
        Launching Jan Twardowski, Mark Watney, Melissa Lewis

        >>> launch(CREW_BACKUP)
        Traceback (most recent call last):
            ...
        PermissionError: Alex Vogel is not an astronaut

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
    #. Use data from "Input" section (see below)
    #. Absolute path is when ``path`` starts with ``current_directory``
    #. Create decorator ``abspath``
    #. If ``path`` is relative, then ``abspath`` will convert it to absolute
    #. If ``path`` is absolute, then ``abspath`` will not modify it
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Ścieżka bezwzględna jest gdy ``path`` zaczyna się od ``current_directory``
    #. Stwórz dekorator ``abspath``
    #. Jeżeli ``path`` jest względne, to ``abspath`` zamieni ją na bezwzględną
    #. Jeżeli ``path`` jest bezwzględna, to ``abspath`` nie będzie jej modyfikował
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        @abspath
        def display(path):
            return str(path)

:Output:
    .. code-block:: text

        >>> from pathlib import Path
        >>> cwd = str(Path().cwd())
        >>> display('iris.csv').startswith(cwd)
        True
        >>> display('iris.csv').endswith('iris.csv')
        True
        >>> display('/home/python/iris.csv')
        '/home/python/iris.csv'

:Hint:
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
