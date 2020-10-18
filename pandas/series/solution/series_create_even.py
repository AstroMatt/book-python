import pandas as pd
import numpy as np
np.random.seed(0)


## Solution 1
s = pd.Series(np.arange(0, 20, 2))

## Solution 2
s = pd.Series(range(0, 20, 2))

## Solution 3
s = pd.Series([x for x in range(0, 20) if x % 2 == 0])


## Result
s: pd.Series
# 0    2
# 1    4
# 2    6
# 3    8
# 4    10
# 5    12
# 6    14
# 7    16
# 8    18
# 9    20
# dtype: int64
