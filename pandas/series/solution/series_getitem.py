import pandas as pd
import numpy as np
np.random.seed(0)


s = pd.Series(
    data = np.random.randn(100),
    index = pd.date_range('2000-01-01', freq='D', periods=100))


s['2000-02-29']
# -0.3627411659871381

s[0]
# 1.764052345967664

s[-1]
# 0.40198936344470165

s[s.size // 2]
# -0.8954665611936756
