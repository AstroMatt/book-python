import numpy as np

DATA = [
    ('x', 'y'),
    (-4.0, 0.0),
    (-3.0, 2.5),
    (-2.0, 2.0),
    (0.0, -2.0),
    (2.0, 0.0),
    (3.0, 7.0)
]

data = np.array(DATA[1:])
x = data[:, 0]
y = data[:, 1]

np.polyfit(x, y, deg=3)


## Alternative solution
header, *data = DATA

x = [x for x,y in data]
y = [y for x,y in data]
result = np.polyfit(x, y, deg=3)

print(result)
# [ 0.25  0.75 -1.5  -2.  ]
