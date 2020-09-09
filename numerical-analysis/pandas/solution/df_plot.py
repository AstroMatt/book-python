import numpy as np
import pandas as pd
from matplotlib.dates import HourLocator, DateFormatter

df = pd.read_excel(
    io='../data/sensors-optima.xlsx',
    parse_dates=['datetime'],
    sheet_name=['Luminance'],
    header=1,
    index_col=0,
)

df = df['Luminance']
df['value'] = df['value'].apply(np.sign)

where = df['location'] == 'Sleeping Quarters upper'
date = df['date'] == '2019-09-28'

activity = df.loc[where & date, 'value'].resample('H').sum()
ax = activity.plot(kind='line', color='red', label='')

# ax.xaxis.set_major_locator(HourLocator())
# ax.xaxis.set_major_formatter(DateFormatter('%H'))

ax.set_yticks([0, 1])


# Only for PyCharm to display chart
import matplotlib.pyplot as plt

plt.plot([], [], color='red', label='0 - sleep')
plt.plot([], [], color='red', label='1 - awake')
plt.legend()
plt.show()
