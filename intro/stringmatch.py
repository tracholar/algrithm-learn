# coding:gbk

def NaiveStringMatcher(T, P):
	n = len(T)
	m = len(P)
	
	for s in range(n-m):
		if P == T[s:s+m]:
			print 'match as %d' % s
			
NaiveStringMatcher('fadfasdfasdfasdfdhsfasdfa','asdf')