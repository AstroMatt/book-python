import pandas as pd
import numpy as np
np.random.seed(0)


cars = pd.DataFrame({
    'mileage': np.random.randint(0, 200_000, size=50),
    'consumption': np.random.randint(0, 21, size=50),
})

cars['type'] = pd.cut(cars['consumption'],
                      bins=[0, 1, 10, np.inf],
                      labels=['electric', 'car', 'tir'],
                      include_lowest=True)


cars['status'] = None

q = cars['mileage'] > 100_000
cars.loc[q, 'status'] = 'old'

q1 = cars['mileage'] >= 10_000
q2 = cars['mileage'] <= 100_000
cars.loc[q1 & q2, 'status'] = 'young'

q = cars['status'].isin(range(0, 10_000))
cars.loc[q, 'status'] = 'new'


cars
cars.describe()
_ = cars.hist(rwidth=0.8, figsize=(17, 5))
cars.groupby(['type', 'status']).describe()
cars.groupby(['type', 'status']).describe().transpose()
