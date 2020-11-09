****
TODO
****

Book TODO
=========
* Machine Learning rewrite
* Newsletter, once a month, what changed in the book


Numerical Analysis
==================
* Introduction to Python
* Dask
* Numba
* Scipy

Numpy
-----
* Poprawić przykłady z argmin i argmax oraz ``unravel_index()``
* Zrobić rozpiskę, które funkcje zwracają ``np.array`` a które robią ``inplace``
* Poprawić mnożenie macierzowe w np-arithmetic
* Poprawić array-concatenate

Pandas
------
* Zrobić rozpiskę, które funkcje zwracają ``np.array`` a które robią inplace
* poprawić przykłady z ``pd.DataFrame.fill()``, ``bfill`` oraz ``ffill``
* df.read_csv('filename.csv', chunksize=5) # five rows at a time, przydatne gdy czytasz plik np. 20GB
* for df in df.read_csv('filename.csv', chunksize=5): print(df)
* df[~...] # ~ - zaprzeczenie warunku
* df.loc[df['col'].str.contains('a|b', regex=True, flags=re.I)]
* ROC Curve - stosunek True Positive do False Positive
* pd.to_datetime(df['Timestamp Column'], unit='s')
* df.set_index('date column')
* df.resample('d') # d - day; m - minute; to taki groupby dla indeksów dat
* df.assign(column_name = lambda x: ...)
* df.agg({}) # first, mean, last, sum, min, max
* df['column'].shift(-1) # previous column
* df.dtypes
* pd.explode()
* series.map()
* series.apply(lambda)
* df[column].drop(axis=1) - drop column
* series.groupby()
* series.plot(kind)
* series.describe() - inaczej się zachowuje dla indeksów numerycznych a inaczej dla timeseries; describe ignores NaN values
* series.describe(percentiles)
* grouping by multiple series
* series.isnull()
* series.isnull().any()
* series.dropna()
* series.groupby([]) and Series.unstack()
* new_series = series / series
* series.describe()
* czym jest axis=0 (wiersze) vs axis=1 (columns)
* pd.to_datetime()
* df.index = pd.to_datetime(df['timestamp'])
* ax = df.plot()
* ax.axhline(df['temperature'].median(), color='r', linestyle=“-“)
* df.index.viewDf.groupby(df.index.date).count()
* df.groupby(df.index.week).count()
* series.isin()
* df[(df.index.hour > 12) & (df.index.hour <= 12)][„temperature”].plot()
* data report by day "D" or "5T" - 5 minute intervals;
* df.resample("D").max().head()dr[„temperature”].resample(“D”).agg([“min”, “max”]).plot()

Python PEP
==========
* str.isfloat()
* str.isint()
* datetime time.now()
* type_check decorator, sprawdzający ``function.__annotations__``
* dict(keys=[...], values=[...])
* time().now()
* from pprint import pprint, print(pretty=True) (albo podawanie formatter)
* JSON datetime encoder, decoder to isoformat (UTC)
* from datetime import parse(str, format)
* from datetime import format(str, format)
* Simple interface for HTTP requests (similar to requests)
* CTypes argtypes, restype from TypeAnnotation
* Context manager ``with logging.DEBUG:``
