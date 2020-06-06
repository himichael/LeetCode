class Solution(object):
	def rob(self, nums):
		if not nums:
			return 0
		n = len(nums)
		if n<=2:
			return max(nums)
		d = dict()
		def dfs(index,status,arr,d):
			if index==n-1:
				return 0
			if (index,status)in d:
				return d[index,status]
			a,b,c = 0,0,0
			a = dfs(index+1,status,arr,d)
			if status:
				b = dfs(index+1,0,arr,d)
			else:
				c = dfs(index+1,1,arr,d)+arr[index]
			d[index,status] = max(a,b,c)
			return d[index,status]
		return max(dfs(0,0,nums[0:n-1],dict()), dfs(0,0,nums[1:],dict()))
		
		
		
	# 动态规划
	def rob(self, nums):
		if not nums:
			return 0
		n = len(nums)
		if n<=2:
			return max(nums)
		dp1 = [0 for _ in xrange(n)]
		dp2 = [0 for _ in xrange(n)]
		dp1[0] = 0
		dp1[1] = nums[1]
		dp2[0] = nums[0]
		dp2[1] = max(nums[0],nums[1])
		
		for i in xrange(2,n):
			dp1[i] = max(dp1[i-1],dp1[i-2]+nums[i])
		for i in xrange(2,n-1):
			dp2[i] = max(dp2[i-1],dp2[i-2]+nums[i])
		return max(dp1[-1],dp2[-2])
		
		
		
	# 动态规划，空间压缩
	def rob(self, nums):
		if not nums:
			return 0
		n = len(nums)
		if n<=2:
			return max(nums)
		def dp(begin,end):
			pre,cur = 0,0
			for i in xrange(begin,end):
				cur,pre = max(cur,pre+nums[i]),cur
			return cur
		return max( dp(0,n-1),dp(1,n) )
		
		