

class Node:
	def __init__(self, data = None):
		self.data = data
		self.left = None
		self.right = None

	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data: 
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data

	def find_item(self, find_value):
		if find_value < self.data:
			if self.left is None:
				return 'Not found'
			return self.left.find_item(find_value)
		elif find_value > self.data:
			if self.right is None:
				return 'Not found'
			return self.right.find_item(find_value)
		else:
			return str(self.data) + ' - is found'

	def show(self):
		if self.left:
			self.left.show()
		print(self.data)
		if self.right:
			self.right.show()
	def max(self):
		if self.right is None:
			print(self.data)
		else:
			self.right.max()
	def min(self):
		if self.left is None:
			print(self.data)
		else:
			self.left.min()

if __name__ == '__main__':
	tree = Node()
	tree.insert(20)
	tree.insert(2)
	tree.insert(23)
	tree.insert(25)
	tree.insert(22)
	tree.insert(1)
	tree.max()
	tree.min()
	# tree.show()
