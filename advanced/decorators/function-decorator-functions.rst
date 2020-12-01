.. _Decorator Function with Func:

****************************
Decorator Function with Func
****************************


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
            log.info(f'Duration: {end - start}')
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
    # "1969-07-21", "02:56:15", "INFO", "Duration: 0:00:00.000209"

    add(1, b=2)
    # "1969-07-21", "02:56:15", "DEBUG", "Calling: function='add', args=(1,), kwargs={'b': 2}"
    # "1969-07-21", "02:56:15", "DEBUG", "Result: 3"
    # "1969-07-21", "02:56:15", "INFO", "Duration: 0:00:00.000154"

    add(a=1, b=2)
    # "1969-07-21", "02:56:15", "DEBUG", "Calling: function='add', args=(), kwargs={'a': 1, 'b': 2}"
    # "1969-07-21", "02:56:15", "DEBUG", "Result: 3"
    # "1969-07-21", "02:56:15", "INFO", "Duration: 0:00:00.000083"


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

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

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
    # {0: 1,
    #  1: 1,
    #  2: 2,
    #  3: 6,
    #  4: 24,
    #  5: 120,
    #  6: 720}

    print(factorial(6))
    # 720

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


    @app.route('/post/<int:pk>')
    def post(pk):
        post = ... # get post from Database by pk
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
    async def index():
        return {'message': 'Hello World'}


    @app.get('/user/{pk}')
    async def user(pk: int):
        return {'pk': pk}


    @app.get('/search')
    async def items(q: Optional[str] = None):
        return {'q': q}

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

.. literalinclude:: solution/decorator_func_syntax.py
    :caption: :download:`Solution <solution/decorator_func_syntax.py>`
    :end-before: # Solution

.. literalinclude:: solution/decorator_func_disable.py
    :caption: :download:`Solution <solution/decorator_func_disable.py>`
    :end-before: # Solution

.. literalinclude:: solution/decorator_func_check.py
    :caption: :download:`Solution <solution/decorator_func_check.py>`
    :end-before: # Solution

.. literalinclude:: solution/decorator_func_astronauts.py
    :caption: :download:`Solution <solution/decorator_func_astronauts.py>`
    :end-before: # Solution

.. literalinclude:: solution/decorator_func_memoization.py
    :caption: :download:`Solution <solution/decorator_func_memoization.py>`
    :end-before: # Solution

.. literalinclude:: solution/decorator_func_abspath.py
    :caption: :download:`Solution <solution/decorator_func_abspath.py>`
    :end-before: # Solution

.. literalinclude:: solution/decorator_func_numeric.py
    :caption: :download:`Solution <solution/decorator_func_numeric.py>`
    :end-before: # Solution

.. literalinclude:: solution/decorator_func_typecheck.py
    :caption: :download:`Solution <solution/decorator_func_typecheck.py>`
    :end-before: # Solution

