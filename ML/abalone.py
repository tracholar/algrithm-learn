
f = open('abalone.txt','w')
for line in open('abalone.data','r'):
	if not line:
		continue
	line = line.replace('M,','')
	line = line.replace('F,','')
	line = line.replace('I,','')
	f.write(line)
	
	
	
