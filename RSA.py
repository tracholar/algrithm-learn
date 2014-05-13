# coding:gbk
# RSA public key 
#

p = 99991
q =	99767
n = p*q
fai = (p-1)*(q-1)
e = 0x10001

def egcd(a,b):
	''' 
	'''
	if b==0:
		return 1,0,a
	x,y,q = egcd(b,a%b)
	
	x,y = y,(x-a/b*y)
	return x,y,q
	
def GetInverse(e,n):
	d,y,q = egcd(e,n)
	if q!=1:
		raise Exception('error')
	else:
		return d % n
		
def modexp(m,e,n):
	s = 1
	while e!=0:
		if e & 1:
			s = (s*m)%n
		e >>= 1
		m = (m*m)%n
	return s
	
d = GetInverse(e,fai)
print 'Public key:',(e,n)
print 'Private key:', (d,n)

m = 1234567
c = modexp(m,e,n)
print 'Message:', m
print 'Cryptography:', c
print 'Decryptography:', modexp(c,d,n)