class Solution(object):
	# 哈希实现
	def firstMissingPositive(self, nums):	
		n = len(nums)
		for i in xrange(n):
			if nums[i]<=0:
				nums[i] = n+1
		for i in xrange(n):
			num = abs(nums[i])
			if num<=n:
				nums[num-1] = -abs(nums[num-1])
		for i in xrange(n):
			if nums[i]>0:
				return i+1
		return n+1
		
		
		
	# 交换下标实现	
	def firstMissingPositive(self, nums):	
		n = len(nums)
		for i in xrange(n):
			while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]:
				nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
		for i in xrange(n):
			if nums[i]-1!=i:
				return i+1
		return n+1
		