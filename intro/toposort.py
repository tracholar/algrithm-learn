# coding:gbk

import numpy as np

inf = np.inf

	
def Hasin(G,v):
	N = len(G)
	hasin = False
	for i in range(N):
		if i==v:
			continue
		if G[i,v] != inf:
			return True
	return False
	
def TopoSort(g):
	G[:,:] = g[:,:]
	L = []
	S = []
	N = len(G)
	for i in range(N):
		if not Hasin(G,i):
			S.append(i)
	
	while len(S)!=0:
		n = S.pop(0)
		L.append(n)
		for i in range(N):
			if n!=i and G[n,i]!=inf:
				G[n,i] = inf
				
				if not Hasin(G,i):
					S.append(i)
					print i,G[:,i]
					
	return L

if __name__ == '__main__':
	G = np.array(
		[[0, inf, inf, inf, inf],
		[2, 0, 3, inf, inf],
		[inf, inf, 0, inf, inf],
		[inf, inf, 5, 0, inf],
		[inf, 2, inf, 1, 0]])
	for i in range(len(G)):
		print i,Hasin(G,i)
	print TopoSort(G)