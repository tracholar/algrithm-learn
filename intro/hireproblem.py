# coding:utf8
import numpy as np

def randomlyPermute(A):
	n = len(A)
	P = np.zeros(n)
	for i in xrange(n):
		P[i] = np.random.rand()
	ind = np.argsort(P)
	return A[ind]
	
x = np.linspace(0,1,100)
print randomlyPermute(x)
	