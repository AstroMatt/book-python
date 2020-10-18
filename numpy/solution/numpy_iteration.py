import numpy as np


DATA = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

for value in DATA.ravel():
    if value % 2 == 0:
        print(value)
# 2
# 4
# 6
# 8


## Alternative solution
for row in DATA:
    for value in row:
        if value % 2 == 0:
            print(value)
# 2
# 4
# 6
# 8

