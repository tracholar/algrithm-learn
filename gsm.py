# coding:utf8
import time

t1 = time.time()

file = open('gsm.dat')
money = {}
while True:
	line=file.readline()
	if not line:
		break
	num = line[:11]
	type = line[11:13]
	second = line[13:17]
	#print num,type,second
	if type == '00':
		price = 0.4
	else:
		price = 0.2
		
	if num in money:
		money[num] += price*int(second,10)
	else:
		money[num] = price*int(second,10)
	#break
t2 = time.time()
print t2-t1
	