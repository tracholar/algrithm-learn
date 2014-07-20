# coding: utf-8
import numpy as np
import bayes
import re 
import matplotlib.pyplot as plt

def TextParse(str):
	listOfTokens = re.split(r'\W+', str)
	return [tok.lower() for tok in listOfTokens if len(tok)>1]

def SplitData(data, label, M, k, seed):
	np.random.seed(seed)
	train = []
	trainLabel = []
	test = []
	testLabel = []
	for i in range(len(data)):
		example = data[i]
		if np.random.randint(0,M) != k :
			test.append(example)
			testLabel.append(label[i])
		else:
			train.append(example)
			trainLabel.append(label[i])
			
	return train, trainLabel, test, testLabel
	
def PreprocessVocablist(vocabList):
	deleteWords = ['is','the', 'i', 'am', 'a', 'an', 'for', 'to', 'get', 'in', 'of', 'up', 'down', 'that']
	ret = []
	for word in vocabList:
		if word not in deleteWords:
			ret.append(word)
	
	return ret 
	
	
if __name__ == '__main__':
	docList = []
	classList = []
	docMat = []
	
	# read email
	for i in range(1,26):
		wordList = TextParse(open('email/spam/%d.txt' % i).read())
		docList.append(wordList)
		classList.append(1)
		
		wordList = TextParse(open('email/ham/%d.txt' % i).read())
		docList.append(wordList)
		classList.append(0)
		
	# create vocab list
	vocabList = bayes.CreateVocabList(docList)
	vocabList = PreprocessVocablist(vocabList)
	
	# convert doc to vector
	docMat = bayes.Words2Vec(vocabList, docList)
	
	
	errors = []
	for k in range(3):
		# spplit to test set and train set 
		trainSet, trainLabel, testSet, testLabel = SplitData(docMat, classList, 3, k, 0)
		
		# get train arguments
		pwc, pc = bayes.TrainNB(trainSet, trainLabel)
		
		# test classify error
		errorCount = 0
		for i in range(len(testSet)):
			if bayes.Classify(testSet[i], pwc, pc) != testLabel[i]:
				errorCount += 1
		
		errorRate = errorCount * 1.0 / len(testSet)
		errors.append(errorRate)
		
		print 'error rate is %.3f of %d' % (errorRate, len(testSet))
	
	print 'average error rate is %.3f' % np.mean(errors)
	
	