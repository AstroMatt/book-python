.. _Decorator Class with Func:

*************************
Decorator Class with Func
*************************


Rationale
=========
* ``MyDecorator`` is a decorator name
* ``myfunction`` is a function name

Syntax:
    .. code-block:: python

        @MyDecorator
        def myfunction(*args, **kwargs):
            ...

Is equivalent to:
    .. code-block:: python

        myfunction = MyDecorator(myfunction)


Syntax
======
* ``cls`` is a pointer to class which is being decorated (``MyClass`` in this case)
* ``Wrapper`` is a closure class
* ``Wrapper`` name is a convention, but you can name it anyhow
* ``Wrapper`` can inherit from ``MyClass``
* Decorator must return pointer to ``Wrapper``

.. code-block:: python
    :caption: Definition

    class MyDecorator:
        def __init__(self, func):
            self._func = func

        def __call__(self, *args, **kwargs):
            return self._func(*args, **kwargs)

.. code-block:: python
    :caption: Decoration

    @MyDecorator
    def myfunction():
        ...

.. code-block:: python
    :caption: Usage

    myfunction()


Example
=======
.. code-block:: python

    class Run:
        def __init__(self, func):
            self._func = func

        def __call__(self, *args, **kwargs):
            return self._func(*args, **kwargs)


    @Run
    def hello(name):
        return f'My name... {name}'


    hello('José Jiménez')
    # 'My name... José Jiménez'


Use Cases
=========
.. code-block:: python
    :caption: Login Check

    class User:
        def __init__(self):
            self.is_authenticated = False

        def login(self, username, password):
            self.is_authenticated = True


    class LoginCheck:
        def __init__(self, func):
            self._func = func

        def __call__(self, *args, **kwargs):
            if user.is_authenticated:
                return self._func(*args, **kwargs)
            else:
                print('Permission Denied')


    @LoginCheck
    def edit_profile():
        print('Editing profile...')


    user = User()

    edit_profile()
    # Permission Denied

    user.login('admin', 'MyVoiceIsMyPassword')

    edit_profile()
    # Editing profile...

.. code-block:: python
    :caption: Dict Cache

    class Cache(dict):
        def __init__(self, func):
            self._func = func

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            self[key] = self._func(*key)
            return self[key]


    @Cache
    def myfunction(a, b):
        return a * b


    myfunction(2, 4)           # 8         # Computed
    myfunction('hi', 3)        # 'hihihi'  # Computed
    myfunction('ha', 3)        # 'hahaha'  # Computed

    myfunction('ha', 3)        # 'hahaha'  # Fetched from cache
    myfunction('hi', 3)        # 'hihihi'  # Fetched from cache
    myfunction(2, 4)           # 8         # Fetched from cache
    myfunction(4, 2)           # 8         # Computed


    myfunction
    # {
    #   (2, 4): 8,
    #   ('hi ', 3): 'hihihi',
    #   ('ha', 3): 'hahaha',
    #   (4, 2): 8,
    # }


Assignments
===========

.. literalinclude:: solution/decorator_cls_syntax.py
    :caption: :download:`Solution <solution/decorator_cls_syntax.py>`
    :end-before: # Solution

.. literalinclude:: solution/decorator_cls_abspath.py
    :caption: :download:`Solution <solution/decorator_cls_abspath.py>`
    :end-before: # Solution

.. literalinclude:: solution/decorator_cls_typecheck.py
    :caption: :download:`Solution <solution/decorator_cls_typecheck.py>`
    :end-before: # Solution
