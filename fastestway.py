# coding:gbk
import numpy as np
import time

def fastway(a,t,e,x,n):
	f0 = [e[0]+a[0][0]]
	f1 = [e[1]+a[1][0]]
	L1 = [0]
	L2 = [1]
	for i in range(1,n):
		if f0[i-1]+a[0][i]<f1[i-1]+t[1][i]+a[0][i]:
			f0.append(f0[i-1]+a[0][i])
			L1.append(0)
		else:
			f0.append(f1[i-1]+t[1][i]+a[0][i])
			L1.append(1)
		
		if f1[i-1]+a[1][i]<f0[i-1]+t[0][i]+a[1][i]:
			f1.append(f1[i-1]+a[1][i])
			L2.append(1)
		else:
			f1.append(f0[i-1]+t[0][i]+a[1][i])
			L2.append(0)
	
	if f0[n-1]+x[0]<=f1[n-1]+x[1]:
		return f0[n-1]+x[0],L1
	else:
		return f1[n-1]+x[1],L2
		
e = [0,0]
n = 1
while True:
	a = np.random.rand(2,n)*10
	t = np.random.rand(2,n)

	x = [1,1]
	t1 = time.time()
	v,L = fastway(a,t,e,x,n)
	t2 = time.time()
	print n,t2-t1,v
	if t2-t1>10:
		break
	n *= 2