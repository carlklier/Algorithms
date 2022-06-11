class HashTable:
	def __init__(self, capacity=13):
		self.capacity = capacity
		self.size = 0
		self.buckets = [None] * self.capacity