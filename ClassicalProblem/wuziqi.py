# coding:gbk
import numpy as np
import sys
import re
import copy

N = 15 # size of chess
BLACK = 1
WHITE = 2
EMPTY = 0

def CreateMap():
	return np.zeros((N, N), dtype=int)
	
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
	
def FindMaxV(map, pos, color):
	map = copy.copy(map)
	if map[pos[0],pos[1]] != EMPTY:
		return 0
	SetPos(map,pos,color)
	maxV = [0,0,0,0]
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
			elif map[i][j] == EMPTY:
				maxV[0] = max(maxV[0], xall*5)
				xall = 0
			else:
				xall = 1
				xlast = ChangeColor(xlast)
			
			
			if map[j][i] == ylast:
				yall += 1
			elif map[j][i] == EMPTY:
				maxV[1] = max(maxV[1], yall*5)
				yall = 0
			else:
				yall = 1
				ylast = ChangeColor(ylast)
	maxV[0] = max(maxV[0],xall*5)
	maxV[1] = max(maxV[1],yall*5)
			
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
			elif map[i][j] == EMPTY:
				maxV[2] = max(maxV[2], all*5)
				all = 0
			else:
				all = 1
				last = ChangeColor(last)
	maxV[2] = max(maxV[2], yall*5)
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
				
			elif map[i][j] == EMPTY:
				maxV[3] = max(maxV[3], all*5)
				all = 0
			else:
				all = 1
				last = ChangeColor(last)
	maxV[3] = max(maxV[3], all*5) - 5
	
	return max(maxV)

def getposstring(map, pos):
	sh = []
	sv = []
	sl = []
	sr = []
	
	
	i = pos[0]
	colormap = ['0','1','2']
	
	for j in range(N):
		sh.append(colormap[map[i][j]])
	
	j = pos[1]
	for i in range(N):
		sv.append(colormap[map[i][j]])
	
	delta = pos[0] - pos[1]
	if delta >0:
		si = delta
		endi = N 
	else:
		si = 0
		endi = N + delta
	
	all = 0
	for i in range(si, endi):
		j = i - delta
		sl.append(colormap[map[i][j]])
	
	sumij = pos[0] + pos[1]
	if sumij >= N:
		si = sumij - N + 1
		endi = N 
	else:
		si = 0
		endi = sumij + 1
	
	all = 0
	for i in range(si, endi):
		j = sumij - i
		sr.append(colormap[map[i][j]])
			
	return ''.join(sh) , ''.join(sv) , ''.join(sl) , ''.join(sr)		
	
def findChanglian(map, pos):
	ret = 0
	
	if map[pos] == 1:
		P = '11111'
	elif map[pos] == 2:
		P = '22222'
	else:
		P = '00000'
	
	for s in getposstring(map, pos):
		ret += s.count(P)
	
	
	return ret
	
def findHuosi(map, pos):
	ret = 0
	
	if map[pos] == 1:
		P = '011110'
	elif map[pos] == 2:
		P = '022220'
	else:
		return 0
	
	for s in getposstring(map, pos):
		ret += s.count(P)
			
	return ret 
	
def findChongsi(map, pos):
	ret = 0
	
	if map[pos] == 1:
		Pa = ['011112','211110','0101110','0111010','0110110']
	elif map[pos] == 2:
		Pa = ['022221','122220','0202220','0222020','0220220']
	else:
		return 0
	
	for P in Pa:
		for s in getposstring(map, pos):
			ret += s.count(P)
		
	return ret 
	
def findHuosan(map, pos):
	ret = 0
	if map[pos] == 1:
		Pa = ['01110','010110','011010']
	elif map[pos] == 2:
		Pa = ['02220','020220','022020']
	else:
		return 0
	
	for P in Pa:
		for s in getposstring(map, pos):
			ret += s.count(P)
	return ret 
	
def findMiansan(map, pos):
	ret = 0
	if map[pos] == 1:
		Pa = ["001112", "211100", "010112", "211010", "011012", "210110", "10011", "11001", "10101", "2011102"]
	elif map[pos] == 2:
		Pa = ["002221", "122200", "020221", "122020", "022021", "120220", "20022", "22002", "20202", "1022201"]
	else:
		return 0
	
	for P in Pa:
		for s in getposstring(map, pos):
			ret += s.count(P)
	return ret 
	
