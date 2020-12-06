import numpy as np
import pandas as pd


DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/xlsx/sensors-optima.xlsx'
WHERE = 'Sleeping Quarters upper'
WHEN = '2019-09-28'


df = pd.read_excel(
    io=DATA,
    parse_dates=['datetime'],
    sheet_name='Luminance',
    header=1,
    index_col=0)

activity = (df
            .loc[df['location'] == WHERE]
            .loc[WHEN, 'value']
            .apply(np.sign)
            .resample('H')
            .sum())

ax = activity.plot(color='red', figsize=(16,5))
_ = ax.set_yticks([0, 1])
_ = ax.set_yticklabels(['sleep', 'awake'])
