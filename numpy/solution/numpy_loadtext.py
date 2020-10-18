import numpy as np


URL = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/iris-dirty.csv'

species = np.loadtxt(URL, max_rows=1, delimiter=',', dtype=str, usecols=(2,3,4))
# array(['setosa', 'versicolor', 'virginica'], dtype='<U10')

features = np.loadtxt(URL, skiprows=1, delimiter=',', usecols=(0,1,2,3))
# array([[5.4, 3.9, 1.3, 0.4],
#        [5.9, 3. , 5.1, 1.8],
#        [6. , 3.4, 4.5, 1.6],
#        [7.3, 2.9, 6.3, 1.8],
#        ...
#        [6.8, 3.2, 5.9, 2.3]])


labels = np.loadtxt(URL, skiprows=1, delimiter=',', usecols=(4))
# array([0, 2, 1, 2, 1, 0, 1, 1, 0, 2, 2, 0, 0, 2, 2, 1, 2, 2, 2, 1, 0, 1,
#        1, 0, 0, 0, 2, 2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2, 1, 1, 1, 2, 2,
#        0, 1, 1, 1, 1, 1, 2, 0, 2, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 2, 0, 0,
#        0, 0, 0, 0, 1, 0, 2, 0, 0, 1, 1, 2, 2, 1, 0, 2, 1, 0, 1, 0, 2, 1,
#        0, 2, 0, 2, 1, 0, 2, 1, 1, 0, 0, 1, 2, 2, 2, 1, 0, 1, 1, 1, 2, 2,
#        0, 2, 2, 0, 2, 1, 2, 0, 0, 1, 0, 2, 0, 2, 1, 2, 2, 2, 1, 0, 2, 1,
#        0, 0, 2, 0, 2, 1, 1, 1, 0, 1, 1, 2, 0, 1, 1, 0, 2, 2, 2])
