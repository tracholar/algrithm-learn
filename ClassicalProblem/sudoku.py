# coding:gbk
import random
import numpy as np

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

PrintSudoku(GetRandomSudoku(0.5))
