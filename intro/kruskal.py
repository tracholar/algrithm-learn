# coding:gbk

import numpy as np

class Edge:
	def __init__(self,u,v,w):
		self.u = u
		self.v = v 
		self.w = w 
	@staticmethod
	def cmp(a,b):
		return a.w - b.w
		
def MSTKruskal(G):
	A = []
	N = len(G)
	R = np.zeros(N)	# 每个节点的父节点，用来表示树的关系
	E = []
	for i in range(0,N):
		for j in range(i+1,N):
			E.append(Edge(i,j,G[i][j]))
			
	
	for i in range(0,N):
		R[i] = i
		
	for e in sorted(E,cmp=Edge.cmp):
		if R[e.u] != R[e.v]:
			A.append(e)
			# Union
			rv = R[e.v]
			ru = R[e.u]
			for i in range(0,N):
				if R[i] == rv:
					R[i] = ru
					
	return A 
	
	
	
	



G = np.random.randint(0,100,(40,40))
G += G.T
for i in range(0,len(G)):
	G[i][i] = 0

A = MSTKruskal(G)
for e in A:
	print '(%d,%d)\t%d' % (e.u,e.v,e.w)
	
