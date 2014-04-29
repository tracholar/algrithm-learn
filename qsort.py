# coding:utf8
import numpy as np
import time
def qsort(A,p,r):
	if p<r:
		q = partition(A,p,r)
		qsort(A,p,q-1)
		qsort(A,q+1,r)
		
def partition(A,p,r):
	x = A[r]
	i = p 
	for j in xrange(p,r):
		if A[j] <= x:
			tmp = A[j]
			A[j] = A[i]
			A[i] = tmp
			i += 1
	A[r] = A[i]
	A[i] = x
	return i 
	
n = 1000000
x = np.random.rand(n)
#print x
t1 = time.time()
qsort(x,0,len(x)-1)
t2 = time.time()
print 'n = ',n,'cost time: ', t2-t1
#print x