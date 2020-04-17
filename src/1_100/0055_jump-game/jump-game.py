class Solution(object):
	def canJump(self, nums):
		if not nums:
			return True
		max_jump = 0
		n = len(nums)
		for i in xrange(n):
			if max_jump>=i:
				max_jump = max(max_jump,i+nums[i])
		if max_jump>=n-1:
			return True
		return False
		
		
		
	# 递归(超时)
	def canJump(self, nums):
		if not nums:
			return True
		n = len(nums)
		def dfs(index):
			if index==n-1:
				return True
			jump = nums[index]+index
			if jump>n-1:
				jump = n-1
			for i in xrange(index+1,jump+1):
				if dfs(i):
					return True
			return False
		return dfs(0)
		
		
		
	# 递归+记忆化(超时)	
	def canJump(self, nums):
		if not nums:
			return True
		n = len(nums)
		cache = dict()
		def dfs(index):
			if index==n-1:
				return True
			if index in cache:
				return cache[index]
			jump = nums[index]+index
			if jump>n-1:
				jump = n-1
			for i in xrange(index+1,jump+1):
				if dfs(i):
					cache[i] = True
					return cache[i]
			cache[index] = False
			return cache[index]
		return dfs(0)	




		
		
		
		