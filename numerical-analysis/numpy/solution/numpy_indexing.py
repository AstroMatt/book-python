import numpy as np


DATA = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

np.array([
    DATA[0][2],
    DATA[2][2],
    DATA[0][0],
    DATA[1][2],
], float).reshape(2, 2)
# array([[3., 9.],
#        [1., 6.]])


np.array([
    [DATA[0,2], DATA[2,2]],
    [DATA[0,0], DATA[1,0]],
], float)
# array([[3., 9.],
#        [1., 6.]])


output = np.zeros(shape=(2,2), dtype=float)
output[0,0] = DATA[0,2]
output[0,1] = DATA[2,2]
output[1,0] = DATA[0,0]
output[1,1] = DATA[1,0]
print(output)
# array([[3., 9.],
#        [1., 6.]])
