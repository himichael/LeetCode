class Solution(object):
	def jump(self, nums):
		if not nums:
			return 0
		max_pos = 0
		end = 0
		step = 0
		n = len(nums)
		for i in xrange(n-1):
			max_pos = max(max_pos,i+nums[i])
			if end==i:
				end = max_pos
				step += 1
		return step
		
		
		
	# DFS(超时)	
	def jump(self, nums):
		if not nums:
			return 0
		n = len(nums)
		self.ans = float("inf")
		def dfs(index,step):
			if index>=n-1:
				self.ans = min(self.ans,step)
				return
			for i in xrange(1,nums[index]+1):
				dfs(i+index,step+1)
		dfs(0,0)
		return self.ans
		
		
		
	# 递归+记忆化(超时)	
	def jump(self, nums):
		if not nums:
			return 0
		n = len(nums)
		self.ans = float("inf")
		cache = dict()
		def dfs(index,step):
			if index>=n-1:
				self.ans = min(self.ans,step)
				return
			if (index,step) in cache:
				return cache[(index,step)]
			for i in xrange(1,nums[index]+1):
				dfs(i+index,step+1)
				cache[(index,step+1)] = self.ans
		dfs(0,0)
		return self.ans