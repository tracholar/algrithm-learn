# coding:utf8

def Parent(i):
	return i/2
	
def Left(i):
	return 2*i
	
def Right(i):
	return 2*i+1
	
def MaxHeapify(A,i):
	l = Left(i)
	r = Right(i)
	if l<len(A) and A[l]>A[i]:
		largest = l 
	else:
		largest = i 
	if r<len(A) and A[r]>A[largest]:
		largest = r 
	if largest != i:
		tmp = A[i]
		A[i] = A[largest]
		A[largest] = tmp
		MaxHeapify(A,largest)

	
x = [0,1,2,3,4,5,6]
for i in range(len(x)-1,0,-1):
	MaxHeapify(x,i)
print x