class Solution(object):
	# 递归+剪枝
	def canPartition(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""				
		if not nums:
			return False
		total = sum(nums)
		if total%2==1:
			return False
		total /= 2
		n = len(nums)
		nums = sorted(nums,reverse=True)
		def dfs(index, remain):
			if remain==0:
				return True
			if index<n and remain<nums[index]:
				return False
			for i in xrange(index,n):
				if dfs(i+1, remain-nums[i]):
					return True
			return False
		return dfs(0,total)
		
	
	# 动态规划实现
	def canPartition(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""				
		if not nums:
			return False
		total = 0 
		for i in nums:
			total += i
		if total%2==1:
			return False
		total /= 2
		dp = [False]*(total+1)
		dp[0] = True
		for c in nums:
			for i in xrange(total,c-1,-1):
				if dp[i-c]:
					dp[i] = True
		return dp[-1]