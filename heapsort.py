# coding:utf8
import numpy as np
import matplotlib.pyplot as plt
import time

def Parent(i):
	return i/2
	
def Left(i):
	return 2*i
	
def Right(i):
	return 2*i+1
	
def MaxHeapify(A,i=1,L=-1):
	if L == -1:
		L = len(A)
	l = Left(i)
	r = Right(i)
	if l<L and A[l]>A[i]:
		largest = l 
	else:
		largest = i 
	if r<L and A[r]>A[largest]:
		largest = r 
	if largest != i:
		tmp = A[i]
		A[i] = A[largest]
		A[largest] = tmp
		MaxHeapify(A,largest,L)

def BuildMaxHeap(A):
	for i in xrange(len(A)/2,0,-1):
		MaxHeapify(A,i)
		
def Heapsort(A):
	BuildMaxHeap(A)
	heapsize=len(A)
	for i in xrange(len(A)-1,0,-1):
		tmp = A[1]
		A[1] = A[i]
		A[i] = tmp
		heapsize -= 1
		MaxHeapify(A,1,heapsize)

x = np.random.rand(11)
x[0] = 0
Heapsort(x)
print x
i=1
ia = []
t = []
while i<=2**15:
	x = np.random.rand(i)
	t1 = time.time()
	Heapsort(x)
	t2 = time.time()
	ia.append(i)
	t.append(t2-t1)
	i *= 2
print t
plt.plot(ia,t)
plt.show()