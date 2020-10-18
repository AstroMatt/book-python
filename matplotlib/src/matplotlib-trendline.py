import matplotlib.pylab as pylab
import numpy as np

x = [1, 3, 5, 7, 9]
y = [2, 3, 4, 3, 4]

# plot the data itself
pylab.plot(x, y, label="data")

# calc the trendline (it is simply a linear fitting)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

pylab.plot(x, p(x), color="red", linestyle='--')

# the line equation:
a = z[0]
b = z[1]
print(f"y = {a:.6}x + ({b:.6})")

# parabolic fit will be:
# z = numpy.polyfit(x, y, 2)
