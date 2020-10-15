import numpy as np


a = np.array([[1, 0, 1, 0],
              [0, 1, 1, 0],
              [3, 2, 1, 0],
              [4, 1, 2, 0]])

b = np.array([
    [4, 1],
    [2, 2],
    [5, 1],
    [2, 3]])


a * b
# Traceback (most recent call last):
#     ...
# ValueError: operands could not be broadcast together with shapes (4,4) (4,2)

a @ b
# array([[ 9,  2],
#        [ 7,  3],
#        [21,  8],
#        [28,  8]])

b * a
# Traceback (most recent call last):
#     ...
# ValueError: operands could not be broadcast together with shapes (4,2) (4,4)

b @ a
# Traceback (most recent call last):
#     ...
# ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 4 is different from 2)

