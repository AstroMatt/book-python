*************
Series Sample
*************


Head
====
.. code-block:: python

    s.head(2)
    s.head(n=1)


Tail
=====
.. code-block:: python

    s.tail(2)
    s.tail(n=1)


First
=====
.. code-block:: python

    s.first('Y')
    s.first('M')
    s.first('D')
    s.first('W')


Last
====
.. code-block:: python

    s.last('Y')
    s.last('M')
    s.last('D')
    s.last('W')


Sample
======
* 1/4 is 25%
* .05 is 5%
* 0.5 is 50%
* 1.0 is 100%

.. code-block:: python
    :caption: `n` number or fraction random rows with and without repetition

    s.sample()
    s.sample(2)
    s.sample(n=2, replace=True)
    s.sample(frac=1/4)
    s.sample(frac=0.5)


Reset Index
===========
.. code-block:: python

    s.sample(frac=1.0).reset_index()


Assignments
===========

Series Sample
--------------
* Assignment: Series Sample
* Last update: 2020-10-01
* Complexity: easy
* Lines of code: 5 lines
* Estimated time: 5 min
* Filename: :download:`assignments/series_sample.py`

English:
    #. Set random seed to zero
    #. Create ``pd.Series`` with 100 random numbers from standard normal distribution
    #. Series Index are following dates since 2000
    #. Print values:

        * first in the series,
        * last 5 elements in the series,
        * first two weeks in the series,
        * last month in the series,
        * three random elements,
        * 125% of random elements with replacement.

Polish:
    #. Ustaw ziarno losowości na zero
    #. Stwórz ``pd.Series`` z 100 losowymi liczbami z rozkładu normalnego
    #. Indeksem w serii mają być kolejne dni od 2000 roku
    #. Wypisz wartości:

        * pierwszy w serii,
        * ostatnie 5 elementów w serii,
        * dwa pierwsze tygodnie w serii,
        * ostatni miesiąc w serii,
        * trzy losowe element,
        * 125% losowych elementów z powtórzeniami.

Hints:
    * ``np.random.seed(0)``
    * ``np.random.randn(n)``
