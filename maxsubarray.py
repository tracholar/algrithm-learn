#coding:utf8
import numpy as np
import matplotlib.pyplot as plt
import math 
import time

def findMaxCrossingSubarray(A,low,mid,high):
	leftsum = - np.inf
	sum = 0
	maxleft = mid
	maxright = mid
	for i in range(mid-1,low-1,-1):
		sum += A[i]
		if sum > leftsum:
			leftsum = sum
			maxleft = i
	
	rightsum = -np.inf
	sum = 0
	for j in range(mid,high+1):
		sum += A[j]
		if sum > rightsum:
			rightsum = sum
			maxright = j
			
	return (maxleft,maxright,leftsum+rightsum)

def findMaxSubarray(A,low,high):
	if low == high:
		return (low,high,A[low])
	else:
		mid = int((low+high)/2)
		leftlow,lefthigh,leftsum = findMaxSubarray(A,low,mid)
		rightlow,righthigh,rightsum = findMaxSubarray(A,mid+1,high)
		crosslow,crosshigh,crosssum = findMaxCrossingSubarray(A,low,mid,high)
		
		if leftsum>rightsum and leftsum>crosssum:
			return (leftlow,lefthigh,leftsum)
		elif rightsum>leftsum and rightsum>crosssum:
			return (rightlow,righthigh,rightsum)
		else:
			return (crosslow,crosshigh,crosssum)


def findMaxSubarray1(A):
	n = A.size
	maxsum = A[0]
	maxi=0
	maxj=0
	for i in range(n):
		sum = 0
		for j in range(i,n):
			sum += A[j]
			if sum > maxsum:
				maxi = i
				maxj = j
				maxsum = sum
	return (maxi,maxj,maxsum)

def findMaxSubarrayFastest(A):
	#动态规划
	# M(t) = max{0, M(t-1) + A[t]}
	M = 0
	maxM = 0
	maxi = 0
	maxj = 0
	tmpi = 0
	for i in range(A.size):
		if A[i] < 0:
			maxM = M
			maxi = tmpi
			tmpi = i
			maxj = i-1
			M = 0
		else:
			M += A[i]
	if maxM < M :
		maxM = M
		maxi = tmpi
		maxj = A.size - 1
		
	return (maxi,maxj,maxM)
	
N = 100
time1 = np.zeros(N)
time2 = np.zeros(N)
time3 = np.zeros(N)
iArray = np.arange(0,N)
nArray = 2**iArray
maxN = 0

for i in iArray:
	n = 2**iArray[i]
	x = np.random.rand(n)-0.5
	#x = np.array([-1,-2,1,2,3,4,5,-4,-3])
	t1 = time.time()
	result = findMaxSubarray(x,0,x.size-1)
	t2 = time.time()
	time1[i] = t2-t1
	
	
	t1 = time.time()
	result = findMaxSubarrayFastest(x)
	t2 = time.time()
	time3[i] = t2-t1
	
	
	t1 = time.time()
	result = findMaxSubarray1(x)
	t2 = time.time()
	time2[i] = t2-t1
	
	maxN = i
	
	#print 'cost time ', t2-t1 , 's'
	#print 'x=',x
	#print 'result ',result
	print n , t2-t1 , time.strftime('%H:%M:%S')
	
	if t2-t1>1:
		break

		
maxN += 1
plt.plot(nArray[:maxN],time2[:maxN],'r.-',
		nArray[:maxN],time1[:maxN],'b.-',
		nArray[:maxN],time3[:maxN],'g.-')
plt.xlabel('n')
plt.ylabel('time(s)')
plt.title('find maxmium subarray')
plt.legend(['direct search','divide and conquer','dynamic programming'])
plt.axis([0,nArray[maxN-1]*1.2,0,time1[maxN-1]*1.2])
plt.show()
