# coding:gbk
import numpy as np
import time
import matplotlib.pyplot as plt

def matrixChainOrder(p):
	n = len(p)-1
	m = np.zeros((n,n),dtype="int32")
	s = np.zeros((n,n),dtype="int32")
	for l in range(1,n):
		for i in range(n-l):
			j = i+l
			m[i,j] = np.iinfo(np.int16).max
			for k in range(i,j):
				q = m[i,k]+m[k+1,j]+p[i-1]*p[k]*p[j]
				if q<m[i,j]:
					m[i,j] = q
					s[i,j] = k
	return m,s
def printOptimalParens(s,i,j):
	if i==j:
		print 'A%d' % i ,
	else:
		print '(',
		printOptimalParens(s,i,s[i,j])
		printOptimalParens(s,s[i,j]+1,j)
		print ')',


def printMatrix(A):
	m,n = A.shape
	for i in range(m):
		for j in range(n):
			print A[i,j],'\t',
		print 

if __name__=='__main__':	
	n=5
	t = []
	nr = []
	while True:
		p = np.random.randint(2,20,n)
		t1 = time.time()
		m,s=matrixChainOrder(p)
		t2 = time.time()
		# print 'm='
		# printMatrix(m)
		# print 's='
		# printMatrix(s) 
		# printOptimalParens(s,0,len(s)-1)
		print n,t2-t1
		nr.append(n)
		t.append(t2-t1)
		n += 5
		if t2-t1>1:
			break
	plt.plot(nr,t,'+',nr,np.array(nr)**3*6e-7)
	plt.show()