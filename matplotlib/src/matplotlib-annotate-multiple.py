import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.005)
y = np.exp(-x / 2.) * np.sin(2 * np.pi * x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)


data_x = 5
data_y = 0
display_x, display_y = ax.transData.transform_point((data_x, data_y))

bbox = dict(boxstyle="round", fc="0.8")
arrowprops = dict(
    arrowstyle="->",
    connectionstyle="angle,angleA=0,angleB=90,rad=10")

offset = 72
ax.annotate('data = (%.1f, %.1f)' % (data_x, data_y),
            (data_x, data_y), xytext=(-2 * offset, offset), textcoords='offset points',
            bbox=bbox, arrowprops=arrowprops)

display = ax.annotate('display = (%.1f, %.1f)' % (display_x, display_y),
                      (display_x, display_y), xytext=(0.5 * offset, -offset),
                      xycoords='figure pixels',
                      textcoords='offset points',
                      bbox=bbox, arrowprops=arrowprops)

plt.show()
