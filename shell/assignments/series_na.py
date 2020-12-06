import pandas as pd

DATA = [1, None, 5, None, 1, 2, 1]


## Solution 1
s = pd.Series(DATA)
s = s.fillna(0, limit=1)
s = s.dropna()
s = s.reset_index(drop=True)


## Solution 2
s = pd.Series(DATA)
s.fillna(0, limit=1, inplace=True)
s.dropna(inplace=True)
s.reset_index(drop=True, inplace=True)


## Solution 3
s = (pd.Series(DATA)
     .fillna(0, limit=1)
     .dropna()
     .reset_index(drop=True))


## Result
s: pd.Series
# 0    1.0
# 1    0.0
# 2    5.0
# 3    1.0
# 4    2.0
# 5    1.0
# dtype: float64
