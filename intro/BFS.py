import numpy as np


def BFS(G,s):
	'''
	find element s in Graph G by BFS
	G is adjoin matrix
	'''
	WHITE=0
	GRAY=1
	BLACK=2
	color = np.zeros(len(G)) #0 WHITE , 1 GRAY , 2 BLACK
	d = np.zeros(len(G)) + np.inf
	parent = np.zeros(len(G)) - 1  # -1 = NIL
	
	d[s] = 0
	color[s] = GRAY
	
	Q = []
	Q.append(s)
	
	while len(Q)!=0:
		u = Q.pop(0)
		
		for i in range(len(G)):
			if G[u,i]!=0:
				if color[i]==WHITE:
					color[i] = GRAY
					d[i] = d[u] + 1
					parent[i] = u
					Q.append(i)
					
		color[u] = BLACK
		
	return color,d,parent
		
G = np.random.randint(0,1000,(1400,1400))/995
color,d,parent = BFS(G,3)
#print 'G',G 
print 'd',max(d)
# print parent


	