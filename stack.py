# coding:utf8


class Stack:
	def __init__(self):
		self.data = []
	def push(self,item):
		self.data.append(item)
		
	def pop(self,item):
		self.data.pop()
		
	def size(self):
		return len(self.data)
		
s = Stack()
s.push(3)
s.push(5)
print s.data,s.size()