# coding:gbk
import numpy as np

inf = np.inf

def ExtendShortestPaths(L,W):
	n = len(L)
	L0 = np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			L0[i,j] = inf
			for k in range(n):
				L0[i,j] = min(L0[i,j],L[i,k]+W[k,j])
				
	return L0

def SlowAllPairsShortestPath(W):
	n = len(W)
	L = W
	i = 1
	while i<n:
		L = ExtendShortestPaths(L,L)
		i *= 2
		print i
		print L
	return L

if __name__ == '__main__':
	G = np.array(
		[[0, 3, 8, inf, -4],
		[inf, 0, inf, 1, 7],
		[inf, 4, 0, inf, inf],
		[2, inf, -5, 0, inf],
		[inf, inf, inf, 6, 0]])
	G = np.random.randint(1,10,(200,200)) * 1.0
	for i in range(len(G)):
		for j in range(len(G)):
			if i==j:
				G[i,j] = 0
				continue
			if G[i,j]>1:
				G[i,j] = inf
	print G
	
	L = SlowAllPairsShortestPath(G)
	print L[L==inf]