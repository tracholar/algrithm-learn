# coding:utf8
class Heap:
	"""
	this is heap
	"""
	data = None
	type = None
	def __init__(self,x=None):
		self.data = x

	def __repr__(self):
		return '%s' %  self.data
		
class MaxHeap(Heap):
	
	def __init__(self,x=None):
		self.type = 'max'
		Heap.__init__(self,x)
	
if __name__=='__main__':
	h = MaxHeap(range(10))
	print h.type,h