from matplotlib import markers
import matplotlib.pyplot as plt
from scipy.sparse.construct import random
from sklearn import cluster
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

#create instances
#x: attribute values
#y: group label

x,y = make_blobs(
    n_samples=150, n_features=2,
    centers=3, cluster_std=0.5,
    shuffle=True,random_state=0
)

print(x)
print(x[:,0])
print(x[:,1])

plt.scatter(
    x[:,0], x[:,1],
    c = "white", marker = "o",
    edgecolors = 'black', s = 50
)

plt.xlabel("First Attribute x1")
plt.ylabel("Second Attribute x2")
# plt.show()

km = KMeans(
    n_clusters = 3, 
    init = 'random',
    n_init = 10, 
    max_iter = 300,
    tol = 1e-04, 
    random_state = 0
)
y_km = km.fit_predict(x)
print(y_km)

#draw the3 clusters
plt.scatter(x[y_km == 0, 0], x[y_km == 0, 1], s=50, c="lightgreen", marker='s', edgecolors='gray', label='cluster 1')
plt.scatter(x[y_km == 1, 0], x[y_km == 1, 1], s=50, c="orange", marker='s', edgecolors='gray', label='cluster 2')
plt.scatter(x[y_km == 2, 0], x[y_km == 2, 1], s=50, c="lightblue", marker='s', edgecolors='gray', label='cluster 3')

#draw the centroids
plt.scatter(
    km.cluster_centers_[:,0], km.cluster_centers_[:,1], s=250, marker='*', c='red', edgecolors='gray', label='centroids'
)

plt.legend(scatterpoints=1)
plt.grid()
plt.show()

distortions = []
for i in range(1, 15):
    km = KMeans(n_clusters=i, init='random', n_init=10, max_iter=300, tol=1e-04, random_state=0)
    km.fit(x)
    distortions.append(km.inertia_)

#Draw figures
plt.plot(range(1, 15), distortions, marker="o")
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.show()