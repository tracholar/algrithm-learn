# coding:utf-8

from sklearn import datasets, svm, grid_search, cross_validation, linear_model
import scipy
import numpy as np

iris = datasets.load_iris()
X,y = iris.data, iris.target
svr = svm.SVC()
params = {'C':scipy.stats.expon(scale=100),'kernel':['rbf'],'gamma':scipy.stats.expon(scale=.1)}


clf = grid_search.RandomizedSearchCV(svr, params, n_iter=100, n_jobs=-1)

clf.fit(X,y)
print clf.score(X,y)
print clf.best_params_



kfold = cross_validation.KFold(len(X), n_folds=3, shuffle=True)
# print [(train,test) for train,test in kfold]
# print y[test]
print [clf.fit(X[train], y[train]).score(X[test],y[test]) for train,test in kfold]


digits = datasets.load_digits()
X = digits.data
y = digits.target

svc = svm.SVC(kernel='linear')
C_s = np.logspace(-10, 0, 10)

kfold = cross_validation.KFold(len(X), n_folds=3, shuffle=True)
for C in C_s:
	svc.C = C
	scores = [svc.fit(X[train], y[train]).score(X[test],y[test]) for train,test in kfold]
	print 'C=%g, score=%f' % (C, np.mean(scores))
	

	
diabetes = datasets.load_diabetes()
X = diabetes.data[:150]
y = diabetes.target[:150]

lasso = linear_model.Lasso()
alphas = np.logspace(-4, -.5, 30)

for alpha in alphas:
	lasso.alpha = alpha

	lasso.fit(X,y)
	print lasso.score(diabetes.data[150:], diabetes.target[150:])
