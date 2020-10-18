*****
Numpy
*****


NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.


Rationale
=========
NumPy is the fundamental package for scientific computing with Python. It contains among other things:

    * a powerful N-dimensional array object
    * sophisticated (broadcasting) functions
    * tools for integrating C/C++ and Fortran code
    * useful linear algebra, Fourier transform, and random number capabilities

Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.

* http://www.numpy.org/


Installation
============
.. code-block:: console
    :caption: Installation

    $ pip install numpy

.. code-block:: console
    :caption: Upgrade

    $ pip install --upgrade numpy

.. code-block:: python
    :caption: Check version

    import numpy as np

    np.__version__
    # '1.19.1'


Performance
===========
.. code-block:: python
    :caption: Results with Jupyter and ``%%timeit -n 1_000_000 -r 10``

    import numpy as np


    np.arange(0, 100, step=2, dtype=float)
    # 756 ns ± 10.3 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

    np.array(range(0, 100, 2), dtype=float)
    # 8.28 µs ± 364 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

    np.array([x for x in range(0, 100) if x % 2 == 0], dtype=float)
    # 9.76 µs ± 324 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

    np.array([float(x) for x in range(0, 100) if x % 2 == 0])
    # 12.7 µs ± 195 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

    np.array([float(x) for x in range(0, 100, 2)])
    # 8.35 µs ± 196 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

    np.array([x for x in range(0, 100, 2)], dtype=float)
    # 5.89 µs ± 77 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)


.. todo:: Assignments:

    * http://www.labri.fr/perso/nrougier/teaching/numpy.100/
    * https://github.com/rougier/numpy-100


References
==========
.. bibliography:: _references/bibliography.bib
    :style: plain
    :labelprefix: NP
    :all:
