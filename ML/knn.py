# coding:utf-8

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

def SplitData(X, y, M, k, seed = 0):
	np.random.seed(seed)
	trainX = []
	trainy = []
	testX = []
	testy = []
	for i in range(len(X)):
		if np.random.randint(0,M)==k:
			testX.append(X[i])
			testy.append(y[i])
		else:
			trainX.append(X[i])
			trainy.append(y[i])
	return trainX, trainy, testX, testy
	
def cmp(a,b):
	if a[0] > b[0]:
		return 1
	return  -1
def Classify(x, X, y, k=3):
	dc = []
	for i in range(len(X)):
		d = np.sqrt(sum((x - X[i])**2))
		dc.append([d,y[i]])
	dc.sort(cmp = cmp)
	cc = np.zeros(3)
	i = 0
	for d, c in dc:
		i += 1
		if i > k:
			break
		# print d,c
		cc[c] += 1
	# print min(cc)
	return np.argmax(cc)
	
	
def Norm(X,mean,std):
	X = np.array(X)
	normX = np.zeros(X.shape)
	for i in range(len(X)):
		normX[i,:] = (X[i,:]-mean) / std
	return normX
	
if __name__ == '__main__':
	X, y, labelmap = ReadData('iris.data')
	# print Classify(np.array([7.,3.6,6.1,2.5]), X, y)
	print 'Data length is %d' % len(y)
	
	N = 50
	r = np.zeros(N)
	rnorm = np.zeros(N)
	for K in range(1,N+1):
		correctRate = np.zeros(3)
		correctRateNorm = np.zeros(3)
		for k in range(3):
			trainX, trainy, testX, testy = SplitData(X, y, 3, k)
			meanX = np.array([np.mean(X[:,i]) for i in range(len(X[0]))])
			stdX = np.array([np.std(X[:,i]) for i in range(len(X[0]))])
			
			trainXNorm = Norm(trainX , meanX, stdX)
			testXNorm = Norm(testX,  meanX, stdX)
			
			# print trainXNorm
			# print meanX,stdX
			for i in range(len(testX)):
				predict = Classify(testX[i],trainX,trainy,K)
				# print predict,testy[i]
				if predict==testy[i]:
					correctRate[k] += 1
				
				predict = Classify(testXNorm[i],trainXNorm,trainy,K)
				if predict==testy[i]:
					correctRateNorm[k] += 1
					
			correctRate[k] /= len(testX)
			correctRateNorm[k] /= len(testX)
			# print len(testX)
		# print correctRate
		print 'k = %d, r = %.3f, rnorm = %.3f' % (K, np.mean(correctRate), np.mean(correctRateNorm))
		r[K-1] = np.mean(correctRate)
		rnorm[K-1] = np.mean(correctRateNorm)
	plt.plot(range(1,N+1), r, 'b.-', range(1,N+1), rnorm, 'r.-')
	plt.title('KNN in different K value with iris data set')
	plt.xlabel('K')
	plt.ylabel('correct rate')
	plt.legend(('Direct KNN', 'Normlized KNN'))
	plt.show()
	
	# plt.plot(X[y==0,0],X[y==0,1],'o', X[y==1,0], X[y==1,1], '+' ,X[y==2,0], X[y==2,1], 'x')
	# plt.legend(labelmap)
	# plt.show()