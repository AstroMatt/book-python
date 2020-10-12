*******************
Functional Paradigm
*******************


Rationale
=========
* In computer science, functional programming is a programming paradigm where programs are constructed by applying and composing functions. [WikipediaFunc]_

* Functions are treated as first-class citizens, meaning that they can be bound to names (including local identifiers), passed as arguments, and returned from other functions, just as any other data type can. [WikipediaFunc]_

* The most significant differences between functional programming from imperative programming is the fact that functional programming avoids side effects, which are used in imperative programming to implement state and I/O.

* Pure functional programming completely prevents side-effects and provides referential transparency. Higher-order functions are rarely used in older imperative programming. A traditional imperative program might use a loop to traverse and modify a list. A functional program, on the other hand, would probably use a higher-order “map” function that takes a function and a list, generating and returning a new list by applying the function to each list item. [Spiewak2008]_

* Proponents of purely functional programming claim that by restricting side effects, programs can have fewer bugs, be easier to debug and test, and be more suited to formal verification. [Hughes1984]_ [Hudak1989]_

* Functional programming languages are typically less efficient in their use of CPU and memory than imperative languages such as C and Pascal [Paulson1996]_. This is related to the fact that some mutable data structures like arrays have a very straightforward implementation using present hardware.

.. code-block:: python

    def hello():
        print('Hello')


    type(hello)
    # <class 'function'>

    callable(hello)
    # True


Higher-Order Function
=====================
* Higher-order functions are functions that can either take other functions as arguments or return them as results.

.. code-block:: python

    def lower():
        ...


    def higher():
        return lower

.. code-block:: python

    def http_request(url, on_success, on_error):
        try:
            result = ...
        except Exception as error:
            return on_error(error)
        else:
            return on_success(result)


    http_request(
        url = 'https://python.astrotech.io',
        on_success = lambda result: print(result),
        on_error = lambda error: print(error))


Pure Functions
==============
* Pure functions (or expressions) have no side effects (memory or I/O).
* This means that pure functions have several useful properties, many of which can be used to optimize the code:

    * If the result of a pure expression is not used, it can be removed without affecting other expressions.
    * If a pure function is called with arguments that cause no side-effects, the result is constant with respect to that argument list (sometimes called referential transparency), i.e., calling the pure function again with the same arguments returns the same result. (This can enable caching optimizations such as memoization.)
    * If there is no data dependency between two pure expressions, their order can be reversed, or they can be performed in parallel and they cannot interfere with one another (in other terms, the evaluation of any pure expression is thread-safe).
    * If the entire language does not allow side-effects, then any evaluation strategy can be used; this gives the compiler freedom to reorder or combine the evaluation of expressions in a program (for example, using deforestation). [WikipediaFunc]_

.. code-block:: python
    :caption: Pure functions

    def add(a, b):
        return a + b


    def odd(x):
        return x % 2


    def cube(x):
        return x ** 3

.. code-block:: python
    :caption: Pure functions

    DATA = [
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
    ]


    def function(data, species):
        result = []
        for *features, label in data:
            if label == species:
                result.append(features)
        return result

.. code-block:: python
    :caption: Impure functions

    DATA = [
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
    ]


    def function(species):
        result = []
        for *features, label in DATA:
            if label == species:
                result.append(features)
        return result


Recursion
=========
* Also known as recurrence
* Iteration (looping) in functional languages is usually accomplished via recursion.
* Recursive functions invoke themselves, letting an operation be repeated until it reaches the base case.
* In general, recursion requires maintaining a stack, which consumes space in a linear amount to the depth of recursion. This could make recursion prohibitively expensive to use instead of imperative loops. However, a special form of recursion known as tail recursion can be recognized and optimized by a compiler into the same code used to implement iteration in imperative languages. Tail recursion optimization can be implemented by transforming the program into continuation passing style during compiling, among other approaches. [WikipediaFunc]_
* CPython implementation doesn't optimize tail recursion
* Tail recursion is not a particularly efficient technique in Python
* Unbridled recursion causes stack overflows!
* Rewriting the algorithm iteratively, is generally a better idea

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

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)


Data Structures
===============
* Purely functional data structures have persistence, a property of keeping previous versions of the data structure unmodified.
* The array with constant access and update times is a basic component of most imperative languages, and many imperative data-structures, such as the hash table and binary heap, are based on arrays. Arrays can be replaced by maps or random access lists, which admit purely functional implementation, but have logarithmic access and update times. [WikipediaFunc]_


Referential Transparency
========================
* Functional programs do not have assignment statements, that is, the value of a variable in a functional program never changes once defined. This eliminates any chances of side effects because any variable can be replaced with its actual value at any point of execution. So, functional programs are referentially transparent. [Hughes1984]_


First-class Function
====================
* If a function can be assigned to a variable or passed as object/variable to other function.
* Can be used as parameters
* Can be used as a return value
* Can be assigned to variables
* Can be stored in data structures such as hash tables, lists, ...

.. code-block:: python

    def lower():
        return 'hello'


    def higher():
        return lower


    result = higher()     # <function __main__.lower()>
    result()              # 'hello'

.. code-block:: python

    from datetime import datetime
    from time import sleep


    now = datetime.now()

    print(now)            # 1969-07-21 02:56:15
    sleep(10)
    print(now)            # 1969-07-21 02:56:15

.. code-block:: python

    from datetime import datetime
    from time import sleep


    now = datetime.now

    print(now())          # 1969-07-21 02:56:15
    sleep(10)
    print(now())          # 1969-07-21 02:56:25


References
==========

.. [WikipediaFunc] Functional programming. URL: https://en.wikipedia.org/wiki/Functional_programming Retrieved: 2020-10-09

.. [Hudak1989] Hudak, Paul. "Conception, evolution, and application of functional programming languages". ACM Computing Surveys. 21 (3): 359–411. doi:10.1145/72551.72554. S2CID 207637854. 1989.

.. [Hughes1984] Hughes, John. "Why Functional Programming Matters". Chalmers University of Technology. 1984.

.. [Spiewak2008] Spiewak, Daniel. "Implementing Persistent Vectors in Scala". Code Commit. 2008.

.. [Paulson1996] Paulson, Larry C. "ML for the Working Programmer". Cambridge University Press. ISBN: 978-0-521-56543-1. Retrieved: 2013-02-10. 1996.
