# coding:gbk
import random
import numpy as np
import time

def PrintSudoku(M):
	n = len(M)
	for i in range(n):
		if i % 3 == 0:
			print '-------------------------'
		for j in range(n):
			if j % 3 ==0:
				print '|',
			print M[i][j] ,
		
		print '|'
	print '-------------------------'
	
def GetRandomList(n):
	L = []
	while len(L) != n:
		i = random.randint(0,n-1) + 1
		if i not in L:
			L.append(i)
			
	return L
	
def GetRandomSudoku(hard=0.8):
	sudoku = [
		[9,7,8,3,1,2,6,4,5],  
		[3,1,2,6,4,5,9,7,8],  
		[6,4,5,9,7,8,3,1,2],  
		[7,8,9,1,2,3,4,5,6],  
		[1,2,3,4,5,6,7,8,9],  
		[4,5,6,7,8,9,1,2,3],  
		[8,9,7,2,3,1,5,6,4],  
		[2,3,1,5,6,4,8,9,7],  
		[5,6,4,8,9,7,2,3,1]  
	]
	
	n = len(sudoku)
	map = GetRandomList(n)
	# print map
	for i in range(n):
		for j in range(n):
			if random.random() > hard:
				sudoku[i][j] = 'x'
			else:
				sudoku[i][j] = map[sudoku[i][j]-1]
	
	return sudoku

def FindFirstNone(sudo):
	for i in range(len(sudo)):
		for j in range(len(sudo)):
			if sudo[i][j] == 'x':
				return i,j 
	return -1,-1
	
def FindAllNone(sudo):
	L = []
	for i in range(len(sudo)):
		for j in range(len(sudo)):
			if sudo[i][j] == 'x':
				L.append((i,j))
	return L

def IsRightSudo(sudo):
	n = len(sudo)
	for i in range(n):
		# PrintSudoku(sudo)
		for j in range(n):
			if sudo[i][j]!='x':
				for k in range(j+1,n):
					if sudo[i][j] == sudo[i][k]:
						return False
			if sudo[j][i] !='x':
				for k in range(j+1,n):
					if sudo[j][i] == sudo[k][i]:
						return False
	for i in range(n/3):
		for j in range(n/3):
			# PrintSudoku(sudo)
			for k in range(9):
				if sudo[i*3+k/3][j*3+(k%3)] == 'x':
					continue
				for m in range(k+1,9):
					if sudo[i*3+k/3][j*3+(k%3)] == sudo[i*3+m/3][j*3+(m%3)]:
						# print i*3+k/3,j*3+(k%3),i*3+m/3,j*3+(m%3)
						# PrintSudoku(sudo)
						return False
				
	return True	
	
def FindCadidateNumber(sudo, i, j):
	L = []
	for k in range(1,10):
		sudo[i][j] = k
		if IsRightSudo(sudo):
			L.append(k)
		sudo[i][j] = 'x'
	return L

	
def SolveSudoku(sudo):
	i,j = FindFirstNone(sudo)
	if i==-1 and j==-1:
		return True
	
	candidateNumber = FindCadidateNumber(sudo,i ,j)
	for k in candidateNumber:
		sudo[i][j] = k 
		# PrintSudoku(sudo)
		if SolveSudoku(sudo):
			return True
		sudo[i][j] = 'x'
	
	return False
	
def SolveSudokuMinCandidateFirst(sudo):
	L = FindAllNone(sudo)
	if len(L)==0:
		return True
	
	candidateNumber = []
	i , j = -1, -1
	for k in range(0,len(L)):
		cnL = FindCadidateNumber(sudo, L[k][0] ,L[k][1])
		# print cnL
		if len(cnL) == 0:
			return False
		
		if k==0 or len(cnL) < len(candidateNumber):
			candidateNumber = cnL
			i, j = L[k]
	# print i,j 
	# print candidateNumber
	for k in candidateNumber:
		sudo[i][j] = k 
		# PrintSudoku(sudo)
		if SolveSudoku(sudo):
			return True
		sudo[i][j] = 'x'
	
	return False

if __name__ == '__main__':
	genT = []
	solveT = []
	for n in range(20):
		t1 = time.time()
		sudo = GetRandomSudoku(0.3)
		t2 = time.time()
		genT.append(t2-t1)
		PrintSudoku(sudo)
		# i,j = FindFirstNone(sudo)
		# print i,j 
		# print FindCadidateNumber(sudo, i, j)
		
		t1 = time.time()
		SolveSudokuMinCandidateFirst(sudo)
		# SolveSudoku(sudo)
		t2 = time.time()
		solveT.append(t2-t1)
		
		PrintSudoku(sudo)
		print IsRightSudo(sudo)

	print 'gen:(%.4f,%.4f)' % (np.mean(genT),np.std(genT))
	print 'solve:(%.4f,%.4f)' % (np.mean(solveT),np.std(solveT))
