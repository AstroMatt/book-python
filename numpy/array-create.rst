************
Array Create
************


Declare
=======
.. code-block:: python
    :caption: 1-dimensional Array

    import numpy as np


    np.array([1, 2, 3])
    # array([1, 2, 3])

    np.array([1.0, 2.0, 3.0])
    # array([1., 2., 3.])

    np.array([1.1, 2.2, 3.3])
    # array([1.1, 2.2, 3.3])

    np.array([1, 2, 3], float)
    # array([ 1., 2., 3.])

    np.array([1, 2, 3], dtype=float)
    # array([ 1., 2., 3.])

.. code-block:: python
    :caption: 2-dimensional Array

    import numpy as np


    np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

.. code-block:: python
    :caption: 3-dimensional Array

    np.array([[[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]],

              [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]])

    # array([[[1, 2, 3],
    #         [4, 5, 6],
    #         [7, 8, 9]],
    #
    #        [[1, 2, 3],
    #         [4, 5, 6],
    #         [7, 8, 9]]])

.. figure:: img/numpy-create-cake.png
    :scale: 50%
    :align: center

    Multi layer cake as an analog for n-dim array [CAKE]_

Range
=====
.. code-block:: python
    :caption: Array from Python ``range()``

    import numpy as np


    np.array(range(5))
    # array([0, 1, 2, 3, 4])

    np.array(range(5), float)
    # array([ 0., 1., 2., 3., 4.])

    np.array(range(5, 10))
    # array([5, 6, 7, 8, 9])

    np.array(range(5, 10), float)
    # array([5., 6., 7., 8., 9.])

    np.array(range(5, 10, 2))
    # array([5, 7, 9])

    np.array(range(5, 10, 2), float)
    # array([5., 7., 9.])

.. code-block:: python
    :caption: Array from Python comprehension

    import numpy as np


    np.array([x for x in range(5)])
    # array([0, 1, 2, 3, 4])

    np.array([x for x in range(5)], float)
    # array([ 0., 1., 2., 3., 4.])

    np.array([x for x in range(5, 10)])
    # array([5, 6, 7, 8, 9])

    np.array([x for x in range(5, 10)], float)
    # array([5., 6., 7., 8., 9.])

    np.array([x for x in range(5, 10, 2)])
    # array([5, 7, 9])

    np.array([x for x in range(5, 10, 2)], float)
    # array([5., 7., 9.])

.. code-block:: python
    :caption: Array from ``np.arange()``

    import numpy as np


    np.arange(5)
    # array([0, 1, 2, 3, 4])

    np.arange(5, dtype=float)
    # array([0., 1., 2., 3., 4.])

    np.arange(5.0)
    # array([0., 1., 2., 3., 4.])

    np.arange(5, 10)
    # array([5, 6, 7, 8, 9])

    np.arange(5, 10, step=2)
    # array([5, 7, 9])

    np.arange(start=5, stop=10, step=2)
    # array([5, 7, 9])

    np.arange(start=5, stop=10, step=2, dtype=float)
    # array([5., 7., 9.])

    np.arange(0.0, 1.0, 0.1)
    # array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

    np.arange(0.0, 1.0, 0.2)
    # array([0. , 0.2, 0.4, 0.6, 0.8])

    np.arange(0.0, 1.0, 0.3)
    # array([0. , 0.3, 0.6, 0.9])


Linspace
========
* ``np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)``
* Return evenly spaced numbers over a specified interval.

.. code-block:: python

    np.linspace(2.0, 3.0, num=5)
    # array([2.  , 2.25, 2.5 , 2.75, 3.  ])

    np.linspace(2.0, 3.0, num=5, endpoint=False)
    # array([2. ,  2.2,  2.4,  2.6,  2.8])

    np.linspace(2.0, 3.0, num=5, retstep=True)
    # (array([2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)


Zeros
=====
.. code-block:: python

    import numpy as np


    np.zeros((2, 3))
    # array([[0., 0., 0.],
    #       [0., 0., 0.]])

    np.zeros(shape=(2, 3))
    # array([[0., 0., 0.],
    #        [0., 0., 0.]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.zeros_like(a)
    # array([[0, 0, 0],
    #        [0, 0, 0]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]], float)

    np.zeros_like(a)
    # array([[0., 0., 0.],
    #        [0., 0., 0.]])


Ones
====
.. code-block:: python

    import numpy as np


    np.ones((3, 2))
    # array([[1., 1.],
    #        [1., 1.],
    #        [1., 1.]])

    np.ones(shape=(3, 2))
    # array([[1., 1.],
    #        [1., 1.],
    #        [1., 1.]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.ones_like(a)
    # array([[1, 1, 1],
    #        [1, 1, 1]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]], float)

    np.ones_like(a)
    # array([[1., 1., 1.],
    #        [1., 1., 1.]])


Empty
=====
* Garbage from memory
* Will reuse previous if given shape was already created

.. code-block:: python

    import numpy as np


    np.empty((3,4))
    # array([[ 2.31584178e+077,  1.29073692e-231,  2.96439388e-323, 0.00000000e+000],
    #       [-2.32034891e+077,  2.68678047e+154,  2.18018101e-314, 2.18022275e-314],
    #       [ 0.00000000e+000,  2.18023445e-314,  1.38338381e-322, 9.03690495e-309]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.empty((2,3))
    # array([[1., 2., 3.],
    #        [4., 5., 6.]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.empty_like(a)
    # array([[1, 2, 3],
    #        [4, 5, 6]])


Full
====
.. code-block:: python

    import numpy as np


    np.full((2, 2), np.inf)
    # array([[inf, inf],
    #        [inf, inf]])

    np.full((2, 2), 10)
    # array([[10, 10],
    #        [10, 10]])


Identity
========
.. code-block:: python

    import numpy as np


    np.identity(2)
    # array([[1., 0.],
    #        [0., 1.]])

    np.identity(3)
    # array([[1., 0., 0.],
    #        [0., 1., 0.],
    #        [0., 0., 1.]])

    np.identity(4, int)
    # array([[1, 0, 0, 0],
    #        [0, 1, 0, 0],
    #        [0, 0, 1, 0],
    #        [0, 0, 0, 1]])


Stringify
=========
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    str(a)
    # '[[1 2 3]\n [4 5 6]\n [7 8 9]]'

    print(a)
    # [[1 2 3]
    #  [4 5 6]
    #  [7 8 9]]

    repr(a)
    # 'array([[1, 2, 3],\n       [4, 5, 6],\n       [7, 8, 9]])'

    a
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

    print(repr(a))
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])


Assignments
===========

Numpy Create Arange
-------------------
* Assignment: Numpy Create Arange
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min
* Filename: :download:`assignments/numpy_create_arange.py`

English:
    #. Create ``a: np.ndarray`` with even numbers from 0 to 100 (without 100)
    #. Numbers must be ``float`` type

Polish:
    #. Stwórz ``a: np.ndarray`` z liczbami parzystymi od 0 do 100 (bez 100)
    #. Liczby muszą być typu ``float``


References
==========
.. [CAKE] https://i.ytimg.com/vi/iCOhz07Ng6g/maxresdefault.jpg
