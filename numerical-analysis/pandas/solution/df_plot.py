import numpy as np
import pandas as pd


DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/xlsx/sensors-optima.xlsx'

df = pd.read_excel(
    io=DATA,
    parse_dates=['datetime'],
    sheet_name='Luminance',
    header=1,
    index_col=0)

location = 'Sleeping Quarters upper'
date = '2019-09-28'

activity = (df
            .loc[df['location'] == location]
            .loc[date, 'value']
            .apply(np.sign)
            .resample('H')
            .sum())

ax = activity.plot(color='red', figsize=(16,5))
_ = ax.set_yticks([0, 1])
_ = ax.set_yticklabels(['sleep', 'awake'])
