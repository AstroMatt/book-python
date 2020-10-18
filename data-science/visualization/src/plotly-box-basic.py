import plotly.offline as py
import plotly.graph_objs as go
import numpy as np

y0 = np.random.randn(50) - 1
y1 = np.random.randn(50) + 1

py.iplot([
    go.Box(y=y0),
    go.Box(y=y1),
])
