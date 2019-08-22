class Solution(object):
	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		import random
		self.d = dict()
		for i in range(len(nums)):
			if(self.d.has_key(nums[i])):
				self.d[nums[i]].append(i)
			else:
				self.d[nums[i]] = [i]
		

	def pick(self, target):
		"""
		:type target: int
		:rtype: int
		"""
		arr = self.d[target]
		n = len(arr)-1
		if(n == 1):
			return arr[0]
		else:
			return arr[ random.randint(0,n) ]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)