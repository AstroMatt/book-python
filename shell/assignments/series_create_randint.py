import numpy as np
import pandas as pd
np.random.seed(0)


data = np.random.randint(0, 10, size=10)
s = pd.Series(data)

s
# 0    5
# 1    0
# 2    3
# 3    3
# 4    7
# 5    9
# 6    3
# 7    5
# 8    2
# 9    4
# dtype: int64
