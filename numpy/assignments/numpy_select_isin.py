import numpy as np
np.random.seed(0)


a = np.random.randint(0, 1025, size=(50, 50))
selection = 2 ** np.arange(11)

mask = np.isin(a, selection)
result = a[mask]
result.sort()
result = np.flip(result)

print(result)
# [1024 1024 1024 1024 1024 1024  512  512  512  512  256  256  256  256
#   256  128  128  128  128  128   64   32   32   32   32   32   16   16
#    16   16   16   16    8    8    4    2    2    2    2    2]


## Alternative solution
np.random.seed(0)

MIN = 0
MAX = 1025
SIZE = (50, 50)
SELECT = 2 ** np.arange(11)


a = np.random.randint(MIN, MAX, size=SIZE)
b = a[np.isin(a, SELECT)]
result.sort()
np.flip(result)


## Alternative solution
sorted(a[np.isin(a, SELECT)], reverse=True)
