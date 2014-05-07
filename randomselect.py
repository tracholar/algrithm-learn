# coding:utf8
import numpy as np
import time

def swap(A,p,q):
	tmp = A[p]
	A[p] = A[q]
	A[q] = tmp
def RandomPartition(A,p,r):
	q = np.random.randint(p,r+1)
	
	swap(A,q,r)
	i = p 
	for j in range(p,r+1):
		if A[j]<=A[r]:
			swap(A,i,j)
			i += 1
	
	
	return i-1
	
def RandomSelect(A,p,r,i):
	if p==r:
		return A[p]
	q = RandomPartition(A,p,r)
	#print q,A
	
	k = q-p
	if i==k:
		return A[q]
	elif i<k:
		return RandomSelect(A,p,q-1,i)
	else:
		return RandomSelect(A,q+1,r,i-k-1)
		
x = np.random.rand(2**20)
#print x
t1=time.time()
print RandomSelect(x,0,len(x)-1,300)
t2=time.time()
print t2-t1
#print x