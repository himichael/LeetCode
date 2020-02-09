class Solution(object):
	def lengthOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0
		dp = [1 for i in xrange(len(nums))]
		res = 0
		for i in xrange(len(nums)):
			for j in xrange(0,i):
				if nums[i]>nums[j]:
					dp[i] = max(dp[i],dp[j]+1)
		
			res = max(res,dp[i])
		return res
		
		

	def lengthOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0
		n = len(nums)
		mem = [ [-1]*(n) for _ in xrange(n+1) ]
		def dfs(pre,cur):
			if cur==len(nums):
				return 0
			if mem[pre+1][cur]>-1:
				return mem[pre+1][cur]
			a = 0
			if pre<0 or nums[cur]>nums[pre]:
				a = dfs(cur,cur+1)+1
			b = dfs(pre,cur+1)
			mem[pre+1][cur] = max(a,b)
			return mem[pre+1][cur]
		return dfs(-1,0)