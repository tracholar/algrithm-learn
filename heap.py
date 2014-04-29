# coding:utf8

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

def PrintHeap(A,i=1):
	if i>= len(A):
		return
	for t in range(int(math.log(i,2))):
		print '  ',
	print A[i]
	PrintHeap(A,Right(i))
	PrintHeap(A,Left(i))
	
x = [0,27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
PrintHeap(x)
for i in range(len(x)-1,0,-1):
	MaxHeapify(x,i)
PrintHeap(x)