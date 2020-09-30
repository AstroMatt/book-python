*********************************
Function Decorator with Functions
*********************************


Rationale
=========
Syntax:
    .. code-block:: python

        @mydecorator
        def myfunction(*args, **kwargs):
            ...

Is equivalent to:
    .. code-block:: python

        myfunction = mydecorator(myfunction)


Syntax
======
* Decorator must return pointer to ``wrapper``
* ``wrapper`` is a closure function
* ``wrapper`` name is a convention, but you can name it anyhow
* ``wrapper`` gets arguments passed to ``function``

.. code-block:: python
    :caption: Definition

    def mydecorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

.. code-block:: python
    :caption: Decoration

    @mydecorator
    def myfunction():
        ...

.. code-block:: python
    :caption: Usage

    myfunction()


Example
=======
.. code-block:: python

    def run(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    @run
    def hello(name):
        return f'My name... {name}'

    hello('José Jiménez')
    # 'My name... José Jiménez'


Use Cases
=========
.. code-block:: python
    :caption: File exists

    import os

    def ifexists(func):
        def wrapper(file):
            if os.path.exists(file):
                return func(file)
            else:
                print(f'File {file} does not exist')
        return wrapper


    @ifexists
    def display(file):
        print(f'Printing file {file}')


    display('/etc/passwd')
    # Printing file /etc/passwd

    display('/tmp/passwd')
    # File /tmp/passwd does not exist

.. code-block:: python
    :caption: Timeit

    from datetime import datetime


    def timeit(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            end = datetime.now()
            print(f'Duration: {end-start}')
            return result
        return wrapper


    @timeit
    def add(a, b):
        return a + b


    add(1, 2)
    # Duration: 0:00:00.000006
    # 3

    add(1, b=2)
    # Duration: 0:00:00.000007
    # 3

    add(a=1, b=2)
    # Duration: 0:00:00.000008
    # 3

.. code-block:: python
    :caption: Debug

    def debug(func):
        def wrapper(*args, **kwargs):
            function = func.__name__
            print(f'Calling: {function=}, {args=}, {kwargs=}')
            result = func(*args, **kwargs)
            print(f'Result: {result}')
            return result
        return wrapper


    @debug
    def add(a, b):
        return a + b


    add(1, 2)
    # Calling: function='add', args=(1, 2), kwargs={}
    # Result: 3
    # 3

    add(1, b=2)
    # Calling: function='add', args=(1,), kwargs={'b': 2}
    # Result: 3
    # 3

    add(a=1, b=2)
    # Calling: function='add', args=(), kwargs={'a': 1, 'b': 2}
    # Result: 3
    # 3

.. code-block:: python
    :caption: Stacked decorators

    from datetime import datetime
    import logging

    logging.basicConfig(
        level='DEBUG',
        datefmt='"%Y-%m-%d", "%H:%M:%S"',
        format='{asctime}, "{levelname}", "{message}"',
        style='{')

    log = logging.getLogger(__name__)


    def timeit(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            end = datetime.now()
            print(f'Duration: {end - start}')
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
    def add(a, b):
        return a + b

    add(1, 2)
    # "1969-07-21", "02:56:15", "DEBUG", "Calling: function='add', args=(1, 2), kwargs={}"
    # "1969-07-21", "02:56:15", "DEBUG", "Result: 3"
    # Duration: 0:00:00.000159
    # 3

    add(1, b=2)
    # "1969-07-21", "02:56:15", "DEBUG", "Calling: function='add', args=(1,), kwargs={'b': 2}"
    # "1969-07-21", "02:56:15", "DEBUG", "Result: 3"
    # Duration: 0:00:00.000162
    # 3

    add(a=1, b=2)
    # "1969-07-21", "02:56:15", "DEBUG", "Calling: function='add', args=(), kwargs={'a': 1, 'b': 2}"
    # "1969-07-21", "02:56:15", "DEBUG", "Result: 3"
    # Duration: 0:00:00.000153
    # 3


Scope
=====
.. code-block:: python
    :caption: Recap information about factorial (``n!``)

    """
    5! = 5 * 4!
    4! = 4 * 3!
    3! = 3 * 2!
    2! = 2 * 1!
    1! = 1 * 0!
    0! = 1
    """

    factorial(5)                                    # = 120
        return 5 * factorial(4)                     # 5 * 24 = 120
            return 4 * factorial(3)                 # 4 * 6 = 24
                return 3 * factorial(2)             # 3 * 2 = 6
                    return 2 * factorial(1)         # 2 * 1 = 2
                        return 1 * factorial(0)     # 1 * 1 = 1
                            return 1                # 1

.. code-block:: python
    :caption: Cache with global scope

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
    :caption: Cache with local scope

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
    :caption: Cache with embedded scope

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
            return n * factorial(n-1)


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
            mimetype='application/json')


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


    @app.get('/')
    async def read_root():
        return {'Hello': 'World'}


    @app.get('/items/{item_id}')
    async def read_item(item_id: int, q: Optional[str] = None):
        return {'item_id': item_id, 'q': q}

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

Decorator Function Disabled
---------------------------
* Assignment name: Decorator Function Disabled
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/decorator_func_disabled.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create decorator ``check``
    #. Decorator calls function, only when ``check.disabled`` is ``False``
    #. Else raise an exception ``PermissionError``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Stwórz dekorator ``check``
    #. Dekorator wywołuje funkcję, tylko gdy ``echo.disabled`` jest ``False``
    #. W przeciwnym przypadku podnieś wyjątek ``PermissionError``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        @check
        def echo(text):
            print(text)

:Output:
    .. code-block:: text

        >>> echo.disabled = False
        >>> echo('hello')
        hello

        >>> echo.disabled = True
        >>> echo('hello')
        Traceback (most recent call last):
            ...
        PermissionError: Function is disabled

Decorator Function Astronauts
-----------------------------
* Assignment name: Decorator Function Astronauts
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 7 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/decorator_func_astronauts.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create decorator ``check_astronauts``
    #. To answer if person is an astronaut check field ``is_astronaut`` in ``crew: list[dict]``
    #. Decorator will call decorated function, only if all crew members are astronauts
    #. If any member is not an astronaut raise ``PermissionError`` and print his first name and last name
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Stwórz dekorator ``check_astronauts``
    #. Aby odpowiedzieć czy osoba jest astronautą sprawdź pole ``is_astronaut`` in ``crew: list[dict]``
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
            return f'Launching: {crew}'

:Output:
    .. code-block:: text

        >>> launch(CREW_PRIMARY)
        'Launching: Jan Twardowski, Mark Watney, Melissa Lewis'

        >>> launch(CREW_BACKUP)
        Traceback (most recent call last):
            ...
        PermissionError: Alex Vogel is not an astronaut

Decorator Function Memoization
------------------------------
* Assignment name: Decorator Function Memoization
* Last update: 2020-10-01
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
* Assignment name: Decorator Function Abspath
* Last update: 2020-10-01
* Complexity level: easy
* Lines of code to write: 7 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/decorator_func_abspath.py`

:English:
    #. Use data from "Input" section (see below)
    #. Absolute path is when ``path`` starts with ``current_directory``
    #. Create function decorator ``abspath``
    #. If ``path`` is relative, then ``abspath`` will convert it to absolute
    #. If ``path`` is absolute, then ``abspath`` will not modify it
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Ścieżka bezwzględna jest gdy ``path`` zaczyna się od ``current_directory``
    #. Stwórz funkcję dekorator ``abspath``
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

:Hints:
    * ``from pathlib import Path``
    * ``current_directory = Path.cwd()``
    * ``path = Path(current_directory, filename)``

Decorator Function Type Check
-----------------------------
* Assignment name: Decorator Function Type Check
* Last update: 2020-10-01
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/decorator_func_typecheck.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create decorator function ``typecheck``
    #. Decorator checks types of all arguments (``*args`` oraz ``**kwargs``)
    #. Decorator checks return type
    #. In case when received type is not expected throw an exception ``TypeError`` with:

        * argument name
        * actual type
        * expected type

    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz dekorator funkcję ``typecheck``
    #. Dekorator sprawdza typy wszystkich argumentów (``*args`` oraz ``**kwargs``)
    #. Dekorator sprawdza typ zwracany
    #. W przypadku gdy otrzymany typ nie jest równy oczekiwanemu wyrzuć wyjątek ``TypeError`` z:

        * nazwa argumentu
        * aktualny typ
        * oczekiwany typ

    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        @typecheck
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
