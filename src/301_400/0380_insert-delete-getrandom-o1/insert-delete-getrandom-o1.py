class RandomizedSet(object):
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.d = dict()
		self.arr = []
		import random

	def insert(self, val):
		"""
		Inserts a value to the set. Returns true if the set did not already contain the specified element.
		:type val: int
		:rtype: bool
		"""
		if val not in self.d:
			self.d[val] = len(self.arr)
			self.arr.append(val)
			return True
		return False
			
			

	def remove(self, val):
		"""
		Removes a value from the set. Returns true if the set contained the specified element.
		:type val: int
		:rtype: bool
		"""
		if val in self.d:
			last_element,index = self.arr[-1],self.d[val]
			self.arr[index] = last_element
			self.d[last_element] = index
			del self.d[val]
			self.arr.pop()
			return True
		return False
		

	def getRandom(self):
		"""
		Get a random element from the set.
		:rtype: int
		"""
		return random.choice(self.arr)
		


# param_3 = obj.getRandom()