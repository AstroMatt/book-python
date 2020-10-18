import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
e = [0.5, 1., 1.5, 2.]

plt.errorbar(x, y, yerr=e, fmt='o')
plt.show()
