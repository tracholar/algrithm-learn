# coding:gbk
import numpy as np

NIL = -1

def GenerateGraphy(N, w=1, sym = True):
	G = np.random.randint(-1,w+1,(N,N))
	if sym:
		G += G.T
		G /= 2
	G = G*1.0
	# print G
	for i in range(N):
		for j in range(N):
			if np.abs(G[i,j]) ==0:
				G[i,j] = np.inf
			if i==j:
				G[i,j] = 0
				
	return G  
	
def Edge(G):
	edg = []
	N = len(G)
	for i in range(N):
		for j in range(N):
			if G[i,j]!=np.inf:
				edg.append((i,j))
	return edg
	
def InitializeSingleSource(G,s):
	N = len(G)
	pi = np.zeros(N) 
	pi[:] = NIL
	d = np.zeros(N) 
	d[:] = np.inf
	d[s] = 0
	return pi,d 
	
# 不同算法Relax边的次数不同
# dijkstra算法每个边都只Relax一次
# 而Bellman-Ford算法每个边|V|-1次
def Relax(u,v,G,pi,d):
	if d[v] > d[u] + G[u,v]:
		d[v] = d[u] + G[u,v]
		pi[v] = u 

def BellmanFord(G,s):
	N = len(G)
	pi,d = InitializeSingleSource(G,s)
	for i in range(N-1):
		for e in Edge(G):
			Relax(e[0],e[1],G,pi,d)
			
	
	for e in Edge(G):
		u = e[0]
		v = e[1]
		# print e,d[v],d[u],G[u,v]
		if d[v]==np.inf or d[v] > d[u] + G[u,v]:
			return False,pi,d
	
	return True,pi,d


def PrintPath(pi,d,s):
	if pi[s]==NIL:
		print 'node\t distance'
		print '%d\t 0' % s
	else:
		PrintPath(pi,d,pi[s])
		print '%d\t %.f' % (s,d[s])
	
G = GenerateGraphy(4,4, False)
print G
b,pi,d = BellmanFord(G,0)

print pi
print d
if b:
	
	for i in range(len(G)):
		print '================='
		print 'we can reachie node %d from 0, tree path as follow:' % i
		print '================='
		PrintPath(pi,d,i)
	