# coding:gbk

import numpy as np
import matplotlib.pyplot as plt
from operator import *

def ReadData(fname):
	feature = []
	label = []
	labelMap = {'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2}
	for line in open(fname):
		dataL = line.strip().split(',')
		if len(dataL)!=5:
			continue
		feature.append([float(x) for x in dataL[0:4]])
		label.append(labelMap[dataL[4]])
	return np.array(feature), np.array(label), labelMap

def cmpFun(a,b):
	print a,b
	return a[1] - b[1]
	
def Classify(x, X, y, k=3):
	dc = []
	for i in range(len(X)):
		d = np.sqrt(sum((x - X[i])**2))
		dc.append([d,y[i]])
	dc.sort(key=itemgetter(0))
	
	cc = np.zeros(k)
	for d, c in dc:
		cc[c] += 1
	return np.argmin(cc)
	
	
if __name__ == '__main__':
	X, y, labelmap = ReadData('iris.data')
	print Classify(np.array([7.,3.6,6.1,2.5]), X, y)
	
	plt.plot(X[y==0,0],X[y==0,1],'o', X[y==1,0], X[y==1,1], '+' ,X[y==2,0], X[y==2,1], 'x')
	plt.legend(labelmap)
	plt.show()