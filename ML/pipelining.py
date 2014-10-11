# coding:utf-8

from sklearn import linear_model, decomposition, datasets
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
import matplotlib.pyplot as plt
import numpy as np

logistic = linear_model.LogisticRegression()

pca = decomposition.PCA()
pipe = Pipeline(steps = [('pca', pca), ('logistic', logistic)])

digits = datasets.load_digits()
X = digits.data
y = digits.target

pca.fit(X)
plt.figure(1, figsize=(4,3))
plt.clf()
plt.axes([.2,.2,.7,.7])
plt.plot(pca.explained_variance_, linewidth=2)
plt.axis('tight')
plt.xlabel('n_components')
plt.ylabel('explained_variance_')


n_components = [20, 40, 64]
Cs = np.logspace(-4, 4, 3)


est = GridSearchCV(pipe, {'pca__n_components':n_components, 'logistic__C':Cs})

est.fit(X,y)
plt.axvline(est.best_estimator_.named_steps['pca'].n_components,
            linestyle=':', label='n_components chosen')
plt.legend(prop=dict(size=12))
