# coding:gbk
# 贪心算法求解活动选择问题
#

def ActivitySelector(s,f,i,j):
	m = i + 1
	while m<j and s[m]<f[i]:
		m += 1
	if m<j:
		return [m] + ActivitySelector(s,f,m,j)
	else:
		return []
		
def GreedyActivitySelector(s,f):
	n = len(s)
	A = [0]
	i = 0
	
	for m in range(1,n):
		if s[m] >= f[i]:
			A = A + [m]
			i = m
	return A
		
s = [0,0,3,4,6,7,5,9,0,10]
f = [0,1,5,6,9,9,9,10,10,12]

print ActivitySelector(s,f,0,len(s))
print GreedyActivitySelector(s,f)

