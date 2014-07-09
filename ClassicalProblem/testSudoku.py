# coding:gbk
import numpy as np
import sudoku
import time

str = '\
0 0 0 0 3 0 0 0 5 \
8 0 5 0 2 9 0 0 0 \
0 0 0 0 0 0 0 9 8 \
0 0 2 5 0 0 4 0 0 \
6 0 0 0 0 0 0 0 1 \
0 0 9 0 0 7 6 0 0 \
4 2 0 0 0 0 0 0 0 \
0 0 0 8 1 0 2 0 4 \
1 0 0 0 6 0 0 0 0'
sudo = [
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
L = str.split(' ')
for i in range(len(L)):
	k = int(L[i])
	
	if k==0:
		sudo[i/9][i%9] = 'x'
	else:
		sudo[i/9][i%9] = k
		
sudoku.PrintSudoku(sudo)
t1 = time.time()
# sudoku.SolveSudokuMinCandidateFirst(sudo)
sudoku.SolveSudoku(sudo)
t2 = time.time()
sudoku.PrintSudoku(sudo)
print '%.3f' % (t2-t1)