import numpy as np


DATA = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

result = DATA.ravel()
print(result)
# array([1, 2, 3, 4, 5, 6, 7, 8, 9])

result = result.reshape(3, 3)
print(result)
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
