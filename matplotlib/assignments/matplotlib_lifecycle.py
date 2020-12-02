import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


url = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/iris.csv'
iris = pd.read_csv(url)

means = iris.groupby('species').mean()
data = dict(means['sepal_length'])

group_names = list(data.keys())
group_data = list(data.values())
group_mean = np.mean(group_data)

fig, ax = plt.subplots()
ax.barh(group_names, group_data)

labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.axvline(group_mean, ls='--', color='red')

plt.show()
