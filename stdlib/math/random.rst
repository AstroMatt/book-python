.. _Math Random:

***********
Math Random
***********


``random``
==========
.. csv-table:: ``random``
    :header-rows: 1

    "Function", "Description"
    "``random.random()``", "Random float:  0.0 <= x < 1.0"
    "``random.randint(min, max)``", "Return a random integer N such that ``min <= N <= max``. Max is included"
    "``random.gauss(mu, sigma)``", "Gaussian distribution. mu is the mean, and sigma is the standard deviation"
    "``random.shuffle(list)``", "Randomize order of list (in place)"
    "``random.choice(list)``", "Single random element from a sequence"
    "``random.sample(list, k)``", "k random elements from list without replacement"
    "``random.seed(a=None, version=2)``", "Initialize the random number generator. If a is omitted or None, the current system time is used"


Pseudo and Pure random numbers
==============================
* What are pseudorandom numbers?
* Why it is not possible to generate a pure random number?
* What is ``random.seed(0)``?


Assignments
===========

Random numbers
--------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/random_sample.py`
* Last update: 2020-10-01

:English:
    #. Print 6 random integers without repetition in range from 1 to 49

:Polish:
    #. Wyświetl 6 losowych i nie powtarzających się liczb całkowitych z zakresu od 1 do 49.

Sum of inner elements
---------------------
* Complexity level: medium
* Lines of code to write: 5 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/random_matrix.py`
* Last update: 2020-10-01

:English:
    #. Use only ``random`` module
    #. Set ``random.seed(0)``
    #. Generate ``outer: List[List[int]]`` with 16x16 random digits (0-9 inclusive)
    #. Calculate sum of inner 4x4 elements
    #. Inner matrix is exactly in the middle of outer

:Polish:
    #. Używaj tylko modułu ``random``
    #. Ustaw ``random.seed(0)``
    #. Wygeneruj ``outer: List[List[int]]`` z 16x16 losowych cyfr (0-9 włącznie)
    #. Policz sumę środkowych 4x4 elementów
    #. Środkowa macierz jest dokładnie w środku większej

.. figure:: img/random-inner-sum.png
    :width: 75%
    :align: center

    Sum of inner elements
