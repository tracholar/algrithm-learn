# coding:utf-8

import numpy as np
from operator import *
import pickle

def ReadData(fname='lenses.data'):
	data = []
	for line in open(fname):
		A = line.strip().split('  ')
		if len(A)<2:
			continue
		A[-1] = int(A[-1]) - 1
		data.append(A[1:])
	return data
	
def Entropy(dataSet):
	n = len(dataSet)
	labelCounts = dict()
	
	for data in dataSet:
		label = data[-1]
		if label not in labelCounts:
			labelCounts[label] = 0
		labelCounts[label] += 1
		
	S = 0.0
	for key, p in labelCounts.items():
		p = p * 1.0 / n 
		S -= p * np.log2(p)
	return S
def SplitDataSet(data, i, v):
	ret = []
	for d in data:
		if d[i] == v:
			t = list(d)
			t.pop(i)
			ret.append(t)
	return ret 
	
def ChooseBestFeature(dataSet):
	n = len(dataSet[0]) - 1
	baseS = Entropy(dataSet)
	bestInfoGain = 0.
	bestFeature = -1
	for i in range(n):
		featureList = [ex[i] for ex in dataSet]
		uniqueVals = set(featureList)
		newS = 0.
		for v in uniqueVals:
			subDataSet = SplitDataSet(dataSet, i, v)
			p = len(subDataSet) * 1.0 / len(dataSet)
			newS += p * Entropy(subDataSet)
		infoGain = baseS - newS
		if infoGain > bestInfoGain:
			bestInfoGain = infoGain
			bestFeature = i 
	return bestFeature

def Majority(classList):
	classCount = {}
	for v in classList:
		if v not in classCount:
			classCount[v] = 0
		classCount[v] += 1
		
	maxClass = v
	maxCount = classCount[v]
	for v,c in classCount.items():
		if c > maxCount:
			maxClass = v 
			maxCount = c 
			
	return maxClass

def CreateTree(dataSet, labels):
	classList = [data[-1] for data in dataSet]
	if classList.count(classList[0]) == len(classList):
		return classList[0]
	if len(dataSet[0]) == 1:
		return Majority(classList)
	
	bestFeat = ChooseBestFeature(dataSet)
	bestFeatLabel = labels[bestFeat]
	Tree = {bestFeatLabel:{}}
	featV = [data[bestFeat] for data in dataSet]
	labels = list(labels)
	labels.pop(bestFeat)
	for v in set(featV):
		Tree[bestFeatLabel][v] = CreateTree(SplitDataSet(dataSet, bestFeat, v), labels)
	
	return Tree
	
def StoreTree(T, fname):
	f = open(fname, 'w')
	pickle.dump(T, f)
	f.close()
	
def GrabTree(fname):
	f = open(fname)
	T = pickle.load(f)
	f.close()
	return T 
	
def Classify(Tree, featLabels, testVec):
	featStr = Tree.keys()[0]
	print featStr,featLabels
	featIndex = featLabels.index(featStr)
	for v in Tree[featStr]:
		if testVec[featIndex] == v:
			if type(Tree[featStr][v]).__name__ == 'dict':
				return Classify(Tree[featStr][v], featLabels, testVec)
			else:
				return Tree[featStr][v]
	return None
	
if __name__ == '__main__':
	'''
	dataset = [[1,1,'yes'],
				[1,1,'yes'],
				[1,0,'no'],
				[0, 1, 'no'],
               [0, 1, 'no']	]
	'''
	dataset = ReadData()
	# print dataset
	
	# print 'S:' , Entropy(dataset)
	# print 'best feature:', ChooseBestFeature(dataset)
	labels = ['age','prescript','astigmatic', 'tearRate']
	T = CreateTree(dataset,labels)
	StoreTree(T,'T.tree')
	c = Classify(T,labels, ['2' , '1' , '2' , '2'])
	print T 
	print c