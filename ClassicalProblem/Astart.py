# coding:gbk

import numpy as np
import sys

N = 40
map = np.zeros((N,N),dtype=int) + 1

for i in range(N):
	map[6][6:20] = 0
	map[N-6][6:20] = 0
map[6:N-6+1,20] = 0

def PrintMap(map):
	m,n = map.shape
	for i in range(m):
		for j in range(n):
			if map[i][j]==1:
				sys.stdout.write(' ')
			else:
				sys.stdout.write('x')
		sys.stdout.write('\n')
	
def AddAdjToOpen(map, s, open, close, parent):
	L = [(s[0]+1,s[1]),(s[0]-1,s[1]),(s[0],s[1]+1),(s[0],s[1]-1)]
	m,n = map.shape
	
	for i,j in L:
		if i>=0 and i<m and j>=0 and j<n and map[i,j]==1 and (i,j) not in close and (i,j) not in open:
			# print (i,j) ,
			open.append((i,j))
			parent[(i,j)] = s
	
def f(s, t, p):
	return np.abs(p[0]-s[0]) + np.abs(p[1]-s[1]) \
		+ np.abs(p[0]-t[0])

def FindMinf(fL):
	min = None
	t = None
	for p, f in fL.items():
		if min is None or min > f:
			min = f 
			t = p 
	
	return t
		
def PrintPath(map, path):
	m,n = map.shape
	for i in range(m):
		for j in range(n):
			if map[i][j]==1:
				if (i,j) not in path:
					sys.stdout.write(' ')
				else:
					sys.stdout.write('+')
			else:
				sys.stdout.write('x')
		sys.stdout.write('\n')

def FindPath(parent, s, t):
	p = []
	while s!=t:
		p.insert(0,t)
		t = parent[t]
	p.insert(0,s)
	return p 
	

def Search(map, s, t):
	
	open = [s]
	close = []
	parent = dict()
	fL = dict()

	
	c = open.pop(0)
	
	while True:
		# print 'c:',c
		# print open
		
		AddAdjToOpen(map,c,open,close,parent)
		close.append(c)
		
		if len(open) == 0:
			return False, parent
		if c==t:
			return True, parent
			
		for i,j in open:
			fL[(i,j)] = f(s, t, (i,j))
			
		i,j = FindMinf(fL)
		c = (i,j)
		for k in range(len(open)):
			if c == open[k]:
				open.pop(k)
				break
		
		fL = dict()
		
		

PrintMap(map)
s = (20,0)
t = (20,39)
isfind, parent = Search(map,s,t)
print isfind
p = FindPath(parent, s, t)
PrintPath(map, p)

