# coding:gbk

def catalan(n):
	if n==1:
		return 1
	p = 0
	for i in xrange(1,n):
		p += catalan(i)*catalan(n-i)
	return p
	
for j in range(1,15):
	print j,catalan(j)
