# coding:utf-8

from sklearn import datasets, svm, grid_search
import scipy

iris = datasets.load_iris()
X,y = iris.data, iris.target
svr = svm.SVC()
params = {'C':scipy.stats.expon(scale=100),'kernel':['rbf'],'gamma':scipy.stats.expon(scale=.1)}


clf = grid_search.RandomizedSearchCV(svr, params, n_iter=100)

clf.fit(X,y)
print clf.score(X,y)
print clf.best_params_


