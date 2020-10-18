import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/school_earnings.csv")

data = [go.Bar(x=df.School, y=df.Gap)]
py.iplot(data, filename='jupyter-basic_bar')
