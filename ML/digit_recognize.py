# coding:utf-8

from sklearn import datasets, svm, grid_search
from sklearn.metrics import classification_report, f1_score


digits = datasets.load_digits()
n_samples = len(digits.images)
X,y = digits.images.reshape((n_samples,-1)), digits.target
svr = svm.SVC()
params = [
	{'C':[1,3,10,30,100,300,1000],'kernel':['rbf','linear']},
	{'C':[1,3,10,30,100,300,1000],'kernel':['rbf'],'gamma':[0.0001,0.0003,0.001,0.003,0.01,0.03]}
]

clf = grid_search.GridSearchCV(svr, params, score_func = f1_score)

clf.fit(X,y)
print clf.score(X,y)
print clf.best_params_

y_pred = clf.predict(X)
print classification_report(y, y_pred)
