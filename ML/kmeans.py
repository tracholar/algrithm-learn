# coding:utf-8

from sklearn import cluster, datasets

iris = datasets.load_iris()
X,y = iris.data, iris.target

kmeans = cluster.KMeans(3)
kmeans.fit(X)
