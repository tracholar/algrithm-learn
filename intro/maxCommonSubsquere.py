# coding:gbk
# Longest Common Subsequence, LCS
# Dynamic Programming
# author:tracholar
# date:2014-05-13
#
import numpy as np


def LCS_Length(x,y):
	m = len(x)+1
	n = len(y)+1
	c = np.zeros((m,n),dtype='int32')
	b = np.zeros((m,n),dtype='int32')  # 1左上，2←，3↑
	
	for i in range(1,m):
		for j in range(1,n):
			if x[i-1]==y[j-1]:
				c[i,j] = c[i-1,j-1] + 1
				b[i,j] = 1
			elif c[i-1,j]>=c[i,j-1]:
				c[i,j] = c[i-1,j]
				b[i,j] = 3
			else:
				c[i,j] = c[i,j-1]
				b[i,j] = 2
	return c,b
	
def printMatrix(A):
	m,n = A.shape
	for i in range(m):
		for j in range(n):
			print A[i,j],'\t',
		print 


def printLCS(b,x,i,j):
	if i==0 or j==0:
		return
	if b[i,j] == 1:
		printLCS(b,x,i-1,j-1)
		print x[i-1],
	elif b[i,j]==2:
		printLCS(b,x,i,j-1)
	else:
		printLCS(b,x,i-1,j)
		
x = np.random.randint(0,10,20)
y = np.random.randint(0,10,30)

c,b = LCS_Length(x,y)
print 'c ='
printMatrix(c)
print 'b ='
printMatrix(b)
print 'x:',x
print 'y:',y
print 'LCS:' ,
printLCS(b,x,len(x),len(y))
