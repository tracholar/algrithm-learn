# coding:gbk
# RB tree
# delete method should be added!
#

import numpy as np

class RBNode:
	def __init__(self,key,color='R'):
		self.key = key
		self.color = color
		self.parent = None
		self.lchild = None
		self.rchild = None
	def __repr__(self):
		return str(self.key) + '(' + self.color + ')'
		
class RBTree:
	def __init__(self):
		self.root = None
	
	def leftRotate(self,x):
		y = x.rchild
		x.rchild = y.lchild
		if y.lchild != None:
			y.lchild.parent = x
		y.parent = x.parent
		if x.parent == None:
			self.root = y
		elif x == x.parent.lchild:
			x.parent.lchild = y
		else:
			x.parent.rchild = y
		y.lchild = x
		x.parent = y
		return
		
	def rightRotate(self,y):
		x = y.lchild
		y.lchild = x.rchild
		if x.rchild != None:
			x.rchild.parent = y
		x.parent = y.parent
		if y.parent == None:
			self.root = x
		elif y == y.parent.lchild:
			y.parent.lchild = x
		else:
			y.parent.rchild = x
		x.rchild = y
		y.parent = x
		return
		
	def insertFixup(self,z):
		
		while z.parent!=None and z.parent.color == 'R':	
			if z.parent == z.parent.parent.lchild:
				y = z.parent.parent.rchild
				if y!=None and y.color == 'R':
					z.parent.parent.color = 'R'
					z.parent.color = 'B'
					y.color = 'B'
					z = z.parent.parent
				elif z==z.parent.rchild:
					z = z.parent
					self.leftRotate(z)
				else:
					z.parent.color = 'B'
					z.parent.parent.color = 'R'
					self.rightRotate(z.parent.parent)
			else:
				y = z.parent.parent.lchild
				if y!=None and y.color == 'R':
					y.color = 'B'
					z.parent.color = 'B'
					z.parent.parent.color = 'R'
					z = z.parent.parent
				elif z == z.parent.lchild:
					z = z.parent
					self.rightRotate(z)
				else:
					z.parent.color = 'B'
					z.parent.parent.color = 'R'
					self.leftRotate(z.parent.parent)
			
		self.root.color = 'B'
		
	def insert(self,node):
		if self.root == None:
			self.root = node
			self.root.color = 'B'
			return
		p = self.root
		while True:
			if node.key <= p.key:
				if p.lchild == None:
					node.parent = p
					p.lchild = node
					self.insertFixup(node)
					break
				p = p.lchild
			else:
				if p.rchild == None:
					node.parent = p
					p.rchild = node
					self.insertFixup(node)
					break
				p = p.rchild
		return
	
	
	def find(self,key):
		p = self.root
		while p!=None and p.key!=key:
			if key > p.key:
				p = p.rchild
			else:
				p = p.lchild
		if p==None or p.key!=key:
			return None
		else:
			return p
		
	def echo(self,node,i):
		if node==None:
			return
		
		self.echo(node.lchild,i+1)
		for j in range(i):
			print '\t',
		print node
		self.echo(node.rchild,i+1)
		return
	def __repr__(self):
		self.echo(self.root,0)
		return ''
		
rbt = RBTree()
for i in np.random.randint(0,200,20):
	rbt.insert(RBNode(i))

	print rbt
	print '-------------------------------------------'
n = rbt.find(i)
print i,n
print n.parent
