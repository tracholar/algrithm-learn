#coding:utf8
import numpy as np
import matplotlib.pyplot as plt
import math

sum = 0.
subsum = []
subsum0 = []
n = []
N = 1
for i in xrange(1,2**25+1):
	sum += 1./i
	if i == N :
		subsum.append(sum)
		subsum0.append(math.log(N))
		n.append(N)
		print N
		N *= 2
	
#print n
	
n = np.array(n)
subsum0 = np.array(subsum0)
subsum = np.array(subsum)
print n,subsum
plt.semilogx(n,subsum0,'r.',n,subsum,'b-')
plt.show()

