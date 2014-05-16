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
	

	