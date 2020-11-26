********
Closures
********


Rationale
=========
.. code-block:: python

    def f(x):
        def g(y):
            return x + y
        return g



Nested Function
===============
* Function inside the function
* Nested functions can access the variables of the enclosing scope

.. code-block:: python

    def run():
        def hello():
            print('hello')
        return hello


    hello()
    # Traceback (most recent call last):
    # NameError: name 'hello' is not defined

    run()
    # <function run.<locals>.hello at 0x104e13700>

    run()()
    # hello

    result = run()
    result()
    # hello


What is closure?
================
* technique by which the data is attached to some code even after end of those other original functions is called as closures
* Closures can avoid use of global variables and provides some form of data hiding
* When the interpreter detects the dependency of inner nested function on the outer function, it stores or makes sure that the variables in which inner function depends on are available even if the outer function goes away
* Method of binding data to a function without actually passing them as parameters is called closure
* It is a function object obj that remembers values in enclosing scopes even if they are not present in memory
* Closures provide some sort of data hiding as they are used as callback functions
* This helps us to reduce the use of global variables
* Useful for replacing hard-coded constants
* Closures prove to be efficient way when we have few functions in our code

.. code-block:: python

    firstname = 'Mark'
    lastname = 'Watney'

    def hello():
        print(firstname, lastname)


    hello()
    # Mark Watney

.. code-block:: python

    firstname = 'Mark'

    def run():
        lastname = 'Watney'

        def hello():
            print(firstname, lastname)

        return hello


    result = run()
    result()
    # Mark Watney

.. code-block:: python

    firstname = 'Mark'

    def run():
        lastname = 'Watney'

        def hello():
            print(firstname, lastname)

        return hello


    result = run()
    del run
    result()
    # Mark Watney


Assignments
===========

.. literalinclude:: solution/function_closure_define.py
    :caption: :download:`Solution <solution/function_closure_define.py>`
    :end-before: # Solution

.. literalinclude:: solution/function_closure_call.py
    :caption: :download:`Solution <solution/function_closure_call.py>`
    :end-before: # Solution
