import random
from matplotlib import pyplot as plt


def random_point(center, std=0.2):
    if not isinstance(std, (tuple, list)):
        std = (std, std)

    x = random.gauss(center[0], std[0])
    y = random.gauss(center[1], std[1])

    return x, y


def distance(A, B):
    """
    Calculate distance between A and B.

    >>> distance((0,0), (1,0))
    1.0

    >>> distance((0,0), (1,1))
    1.4142135623730951
    """
    sum = 0
    for a, b in zip(A, B):
        sum += (b - a) ** 2

    return sum ** 0.5


def plot_list_of_points(list_of_points, color='black'):
    """
    list_of_points: [(x1, y1), (x2, y2), (x3, y3), ...]
    """
    plt.plot([p[0] for p in list_of_points],
             [p[1] for p in list_of_points],
             'o',
             color=color,
             alpha=0.3)


A = [0,3]
B = [2,4]
STANDARD_DEVIATION_A = 0.8
STANDARD_DEVIATION_B = 1.0

p1 = [random_point(A, STANDARD_DEVIATION_A)
          for _ in range(0,500)]

p2 = [random_point(B, STANDARD_DEVIATION_B)
          for _ in range(0,500)]

plot_list_of_points(p1, 'red')
plot_list_of_points(p2, 'blue')
plt.axis('equal')
plt.show()

classified_points_A = []
classified_points_B = []


for p in p1 + p2:
    if distance(A, p) < distance(B, p):
        classified_points_A.append(p)
    else:
        classified_points_B.append(p)


plot_list_of_points(classified_points_A, 'red')
plot_list_of_points(classified_points_B, 'blue')
plt.axis('equal')
plt.show()
