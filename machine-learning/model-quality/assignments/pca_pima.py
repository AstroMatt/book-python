import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import datasets

features = []
labels = []


with open('../_contrib/pima-diabetes.csv') as file:
    for line in file:
        vector = line.split(',')
        features.append([float(x) for x in vector[:-1]])
        labels.append(int(vector[-1]))


pca = decomposition.PCA(n_components=3)
pca.fit(features)
features = pca.transform(features)

plt.clf()

fig = plt.figure(1, figsize=(4, 3))
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

plt.cla()

# Reorder the labels to have colors matching the cluster results
labels = np.choose(labels, [1, 2, 0]).astype(np.float)

ax.scatter(
    features[labels == 1, 0],
    features[labels == 1, 1],
    features[labels == 1, 2],
)

ax.scatter(
    features[labels == 0, 0],
    features[labels == 0, 1],
    features[labels == 0, 2],
)


ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])

plt.show()
