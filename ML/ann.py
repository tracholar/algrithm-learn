# coding:gbk

import numpy as np






class NN():
	def __init__(self, ni, nh, no):
		self.ni = ni
		self.nh = nh
		self.no = no 
		
		self.ai = np.ones(self.ni+1)
		self.ah = np.ones(self.nh)
		self.ao = np.ones(self.no)
		
		self.wi = np.random.rand(self.ni+1, self.nh)
		self.wo = np.random.rand(self.nh+1, self.no)
		
		
if __name__ == '__main__':
	n = NN(4,5,3)
	
	print __name__
	print n
		