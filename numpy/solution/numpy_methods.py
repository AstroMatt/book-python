import numpy as np

DATA = np.array([[44, 47, 64, 67],
                 [67,  9, 83, 21],
                 [36, 87, 70, 88]])

DATA[:, -1].fill(0)
result = DATA.transpose()
result = result.astype(float)
result[0].fill(np.nan)

print(result)
# array([[nan, nan, nan],
#        [47.,  9., 87.],
#        [64., 83., 70.],
#        [ 0.,  0.,  0.]])
