"""
>>> red
3
>>> green
2
>>> blue
2
"""

DATA = ['red', 'green', 'blue', 'red', 'green', 'red', 'blue']

red = 0
green = 0
blue = 0

for color in DATA:
    if color == 'red':
        red += 1
    elif color == 'green':
        green += 1
    elif color == 'blue':
        blue += 1
