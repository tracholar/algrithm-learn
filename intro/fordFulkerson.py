# coding:gbk
# Ford-Fulkerson method for solving the
# maximum-flow problem.
# three import ideas:
# 	*residual networks
# 	*augmenting paths
# 	*cuts

import numpy as np


def CaculateGf(G, f, Gf):
	n = len(G)
	for i in range(n):
		for j in range(n):
			if G[i][j]!=0:
				Gf[i][j] = G[i][j] - f[i][j]
			elif G[j][i]!=0:
				Gf[i][j] = f[j][i]
			else:
				Gf[i][j] = 0
# DFS	
def FindPath(G, s, t, path, L = None):
	if L is None:
		L = [s]
	if s==t:
		path.insert(0,s)
		return True
	n = len(G)
	# print 's,t' ,s,t
	for i in range(n):
		if i!=s and G[s][i]!=0 and i not in L:
			L.append(i)
			
			if FindPath(G,i,t, path, L):
				path.insert(0,s)
				return True
			
	
	return False
	
def PathCf(G, path):
	n = len(path)
	r = G[path[0]][path[1]];
	for i in range(1,n-1):
		if r>G[path[i]][path[i+1]]:
			r = G[path[i]][path[i+1]]
		
	return r 
	
def FordFulkerson(G, s, t):
	n = len(G)
	f = np.zeros((n,n))
	
	Gf = np.zeros((n,n))
	CaculateGf(G, f, Gf)
	# print Gf
	p = []
	while FindPath(Gf, s, t, p):
		cfp = PathCf(Gf,p)
		print p,cfp
		for i in range(len(p)-1):
			u = p[i]
			v = p[i+1]
			if G[u][v]!=0:
				f[u][v] += cfp
			else:
				f[v][u] -= cfp
		CaculateGf(G, f, Gf)
		p = []
		# print 'GF',Gf
		
	return f,sum(f[s][:])
		
G1 = np.array([
	[0, 16, 13, 0, 0, 0],
	[0, 0, 0, 12, 0, 0],
	[0, 4, 0, 0, 14, 0],
	[0, 0, 9, 0, 0, 20],
	[0, 0, 0, 7, 0, 4],
	[0, 0, 0, 0, 0, 0]
	])
G2 = np.array([
	[0, 1000, 1000, 0],
	[0, 0, 1, 1000],
	[0, 0, 0, 1000],
	[0, 0, 0, 0]
	])
# p = []
# print FindPath(G, 0, 5, p)
# print p
print FordFulkerson(G2, 0, 3)