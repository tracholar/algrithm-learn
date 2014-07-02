# coding:gbk
import numpy as np

def MSTPrim(G,r):
	N = len(G)
	key = np.zeros(N,dtype=int)+np.inf
	pi = np.zeros(N,dtype=int)-1
	
	key[r] = 0
	Q = range(N)
	while len(Q)!=0:
		t = key[Q[0]]
		minI = 0
		for i in range(len(Q)):
			if key[Q[i]] < t:
				minI = i
		u = Q.pop(minI)
		
		for v in range(N):
			if (v!=u) and (v in Q) and G[u][v]<key[v]:
				pi[v] = u 
				key[v] = G[u][v]
				
	return N,pi
	
G = np.random.randint(0,100,(40,40))*1.0
G += G.T 
for i in range(len(G)):
	for j in range(len(G[0])):
		if G[i][j]>100:
			G[i][j] = np.inf
			
N,pi = MSTPrim(G,0)
for i in range(1,N):
	print '(%d, %d) %d' % (i,pi[i],G[i][pi[i]])
