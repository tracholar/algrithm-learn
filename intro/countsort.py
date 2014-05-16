# coding:utf8
# counting sort
# A[i] is integer in [0,k]
import numpy as np
import time

def CountingSort(A,k):
	C = np.zeros(k+1,dtype=np.int32)
	for a in A:
		C[a] += 1
	for i in xrange(1,k+1):
		C[i] += C[i-1]
	
	B = np.zeros(len(A),np.int32)
	for j in xrange(len(A)-1,-1,-1):
		B[ C[ A[j] ]-1 ] = A[j]
		C[ A[j] ] -= 1
		
	return B
		
if __name__ == '__main__':
	k = 100
	x = np.random.randint(k,size=100000)
	t1 = time.time()
	B = CountingSort(x,k)
	t2 = time.time()
	print t2-t1
	#print x
	#print CountingSort(x,k)
			