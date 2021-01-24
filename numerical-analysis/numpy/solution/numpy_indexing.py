import numpy as np


INPUT = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

OUTPUT = np.zeros(shape=(2,2), dtype=float)

OUTPUT[0,0] = INPUT[0,2]
OUTPUT[0,1] = INPUT[2,2]
OUTPUT[1,0] = INPUT[0,0]
OUTPUT[1,1] = INPUT[1,0]

print(OUTPUT)
