import numpy as np
height = np.random.randint(low=140, high=201,size=100)
weight = np.random.randint(low=40, high=101,size=100)

print(height)
print([weight[i] for i in range(0, 5)])

x = height.reshape(height.shape[0],1)
y = weight.reshape(weight.shape[0],1)
print(x.shape)
print([x[i][0] for i in range(0, 5)])
print([y[i][0] for i in range(0, 5)])

data = np.hstack((x, y))

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 10))
plt.subplot(221)
plt.scatter(data[:,0], data[:,1])
plt.title("Data Distribution")
plt.xlabel("height")
plt.ylabel("weight")


from sklearn.cluster import KMeans as KM
y_pred=KM(n_clusters=4).fit_predict(data)
plt.subplot(222)
plt.scatter(data[:,0], data[:,1], c=y_pred)
plt.title("K-means Result")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()
