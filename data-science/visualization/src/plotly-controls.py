import plotly.offline as py
import numpy as np

data = []
steps = []

for step in np.arange(0, 5, 0.1):
    data.append({
        'visible': False,
        'line': {'color': '00CED1', 'width': 6},
        'name': f'𝜈 = {step}',
        'x': np.arange(0, 10, 0.01),
        'y': np.sin(step * np.arange(0, 10, 0.01)),
    })

data[10]['visible'] = True

for i in range(len(data)):
    step = {
        'method': 'restyle',
        'args': ['visible', [False] * len(data)],
    }

    step['args'][1][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [{
    'active': 10,
    'currentvalue': {"prefix": "Frequency: "},
    'pad': {"t": 50},
    'steps': steps
}]

py.iplot({
    'data': data,
    'layout': {'sliders': sliders}},
    filename='Sine Wave Slider')
