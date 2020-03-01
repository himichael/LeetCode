class Solution(object):
	def productExceptSelf(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		if not nums:
			return []
		n = len(nums)	
		left = [0 for _ in xrange(n)]
		right = [0 for _ in xrange(n)]
		res = [0 for _ in xrange(n)]
		left[0] = 1
		right[n-1] = 1
		for i in xrange(1,n):
			left[i] = left[i-1]*nums[i-1]
		for i in xrange(n-2,-1,-1):
			right[i] = right[i+1]*nums[i+1]
		for i in xrange(n):
			res[i] = left[i]*right[i]
		return res
		
		
		
	# 另一种解法	
	def productExceptSelf(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		if not nums:
			return []
		n = len(nums)
		res = [0 for _ in xrange(n)]
		k = 1
		for i in xrange(n):
			res[i] = k
			k = k*nums[i]
		k = 1
		for i in xrange(n-1,-1,-1):
			res[i] *= k
			k = k*nums[i]
		return res
		