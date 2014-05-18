# coding:utf8
import time

class BTNode:
	def BTNode(self,n=0,key=None,isleaf=True,children=None):
		self.n = n	# 关键字数
		self.key = key	# 关键字列表，长度为n，以非降序存放
		self.isleaf = isleaf	# 是否为叶子节点
		self.children = children	# 孩子列表，长度为n+1

def DiskRead(c):
	time.sleep(0.01)	# sleep 0.01s
def DiskWrite(c):
	time.sleep(0.01)

class BTree:
	def BTree(self):
		self.root = BTNode()
		self.t = 2	# 最小度
		
		
	def search(self,x,k):
		i = 0
		while i<x.n and k>x.key[i]:
			i += 1
		if i<x.n and k==x.key[i]:
			return (x,i)
		elif x.isleaf:
			return None
		else:
			DiskRead(x.children[i])
			return self.search(x.children[i],k)
	
	def SplitChild(self,x,i,y):
		t = self.t
		z = BTNode()
		z.isleaf = y.isleaf
		z.n = self.t - 1
		
		z.key = y.key[t:2*t-1]
		
		if not y.isleaf:
			z.children = y.children[self.t:2*self.t]
			
		y.children = y.children[0:self.t-1]
		y.n = self.t - 1
		x.children.insert(i,z)
		x.key.insert(i,y.key[t-1])
		x.n += 1
		y.key = y.key[:t-1]
		DiskWrite(y)
		DiskWrite(z)
		DiskWrite(x)

	