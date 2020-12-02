***********
Polynomials
***********


Defining
========

Polynomial of degree three
--------------------------
.. code-block:: text
    :caption: Polynomial of degree three

    Ax^3 + Bx^2 + Cx^1 + D = 0
    1x^3 + 2x^2 + 3x^1 + 4 = 0

.. code-block:: python

    import numpy as np


    np.poly1d([1, 2, 3, 4])
    # poly1d([1, 2, 3, 4])

.. figure:: img/polynomial-3deg.png
    :width: 75%
    :align: center

    Polynomial of degree three ``Ax^3 + Bx^2 + Cx^1 + D = 0`` :cite:`NumpyPolynomial`

Polynomial of degree six
------------------------
.. code-block:: text
    :caption: Polynomial of degree six

    Ax^6 + Bx^5 + Cx^4 + Dx^3 + Ex^2 + Fx + G = 0
    1x^6 + 2x^5 + 3x^4 + 4x^3 + 5x^2 + 6x + 7 = 0

.. code-block:: python

    import numpy as np


    np.poly1d([1, 2, 3, 4, 5, 6, 7])
    # poly1d([1, 2, 3, 4, 5, 6, 7])

.. figure:: img/polynomial-6deg.png
    :width: 75%
    :align: center

    Polynomial of degree six ``Ax^6 + Bx^5 + Cx^4 + Dx^3 + Ex^2 + Fx + G = 0`` :cite:`NumpyPolynomial`


Find coefficients
=================
* Find the coefficients of a polynomial with the given sequence of roots
* Specifying the roots of a polynomial still leaves one degree of freedom, typically represented by an undetermined leading coefficient.

.. code-block:: python

    import numpy as np


    np.poly([0, 0, 0])
    # array([1., 0., 0., 0.])

    np.poly([1, 2])
    # array([ 1., -3.,  2.])

    np.poly([1, 2, 3, 4, 5, 6, 7])
    # array([ 1.0000e+00, -2.8000e+01,  3.2200e+02, -1.9600e+03,  6.7690e+03,
    #        -1.3132e+04,  1.3068e+04, -5.0400e+03])


Roots
=====
* Return the roots of a polynomial

.. code-block:: python

    import numpy as np


    np.roots([1, 2])
    # array([-2.])

    np.roots([0, 1, 3])
    # array([-3.])

    np.roots([1, 4, -2, 3])
    # array([-4.57974010+0.j , 0.28987005+0.75566815j, 0.28987005-0.75566815j])

    np.roots([ 1, -11, 9, 11, -10])
    #array([10.+0.0000000e+00j, -1.+0.0000000e+00j,
    #       1.+9.6357437e-09j, 1.-9.6357437e-09j])


Derivatives
===========

Derivative of a polynomial
--------------------------
.. code-block:: python

    import numpy as np


    np.polyder([1/4, 1/3, 1/2, 1, 0])
    # array([1., 1., 1., 1.])

    np.polyder([0.25, 0.33333333, 0.5, 1, 0])
    # array([1., 0.99999999, 1., 1.])

    np.polyder([1, 2, 3, 4])
    # array([3, 4, 3])

Antiderivative (indefinite integral) of a polynomial
----------------------------------------------------
* Return an antiderivative (indefinite integral) of a polynomial

.. code-block:: python

    import numpy as np


    np.polyint([1, 1, 1, 1])
    # array([0.25, 0.33333333, 0.5, 1., 0.])

    np.polyint([16, 9, 4, 2])
    # array([4., 3., 2., 2., 0.])


Evaluation
==========

Evaluate a polynomial at specific values
----------------------------------------
* Compute polynomial values
* Horner's scheme is used to evaluate the polynomial

.. code-block:: python

    import numpy as np


    np.polyval([1, -2, 0, 2], 4)
    # 34

Least squares polynomial fit
----------------------------
* Least squares polynomial fit

.. code-block:: python

    import numpy as np


    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [0, 2, 1, 3, 7, 10, 11, 19]

    np.polyfit(x, y, 2)
    # array([ 0.375 , -0.88690476, 1.05357143])


Polynomial Arithmetic
=====================
* ``np.polyadd()``
* ``np.polysub()``
* ``np.polymul()``
* ``np.polydiv()``

Sum of two polynomials
----------------------
.. code-block:: python

    import numpy as np


    np.polyadd([1, 2], [9, 5, 4])
    # array([9, 6, 6])


Assignments
===========

Numpy Polyfit
-------------
* Assignment: Numpy Polyfit
* Last update: 2020-10-01
* Complexity: easy
* Lines of code: 4 lines
* Estimated time: 5 min
* Filename: :download:`solution/numpy_polyfit.py`

English:
    #. Use data from "Given" section (see below)
    #. Given are points coordinates in Cartesian system
    #. Separate first row (header) from data
    #. Calculate coefficients of best approximating polynomial of 3rd degree

Polish:
    #. Użyj danych z sekcji "Given" (patrz poniżej)
    #. Dane są koordynaty punktów w układzie kartezjańskim
    #. Odseparuj pierwszy wiersz (nagłówek) do danych
    #. Oblicz współczynniki najlepiej dopasowanego wielomianu 3 stopnia

Given:
    .. code-block:: python

        DATA = [
            ('x', 'y'),
            (-4.0, 0.0),
            (-3.0, 2.5),
            (-2.0, 2.0),
            (0.0, -2.0),
            (2.0, 0.0),
            (3.0, 7.0),
        ]
