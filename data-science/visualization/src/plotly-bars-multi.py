import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/school_earnings.csv")

trace_women = go.Bar(x=df.School,
                     y=df.Women,
                     name='Women',
                     marker=dict(color='#ffcdd2'))

trace_men = go.Bar(x=df.School,
                   y=df.Men,
                   name='Men',
                   marker=dict(color='#A2D5F2'))

trace_gap = go.Bar(x=df.School,
                   y=df.Gap,
                   name='Gap',
                   marker=dict(color='#59606D'))

data = [trace_women, trace_men, trace_gap]

layout = go.Layout(title="Average Earnings for Graduates",
                   xaxis=dict(title='School'),
                   yaxis=dict(title='Salary (in thousands)'))

fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename='jupyter-styled_bar')
