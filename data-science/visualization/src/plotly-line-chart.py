import plotly.offline as py
import plotly.graph_objs as go
import math
import numpy as np

x = [1, 2, 3, 4]
y = [4, 3, 2, 1]

py.iplot({
    "data": [go.Scatter(x=x, y=y)],
    "layout": go.Layout(title="hello world")
})

x = [x for x in np.arange(0, 10, 0.1)]
y = [math.sin(y) for y in np.arange(0, 5, 0.1)]

py.iplot({
    "data": [go.Scatter(x=x, y=y)],
    "layout": go.Layout(title="Sin(x)")
})
