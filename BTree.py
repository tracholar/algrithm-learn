# coding:utf8


class BTNode:
	def BTNode(self,n=0,key=None,isleaf=True,children=None):
		self.n = n
		self.key = key
		self.isleaf = isleaf
		self.children = children

class BTree:
	def BTree(self):
		self.root = BTNode()
	

	