import numpy as np


DATA = np.array([[44, 47, 64, 67],
                 [67,  9, 83, 21],
                 [36, 87, 70, 88]])

DATA.sort(axis=-1)
# array([[23, 63, 64, 74],
#        [11, 24, 29, 44],
#        [45, 49, 78, 93]])

result = np.flip(DATA, axis=0)
# array([[36, 70, 87, 88],
#        [ 9, 21, 67, 83],
#        [44, 47, 64, 67]])

result
