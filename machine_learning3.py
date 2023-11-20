import numpy as np
import seaborn as sb
import matplotlib.pyplot as plot
from sklearn.cluster import KMeans
from sklearn.datasets._samples_generator import make_blobs

# x, y_true = make_blobs(n_samples=800, centers=5, cluster_std=0.45, random_state=0)
x, y_true = make_blobs(centers=3, cluster_std=0.5)
# print(x)
# print(y_true)
# print(xy)
plot.scatter(x[:, 0], x[:, 1], s=30)
func = KMeans(n_clusters=3)
func.fit(x)
y_func = func.predict(x)
xyy1 = np.c_[np.array(x), np.array(y_true), np.array(y_func)]
print(xyy1)
plot.scatter(x[:, 0], x[:, 1], c=y_func, s=15)
centers = func.cluster_centers_
plot.scatter(centers[:, 0], centers[:, 1], c='red', s=75, alpha=1)
plot.show()