def findHuoer(map, pos):
	ret = 0
	if map[pos] == 1:
		Pa = ["00110", "01100", "01010", "010010"]
	elif map[pos] == 2:
		Pa = ["00220", "02200", "02020", "020020"]
	else:
		return 0
	
	for P in Pa:
		for s in getposstring(map, pos):
			ret += s.count(P)
	return ret 
	
def findMianer(map, pos):
	ret = 0
	if map[pos] == 1:
		Pa = ["000112", "211000", "001012", "210100", "100001", "2010102", "2011002", "2001102"]
	elif map[pos] == 2:
		Pa = ["000221", "122000", "002021", "120200", "200002", "1020201", "1022001", "1002201"]
	else:
		return 0
	
	for P in Pa:
		for s in getposstring(map, pos):
			ret += s.count(P)
	return ret 
	
def findSisi(map, pos):
	ret = 0
	if map[pos] == 1:
		Pa = ["211112"]
	elif map[pos] == 2:
		Pa = ["122221"]
	else:
		return 0
	
	for P in Pa:
		for s in getposstring(map, pos):
			ret += s.count(P)
	return ret 
	
def findSisan(map, pos):
	ret = 0
	if map[pos] == 1:
		Pa = ["21112"]
	elif map[pos] == 2:
		Pa = ["12221"]
	else:
		return 0
	
	for P in Pa:
		for s in getposstring(map, pos):
			ret += s.count(P)
	return ret 
	
def findSier(map, pos):
	ret = 0
	if map[pos] == 1:
		Pa = ["2112"]
	elif map[pos] == 2:
		Pa = ["1221"]
	else:
		return 0
	
	for P in Pa:
		for s in getposstring(map, pos):
			ret += s.count(P)
	return ret 
	
								
	
def heuristicValue(map, pos, color):
	ret = 0
	map = copy.copy(map)
	SetPos(map, pos, color)
	i = pos[0]
	j = pos[1]
	
	ret += findChanglian(map, pos) * 1000	\
		+ findHuosi(map, pos) * 800			\
		+ findChongsi(map, pos) * 100		\
		+ findHuosan(map, pos) * 90			\
		+ findMiansan(map, pos) * 50		\
		+ findHuoer(map, pos) * 30			\
		+ findMianer(map, pos) * 20			\
		- findSisi(map, pos) * 10			\
		- findSisan(map, pos) * 10			\
		- findSier(map, pos) * 10			\
		+ min(i, j, N-i-1, N-j-1)
	
	return ret 
	
	
def FindMaxPos(map, color):
	value = np.zeros((N,N))
	maxV = 0
	maxi = 0
	maxj = 0
	for i in range(N):
		for j in range(N):
			if map[i][j] != EMPTY:
				continue
			
			
			value[i][j] = heuristicValue(map, (i,j), color)
			if maxV < value[i][j]:
				maxV = value[i][j]
				maxi, maxj = i, j 
	# print value
	# print maxi, maxj, maxV
	return maxi, maxj
			
			
def SearchNextPos(map, color):
	return FindMaxPos(map, color)

if __name__ == '__main__':
	map = CreateMap()
	print 'Begin!'
	PrintMap(map)
	while True:
		line = sys.stdin.readline().strip()
		if not re.match(r'^\d{1,2} \d{1,2}$', line):
			if line in ['q','Q','quit']:
				break
			print 'Input formet error, please input with formet number + space + number'
			continue
		x, y = line.split(' ')
		x = int(x)
		y = int(y)
		
		if SetPos(map,(x-1,y-1),BLACK):
			PrintMap(map)
			
			if IsWin(map)==BLACK:
				print 'You win!'
				break
				
			pos = SearchNextPos(map, WHITE)
			if not SetPos(map, pos, WHITE):
				print 'Error: position (%d, %d) is not empty!' % (pos[0]+1,pos[1]+1)
			PrintMap(map)
			if IsWin(map)==WHITE:
				print 'You loss!'
				break
		else:
			print 'Error: position (%d, %d) is not empty!' % (x,y)
		
		