import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 6, 8]
labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

plt.xticks(x, labels, rotation='vertical')
plt.plot(x, y, marker='o')
plt.show()
