#coding:utf8
import numpy as np
import time

def RadixSort(A,d):
	B = A[:]
	for i in range(d-1,-1,-1):
		C = np.zeros(256,dtype=np.int32)
		AA = B[:]
		for a in AA:
			C[ord(a[i])] += 1
		for j in xrange(1,256):
			C[j] += C[j-1]
		for k in range(len(AA)-1,-1,-1):
			B[ C[ord(AA[k][i])] -1 ] = AA[k]
			C[ord(AA[k][i])] -= 1
		
	return B 
	
x = ["COW", "DOG", "SEA", "RUG", "ROW", "MOB", "BOX", "TAB", "BAR", "EAR", "TAR", "DIG", "BIG", "TEA", "NOW", "FOX"]

print RadixSort(x,3)