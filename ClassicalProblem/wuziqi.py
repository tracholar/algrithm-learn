# coding:gbk
import numpy as np
import sys

N = 15 # size of chess
BLACK = 1
WHITE = 2
EMPTY = 0

def CreateMap():
	return np.zeros((N, N))
	
def PrintMap(map):
	print ' ', 
	for i in range(N):
		print ((i+1) % 10),
	print 
	for i in range(N):
		print ((i+1) % 10),'',
		for j in range(N):
			if map[i,j] == EMPTY:
				sys.stdout.write('·')
			elif map[i,j] == WHITE:
				sys.stdout.write('○')
			elif map[i,j] == BLACK:
				sys.stdout.write('●')
		sys.stdout.write('\n')

def SetPos(map, pos, v):
	if map[pos[0],pos[1]] == EMPTY:
		map[pos[0],pos[1]] = v
		return True
	else:
		return False
		
def ChangeColor(c):
	if c == BLACK:
		return WHITE
	elif c == WHITE:
		return BLACK
	return EMPTY
				
	
def IsWin(map):
	
	for i in range(N):
		xall = 0
		cx = BLACK
		xlast = BLACK
		yall = 0
		cy = BLACK
		ylast = BLACK
		
		for j in range(N):
			if map[i][j] == xlast:
				xall += 1
				if xall == 5:
					return xlast
			elif map[i][j] == EMPTY:
				xall = 0
			else:
				xall = 1
				xlast = ChangeColor(xlast)
				
			if map[j][i] == ylast:
				yall += 1
				if yall == 5:
					return ylast
			elif map[j][i] == EMPTY:
				yall = 0
			else:
				yall = 1
				ylast = ChangeColor(ylast)
	
	for delta in range(5-N,N-5+1):
		all = 0
		last = BLACK
		c = BLACK
		
		if delta<0:
			si = 0
			endi = N + delta
		else:
			si = delta
			endi = N
			
		for i in range(si,endi):
			j = i - delta
			if map[i][j] == last:
				all += 1
				if all == 5:
					return last
			elif map[i][j] == EMPTY:
				all = 0
			else:
				all = 1
				last = ChangeColor(last)
	
	for sumij in range(4,2*N-5):
		all = 0
		last = BLACK
		c = BLACK
		
		if sum<N:
			si = 0
			endi = sumij + 1
		else:
			si = sumij +1 - N
			endi = N
			
		for i in range(si,endi):
			j = sumij - i
			if map[i][j] == last:
				all += 1
				if all == 5:
					return last
			elif map[i][j] == EMPTY:
				all = 0
			else:
				all = 1
				last = ChangeColor(last)
	return False
	
def SearchNextPos(map):
	return 0,0

if __name__ == '__main__':
	map = CreateMap()
	map[7,7] = BLACK
	map[7,8] = WHITE
	PrintMap(map)
	while True:
		line = sys.stdin.readline().strip()
		x, y = line.split(' ')
		x = int(x)
		y = int(y)
		
		if SetPos(map,(x-1,y-1),BLACK):
			PrintMap(map)
			if IsWin(map)==BLACK:
				print 'You win!'
				break
				
			pos = SearchNextPos(map)
			if not SetPos(map, pos, WHITE):
				print 'Error: position (%d, %d) is not empty!' % (pos[0]+1,pos[1]+1)
			PrintMap(map)
			if IsWin(map)==WHITE:
				print 'You loss!'
				break
		else:
			print 'Error: position (%d, %d) is not empty!' % (x,y)
		
		