
class Node:
	def __init__(self, value = None, next = None):
		self.value = value
		self.next = next

class LinkedList:

	def __init__(self):
		self.first = None
		self.last = None
		self.length = 0

	def add(self, x):
		self.length += 1
		if self.first == None:
			self.first = self.last = Node(x, None)
		else: 
			self.last.next = self.last = Node(x, None)

	def push(self, x):
		self.length += 1
		if self.first == None:
			self.first = self.last = Node(x, None)
		else:
			self.first = Node(x, self.first)	

			
	def show(self):
		if self.first != None:
			current = self.first
			print(current.value)
			while current.next != None:
				current = current.next
				print(current.value)

if __name__ == '__main__':
	l1 = LinkedList()
	l1.add('12')
	l1.add(2)
	l1.push(3)
	l1.show()


