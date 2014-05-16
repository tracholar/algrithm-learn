# coding:utf8
def Hash(k):
	A = 2654435769.0/2**32	#0.618
	b = k*A
	p = 14	#取前14bits
	return int((2**p)*(b-int(b)))

class OverflowException(Exception):
	def __init__(self,msg):
		Exception.__init__(self)
		self.msg = msg
		print msg
# 开散列
NIL = -1
m = 97

c=0

def H1(k):
	return (k*10007) % m
	
def H2(k):
	return 1 + ((k*36467) % (m-1))
	
def h(k,i): #线性探查
	return (k*10007 + i)%m
def h2(k,i):  #双重散列
	return (H1(k)+i*H2(k)) % m
def HashInsert(T,k):
	global c
	i=0
	while True:
		j=h2(k,i)
		if T[j]==NIL:
			T[j] = k 
			return j 
		else:
			c+=1
			print k,i,j,'Conflict'
			i += 1
		if i==m:
			break
			
	raise OverflowException('Hash table overflow')
def HashSearch(T,k):
	i=0
	while True:
		j=h(k,i)
		if T[j]==k:
			return j
		i += 1
		if T[i]==NIL or i==m:
			return NIL
T1 = [NIL]*m
T2 = [NIL]*m	
for i in range(0,5000,97):
	HashInsert(T1,i)
print c,len(range(0,5000,97))
print T1