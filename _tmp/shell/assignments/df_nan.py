import pandas as pd
import numpy as np


DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/iris-dirty.csv'

COLUMNS = [
    'Sepal length',
    'Sepal width',
    'Petal length',
    'Petal width',
    'Species']


iris = pd.read_csv('../_data/iris-dirty.csv')
species = dict(enumerate(iris.columns[2:]))
iris.columns = COLUMNS
iris['Species'].replace(species, inplace=True)
iris.loc[iris['Petal length'] < 4.0, 'Petal length'] = np.nan
iris = iris.interpolate('linear')
iris.dropna(inplace=True)
print('Size:', len(iris))
iris.head(2)
