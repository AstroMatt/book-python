import numpy as np


data = np.array([[-1.1, 0.0, 1.1],
                 [2.2, 3.3, 4.4]])

data = data.astype(int)
# array([[-1,  0,  1],
#        [ 2,  3,  4]])

data.astype(bool)
# array([[ True, False,  True],
#        [ True,  True,  True]])
