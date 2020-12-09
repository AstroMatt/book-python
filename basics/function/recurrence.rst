.. _Function Recurrence:

*******************
Function Recurrence
*******************

.. epigraph::
    * Aby zrozumieć rekurencję – musisz najpierw zrozumieć rekursję.
    * Aby zrozumieć rekursję - musisz najpierw zrozumieć rekurencję.


Rationale
=========
* Also known as recursion
* Python isn't a functional language
* CPython implementation doesn't optimize tail recursion
* Tail recursion is not a particularly efficient technique in Python
* Unbridled recursion causes stack overflows!
* Rewriting the algorithm iteratively, is generally a better idea

.. figure:: img/function-recurrence-hanoi.jpg

    Hanoi Tower as a standard example of a recurrence. Source: [hanoi]_


Example
=======
.. code-block:: python

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

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


Recursion Depth Limit
=====================
* Default recursion depth limit is 1000
* Warning: Anaconda sets default recursion depth limit to 2000

.. code-block:: python

    import sys

    sys.setrecursionlimit(3000)


References
==========
.. [hanoi] https://dyermath.files.wordpress.com/2015/06/hanoi-13.jpg


Assignments
===========

.. literalinclude:: assignments/function_recurrence_brackets.py
    :caption: :download:`Solution <assignments/function_recurrence_brackets.py>`
    :end-before: # Solution
