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
		
		
		
	# 基于二分的O(NlogN)实现	
	def lengthOfLIS(self, nums):	
		if not nums:
			return 0
		n = len(nums)
		if n<=1:
			return n
		dp = [nums[0]]
		for i in xrange(1,n):
			if nums[i]>dp[-1]:
				dp.append(nums[i])
			else:
				begin = 0
				end = len(dp)-1
				while begin<=end:
					mid = begin+(end-begin)/2
					if dp[mid]<nums[i]:
						begin = mid+1
					elif dp[mid]>nums[i]:
						end = mid-1
					else:
						begin = mid
						break
				dp[begin] = nums[i]
		return len(dp)		
		
		