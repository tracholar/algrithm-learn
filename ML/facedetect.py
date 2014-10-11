# coding:utf-8

import logging
from time import time
from sklearn.datasets import fetch_lfw_people
from sklearn.cross_validation import train_test_split
from sklearn.decomposition import RandomizedPCA
from sklearn.grid_search import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix



logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

lfw_people = fetch_lfw_people(data_home='D:\\My documents\\code\\dataset\\', resize=0.4)

n_samples, h, w = lfw_people.images.shape

X = lfw_people.data
n_features = X.shape[1]

y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]

print("Total dataset size:")
print("n_samples: %d" % n_samples)
print("n_features: %d" % n_features)
print("n_classes: %d" % n_classes)


# split data into training and testing set 
X_train, X_test, y_train, y_test = train_test_split(
		X, y, test_size = 0.25)
		
n_components = 150
print("Extracting the top %d eigenfaces from %d faces"
      % (n_components, X_train.shape[0]))
t0 = time()	  
pca = RandomizedPCA(n_components = n_components, whiten=True).fit(X_train)
print("done in %0.3fs" % (time() - t0))

eigenfaces = pca.components_.reshape((n_components, h, w))

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)

print 'done transform'


print 'Fiting the classifier to the training set '

params = {'C':[1e3,5e3,1e4,5e4,1e5]}

clf = GridSearchCV( SVC(kernel='linear'), params)
clf.fit(X_train_pca, y_train)

print 'Best estimator found by grid search:'
print clf.best_estimator_


print 'Predicting people names'

y_pred = clf.predict(X_test_pca)
print classification_report(y_test, y_pred)
print confusion_matrix(y_test, y_pred, labels=range(n_classes))
