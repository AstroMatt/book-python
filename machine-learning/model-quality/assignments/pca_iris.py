import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import datasets


iris = datasets.load_iris()
features = iris.data
labels = iris.target

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
    edgecolor='k')

ax.scatter(
    features[labels == 0, 0],
    features[labels == 0, 1],
    features[labels == 0, 2],
    edgecolor='k')


ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])

plt.show()
