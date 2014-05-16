# coding:gbk
# factor big number
import math
def factor1(n):
	if n == 1:
		return 1
	for i in xrange(2,n):
		if n%i ==0:
			return i,factor1(n/i)
	return n
			
n = 0xc0536d102f12b476c0ac50af8ecd3d04b41092487471d4a3a976724f4da88c9f
print factor1(n)