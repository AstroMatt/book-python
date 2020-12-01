*********
Namespace
*********


Rationale
=========
* Functions provide namespaces
* Only code inside that namespace can access it's locals

.. code-block:: python

    def run(a=1):
        b = 2
        print(f'{a=}, {b=}')


    print(a)
    # Traceback (most recent call last):
    # NameError: name 'a' is not defined

    print(b)
    # Traceback (most recent call last):
    # NameError: name 'b' is not defined

    run()
    # a=1, b=2


Locals
======
.. code-block:: python

    def run(a=1):
        b = 1
        print(locals())


Define
======

.. code-block:: python

    def run():
        def a():
            print('a')

        def b():
            print('b')


    run()


Execute
=======
.. code-block:: python

    def run():
        def a():
            print('a')

        def b():
            print('b')

        a()
        b()


    result = run()
    print(result)
    # None

Return
======
.. code-block:: python

    def run():
        def a():
            print('a')

        def b():
            print('b')

        return b

    run()()
    run().__call__()
