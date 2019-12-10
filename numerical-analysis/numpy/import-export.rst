**********************
Data Import and Export
**********************


np.loadtxt()
============
.. code-block:: python

    import numpy as np


    url = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/numpy/data/iris.csv'

    a = np.loadtxt(url)
    # ValueError: could not convert string to float: 'sepal_length,sepal_width,petal_length,petal_width,species'

    a = np.loadtxt(url, skiprows=1)
    # ValueError: could not convert string to float: '5.4,3.9,1.3,0.4,setosa'

    a = np.loadtxt(url, skiprows=1, delimiter=',')
    # ValueError: could not convert string to float: 'setosa'

    a = np.loadtxt(url, skiprows=1, delimiter=',', usecols=(0,1,2,3))
    # array([[5.4, 3.9, 1.3, 0.4],
    #        [5.9, 3. , 5.1, 1.8],
    #        [6. , 3.4, 4.5, 1.6],
    #        [7.3, 2.9, 6.3, 1.8],
    #        [5.6, 2.5, 3.9, 1.1],
    #        ...,
    # ])

    a = np.loadtxt(url, skiprows=1, max_rows=3, delimiter=',', usecols=(0,1,2,3))
    # array([[5.4, 3.9, 1.3, 0.4],
    #        [5.9, 3. , 5.1, 1.8],
    #        [6. , 3.4, 4.5, 1.6]])

    a = np.loadtxt(url, max_rows=1, delimiter=',', dtype=str, usecols=(0,1,2,3))
    # array(['sepal_length', 'sepal_width', 'petal_length', 'petal_width'], dtype='<U12')


np.savetxt()
============

``int``
-------
.. code-block:: python

    import numpy as np


    a = np.array([[1,2,3],
                  [4,5,6]])

    np.savetxt('/tmp/filename.csv', a, delimiter=',')
    # 1.000000000000000000e+00,2.000000000000000000e+00,3.000000000000000000e+00
    # 4.000000000000000000e+00,5.000000000000000000e+00,6.000000000000000000e+00

    np.savetxt('/tmp/filename.csv', a, delimiter=',', fmt='%d')
    # 1,2,3
    # 4,5,6

``float``
---------
.. code-block:: python

    import numpy as np


    a = np.array([[5.4, 3.9, 1.3, 0.4],
                  [5.9, 3. , 5.1, 1.8],
                  [6. , 3.4, 4.5, 1.6],
                  [7.3, 2.9, 6.3, 1.8],
                  [5.6, 2.5, 3.9, 1.1]])

    np.savetxt('/tmp/filename.csv', a, delimiter=',')
    # 5.400000000000000355e+00,3.899999999999999911e+00,1.300000000000000044e+00,4.000000000000000222e-01
    # 5.900000000000000355e+00,3.000000000000000000e+00,5.099999999999999645e+00,1.800000000000000044e+00
    # 6.000000000000000000e+00,3.399999999999999911e+00,4.500000000000000000e+00,1.600000000000000089e+00
    # 7.299999999999999822e+00,2.899999999999999911e+00,6.299999999999999822e+00,1.800000000000000044e+00
    # 5.599999999999999645e+00,2.500000000000000000e+00,3.899999999999999911e+00,1.100000000000000089e+00

    np.savetxt('/tmp/filename.csv', a, delimiter=',', fmt='%.1f')
    # 5.4,3.9,1.3,0.4
    # 5.9,3.0,5.1,1.8
    # 6.0,3.4,4.5,1.6
    # 7.3,2.9,6.3,1.8
    # 5.6,2.5,3.9,1.1

    np.savetxt('/tmp/filename.csv', a, delimiter=',', fmt='%.2f')
    # 5.40,3.90,1.30,0.40
    # 5.90,3.00,5.10,1.80
    # 6.00,3.40,4.50,1.60
    # 7.30,2.90,6.30,1.80
    # 5.60,2.50,3.90,1.10


Other
=====
* ``np.load()``, ``np.loads()`` - ``pickle``
* ``np.fromstring()``
* ``np.fromregex()``
* ``np.genfromtxt()`` - Load data with missing values handled as specified
* ``scipy.io.loadmat()`` - reads MATLAB data files


Assignments
===========

Load Dirty CSV
--------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/numpy_loadtext.py`

:English:
    #. Load text from URL given as input (see below)
    #. From the first line select Iris species names and save as ``species: ndarray``
    #. For other lines:

        #. Read columns with data and save to ``features: ndarray``
        #. Read last column with species numbers and save to ``labels: ndarray``

    #. Print ``species``, ``labels`` and ``features``

:Polish:
    #. Wczytaj tekst z URL podanego na wejściu (patrz sekcja input)
    #. Z pierwszej linii wybierz nazwy gatunków Irysów i zapisz rezultat jako ``species: ndarray``
    #. W pozostałych linii:

        * Wczytaj kolumny z danymi i zapisz do ``features: ndarray``
        * Wczytaj ostatnią kolumnę z numerami gatunków i zapisz do ``labels: ndarray``

    #. Wyświetl ``species``, ``labels`` i ``features``

:Input:
    .. code-block:: text

        https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/numpy/data/iris-dirty.csv

:Output:
    .. code-block:: python

        species: ndarray
        # array(['setosa', 'versicolor', 'virginica'], dtype='<U10')

        features: ndarray
        # array([[5.4, 3.9, 1.3, 0.4],
        #        [5.9, 3. , 5.1, 1.8],
        #        [6. , 3.4, 4.5, 1.6],
        #        [7.3, 2.9, 6.3, 1.8],
        #        ...
        #        [6.8, 3.2, 5.9, 2.3]])

        labels: ndarray
        # array([0., 2., 1., 2., ..., 0., 2., 2., 2.])

