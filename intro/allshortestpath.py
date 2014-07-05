# coding:gbk

from shortestpath import *

def PrintAllPath(PI,D,i,j):
	if i==j:
		print '%d\t0' % i 
		
	elif PI[i,j] == NIL:
		print 'no path from %d to %d' % (i,j)
		return
	else:
		PrintAllPath(PI,D,i,PI[i,j])
		print '%d\t%.f' % (j,D[i,j])
	
	
	
	
if __name__ == '__main__':
	G = np.array(
		[[0, inf, inf, inf, inf],
		[2, 0, 3, inf, inf],
		[inf, inf, 0, inf, inf],
		[inf, inf, 5, 0, inf],
		[inf, 2, inf, 1, 0]])
	print G
	N = len(G)
	
	D = np.zeros((N,N)) 
	PI = np.zeros((N,N),dtype=int) 
	B = []
	
	for i in range(N):
		b,pi,d = Dijkstra(G,i)
		B.append(b)
		PI[i,:] = pi
		D[i,:] = d

	print PI
	print D
	
	for i in range(N):
		for j in range(N):
			print '================='
			print 'we can reachie node %d from %d, tree path as follow:' % (j,i)
			print '================='
			
			PrintAllPath(PI,D,i,j)