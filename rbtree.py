import numpy as np

class RBNode:
	def __init__(self,key,color='R'):
		self.key = key
		self.color = color
		self.parent = None
		self.lchild = None
		self.rchild = None
	def __repr__(self):
		return str(self.key) + ' ' + self.color
		
class RBTree:
	def __init__(self):
		self.root = None 
	
	def leftRotate(self,z):
		
	def rightRotate(self,z):
		
	def insertFixup(self,z):
		if z.parent == None:
			break
		while z.parent.color == 'R':
			if z.parent == z.parent.parent.lchild:
				y = z.parent.parent.rchild
				if y.color == 'R':
					
			
		self.root.color = 'B'
		
	def insert(self,node):
		if self.root == None:
			self.root = node
			return
		p = self.root
		while True:
			if node.key <= p.key:
				if p.lchild == None:
					node.parent = p
					p.lchild = node
					self.inserFixup(node)
					break
				p = p.lchild
			else:
				if p.rchild == None:
					node.parent = p
					p.rchild = node
					self.inserFixup(node)
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
		
	def echo(self,node):
		if node==None:
			return
		
		self.echo(node.lchild)
		print node.key,node.color
		self.echo(node.rchild)
		return
	def __repr__(self):
		self.echo(self.root)
		return ''
		
rbt = RBTree()
for i in np.random.rand(100):
	rbt.insert(RBNode(i))

print rbt
n = rbt.find(i)
print i,n
print n.parent
