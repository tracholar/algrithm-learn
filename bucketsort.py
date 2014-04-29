# coding:utf8
# BucketSort
import numpy as np

def BucketSort(A):
	n = len(A)
	B = [[]]*n 
	for i in range(n):
		a = A[i]
		B[int(n*a)].append(a)
	
	Z = np.zeros(n)
	k = 0
	for i in range(n):
		B[i].sort()
		for j in B[i]:
			Z[k] = j
			k += 1
	return Z
	
x = np.random.rand(20)
print BucketSort(x)