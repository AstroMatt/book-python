import numpy as np


DATA = np.array([
    [2, 8, 1, 5],
    [8, 8, 4, 4],
    [5, 5, 2, 5],
    [1, 0, 6, 0],
])

result = DATA[1:3, 1:3]

print(result)
# [[8 4]
#  [5 2]]
