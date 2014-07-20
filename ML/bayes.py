# coding:utf-8
import numpy as np

def LoadData():
	posts = ['my dog has flea probems help please','maybe not take him to dog park stupid','my dalmation is so cute I love him','stop posting stupid worthless garbage','mr licks ate my steak how to stop him','quit buying worthless dog food stupid']
	postsList = []
	for s in posts:
		postsList.append(s.split(' '))
	
	classVec = [0,1,0,1,0,1]
	
	return postsList, classVec
	
def CreateVocabList(data):
	vocabSet = set([])
	
	# print data
	for doc in data:
		# print doc
		vocabSet = vocabSet | set(doc)
	
	return list(vocabSet)

def Words2Vec(vocabList, data):
	wordN = len(vocabList)
	dataN = len(data)
	ret = np.zeros((dataN, wordN))
	for i in range(dataN):
		for j in range(wordN):
			word = vocabList[j]
			if word in data[i]:
				ret[i,j] += 1
	return ret 

def TrainNB(X, y):
	docN = len(X)
	wordsN = len(X[0])
	pc = np.zeros(2) + 2
	pwc = np.ones((2, wordsN))
	
	for i in range(docN):
		if y[i] == 1:
			pc[1] += 1
			pwc[1] += X[i]
		else:
			pc[0] += 1
			pwc[0] += X[i]
	
	pwc[0] /= pc[0]
	pwc[1] /= pc[1]
	return pwc, pc / docN
	
def Classify(v, pwc, pc):
	p1 = np.sum(v * np.log10(pwc[1])) + np.log10(pc[1])
	p0 = np.sum(v * np.log10(pwc[0])) + np.log10(pc[0])
	
	if p1 > p0:
		return 1
	else:
		return 0
	
if __name__ == '__main__':
	data, y = LoadData()
	vocab = CreateVocabList(data)
	X = Words2Vec(vocab, data)
	print X
	pwc, pc = TrainNB(X, y)
	print pwc, pc
	v = np.random.randint(0,2,len(X[0]))
	for i in range(len(v)):
		if v[i]==1:
			print vocab[i],
	print 
	print Classify(v, pwc, pc)