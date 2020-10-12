import matplotlib.pyplot as plt
import pandas as pd


url = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/iris.csv'
iris = pd.read_csv(url)

ratio = iris["sepal_length"] / iris["sepal_width"]

for name, group in iris.groupby("species"):
    plt.scatter(group.index, ratio[group.index], label=name)

plt.legend()
plt.show()
