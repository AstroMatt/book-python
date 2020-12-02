import numpy as np


a = np.array([[0, 1], [2, 3]], float)
b = np.array([2, 3], float)
c = np.array([[1, 1], [4, 0]], float)

a = np.sqrt(a)
b = np.sqrt(b)
c = c ** 2

result = (a + b) * c
print(result)
# [[ 1.41421356  2.73205081]
#  [45.254834    0.        ]]
